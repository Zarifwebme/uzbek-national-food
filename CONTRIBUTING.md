# Loyihaga hissa qo'shish (Contributing to Uzbek National Food Data)

Salom! Loyihamizni boyitishga va O'zbek milliy taomlari haqida ochiq ma'lumotlar bazasini yaratishga qiziqish bildirganingiz uchun rahmat. 🇺🇿

Ushbu loyiha hamma uchun ochiq va biz yangi contributor'larni mamnuniyat bilan kutib qolamiz.

## Qanday qilib yordam berish mumkin?

Siz loyihaga bir necha usulda hissa qo'shishingiz mumkin:
1. **Yangi ma'lumot qo'shish:** `data/taomlar.json` fayliga yangi taomlar yoki tafsilotlar qo'shish.
2. **Xatolarni tuzatish:** Ma'lumotlardagi imlo xatolarini yoki noto'g'ri faktlarni to'g'rilash.
3. **Tarjima:** Tavsiflarni ingliz yoki boshqa tillarga tarjima qilish.
4. **Kod sifatini oshirish:** JSON strukturasini yaxshilash yoki tekshiruvchi skriptlar yozish.

## Qadam-baqadam yo'riqnoma

Hissa qo'shish uchun quyidagi qadamlarni bajaring:

1. Ushbu repozitoriyani **Fork** qiling.
2. O'z kompyuteringizga **Clone** qiling:
   ```bash
   git clone [https://github.com/SizningUsername/uzbek-national-food.git](https://github.com/SizningUsername/uzbek-national-food.git)
Yangi Branch oching:

Bash
git checkout -b feature/yangi-taom-nomi
O'zgarishlarni kiriting va Commit qiling:

Bash
git commit -m "Yangi taom qo'shildi: Somsa"
Branch'ingizni GitHub'ga Push qiling:

Bash
git push origin feature/yangi-taom-nomi
Asosiy repozitoriyaga Pull Request yuboring.

JSON standarti
Yangi ma'lumot qo'shayotganda quyidagi formatga amal qiling:

JSON
{
  "id": yangi_id,
  "name": "Taom nomi",
  "description": "Taom haqida qisqacha ma'lumot",
  "ingredients": ["masalliq 1", "masalliq 2"]
}
