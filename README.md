# Telegram Userbot

Bu userbot Telegram profilingizdan avtomatik javoblar yuborish va OpenAI bilan integratsiya qilish uchun yaratilgan.

## Ishga tushirish yo‘riqnomasi:

### 1. Pythonni o‘rnating
Loyihani ishlatish uchun Python 3.8 yoki undan yuqori versiya talab qilinadi. Python’ni quyidagi sayt orqali yuklab olishingiz mumkin: [Python rasmiy sayti](https://www.python.org).

### 2. Loyihaga kerakli kutubxonalarni o‘rnating
```bash
pip install -r requirements.txt
```
### 3. Virtual muhit yaratish
Avvalo virtual muhit yarating va uni faollashtiring:

#### Virtual muhit yaratish
```bash
python -m venv test_env
```
#### Virtual muhitni faollashtirish (Linux yoki MacOS)
```bash
source test_env/bin/activate
```
#### Virtual muhitni faollashtirish (Windows)
```bash
test_env\Scripts\activate
```
#### TELEGRAM_USERBOT


### 3. Botni ishga tushirish
```bash
python main.py
```

### Hozirgi muammolar va kelajakdagi rejalashtirish
- Har bir foydalanuvchi uchun alohida Telegram va OpenAI konfiguratsiyasini boshqarish.
- Dastur xavfsizligini kuchaytirish uchun ma’lumotlarni shifrlash.
- OpenAI'ga bog‘liq cheklovlarni avtomatik tekshirish va xabar berish.

## Loyihani qo‘llab-quvvatlash
Agar muammolar yuzaga kelsa yoki yangi funksiyalar qo‘shishni xohlasangiz, GitHub’ga masala yaratishingiz yoki PR (Pull Request) yuborishingiz mumkin.