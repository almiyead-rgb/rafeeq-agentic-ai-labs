# Evidence cards · بطاقات الأدلة

> Optional working aid: if you use it, keep a local copy and duplicate the card below for each claim you need to structure.
>
> أداة عمل اختيارية: عند استخدامها احتفظ بنسخة محلية وكرر البطاقة لكل ادعاء تحتاج إلى تنظيمه.

## Evidence index · فهرس الأدلة

| Evidence ID | Claim · الادعاء | Cell/gate · الخلية/البوابة | Result | Assessment run ID · معرف تشغيل التقييم |
|---|---|---|---|---|
| `EV-[TODO]` | `[TODO]` | `C[TODO]` | `PASS / FAIL` | `[TODO]` |

---

## Evidence card `EV-[TODO]` · بطاقة الدليل

| Field | Entry · الإدخال |
|---|---|
| Claim being proven · الادعاء المثبت | `[TODO: one testable sentence]` |
| Course objective · هدف الدورة | `[TODO]` |
| Day and cell ID · اليوم ورقم الخلية | `Day [TODO] · C[TODO]` |
| Public case ID · رقم الحالة العامة | `[TODO]` |
| Synthetic fixture ID · معرف الحالة المصطنعة | `[TODO]` |
| Preconditions · الشروط المسبقة | `[TODO]` |
| Action executed · الإجراء المنفذ | `[TODO]` |
| Expected result · النتيجة المتوقعة | `[TODO]` |
| Actual result · النتيجة الفعلية | `[TODO]` |
| Status · الحالة | `PASS / FAIL` |
| Key metric · المقياس الرئيس | `[TODO or Not measured]` |
| Notebook output reference · مرجع مخرج الدفتر | `C[TODO] · output [TODO]` |
| Public file or report path · مسار الملف أو التقرير العام | `[TODO]` |
| Assessment `run_id` from `assessment_results.json` · `run_id` للتقييم من `assessment_results.json` | `[TODO if available]` |
| Run timestamp (UTC) · وقت التشغيل | `[TODO]` |
| Reproduction steps · خطوات إعادة التنفيذ | `1. [TODO] 2. [TODO] 3. [TODO]` |

### Safe observation · الملاحظة الآمنة

`[TODO: summarize the observable decision, tool call, route, result, and counters. Do not paste raw records or private reasoning.]`

`[TODO: لخّص القرار المرصود واستدعاء الأداة والمسار والنتيجة والعدادات. لا تلصق سجلات خامًا أو تفكيرًا داخليًا خاصًا.]`

### Redaction check · فحص التنقيح

- [ ] Synthetic identifiers only. · معرفات مصطنعة فقط.
- [ ] No password, token, API key, cookie, private link, or environment value. · لا كلمة مرور أو رمز وصول أو مفتاح API أو Cookie أو رابط خاص أو قيمة بيئة.
- [ ] No real person, customer, employee, order, payment, or support data. · لا بيانات حقيقية لشخص أو عميل أو موظف أو طلب أو دفعة أو دعم.
- [ ] No copied solution, instructor note, answer key, scoring rule, or hidden test. · لا حل منسوخ أو ملاحظة مدربة أو مفتاح إجابة أو قاعدة درجات أو اختبار خفي.
- [ ] No private chain-of-thought. · لا تفكير داخلي خاص.

### Failure note, if applicable · ملاحظة الفشل عند الحاجة

- First useful error · أول خطأ مفيد: `[TODO]`
- Likely control or component · الضابط أو المكون المحتمل: `[TODO]`
- Smallest learner change tried · أصغر تعديل جُرّب: `[TODO]`
- Retest result · نتيجة إعادة الفحص: `[TODO]`
