# Contributing · المساهمة

This repository is an instructor-controlled course project. Changes must protect the learner path, the public/private boundary, and the reproducibility of the Colab lab.

هذا المستودع مشروع دورة تديره المدربة. يجب أن تحمي التغييرات مسار المتدرب، والفصل بين العام والخاص، وقابلية إعادة تشغيل لاب كولاب.

## Working rules · قواعد العمل

1. Create a focused branch such as `build/02-learner-portal`.
2. Keep English on the left (`dir="ltr"`) and Arabic on the right (`dir="rtl"`) in dual-language layouts.
3. Use synthetic examples only; never copy production data.
4. Do not add answer keys, hidden tests, instructor notes, grades, or recovery checkpoints.
5. Keep the active Colab path pointed at the cumulative notebook, and preserve a credential-free clean-runtime check.
6. Do not add an official logo, `official`/`approved` wording, or institutional topic without written authorization.
7. Run `python scripts/validate_release.py` and `python scripts/validate_notebook.py` before requesting review.
8. Keep temporary checkpoints, raw output, and ZIP bundles out of Git. A learner may commit only the final C29-redacted reports and manifest to their own repository.

---

1. أنشئ فرعًا مركزًا مثل `build/02-learner-portal`.
2. أبقِ الإنجليزية يسارًا (`dir="ltr"`) والعربية يمينًا (`dir="rtl"`) في التخطيطات الثنائية.
3. استخدم أمثلة مصطنعة فقط، ولا تنسخ بيانات تشغيلية.
4. لا تضف مفاتيح إجابة أو اختبارات خفية أو ملاحظات المدربة أو درجات أو نقاط استعادة فعلية.
5. أبقِ مسار كولاب الفعّال مرتبطًا بالدفتر التراكمي، وحافظ على فحص نظيف بلا بيانات دخول.
6. لا تضف شعارًا رسميًا أو وصف `official`/`approved` أو Topic مؤسسيًا دون تفويض مكتوب.
7. شغّل `python scripts/validate_release.py` و`python scripts/validate_notebook.py` قبل طلب المراجعة.
8. أبقِ نقاط الحفظ المؤقتة والمخرجات الخام وحزم ZIP خارج Git. يجوز للمتدرب رفع تقارير C29 المنقحة النهائية وبيان الملفات إلى مستودعه فقط.

## Pull request evidence · أدلة طلب الدمج

- Scope and learner impact.
- Screenshots for desktop and mobile when the portal changes.
- Validation result.
- Confirmation that no secret, personal data, hidden assessment, or official branding was added.

---

- النطاق وأثره في المتدرب.
- صور سطح المكتب والجوال عند تغيير البوابة.
- نتيجة الفحص.
- تأكيد عدم إضافة سر أو بيانات شخصية أو تقييم خفي أو هوية رسمية.
