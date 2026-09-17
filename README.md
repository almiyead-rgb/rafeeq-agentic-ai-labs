# Rafeeq Mini Labs · لابات رفيق المصغّر

> **Pre-release `0.1.0-alpha` — not ready for learner use.**  
> **إصدار تمهيدي `0.1.0-alpha` — غير جاهز لاستخدام المتدربين.**

A bilingual, beginner-first learning portal and cumulative lab for **Advanced Agentic AI Systems Engineering**.

بوابة تعلم ثنائية اللغة ولاب تراكمي مهيأ للمبتدئين لدورة **هندسة أنظمة الذكاء الاصطناعي التوكيلي المتقدمة**.

## Foundation status · حالة التأسيس

This repository currently contains the approved static portal foundation, governance files, and protected folder boundaries. It intentionally does **not** contain a runnable notebook, datasets, agent code, tests, or an active Colab link yet.

يحتوي المستودع حاليًا على الأساس المعتمد للبوابة الثابتة، وملفات الحوكمة، وحدود المجلدات المحمية. ولا يحتوي عمدًا حتى الآن على دفتر قابل للتشغيل أو بيانات أو كود للوكلاء أو اختبارات أو رابط كولاب فعّال.

## Target learner experience · تجربة المتدرب المستهدفة

```text
Learn → Open Colab → Complete TODO → Run Test → Save Evidence → Checkpoint
```

- One cumulative notebook covering planned cells `C0–C29`.
- Three in-person training days.
- Google Colab Free with the standard CPU runtime.
- `LLM_MODE=stub` as the mandatory default.
- No API key, GPU, terminal, PAT, or paid service required.
- English on the left and Arabic on the right in the dual-language view.
- Simulated educational data only.

---

- دفتر تراكمي واحد يغطي الخلايا المخطط لها `C0–C29`.
- ثلاثة أيام تدريب حضورية.
- Google Colab المجاني مع بيئة CPU القياسية.
- الوضع الإلزامي الافتراضي هو `LLM_MODE=stub`.
- لا حاجة إلى مفتاح API أو GPU أو Terminal أو PAT أو خدمة مدفوعة.
- الإنجليزية يسارًا والعربية يمينًا في العرض الثنائي.
- بيانات تعليمية مصطنعة فقط.

## Repository map · خريطة المستودع

| Path | Purpose · الغرض | Foundation state · حالة التأسيس |
|---|---|---|
| `docs/` | GitHub Pages learner portal · بوابة المتدرب | Static pre-release homepage · صفحة تمهيدية ثابتة |
| `notebooks/` | Cumulative Colab notebook · دفتر كولاب التراكمي | Reserved · محجوز |
| `data/public/` | Public synthetic datasets · البيانات المصطنعة العامة | Reserved · محجوز |
| `src/rafeeq/` | Reusable project code · كود المشروع القابل لإعادة الاستخدام | Reserved · محجوز |
| `mcp_server/` | Local MCP server · خادم MCP المحلي | Reserved · محجوز |
| `tests/public/` | Learner-visible tests · الاختبارات العامة | Reserved · محجوز |
| `tests/schemas/` | Data and output schemas · مخططات البيانات والمخرجات | Reserved · محجوز |
| `reports/templates/` | Report templates · قوالب التقارير | Reserved · محجوز |
| `reports/checkpoints/` | Locally generated evidence · أدلة التشغيل المحلية | Ignored by Git · مستثنى من Git |
| `recovery/` | Public recovery policy only · سياسة الاستعادة العامة فقط | Policy scaffold · أساس السياسة |

Hidden evaluations, answer keys, instructor notes, and actual recovery checkpoints must remain in the separate private instructor repository. They must never be stored in a branch, tag, release, issue, or history of this public repository.

يجب أن تبقى التقييمات الخفية ومفاتيح الإجابات وملاحظات المدربة ونقاط الاستعادة الفعلية في مستودع المدربة الخاص والمنفصل. ويُمنع وضعها في أي فرع أو وسم أو إصدار أو Issue أو سجل لهذا المستودع العام.

## Portal preview · معاينة البوابة

Open [`docs/index.html`](docs/index.html) locally. The page is deliberately marked **Pre-release** and does not expose an active notebook or Colab action.

افتح [`docs/index.html`](docs/index.html) محليًا. تحمل الصفحة وسم **إصدار تمهيدي** عمدًا، ولا تعرض دفترًا أو إجراء كولاب فعّالًا.

## Foundation verification · فحص الأساس

```bash
python scripts/validate_foundation.py
```

The validator checks required files, local page references, JSON validity, forbidden public paths, zero-byte files, common secret patterns, and the pre-release gate.

يتحقق الفاحص من الملفات المطلوبة، وروابط الصفحة المحلية، وصحة JSON، والمسارات المحظورة في العام، والملفات الفارغة، وأنماط الأسرار الشائعة، وبوابة الإصدار التمهيدي.

## Instructor · المدربة

**Meaad Al-Marri · ميعاد المري**

The course portal may link to [SDAIA Academy on GitHub](https://github.com/SDAIAAcademy) as an external reference. This pre-release does not use an official logo or claim official endorsement, approval, or ownership.

قد تربط بوابة الدورة إلى [SDAIA Academy on GitHub](https://github.com/SDAIAAcademy) بوصفه مرجعًا خارجيًا. لا يستخدم هذا الإصدار التمهيدي شعارًا رسميًا ولا يدّعي اعتمادًا أو موافقة أو ملكية رسمية.

## License status · حالة الترخيص

No license has been selected during the foundation phase. All rights remain reserved until content ownership and the publishing authority are confirmed.

لم تُعتمد رخصة خلال مرحلة التأسيس. تبقى جميع الحقوق محفوظة حتى تأكيد ملكية المحتوى والجهة المخولة بالنشر.

Educational simulation only. Never enter real customer data, credentials, private links, or API keys.

محاكاة تعليمية فقط. لا تُدخل بيانات عملاء حقيقية أو بيانات دخول أو روابط خاصة أو مفاتيح API.
