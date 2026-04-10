from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
import os

# ── Load data ─────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "../data/taomlar.json"), encoding="utf-8") as f:
    DISHES: list[dict] = json.load(f)

with open(os.path.join(BASE_DIR, "../data/viloyatlar.json"), encoding="utf-8") as f:
    REGIONS: list[dict] = json.load(f)

SUPPORTED_LANGS = {"uz", "ru", "en"}

# ── App ───────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="O'zbek Milliy Taomlari API",
    description="Open API for Uzbek national dishes database. Supports filtering by language, region and tags.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Helpers ───────────────────────────────────────────────────────────────────


def get_localized(dish: dict, lang: str) -> dict:
    """Return dish with localized fields merged at root level."""
    locale = dish.get(lang, dish.get("uz", {}))
    return {
        "id": dish["id"],
        "name": locale.get("name", ""),
        "category": locale.get("category", ""),
        "description": locale.get("description", ""),
        "ingredients": locale.get("ingredients", []),
        "tags": locale.get("tags", []),
        "region_ids": dish["region_ids"],
        "region_names": locale.get("region_names", []),
        "preparation_time_min": dish["preparation_time_min"],
        "calories_per_100g": dish["calories_per_100g"],
    }


def validate_lang(lang: str) -> str:
    lang = lang.lower()
    if lang not in SUPPORTED_LANGS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language '{lang}'. Supported: {sorted(SUPPORTED_LANGS)}",
        )
    return lang


# ── Routes ────────────────────────────────────────────────────────────────────


@app.get("/", tags=["Info"], include_in_schema=False)
def root():
    return {
        "name": "O'zbek Milliy Taomlari API",
        "version": "1.0.0",
        "total_dishes": len(DISHES),
        "supported_languages": sorted(SUPPORTED_LANGS),
        "docs": "/docs",
    }


@app.get("/dishes", tags=["Dishes"])
def list_dishes(
    lang: str = Query("uz", description="Language code: uz | ru | en"),
    region_id: Optional[int] = Query(
        None, description="Filter by region ID (0 = all regions)"
    ),
    tags: Optional[str] = Query(
        None, description="Comma-separated tags to filter by (AND logic)"
    ),
    category: Optional[str] = Query(None, description="Filter by category name"),
    max_calories: Optional[int] = Query(None, description="Maximum calories per 100g"),
    max_time: Optional[int] = Query(
        None, description="Maximum preparation time in minutes"
    ),
    skip: int = Query(0, ge=0, description="Pagination offset"),
    limit: int = Query(20, ge=1, le=100, description="Number of results (max 100)"),
):
    """
    List dishes with optional filters.

    - **lang**: Response language (`uz`, `ru`, `en`)
    - **region_id**: Filter by region ID from `/regions`
    - **tags**: Comma-separated list of tags (e.g. `meat,festive`)
    - **category**: Filter by category name in the selected language
    - **max_calories**: Upper limit for calories per 100g
    - **max_time**: Upper limit for preparation time in minutes
    """
    lang = validate_lang(lang)
    results = DISHES

    # Filter: region_id
    if region_id is not None:
        results = [
            d for d in results if region_id in d["region_ids"] or 0 in d["region_ids"]
        ]

    # Filter: tags (AND — dish must contain ALL requested tags)
    if tags:
        requested_tags = [t.strip().lower() for t in tags.split(",") if t.strip()]
        if requested_tags:
            results = [
                d
                for d in results
                if all(
                    any(
                        rt in tag.lower()
                        for tag in d.get(lang, d.get("uz", {})).get("tags", [])
                    )
                    for rt in requested_tags
                )
            ]

    # Filter: category (case-insensitive, in selected language)
    if category:
        cat_lower = category.lower()
        results = [
            d
            for d in results
            if cat_lower in d.get(lang, d.get("uz", {})).get("category", "").lower()
        ]

    # Filter: max_calories
    if max_calories is not None:
        results = [d for d in results if d["calories_per_100g"] <= max_calories]

    # Filter: max_time
    if max_time is not None:
        results = [d for d in results if d["preparation_time_min"] <= max_time]

    total = len(results)
    paginated = results[skip : skip + limit]

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "results": [get_localized(d, lang) for d in paginated],
    }


@app.get("/dishes/search", tags=["Dishes"])
def search_dishes(
    q: str = Query(
        ...,
        min_length=1,
        description="Search query (searches name, description, ingredients)",
    ),
    lang: str = Query("uz", description="Language code: uz | ru | en"),
):
    """
    Full-text search across dish name, description and ingredients.
    """
    lang = validate_lang(lang)
    q_lower = q.lower()

    matches = []
    for dish in DISHES:
        locale = dish.get(lang, dish.get("uz", {}))
        searchable = " ".join(
            [
                locale.get("name", ""),
                locale.get("description", ""),
                " ".join(locale.get("ingredients", [])),
                " ".join(locale.get("tags", [])),
            ]
        ).lower()

        if q_lower in searchable:
            matches.append(get_localized(dish, lang))

    return {
        "query": q,
        "lang": lang,
        "total": len(matches),
        "results": matches,
    }


@app.get("/dishes/{dish_id}", tags=["Dishes"])
def get_dish(
    dish_id: int,
    lang: str = Query("uz", description="Language code: uz | ru | en"),
):
    """Get a single dish by ID."""
    lang = validate_lang(lang)
    dish = next((d for d in DISHES if d["id"] == dish_id), None)
    if not dish:
        raise HTTPException(status_code=404, detail=f"Dish with id={dish_id} not found")
    return get_localized(dish, lang)


@app.get("/regions", tags=["Meta"])
def list_regions(
    lang: str = Query("uz", description="Language code: uz | ru | en"),
):
    """Return all Uzbekistan regions."""
    return [{"id": d["id"], "name": d[f"name_{lang}"]} for d in REGIONS]


@app.get("/tags", tags=["Meta"])
def list_tags(lang: str = Query("uz", description="Language code: uz | ru | en")):
    """Return all unique tags in the selected language."""
    lang = validate_lang(lang)
    all_tags: set[str] = set()
    for dish in DISHES:
        locale = dish.get(lang, dish.get("uz", {}))
        all_tags.update(locale.get("tags", []))
    return sorted(all_tags)


@app.get("/categories", tags=["Meta"])
def list_categories(lang: str = Query("uz", description="Language code: uz | ru | en")):
    """Return all unique categories in the selected language."""
    lang = validate_lang(lang)
    cats: set[str] = set()
    for dish in DISHES:
        locale = dish.get(lang, dish.get("uz", {}))
        cat = locale.get("category", "")
        if cat:
            cats.add(cat)
    return sorted(cats)
