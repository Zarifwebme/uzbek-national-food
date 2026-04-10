# 🍽️ Uzbek Food API — FastAPI

REST API for the Uzbek national dishes database. Built with FastAPI.

## Setup

```bash
pip install -r requirements.txt
```

Place `taomlar.json` and `viloyatlar.json` in the same folder as `main.py`.

## Run

```bash
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`  
Swagger docs: `http://localhost:8000/docs`

---

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/regions` | List all regions |
| GET | `/dishes` | List/filter dishes |
| GET | `/dishes/search` | Full-text search |
| GET | `/dishes/{id}` | Get dish by ID |
| GET | `/tags` | List all tags |
| GET | `/categories` | List all categories |

---

## Query Parameters

### `GET /dishes`

| Param | Type | Default | Description |
|---|---|---|---|
| `lang` | string | `uz` | Language: `uz`, `ru`, `en` |
| `region_id` | int | — | Filter by region ID |
| `tags` | string | — | Comma-separated tags (AND logic) |
| `category` | string | — | Filter by category |
| `max_calories` | int | — | Max calories per 100g |
| `max_time` | int | — | Max preparation time (minutes) |
| `skip` | int | `0` | Pagination offset |
| `limit` | int | `20` | Results per page (max 100) |

---

## Examples

```bash
# All soups in Russian
GET /dishes?lang=ru&category=Суп

# Festive meat dishes in English
GET /dishes?lang=en&tags=meat,festive

# Dishes from Samarkand (region_id=8)
GET /dishes?region_id=8&lang=uz

# Quick dishes under 30 min, under 200 kcal
GET /dishes?max_time=30&max_calories=200

# Full-text search in English
GET /dishes/search?q=rice&lang=en

# Single dish in Uzbek
GET /dishes/1?lang=uz
 
# All tags in Russian
GET /tags?lang=ru
 
# All regionns in Russian
GET /regions?lang=ru
```
