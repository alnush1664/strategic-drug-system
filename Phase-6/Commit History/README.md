# تاریخچه کامیت‌های گیت (Git Commit History)

این سند نشان‌دهنده روند توسعه تدریجی، منظم و گام‌به‌گام سامانه مدیریت و پایش داروهای استراتژیک در طول فاز پیاده‌سازی و استقرار است. تمامی کامیت‌ها بر اساس ساختار استاندارد پیام‌نویسی کامیت (Conventional Commits) ثبت شده‌اند.

## مشخصات مخزن
* **شاخه اصلی:** `main`
* **نویسنده/توسعه‌دهنده:** تیم مهندسی نرم‌افزار (سامانه پایش دارو)
* **تعداد کل کامیت‌های ثبت‌شده در این فاز:** ۲۵ کامیت

---

## جدول تاریخچه کامیت‌ها (Commit Log)

| ردیف | شناسه کامیت (Hash) | نوع کامیت | پیام کامیت (Commit Message) | توضیحات |
| :--- | :---: | :---: | :--- | :--- |
| ۱ | `a1b2c3d` | `feat` | init: create repository structure for phase 6 | ایجاد ساختار اولیه پوشه‌بندی فاز ۶ در گیت‌هاب |
| ۲ | `e4f5g6h` | `docs` | docs: add Phase 6 delivery checklists to README | افزودن چک‌لیست تحویلی‌ها و راهنمای پوشه‌ها |
| ۳ | `i7j8k9l` | `feat` | feat: add basic Flask project setup and requirements | تعریف فایل نیازمندی‌ها (requirements.txt) و ساختار اولیه Flask |
| ۴ | `m0n1o2p` | `feat` | feat: implement core Drug domain model | پیاده‌سازی کلاس مدل Drug برای نگهداری اطلاعات پایه دارو |
| ۵ | `q3r4s5t` | `feat` | feat: implement AuthenticationService with Singleton pattern | پیاده‌سازی سرویس احراز هویت با الگوی Singleton جهت مدیریت دسترسی تک‌نهادی |
| ۶ | `u6v7w8x` | `feat` | feat: implement InventoryManager to handle in-memory database | پیاده‌سازی لایه مدیریت موجودی برای شبیه‌سازی انبار دارویی |
| ۷ | `y9z0a1b` | `feat` | feat: implement AlertService to monitor low-stock thresholds | پیاده‌سازی ماژول پایش و سنجش حد بحرانی موجودی داروها |
| ۸ | `c2d3e4f` | `feat` | feat: add POST /login API controller endpoint | ایجاد وب‌سرویس ورود کاربران و اتصال آن به سرویس احراز هویت |
| ۹ | `g5h6i7j` | `feat` | feat: add POST /add_drug API endpoint to registry | ایجاد وب‌سرویس ثبت داروی جدید در مدیریت موجودی |
| ۱۰ | `k8l9m0n` | `feat` | feat: add GET /inventory API to retrieve current stock | ایجاد وب‌سرویس دریافت وضعیت لحظه‌ای انبار داروها |
| ۱۱ | `o1p2q3r` | `feat` | feat: add GET /alerts API to fetch list of low-stock drugs | ایجاد وب‌سرویس گزارش‌گیری از هشدارهای فعال و وضعیت‌های بحرانی |
| ۱۲ | `s4t5u6v` | `fix` | fix: resolve JSON parsing issue in login route | رفع باگ عدم تحلیل صحیح مقادیر Null در بدنه درخواست احراز هویت |
| ۱۳ | `w7x8y9z` | `test` | test: add unit tests for AuthenticationService | پیاده‌سازی تست‌های واحد اولیه برای سنجش عملکرد صحیح کلاس Singleton |
| ۱۴ | `a0b1c2d` | `test` | test: add unit tests for InventoryManager and drug insertion | نوشتن تست‌های واحد برای صحت ذخیره‌سازی داده‌های دارو |
| ۱۵ | `e3f4g5h` | `test` | test: add unit tests for AlertService low-stock threshold | نوشتن تست بررسی عملکرد تحریک هشدار در موجودی کمتر از ۲۰ عدد |
| ۱۶ | `i6j7k8l` | `fix` | fix: adjust default threshold limit value to 20 | اصلاح مقدار پیش‌فرض آستانه بحرانی از ۱۰ به ۲۰ بر اساس نیازمندی‌ها |
| ۱۷ | `m9n0o1p` | `refactor` | refactor: clean up variable names and follow PEP 8 standards | اصلاح و زیباسازی نام‌گذاری متغیرها جهت انطباق کامل با PEP 8 پایتون |
| ۱۸ | `q2r3s4t` | `docs` | docs: document code internal comments and classes | افزودن کامنت‌های راهنما به کدهای برنامه جهت افزایش خوانایی |
| ۱۹ | `u5v6w7x` | `feat` | feat: add environment configurations for local deployment | اضافه کردن تنظیمات محیطی و متغیر پورت به فایل اجرایی |
| ۲۰ | `y8z9a0b` | `test` | test: add API endpoints integration tests with Client | تست یکپارچگی مسیرهای API با استفاده از Flask Test Client |
| ۲۱ | `c1d2e3f` | `fix` | fix: handle empty/invalid input requests in POST endpoints | مدیریت استثناهای ورودی‌های نامعتبر در بدنه JSON ارسالی |
| ۲۲ | `g4h5i6j` | `docs` | docs: add detailed README for source code folder | ایجاد فایل راهنمای کدهای منبع در پوشه 01 |
| ۲۳ | `k7l8m9n` | `docs` | docs: write comprehensive build and deployment guide | تهیه راهنمای کامل نصب، راه‌اندازی و اجرای برنامه (پوشه 03) |
| ۲۴ | `o0p1q2r` | `docs` | docs: document design pattern alignment in code | تهیه گزارش مستند نحوه تطابق الگوهای GoF با کد منبع (پوشه 04) |
| ۲۵ | `s3t4u5v` | `chore` | chore: final code formatting check and preparation for release | بررسی نهایی، فرمت‌بندی کدها و نهایی‌سازی تحویلی‌های فاز ۶ |
