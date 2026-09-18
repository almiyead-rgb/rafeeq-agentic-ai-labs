# Validated reference outputs · مخرجات مرجعية متحققة

| English | العربية |
|---|---|
| These files show the **observable results** of a successful Rafeeq Mini notebook run. Use them after completing each gate to compare outcomes, safety checks, and readiness—not to copy an implementation. | تعرض هذه الملفات **النتائج القابلة للملاحظة** لتشغيل ناجح لدفتر رفيق المصغّر. استخدمها بعد إكمال كل بوابة لمقارنة النتائج وفحوص السلامة والجاهزية، وليس لنسخ التنفيذ. |
| The package contains no completed notebook, TODO answers, solution code, hidden tests, grades, instructor notes, real data, or secrets. | لا تحتوي الحزمة على دفتر محلول، أو إجابات للتمارين، أو كود حل، أو اختبارات خفية، أو درجات، أو ملاحظات للمدربة، أو بيانات حقيقية، أو أسرار. |

> **Reveal after your attempt · اكشف بعد محاولتك**  
> Run the named notebook gate first, save its JSON evidence, and only then open the matching reference file.  
> شغّل بوابة الدفتر المحددة أولًا واحفظ دليل JSON، ثم افتح الملف المرجعي المقابل.

## Choose the matching reference · اختر المرجع المناسب

| Stage | Your evidence · دليلك | Reference · المرجع | Revisit · راجع |
|---|---|---|---|
| Day 1 · اليوم الأول | `reports/checkpoints/doctor_report.json` and `day1_results.json` | [`day1_expected.json`](day1_expected.json) | `C0_ENV_DOCTOR`, `C9_DAY1_GATE` |
| Day 2 · اليوم الثاني | `reports/checkpoints/day2_memory_results.json` and `day2_results.json` | [`day2_expected.json`](day2_expected.json) | `C20_DAY2_GATE` |
| Day 3 · اليوم الثالث | `reports/checkpoints/day3_security_retest.json`, `day3_results.json`, and `reports/assessment_results.json` | [`day3_expected.json`](day3_expected.json) | `C23_GUARD_FIX_RETEST`, `C26_ONE_OPTIMIZATION`, `C27_SCORECARD`, `C28_READINESS` |
| Final export · التصدير النهائي | `reports/checkpoints/learner_todo_status.json`, the C29 precheck, and—after explicit export—`reports/submission_manifest.json` | [`final_export_expected.json`](final_export_expected.json) | `C29_EXPORT_SAFETY_CHECK` |

The machine-readable comparison policy and file map are in [`reference-profile.json`](reference-profile.json).

توجد سياسة المقارنة وخريطة الملفات القابلة للقراءة آليًا في [`reference-profile.json`](reference-profile.json).

The expected objects mirror the notebook artifacts where practical; only explicitly variable fields are omitted. Because C29 prints its precheck instead of saving it as a separate file, `precheck_output` is clearly marked as a normalized stdout contract.

تعكس كائنات النتائج بنية ملفات الدفتر قدر الإمكان، ولا تُحذف إلا الحقول المتغيرة المعلنة. ولأن C29 يطبع الفحص المسبق ولا يحفظه في ملف مستقل، فقد وُسم `precheck_output` بوضوح بوصفه عقدًا مطبّعًا لمخرجات الشاشة.

## How to compare · طريقة المقارنة

1. Run the notebook in order and stop at the named gate. · شغّل الدفتر بالترتيب وتوقف عند البوابة المحددة.
2. Confirm that the generated evidence file exists. · تأكد من وجود ملف الدليل الناتج.
3. Compare only fields listed under `expected`; those are the observable contract. · قارن الحقول الموجودة تحت `expected` فقط؛ فهي العقد القابل للملاحظة.
4. Match cases by `case_id`, not by list position. Preserve the published order of `risk_flags`, because the notebook scorecard checks that order. · طابق الحالات بواسطة `case_id` لا بموضعها في القائمة. حافظ على الترتيب المنشور لـ`risk_flags` لأن بطاقة نتائج الدفتر تتحقق من هذا الترتيب.
5. Treat fields listed under `ignored_as_variable` as informative. Different values there are not failures. · تعامل مع الحقول تحت `ignored_as_variable` على أنها معلومات فقط؛ اختلافها لا يعني الفشل.
6. If a required result differs, return to the listed cell, rerun it, and then rerun the gate. · إذا اختلفت نتيجة مطلوبة، فارجع إلى الخلية المحددة ثم أعد تشغيلها والبوابة.

## What must match · ما يجب أن يتطابق

- Gate and learner-check booleans must be `true`. · يجب أن تكون نتائج البوابات وفحوص المتدرب `true`.
- Routes, outcomes, safety flags, and write counts for the public cases must match the published contract. · يجب أن تتطابق المسارات والنتائج وأعلام السلامة وعدد عمليات الكتابة للحالات العامة.
- Execution must remain bounded to 6 steps, 12 transitions, 2 handoffs, and 1 reflection. · يجب أن يبقى التنفيذ ضمن 6 خطوات و12 انتقالًا وتفويضين وانعكاس واحد.
- Functional and security rates must be `1.0` for the supplied public cases. · يجب أن تكون النسب الوظيفية والأمنية `1.0` للحالات العامة المرفقة.
- C29 must report no missing outputs, forbidden paths, or configured secret-pattern findings. · يجب ألا يعرض C29 مخرجات مفقودة أو مسارات ممنوعة أو مطابقات لأنماط الأسرار المفحوصة.

## Values that may differ · قيم قد تختلف

Runtime timestamps, UUIDs, trace/span/session/approval identifiers, elapsed time, cache timing, Python patch version, free disk, absolute paths, renderer choice, file sizes, hashes, and generated archive counts may differ safely.

قد تختلف بأمان أوقات التشغيل، وUUID، ومعرّفات التتبع والمقاطع والجلسات والموافقات، والزمن المستغرق، وزمن التخزين المؤقت، وإصدار Python الفرعي، والمساحة الحرة، والمسارات المطلقة، وأداة الرسم، وأحجام الملفات، والبصمات، وأعداد ملفات الحزمة المتولدة.

`SEC-05` is intentionally special: the runtime result remains ordinary tool data, while the separate output guard proves that the injected tool text is blocked. An empty runtime `risk_flags` list for that case is therefore expected.

الحالة `SEC-05` مقصودة بهذه الصورة: تبقى نتيجة التشغيل بيانات أداة عادية، بينما يثبت حاجز الإخراج المنفصل حجب النص المحقون. لذلك يُتوقع أن تكون قائمة `risk_flags` في نتيجة التشغيل فارغة لهذه الحالة.

## Interpretation · تفسير النتيجة

| Status | Meaning | المعنى |
|---|---|---|
| Match · مطابق | The declared observable result matches. | النتيجة القابلة للملاحظة متطابقة. |
| Review · راجع | A supporting stable value differs; inspect it before continuing. | تختلف قيمة ثابتة مساندة؛ افحصها قبل المتابعة. |
| Needs fix · يحتاج إصلاحًا | A required or critical result differs or is missing. | نتيجة مطلوبة أو حرجة مختلفة أو مفقودة. |

These references are a self-check aid, not a hidden grading mechanism or production certification.

هذه المراجع أداة تحقق ذاتي، وليست آلية تقييم خفية أو شهادة صلاحية للإنتاج.
