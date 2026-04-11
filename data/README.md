> [!WARNING]
> **Muhim eslatma:** Ma'lumotlar sun'iy intellektdan olinganda ularni albatta tekshirib, tahrirlang. AI xato yoki eskirgan ma'lumot berishi mumkin.

# 🍽️ O'zbek Taomlari JSON Ma'lumotlar Bazasi

O'zbek milliy taomlari to'plami — strukturaviy JSON formatda.

---

## 📁 Fayl tuzilmasi

```
uzbek_taomlari/
├── taomlar.json   # Asosiy taomlar ma'lumotlar bazasi
├── viloyatlar.json       # Viloyatlar ro'yxati
└── README.md
```

---

## 📦 Ma'lumot formati

### Taom (`taomlari.json`)

```json
{
  "id": 1,
  "name": "Palov (Osh)",
  "category": "Asosiy taom",
  "description": "Guruch, go'sht va sabzi bilan tayyorlangan taom — O'zbekistonning milliy ramzi.",
  "ingredients": ["Guruch", "Go'sht", "Sabzi", "Piyoz", "Yog'", "Zira", "Tuz"],
  "preparation_time_min": 90,
  "calories_per_100g": 210,
  "tags": ["guruchli", "go'shtli", "bayram taomi", "an'anaviy"],
  "region_ids": [0],
  "region_names": ["Barcha viloyatlarda"]
}
```

| Maydon | Tur | Tavsif |
|--------|-----|--------|
| `id` | `number` | Unikal identifikator |
| `name` | `string` | Taom nomi (o'zbekcha) |
| `category` | `string` | Taom kategoriyasi |
| `description` | `string` | Qisqa tavsif |
| `ingredients` | `string[]` | Ingredientlar ro'yxati |
| `preparation_time_min` | `number` | Tayyorlash vaqti (daqiqada) |
| `calories_per_100g` | `number` | 100 grammdagi kaloriya |
| `tags` | `string[]` | Qidiruv teglari |
| `region_ids` | `number[]` | Viloyat IDlari (`[0]` = barcha viloyatlar) |

---

### Viloyat (`viloyatlar.json`)

```json
{
  "id": 8,
  "name_uz": "Samarqand viloyati",
  "name_oz": "Самарқанд вилояти",
  "name_ru": "Самаркандская область",
  "name_en": "Samarkand Region"
}
```

---

## 🗃️ Kategoriyalar

| Kategoriya |
|------------|
| Asosiy taom |
| Kabob |
| Sho'rva |
| Non | 
| Xamirli taom |
| Shirinlik |
| Ichimlik |
| Sut mahsuloti |
| Marosim taomi |

---

## 🚀 Foydalanish

### JavaScript / Node.js

```javascript
const fs = require('fs');
const taomlari = JSON.parse(fs.readFileSync('taomlar.json', 'utf-8'));

// Kategoriya bo'yicha filtrlash
const sho'rvalar = taomlari.filter(t => t.category === "Sho'rva");

// Ingredient bo'yicha qidirish
const guruchlilar = taomlari.filter(t => t.ingredients.includes('Guruch'));

// Tez tayyorlanadigan taomlar (30 daqiqagacha)
const tezkor = taomlari.filter(t => t.preparation_time_min <= 30);

// Samarqand taomlari (viloyat id: 8)
const samarqand = taomlari.filter(t => t.region_ids.includes(8));
```

### Python

```python
import json

with open('taomlar.json', 'r', encoding='utf-8') as f:
    taomlari = json.load(f)

# Respublikaviy taomlar (barcha viloyatlarda)
respublika = [t for t in taomlari if t['region_ids'] == [0]]

# Eng kam kaloriyali 5 ta taom
engoz = sorted(taomlari, key=lambda x: x['calories_per_100g'])[:5]

# Teg bo'yicha filtrlash
bayram = [t for t in taomlari if 'bayram taomi' in t['tags']]
```

---

## 📄 Litsenziya

MIT License — bepul foydalanish, tarqatish va o'zgartirish mumkin.