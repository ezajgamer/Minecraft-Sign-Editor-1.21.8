# Minecraft-Sign-Editor-1.21.8
Minecraft Sign Editor 1.21.8
----------------------------------------------

Project Description: Minecraft Sign Editor

Overview
This project is a desktop GUI application written in Python using the PySide6 (Qt) library that helps Minecraft players quickly and easily generate /setblock commands for in-game signs.

📌 Key Features

Supports all sign types in Minecraft 1.21.8 (standing, wall, and hanging signs).

Simple Facing selection for wall and hanging signs.

Rotation control for standing signs using arrow indicators (↑, ↗, →, ...).

Full text customization across four lines:

Enter custom text.

Pick text color with a Color Picker.

Toggle Bold and Italic styles.

Glowing Text effect with on/off switch.

One-click Copy of the generated command to the clipboard.

Signature & Version: displays “Ezaj Gamer” at the bottom along with version (0.6.1) and today’s date.

💻 Requirements

Python 3.7 or newer

PySide6 (pip install PySide6)

🚀 Running the Application

pip install -r requirements.txt   # Install dependencies
python "sign editor V0.6.1.py"       # Launch the GUI

📦 Building an Executable

PyInstaller:

pyinstaller --onefile --windowed --name "sign editor V0.6.1" "sign editor V0.6.1.py"

Nuitka:

pip install zstandard nuitka
python -m nuitka --standalone --onefile --windows-console-mode=disable --enable-plugin=pyside6 "sign editor V0.6.1.py"

✨ How to Use

Launch the application.

Select a Sign Type.

Choose Facing (for wall/hanging) or Rotation arrow (for standing).

Toggle Glowing Text if desired.

Edit up to 4 lines of text with colors and styles.

Click Generate Command, then Copy to Clipboard.

Paste the command in Minecraft to place your custom sign instantly.






------------------------------------------------------
وصف المشروع: Minecraft Sign Editor

نبذة
هذا المشروع عبارة عن تطبيق سطح مكتب (GUI) مكتوب بلغة Python ويستخدم مكتبة PySide6 (Qt) ليساعد لاعبين ماينكرافت على توليد أوامر /setblock الخاصة بلوحات اللاعبين (Signs) بكل سهولة وسرعة.

📌 الميزات الرئيسية

دعم جميع أنواع اللوحات في إصدار ماينكرافت 1.21.8 (عادية، جدارية، ومعلقة).

اختيار الاتجاه (Facing) للّافتات الجدارية والمعلقة بأسلوب مبسّط.

تدوير اللوحات الواقفة (Rotation) باستخدام أسهم تشير للاتجاه (↑, ↗, →, ...).

تحكم كامل في نص اللوحة عبر 4 أسطر:

كتابة النص.

اختيار لون النص عبر Color Picker.

تفعيل الخيارات: عريض (Bold) ومائل (Italic).

النص المتوهّج (Glowing Text) بخيار تشغيل/إيقاف.

نسخ الأمر الناتج للوحة الحافظة بنقرة واحدة.

التوقيع والإصدار: يظهر اسم "Ezaj Gamer" أسفل الواجهة مع رقم الإصدار (0.6.1) وتاريخ اليوم.

💻 المتطلبات

Python 3.7 أو أحدث

PySide6 (يمكن تثبيتها بـ pip install PySide6)

🚀 طريقة التشغيل

pip install -r requirements.txt   # لتثبيت PySide6
python "sign editor V0.6.1.py"       # لتشغيل التطبيق

📦 بناء exe

PyInstaller:

pyinstaller --onefile --windowed --name "sign editor V0.6.1" "sign editor V0.6.1.py"

Nuitka:

pip install zstandard nuitka
python -m nuitka --standalone --onefile --windows-console-mode=disable --enable-plugin=pyside6 "sign editor V0.6.1.py"

✨ الاستخدام

شغّل التطبيق.

حدّد نوع اللوحة.

اختَر اتجاه أو سهم التدوير.

فعّل "Glowing Text" إذا حاب يخوّن.

حرّر 4 أسطر النص مع الألوان والستايل.

اضغط "Generate Command" وبعدين "Copy to Clipboard".

الصق الأمر داخل ماينكرافت وشوف اللوحة جَاهزة على طول!

ملاحظة: التطبيق مصمم بخفة وسلاسة ويشتغل بدون كونسول مزعج.



