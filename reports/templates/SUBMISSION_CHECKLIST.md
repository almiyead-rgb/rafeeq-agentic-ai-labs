# Final submission checklist · قائمة التحقق من التسليم النهائي

Check every required item in **your own public repository**. A checked box is a declaration; verify it before marking it complete.

أكمل كل بند إلزامي في **مستودعك العام أنت**. وضع علامة على البند إقرار؛ تحقّق منه قبل اعتماده.

## A. Repository setup · إعداد المستودع

- [ ] During preflight, I created a **new empty public repository** through the GitHub website; I did not use Fork, and I left it completely empty until the clean C29 upload. · أثناء التجهيز المسبق أنشأت **مستودعًا عامًا جديدًا وفارغًا** عبر موقع GitHub، ولم أستخدم Fork، وتركته فارغًا تمامًا حتى رفع C29 النظيف.
- [ ] The repository belongs to my GitHub account and has a clear project name. · المستودع تابع لحسابي في GitHub واسمه واضح.
- [ ] After C29 printed `FINAL_EXPORT_CREATED`, I extracted `rafeeq-mini-submission.zip` and uploaded its clean **contents**. I did not upload the ZIP itself or an extra outer folder. · بعد أن طبع C29 العبارة `FINAL_EXPORT_CREATED`، فككت `rafeeq-mini-submission.zip` ورفعت **محتوياته** النظيفة، ولم أرفع ملف ZIP نفسه أو مجلدًا خارجيًا زائدًا.
- [ ] In Colab I selected **File → Download → Download .ipynb**, named the file `Rafeeq_Mini_Capstone.ipynb`, and placed it in the extracted `notebooks/` folder before upload. · اخترت في كولاب **File → Download → Download .ipynb**، وسمّيت الملف `Rafeeq_Mini_Capstone.ipynb`، ووضعته داخل مجلد `notebooks/` المستخرج قبل الرفع.
- [ ] I did not upload `reports/checkpoints/`; it contains temporary local gate evidence. · لم أرفع `reports/checkpoints/` لأنه يحتوي أدلة بوابات محلية مؤقتة.
- [ ] `README.md`, `notebooks/`, `data/`, `src/`, `reports/`, and `.github/` are visible at the repository root. · تظهر `README.md` و`notebooks/` و`data/` و`src/` و`reports/` و`.github/` في جذر المستودع.
- [ ] The repository URL opens without signing in. · يفتح رابط المستودع دون تسجيل دخول.
- [ ] I used the instructor-assigned `learner_id` or GitHub username in public files; my real name, email, phone number, and national ID appear only in the private hand-in form. · استخدمت `learner_id` الذي تقدمه المدربة أو اسم مستخدم GitHub في الملفات العامة، ولم أضع اسمي الحقيقي أو بريدي أو رقم هاتفي أو هويتي الوطنية إلا في نموذج التسليم الخاص.

## B. Colab and reproducibility · كولاب وقابلية إعادة التشغيل

- [ ] I opened the notebook from the official `almiyead-rgb` course repository using the course Colab link, not from my own repository. · فتحت الدفتر من مستودع الدورة الرسمي `almiyead-rgb` برابط كولاب، لا من مستودعي.
- [ ] I selected **File → Save a copy in Drive** before editing. · اخترت **File → Save a copy in Drive** قبل التعديل.
- [ ] I worked from the saved Drive copy through C29; the preflight GitHub repository remained empty until the final export. · عملت من نسخة Drive المحفوظة حتى C29، وبقي مستودع GitHub المنشأ في التجهيز فارغًا حتى التصدير النهائي.
- [ ] I used Google Colab Free with the standard CPU runtime. · استخدمت Google Colab المجاني وبيئة CPU القياسية.
- [ ] `LLM_MODE=stub` remained the default; the required path uses no paid model or API key. · بقي `LLM_MODE=stub` الوضع الافتراضي، ولا يستخدم المسار الإلزامي نموذجًا مدفوعًا أو مفتاح API.
- [ ] I ran the notebook from `C0` to `C29` in order in a clean runtime. · شغلت الدفتر من `C0` إلى `C29` بالترتيب في بيئة نظيفة.
- [ ] `C0_ENV_DOCTOR` returned `C0 = READY` and `all_passed=true`. · أعاد `C0_ENV_DOCTOR` القيمتين `C0 = READY` و`all_passed=true`.
- [ ] No required output depends on unsaved Colab memory or a file that exists only in `/content`. · لا يعتمد مخرج إلزامي على ذاكرة كولاب غير المحفوظة أو ملف موجود فقط داخل `/content`.

## C. Daily gates · بوابات الأيام

- [ ] `C9_DAY1_GATE` reports `all_passed=true` after `C1_ARCHITECTURE` through `C8_MCP_CLIENT`: typed state, bounded graph, observable traces, ReAct, tool schema, and MCP server/client. · تعرض `C9_DAY1_GATE` القيمة `all_passed=true` بعد `C1_ARCHITECTURE` حتى `C8_MCP_CLIENT`: الحالة المحددة والمخطط المحدود والتتبع المرصود وReAct ومخطط الأداة وخادم/عميل MCP.
- [ ] The Day 1 checkpoint label recorded in Drive/report is `checkpoint(day-1): pass C9 core tools and MCP`. · تسمية نقطة اليوم الأول المسجلة في Drive أو التقرير مطابقة للنص المحدد.
- [ ] `C20_DAY2_GATE` reports `all_passed=true` after restore, session memory, scoped recall, policy retrieval, specialists, supervisor, typed delegation, Plan-and-Execute, refund gate, and interrupt/resume. · تعرض `C20_DAY2_GATE` القيمة `all_passed=true` بعد الاستعادة وذاكرة الجلسة والاسترجاع المعزول والسياسات والوكلاء والمنسق والتفويض المحدد وPlan-and-Execute وبوابة الاسترداد والإيقاف/الاستئناف.
- [ ] The Day 2 checkpoint label recorded in Drive/report is `checkpoint(day-2): pass C20 memory and orchestration`. · تسمية نقطة اليوم الثاني المسجلة في Drive أو التقرير مطابقة للنص المحدد.
- [ ] The enabled final `C29_EXPORT_SAFETY_CHECK` prints `FINAL_EXPORT_CREATED` after threat model, attack suite, guard fix/retest, reflection gate, trace evaluation, one measured optimization, scorecard, and readiness. · يطبع التشغيل النهائي المفعّل لـ`C29_EXPORT_SAFETY_CHECK` العبارة `FINAL_EXPORT_CREATED` بعد نموذج التهديد وحزمة الهجوم وإصلاح الحاجز وإعادة الفحص وبوابة المراجعة وتقييم التتبع وتحسين واحد مقاس وبطاقة الأداء والجاهزية.
- [ ] I completed `TODO-14`, set all four review flags to `True`, enabled `FINAL_EXPORT`, and received `FINAL_EXPORT_CREATED`. · أكملت `TODO-14` وضبطت علامات المراجعة الأربع على `True` وفعّلت `FINAL_EXPORT` وظهرت `FINAL_EXPORT_CREATED`.
- [ ] The GitHub upload commit message is `feat: submit Rafeeq Mini capstone`. · رسالة Commit لرفع GitHub مطابقة للنص المحدد.

## D. Required project files · ملفات المشروع المطلوبة

- [ ] `notebooks/Rafeeq_Mini_Capstone.ipynb` exists and contains my completed learner work. · يوجد الدفتر ويحتوي على عملي المكتمل.
- [ ] `reports/PROJECT_REPORT.md` is complete and links claims to evidence. · تقرير المشروع مكتمل ويربط الادعاءات بالأدلة.
- [ ] `reports/SECURITY_ASSESSMENT.md` is complete and records residual risk. · التقييم الأمني مكتمل ويسجل المخاطر المتبقية.
- [ ] `reports/trace.jsonl` is sanitized and visible in the public repository. · يظهر `reports/trace.jsonl` المنقح في المستودع العام.
- [ ] `reports/assessment_results.json` is visible in the public repository. · يظهر `reports/assessment_results.json` في المستودع العام.
- [ ] `reports/monitoring_dashboard.png` is visible in the public repository. · تظهر `reports/monitoring_dashboard.png` في المستودع العام.
- [ ] `reports/submission_manifest.json` is visible in the public repository and reports `all_passed=true`. · يظهر `reports/submission_manifest.json` في المستودع العام ويعرض `all_passed=true`.
- [ ] `reports/EVIDENCE_CARD.md` contains three completed, sanitized cards—one per day—created from the required template after extraction. · يحتوي `reports/EVIDENCE_CARD.md` ثلاث بطاقات مكتملة ومنقحة—بطاقة لكل يوم—منشأة من القالب الإلزامي بعد فك الحزمة.
- [ ] `rafeeq-mini-submission.zip`, temporary checkpoints, and raw outputs were not uploaded. · لم أرفع `rafeeq-mini-submission.zip` أو نقاط التقدم المؤقتة أو المخرجات الخام.
- [ ] The reports contain actual values from my final run; unmeasured metrics are marked `Not measured`. · تحتوي التقارير على قيم تشغيل فعلية، والمقاييس غير المنفذة محددة بـ`Not measured`.

## E. Safety and integrity · السلامة والنزاهة

- [ ] I used supplied synthetic data only. · استخدمت البيانات المصطنعة المرفقة فقط.
- [ ] No real customer, employee, trainee, order, payment, or support data is present. · لا توجد بيانات حقيقية لعميل أو موظف أو متدرب أو طلب أو دفعة أو دعم.
- [ ] No password, token, API key, cookie, private link, `.env`, or environment file containing secrets is present. The supplied credential-free `.env.example` is allowed. · لا توجد كلمة مرور أو رمز وصول أو مفتاح API أو Cookie أو رابط خاص أو `.env` أو ملف بيئة يحمل أسرارًا. يُسمح بملف `.env.example` المرفق والخالي من بيانات الدخول.
- [ ] No copied solution, answer key, instructor material, grade, scoring rule, recovery checkpoint, or hidden test is present. · لا يوجد حل منسوخ أو مفتاح إجابة أو مادة للمدربة أو درجة أو قاعدة تقييم أو نقطة استعادة أو اختبار خفي.
- [ ] Traces contain observable decisions and tool results only; no private chain-of-thought is stored. · تتضمن سجلات التتبع القرارات المرصودة ونتائج الأدوات فقط، ولا تخزن التفكير الداخلي الخاص.
- [ ] All refund and action results are clearly marked as simulations. · جميع نتائج الاسترداد والإجراءات موضحة بصفتها محاكاة.
- [ ] I did not commit `rafeeq-mini-submission.zip`, raw trace dumps, or temporary runtime files. · لم أرفع `rafeeq-mini-submission.zip` أو سجلات خامًا أو ملفات مؤقتة لبيئة التشغيل.

## F. GitHub Actions verification · التحقق عبر GitHub Actions

- [ ] I opened **Actions → Learner submission quality** for the exact final commit and waited until it showed a green check. · فتحت **Actions ← Learner submission quality** لنفس Commit النهائي وانتظرت حتى ظهرت العلامة الخضراء.
- [ ] If a run was red, I opened the first failed step, repaired the smallest relevant learner TODO in the saved Drive notebook, reran dependent gates through C29, exported again, and uploaded a new commit. · إذا كان التشغيل أحمر فقد فتحت أول خطوة فاشلة، وأصلحت أصغر TODO مرتبط في دفتر Drive، وأعدت البوابات التابعة حتى C29 والتصدير، ثم رفعت Commit جديدًا.
- [ ] I did not edit workflows, validators, public tests, or generated evidence to hide a failure. · لم أعدّل Workflows أو أدوات التحقق أو الاختبارات العامة أو الأدلة المولدة لإخفاء فشل.

## G. Final hand-in record · سجل التسليم النهائي

Complete this block in the designated hand-in form **after** the GitHub upload. Do not edit and recommit a repository file merely to insert the SHA of the commit that already contains it.

أكمل هذا الجزء في نموذج التسليم المحدد **بعد** رفع GitHub. لا تعدّل ملفًا داخل المستودع وتعيد رفعه فقط لإضافة معرف Commit الذي يحتوي الملف نفسه.

| Item | Value · القيمة |
|---|---|
| Public learner ID · معرف المتدرب العام | `[learner_id]` |
| Public repository URL · رابط المستودع العام | `[TODO]` |
| Final notebook URL · رابط الدفتر النهائي | `[TODO]` |
| Final commit URL · رابط آخر Commit | `[TODO]` |
| Final commit SHA · معرف آخر Commit | `[TODO]` |
| `C9_DAY1_GATE` marker | `all_passed=true / all_passed=false` |
| `C20_DAY2_GATE` marker | `all_passed=true / all_passed=false` |
| Final `C29_EXPORT_SAFETY_CHECK` marker | `FINAL_EXPORT_CREATED / FINAL_EXPORT_BLOCKED / FINAL_EXPORT_SKIPPED` |
| Clean run date (UTC) · تاريخ التشغيل النظيف | `[TODO]` |
| **Learner submission quality** | `GREEN / RED / PENDING` |

- [ ] I used the private hand-in form/link provided by the instructor; I did not invent or infer a public submission destination. · استخدمت رابط/نموذج التسليم الخاص الذي تقدمه المدربة، ولم أفترض وجهة تسليم عامة.
- [ ] I followed the deadline and late/resubmission policy provided by the instructor during the course. · اتبعت الموعد النهائي وسياسة التأخير/إعادة التسليم التي تقدمها المدربة أثناء الدورة.
- [ ] I kept the receipt/confirmation issued by the form or instructor. I understand that a green Actions run is not proof of receipt. · احتفظت بإثبات/تأكيد الاستلام الصادر من النموذج أو المدربة، وأفهم أن نجاح Actions ليس إثبات استلام.
- [ ] If I resubmitted, I preserved commit history, submitted a new green commit, and updated the private form with the new commit URL according to the instructor's policy. · إذا أعدت التسليم فقد حافظت على سجل Commits، وأرسلت Commit جديدًا ناجحًا، وحدّثت النموذج الخاص برابط Commit الجديد وفق سياسة المدربة.

## Pass gate · شرط الاجتياز

The submission is ready for assessment only when the repository is public and accessible, extracted project files are visible, C9 and C20 show `all_passed=true`, the enabled final C29 run prints `FINAL_EXPORT_CREATED`, both learner reports, all four generated artifacts, and the three required evidence cards are complete, the exact final commit has a green **Learner submission quality** run, and every safety declaration above is true.

يصبح التسليم جاهزًا للتقييم فقط عندما يكون المستودع عامًا ويمكن الوصول إليه، وتظهر ملفات المشروع المستخرجة، وتعرض C9 وC20 القيمة `all_passed=true`، ويطبع تشغيل C29 النهائي المفعّل `FINAL_EXPORT_CREATED`، ويكتمل تقريرا المتدرب والملفات الأربعة المولدة وبطاقات الأدلة الثلاث، ويظهر فحص **Learner submission quality** أخضر لنفس Commit النهائي، وتكون جميع إقرارات السلامة أعلاه صحيحة.
