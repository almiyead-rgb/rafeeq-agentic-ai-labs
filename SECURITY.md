# Security Policy · سياسة الأمان

## Supported state · الحالة المدعومة

`0.1.0-alpha` is a local pre-release foundation. It is not approved for learner distribution or production use.

الإصدار `0.1.0-alpha` أساس تمهيدي محلي، ولم يعتمد بعد للتوزيع على المتدربين أو للاستخدام الإنتاجي.

## Never commit · ممنوع رفعه

- Passwords, tokens, API keys, cookies, private repository links, or `.env` files.
- Real customer, employee, trainee, order, payment, or support-ticket data.
- Reference solutions, answer keys, hidden evaluations, hidden attack cases, instructor notes, grades, or actual recovery checkpoints.
- Generated learner evidence or exported submission bundles.

---

- كلمات المرور أو رموز الوصول أو مفاتيح API أو Cookies أو روابط المستودعات الخاصة أو ملفات `.env`.
- بيانات حقيقية لعميل أو موظف أو متدرب أو طلب أو دفعة أو تذكرة دعم.
- الحلول المرجعية أو مفاتيح الإجابة أو التقييمات وحالات الهجوم الخفية أو ملاحظات المدربة أو الدرجات أو نقاط الاستعادة الفعلية.
- أدلة المتدربين الناتجة أو حزم التسليم المصدرة.

Use synthetic data only. The private instructor repository is still not a secrets manager.

استخدم بيانات مصطنعة فقط. مستودع المدربة الخاص ليس مديرًا للأسرار.

## Reporting a concern · الإبلاغ عن مشكلة

Do not open a public issue for a vulnerability, exposed credential, private link, or leaked learner information. Contact the repository owner privately, include the affected path and the minimum reproduction detail, and redact every secret or personal value.

لا تفتح Issue عامًا لثغرة أو بيان دخول مكشوف أو رابط خاص أو معلومات متدرب متسربة. تواصل مع مالك المستودع بقناة خاصة، وحدد المسار المتأثر وأقل قدر لازم لإعادة المشكلة، مع حجب كل سر أو قيمة شخصية.

If a credential is exposed, revoke or rotate it first. Deleting a file or commit does not make an exposed secret safe again.

إذا انكشف بيان دخول، فألغِه أو دوّره أولًا. حذف الملف أو الـCommit لا يجعل السر المكشوف آمنًا مجددًا.
