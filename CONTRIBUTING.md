> [!WARNING]
> **Muhim eslatma:** Ma'lumotlar sun'iy intellektdan olinganda ularni albatta tekshirib, tahrirlang. AI xato yoki eskirgan ma'lumot berishi mumkin.

# 🤝 Loyihaga hissa qo‘shish (Contributing to Uzbek National Food Data)

Salom! Loyihamizni boyitishga va **O‘zbek milliy taomlari haqida ochiq ma’lumotlar bazasini yaratishga** qiziqish bildirganingiz uchun rahmat.

Ushbu loyiha hamma uchun ochiq va biz yangi contributor'larni mamnuniyat bilan kutib qolamiz.

---

## 📌 Qanday qilib yordam berish mumkin?

Siz loyihaga bir necha usulda hissa qo‘shishingiz mumkin:

### 1. 🍽️ Yangi ma’lumot qo‘shish
`data/taomlar.json` fayliga yangi taomlar yoki tafsilotlar qo‘shish.

### 2. 🛠️ Xatolarni tuzatish
Ma’lumotlardagi imlo xatolarini yoki noto‘g‘ri faktlarni to‘g‘rilash.

### 3. 💻 Kod sifatini oshirish
JSON strukturasini yaxshilash yoki tekshiruvchi skriptlar yozish.

---

## 🚀 Qadam-baqadam yo‘riqnoma

Hissa qo‘shish uchun quyidagi qadamlarni bajaring:

### 1. Repository'ni Fork qiling
GitHub orqali ushbu repozitoriyani o‘z accountingizga fork qiling.

### 2. Clone qiling

```bash
git https://github.com/Zarifwebme/uzbek-national-food.git
```

### 3. Yangi branch oching

```bash
git checkout -b feature/yangi-taom-nomi
```

### 4. O‘zgarish kiriting va commit qiling

```bash
git commit -m "Yangi taom qo‘shildi: Somsa"
```

### 5. GitHub'ga push qiling

```bash
git push origin feature/yangi-taom-nomi
```

### 6. Pull Request yuboring
GitHub orqali asosiy repository'ga Pull Request oching.

---

## 📋 JSON Standarti

Yangi ma’lumot qo‘shayotganda quyidagi formatga amal qiling:

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
}
```

---

## ⚠️ Muhim Eslatmalar

- Har bir taom uchun **unikal `id`** kiriting.
- JSON formatini buzmaslikka e’tibor bering.
- Imlo va grammatika xatolarini tekshirib chiqing.
- Pull Request yuborishdan oldin ma’lumotlarning to‘g‘riligiga ishonch hosil qiling.

---

## ❤️ Rahmat

Sizning hissangiz ushbu loyihani yanada foydali va boy qilishga yordam beradi.  
Birgalikda O‘zbek milliy taomlarini dunyoga tanitamiz! 🇺🇿✨
