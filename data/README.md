# 🍽️ Uzbek National Dishes — Open JSON Database

> A structured, open-source database of Uzbekistan's national dishes, ready for developers, researchers, and food app builders.

---

## 📖 About

This project was created to digitize Uzbek culinary heritage and provide a ready-to-use data source for developers. The database covers dishes from all regions of Uzbekistan with consistent, structured fields.

Currently includes **80+ national dishes** across all major categories.

---

## 📁 File Structure

```
uzbek-food-db/
│
├── uzbek_taomlari.json   # Main dish database
├── viloyatlar.json        # Uzbekistan regions reference
└── README.md
```

---

## 🗂️ Data Structure

Each dish entry contains the following fields:

```json
{
  "id": 1,
  "name": "Palov (Osh)",
  "category": "Asosiy taom",
  "description": "Rice dish with meat and carrots, the national symbol of Uzbekistan.",
  "ingredients": ["Guruch", "Go'sht", "Sabzi", "Piyoz", "Yog'", "Zira", "Tuz"],
  "preparation_time_min": 90,
  "calories_per_100g": 210,
  "tags": ["guruchli", "go'shtli", "bayram taomi", "an'anaviy"],
  "region_ids": [0],
  "region_names": ["Barcha viloyatlarda"]
}
```

| Field | Type | Description |
|---|---|---|
| `id` | `number` | Unique identifier |
| `name` | `string` | Dish name (Uzbek) |
| `category` | `string` | Dish category |
| `description` | `string` | Short description |
| `ingredients` | `string[]` | List of ingredients |
| `preparation_time_min` | `number` | Preparation time in minutes |
| `calories_per_100g` | `number` | Calories per 100g |
| `tags` | `string[]` | Search tags |
| `region_ids` | `number[]` | Region IDs from `viloyatlar.json` (`[0]` = all regions) |
| `region_names` | `string[]` | Region names in Uzbek |

---

## 🌍 Regions

Regions are stored in `viloyatlar.json` and linked via `region_ids`. Each region entry includes multilingual names:

```json
{
  "id": 8,
  "soato_id": 1718,
  "name_uz": "Samarqand viloyati",
  "name_oz": "Самарқанд вилояти",
  "name_ru": "Самаркандская область",
  "name_en": "Samarkand Region"
}
```

> Dishes available nationwide use `"region_ids": [0]` and `"region_names": ["Barcha viloyatlarda"]`.

---

## 🗃️ Categories

| Category | Count |
|---|---|
| Asosiy taom (Main dish) | 20+ |
| Kabob (Kebab) | 10+ |
| Sho'rva (Soup) | 12+ |
| Non / Xamirli taom (Bread / Pastry) | 12+ |
| Shirinlik (Dessert) | 6+ |
| Ichimlik (Drink) | 5+ |
| Sut mahsuloti (Dairy) | 3+ |
| Marosim taomi (Ceremonial) | 2+ |

---

## 🚀 Usage

### JavaScript / Node.js

```javascript
const fs = require('fs');
const dishes = JSON.parse(fs.readFileSync('uzbek_taomlari.json', 'utf-8'));

// Filter by category
const soups = dishes.filter(d => d.category === "Sho'rva");

// Search by ingredient
const riceDishes = dishes.filter(d => d.ingredients.includes('Guruch'));

// Quick meals (under 30 min)
const quick = dishes.filter(d => d.preparation_time_min <= 30);

// Dishes from Samarkand (region id: 8)
const samarkand = dishes.filter(d => d.region_ids.includes(8));
```

### Python

```python
import json

with open('uzbek_taomlari.json', 'r', encoding='utf-8') as f:
    dishes = json.load(f)

# Nationwide dishes
nationwide = [d for d in dishes if d['region_ids'] == [0]]

# Lowest calorie dishes
lightest = sorted(dishes, key=lambda x: x['calories_per_100g'])[:5]

# Dishes by tag
festive = [d for d in dishes if 'bayram taomi' in d['tags']]
```

### Fetch (Browser)

```javascript
const res = await fetch('uzbek_taomlari.json');
const dishes = await res.json();

const kebabs = dishes.filter(d => d.category === 'Kabob');
```

---

## 🤝 Contributing

Want to add a dish or improve existing data?

1. **Fork** the repository
2. Create a branch: `git checkout -b feat/new-dish`
3. Edit `uzbek_taomlari.json` following the schema above
4. Open a **Pull Request**

### Data quality guidelines

- All required fields must be filled
- `id` must be unique
- `ingredients` should be written in Uzbek
- `calories_per_100g` should be provided even if approximate
- `region_ids` must reference valid IDs from `viloyatlar.json` (or `[0]` for nationwide)

---

## 📜 License

This project is distributed under the **MIT License** — free to use for personal and commercial purposes.

---

## ⭐ Support

If this project is useful to you, please give it a ⭐ on GitHub — it helps the project grow!
