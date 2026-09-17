# Learner guide · دليل المتدرب

This guide is the beginner path from an empty GitHub account to a verified Rafeeq Mini submission. The project uses free Google Colab CPU, synthetic data, and a deterministic stub model.

هذا الدليل هو المسار المبسط من حساب GitHub جديد إلى تسليم رفيق المصغّر المتحقق منه. يستخدم المشروع Google Colab CPU المجاني وبيانات مصطنعة ونموذج Stub حتميًا.

## 1. Project scenario · سيناريو المشروع

Rafeeq Mini is a bilingual agentic operations assistant for a fictional delivery company. It understands an Arabic or English order/refund request, verifies the supplied synthetic customer scope, retrieves the active policy, routes the task to a specialist, and pauses a simulated refund above SAR 500 for documented human approval.

رفيق المصغّر مساعد عمليات وكيلي ثنائي اللغة لشركة توصيل افتراضية. يفهم طلبًا بالعربية أو الإنجليزية عن طلب شراء أو استرداد، ويتحقق من نطاق العميل المصطنع، ويسترجع السياسة السارية، ويوجه المهمة إلى وكيل متخصص، ويوقف الاسترداد المحاكى الأعلى من 500 ريال حتى توثيق الموافقة البشرية.

No real customer, payment, order, or enterprise system is used.

لا يستخدم المشروع أي عميل أو دفعة أو طلب أو نظام مؤسسي حقيقي.

## 2. Create the accounts once · إنشاء الحسابات مرة واحدة

| Service | Beginner action | إجراء المبتدئ |
|---|---|---|
| GitHub | Create an account, verify the email, and keep the username available. Use a password manager and enable account protections offered by GitHub. [Official account guide](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) | أنشئ حسابًا، وفعّل البريد، واحتفظ باسم المستخدم. استخدم مدير كلمات مرور وفعّل وسائل حماية الحساب التي يوفرها GitHub. [الدليل الرسمي](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) |
| Google Colab | Open [Google Colab](https://colab.research.google.com/) with the Google account that will hold your Drive copy. | افتح [Google Colab](https://colab.research.google.com/) بالحساب الذي سيحفظ نسخة الدفتر في Drive. |

Never share a password, one-time code, recovery code, token, or API key with the instructor, another learner, an issue, or a notebook.

لا تشارك كلمة مرور أو رمز تحقق أو رمز استعادة أو Token أو مفتاح API مع المدربة أو متدرب آخر أو Issue أو دفتر كولاب.

## 3. Open the official course notebook · افتح دفتر الدورة الرسمي

Your starting point is the notebook in the official course repository owned by `almiyead-rgb`—not a learner repository. Open it with the course Colab button/link below:

نقطة البداية هي الدفتر في مستودع الدورة الرسمي التابع للحساب `almiyead-rgb`، وليس مستودع المتدرب. افتحه بزر/رابط كولاب الآتي:

**[Open the official Rafeeq Mini notebook in Google Colab · افتح دفتر رفيق الرسمي في كولاب](https://colab.research.google.com/github/almiyead-rgb/rafeeq-agentic-ai-labs/blob/main/notebooks/Rafeeq_Mini_Capstone.ipynb)**

1. Confirm the address contains `github/almiyead-rgb/rafeeq-agentic-ai-labs`. · تأكد أن العنوان يحتوي `github/almiyead-rgb/rafeeq-agentic-ai-labs`.
2. Immediately select **File → Save a copy in Drive**. · اختر فورًا **File → Save a copy in Drive**.
3. Work only in that Drive copy; do not edit the official source. · اعمل فقط في نسخة Drive، ولا تعدل المصدر الرسمي.
4. Keep the original cell IDs `C0–C29` and use the standard CPU runtime; no GPU is needed. · احتفظ بمعرفات الخلايا `C0–C29` واستخدم CPU القياسي؛ لا حاجة إلى GPU.

Official reference: [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)

## 4. Build in Drive until C29 · ابنِ المشروع في Drive حتى C29

You do **not** need your own GitHub repository before C29. Across the three days, reopen your saved Drive copy, run from the top, complete only learner `TODO` areas, and save after every passed gate. The two daily checkpoint messages are labels in the notebook/report, not Git commits.

لا تحتاج إلى مستودع GitHub خاص بك قبل C29. خلال الأيام الثلاثة، أعد فتح نسخة Drive المحفوظة، وشغّل من الأعلى، وأكمل مناطق `TODO` الخاصة بالمتدرب فقط، واحفظ بعد كل بوابة ناجحة. رسالتا نقطتي التقدم اليوميتين تسميات داخل الدفتر/التقرير، وليستا Git commits.

## 5. At C29, create the repository and upload the clean export · عند C29 أنشئ المستودع وارفع التصدير النظيف

Only after `C29_EXPORT_SAFETY_CHECK` passes, create or use your own **empty public repository**. The guaranteed beginner path uses the GitHub website and requires no terminal, PAT, or template setting.

بعد نجاح `C29_EXPORT_SAFETY_CHECK` فقط، أنشئ أو استخدم مستودعك العام **الفارغ**. يستخدم مسار المبتدئ المضمون موقع GitHub، ولا يحتاج إلى Terminal أو PAT أو تفعيل قالب.

1. While signed in, select **+ → New repository**, choose your personal account, and use a clear name such as `rafeeq-mini-yourusername`. · بعد تسجيل الدخول اختر **+ → New repository**، ثم حسابك الشخصي، واستخدم اسمًا واضحًا مثل `rafeeq-mini-yourusername`.
2. Select **Public**. Leave README, `.gitignore`, license, and template options unselected so the repository is empty. · اختر **Public**، واترك README و`.gitignore` والرخصة والقالب دون تحديد ليبقى المستودع فارغًا.
3. Select **Create repository**. Do **not** use Fork; this is a standalone project, not a contribution to the instructor repository. · اختر **Create repository**. لا تستخدم **Fork**؛ هذا مشروع مستقل وليس مساهمة في مستودع المدربة.

Official reference: [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

If the instructor later enables and announces a verified GitHub template, you may use **Use this template → Create a new repository** instead. The guaranteed path does not depend on that option, and Fork remains prohibited.

إذا فعّلت المدربة لاحقًا قالب GitHub موثقًا وأعلنت عنه، فيمكن استخدام **Use this template → Create a new repository** بدلًا من ذلك. لا يعتمد المسار المضمون على هذا الخيار، ويظل Fork ممنوعًا.

Now prepare and upload the clean export—not the ZIP:

الآن جهّز التصدير النظيف وارفعه، لا ملف ZIP:

Complete `TODO-14`, confirm all four review flags are `True`, deliberately enable the `FINAL_EXPORT` switch, and rerun C29. `FINAL_EXPORT_SKIPPED` means the switch is still off; `FINAL_EXPORT_BLOCKED` means at least one safety or completion gate still fails.

أكمل `TODO-14`، وتأكد أن علامات المراجعة الأربع `True`، ثم فعّل مفتاح `FINAL_EXPORT` عمدًا وأعد تشغيل C29. تعني `FINAL_EXPORT_SKIPPED` أن المفتاح ما زال مغلقًا، وتعني `FINAL_EXPORT_BLOCKED` أن أحد فحوص السلامة أو الاكتمال ما زال فاشلًا.

1. Confirm that C29 prints `FINAL_EXPORT_CREATED`. In Colab open the left **Files** pane, locate the printed path for `rafeeq-mini-submission.zip`, open its three-dot menu, and select **Download**. · تأكد أن C29 يعرض `FINAL_EXPORT_CREATED`. افتح لوحة **Files** اليسرى في كولاب، وحدد المسار المطبوع لملف `rafeeq-mini-submission.zip`، ثم افتح قائمة النقاط الثلاث واختر **Download**.
2. Extract the ZIP on your computer. · فك ضغط الملف على جهازك.
3. Inspect the extracted tree. It contains the sanitized public template files and required reports, but deliberately excludes the notebook currently open in Colab and `reports/checkpoints/`. · افحص البنية المستخرجة؛ تحتوي ملفات القالب العامة المنقحة والتقارير المطلوبة، لكنها تستبعد عمدًا دفتر كولاب الجاري ومجلد `reports/checkpoints/`.
4. In Colab select **File → Download → Download .ipynb**. This downloads your completed working copy. · في كولاب اختر **File → Download → Download .ipynb** لتنزيل نسخة عملك المكتملة.
5. Rename the downloaded file exactly `Rafeeq_Mini_Capstone.ipynb` if needed, then place it inside the extracted `notebooks/` folder. · عند الحاجة أعد تسمية الملف إلى `Rafeeq_Mini_Capstone.ipynb` بالضبط، ثم ضعه داخل مجلد `notebooks/` المستخرج.
6. Confirm the combined folder now contains `notebooks/Rafeeq_Mini_Capstone.ipynb`, `reports/PROJECT_REPORT.md`, `reports/SECURITY_ASSESSMENT.md`, `reports/trace.jsonl`, `reports/assessment_results.json`, `reports/monitoring_dashboard.png`, and `reports/submission_manifest.json`. · تأكد أن المجلد المدمج يحتوي الدفتر والتقريرين والملفات الأربعة بالمسارات المحددة.
7. Remove nothing required, but do not add `rafeeq-mini-submission.zip`, `reports/checkpoints/`, raw outputs outside the sanitized trace, temporary runtime files, credentials, private links, or real data. · لا تحذف ملفًا إلزاميًا، ولا تضف `rafeeq-mini-submission.zip` أو `reports/checkpoints/` أو مخرجات خامًا خارج الأثر المنقح أو ملفات تشغيل مؤقتة أو بيانات دخول أو روابط خاصة أو بيانات حقيقية.
8. In your empty repository select **Add file → Upload files**. · في مستودعك الفارغ اختر **Add file → Upload files**.
9. Drag the **contents inside** the combined folder. Do not upload only the ZIP, and do not create an extra outer folder. · اسحب **المحتويات داخل** المجلد المدمج؛ لا ترفع ملف ZIP فقط ولا تنشئ مجلدًا خارجيًا زائدًا.
10. Use the commit message `feat: submit Rafeeq Mini capstone`. · استخدم رسالة الحفظ `feat: submit Rafeeq Mini capstone`.
11. Verify that `README.md`, `notebooks/`, `data/`, `src/`, `mcp_server/`, `tests/`, and `reports/` appear at the repository root. · تحقق من ظهور `README.md` والمجلدات المذكورة في جذر المستودع.

Official reference: [Adding a file to a repository](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)

## 6. Use the safe run loop · استخدم دورة التشغيل الآمنة

For every learner task:

لكل مهمة متدرب:

```text
Read the objective → complete TODO → run the cell → run the public check
→ inspect the result → save in Drive → continue only after PASS
```

```text
اقرأ الهدف ← أكمل TODO ← شغّل الخلية ← شغّل الفحص العام
← افحص النتيجة ← احفظ في Drive ← لا تنتقل إلا بعد PASS
```

- Run from top to bottom. Do not skip dependencies. · شغّل من الأعلى إلى الأسفل ولا تتجاوز الاعتماديات.
- Change only learner `TODO` areas. · عدّل مناطق `TODO` الخاصة بالمتدرب فقط.
- Do not bypass a failed check. Read its message and repair the smallest relevant learner change. · لا تتحايل على فحص فاشل؛ اقرأ رسالته وأصلح أصغر تعديل مرتبط.
- Do not store private chain-of-thought. Keep only decision, tool, route, result, counters, and a short operational rationale. · لا تخزن التفكير الداخلي الخاص؛ احتفظ بالقرار والأداة والمسار والنتيجة والعدادات ومبرر تشغيلي قصير.

## 7. Three-day progression · التدرج خلال ثلاثة أيام

| Day | Cells | Build outcome · ناتج البناء | Gate |
|---|---|---|---|
| Day 1 · اليوم الأول | `C0–C9` | Architecture, typed state, bounded graph, observable traces, ReAct, tool schema, and local MCP server/client. · معمارية وحالة محددة ومخطط محدود وتتبع مرصود وReAct ومخطط أداة وخادم/عميل MCP محلي. | `C9_DAY1_GATE` |
| Day 2 · اليوم الثاني | `C10–C20` | Restore, session memory, scoped recall, policy retrieval, specialists, supervisor, typed delegation, Plan-and-Execute, and interrupt/resume approval. · استعادة وذاكرة جلسة واسترجاع معزول وسياسات ووكلاء ومنسق وتفويض محدد وPlan-and-Execute وإيقاف/استئناف للموافقة. | `C20_DAY2_GATE` |
| Day 3 · اليوم الثالث | `C21–C29` | Threat model, attack suite, guard fix/retest, reflection gate, trace evaluation, one measured optimization, scorecard, readiness, and safe export. · نموذج تهديد وحزمة هجوم وإصلاح وإعادة فحص وبوابة مراجعة وتقييم تتبع وتحسين واحد مقاس وبطاقة أداء وجاهزية وتصدير آمن. | `C29_EXPORT_SAFETY_CHECK` |

Full cell mapping: [`notebooks/README.md`](../notebooks/README.md)

## 8. Save daily checkpoints · احفظ نقاط التقدم اليومية

After each gate passes, save the Drive notebook and record the matching checkpoint label in the notebook/report. In the guaranteed empty-repository path, only the final line is used as the GitHub upload commit message:

بعد نجاح كل بوابة احفظ دفتر Drive وسجل تسمية نقطة التقدم المطابقة في الدفتر أو التقرير. في مسار المستودع الفارغ المضمون تُستخدم الرسالة الأخيرة فقط بوصفها رسالة GitHub عند الرفع:

```text
checkpoint(day-1): pass C9 core tools and MCP
checkpoint(day-2): pass C20 memory and orchestration
feat: submit Rafeeq Mini capstone
```

The first two lines document the Day 1 and Day 2 gates; they are not required Git commits while the repository is empty. The final line is the commit message for uploading the extracted C29 files. If a verified template workflow is enabled later, the instructor may authorize daily commits using the same labels.

توثق الرسالتان الأوليان بوابتي اليومين الأول والثاني، وليستا Git commits إلزاميين ما دام المستودع فارغًا. الرسالة الأخيرة هي رسالة Commit لرفع ملفات C29 المستخرجة. إذا فُعّل لاحقًا مسار قالب موثق، فقد تسمح المدربة بعمليات حفظ يومية بالتسميات نفسها.

Inspect every exported file before uploading. A commit must never include a credential, private link, real data, raw runtime dump, completed solution, instructor material, hidden test, temporary checkpoint, or `rafeeq-mini-submission.zip`.

افحص كل ملف مصدّر قبل رفعه. ويُمنع أن يتضمن Commit بيانات دخول أو رابطًا خاصًا أو بيانات حقيقية أو سجل تشغيل خامًا أو حلًا مكتملًا أو مادة للمدربة أو اختبارًا خفيًا أو نقطة مؤقتة أو `rafeeq-mini-submission.zip`.

## 9. Recover after Runtime loss · استعد العمل بعد فقد البيئة

Colab may disconnect or reset. This does not mean the project is lost.

قد يفصل كولاب الاتصال أو يعيد ضبط البيئة، وهذا لا يعني فقد المشروع.

1. Reopen the latest Drive copy. · افتح أحدث نسخة في Drive.
2. Select CPU and run `C0_ENV_DOCTOR`. · اختر CPU وشغّل `C0_ENV_DOCTOR`.
3. Rerun completed cells from the top to rebuild Python state. · أعد تشغيل الخلايا المكتملة من الأعلى لبناء حالة Python.
4. Stop at your last passed gate, compare it with the saved checkpoint label and gate evidence, then continue. · توقف عند آخر بوابة ناجحة وقارنها بتسمية نقطة التقدم ودليل البوابة المحفوظين ثم تابع.

Detailed recovery: [`recovery/README.md`](../recovery/README.md)

## 10. Complete the reports · أكمل التقارير

The notebook generates the two required learner reports: `C23_GUARD_FIX_RETEST` creates the security assessment and `C28_READINESS` creates the project report.

يولد الدفتر تقريري المتدرب الإلزاميين: تنشئ `C23_GUARD_FIX_RETEST` التقييم الأمني، وتنشئ `C28_READINESS` تقرير المشروع.

- `reports/PROJECT_REPORT.md`
- `reports/SECURITY_ASSESSMENT.md`

Use [`reports/templates/SUBMISSION_CHECKLIST.md`](../reports/templates/SUBMISSION_CHECKLIST.md) locally before upload. It is a verification aid, not a seventh deliverable.

استخدم [`reports/templates/SUBMISSION_CHECKLIST.md`](../reports/templates/SUBMISSION_CHECKLIST.md) محليًا قبل الرفع. هي أداة تحقق وليست مخرجًا سابعًا.

Review the generated reports for accuracy. The detailed templates in `reports/templates/` are optional enrichment references; do not replace a failed result or invent a value. If the instructor requests enrichment, edit only after the final generating cell so a rerun does not overwrite your work.

راجع دقة التقريرين المولدين. القوالب المفصلة في `reports/templates/` مراجع اختيارية للإثراء؛ لا تستبدل نتيجة فاشلة ولا تخترع قيمة. إذا طلبت المدربة إثراءً إضافيًا فعدّل بعد آخر خلية تولد التقرير حتى لا تمحو إعادة التشغيل عملك.

The clean final run generates `reports/trace.jsonl` at C25, `reports/assessment_results.json` and `reports/monitoring_dashboard.png` at C27, and the reports/readiness result at C28. C29 performs the final safety check, creates `reports/submission_manifest.json`, and packages the clean files. These four sanitized artifacts are required inside the extracted C29 files uploaded to the learner repository. `EVIDENCE_CARD_TEMPLATE.md` is an optional aid for structuring claims inside the two required reports.

ينتج التشغيل النهائي النظيف `reports/trace.jsonl` عند C25، و`reports/assessment_results.json` و`reports/monitoring_dashboard.png` عند C27، والتقارير/نتيجة الجاهزية عند C28. ينفذ C29 فحص السلامة النهائي، وينشئ `reports/submission_manifest.json`، ويحزم الملفات النظيفة. هذه الملفات الأربعة المنقحة إلزامية داخل ملفات C29 المستخرجة التي تُرفع إلى مستودع المتدرب. قالب `EVIDENCE_CARD_TEMPLATE.md` أداة اختيارية لتنظيم الادعاءات داخل التقريرين الإلزاميين.

When `C29_EXPORT_SAFETY_CHECK` succeeds, it creates `rafeeq-mini-submission.zip` as a transport container. Extract it and upload its clean contents as described in section 5; do not upload the ZIP itself.

عند نجاح `C29_EXPORT_SAFETY_CHECK` ينشئ `rafeeq-mini-submission.zip` بوصفه حاوية نقل. فك ضغطه وارفع محتوياته النظيفة كما في القسم 5، ولا ترفع ملف ZIP نفسه.

Use the templates in [`reports/templates/`](../reports/templates/). Every important claim needs a cell ID, a public case or metric, and its result; add the assessment `run_id` from `reports/assessment_results.json` when available. Do not invent a C29 export ID. After export, the manifest timestamp and SHA-256 values may be used for file verification, not as required fields inside reports generated earlier. Record the final repository and commit links in the designated hand-in form after upload.

استخدم القوالب في [`reports/templates/`](../reports/templates/). يحتاج كل ادعاء مهم إلى رقم خلية وحالة عامة أو مقياس ونتيجته؛ وأضف `run_id` للتقييم من `reports/assessment_results.json` عند توفره. لا تخترع معرفًا لتصدير C29. بعد التصدير يمكن استخدام وقت البيان وقيم SHA-256 للتحقق من الملفات، وليس كحقول مطلوبة داخل تقارير مولدة سابقًا. سجل رابط المستودع وCommit النهائيين في نموذج التسليم المحدد بعد الرفع.

## 11. Pass conditions · شروط الاجتياز

Your project is ready for assessment only when all conditions below are true:

يكون مشروعك جاهزًا للتقييم فقط عند تحقق جميع الشروط التالية:

- Your repository is public, owned by you, created as a new repository through the browser, and is not a fork. · مستودعك عام وتملكه أنت ومنشأ كمستودع جديد عبر المتصفح وليس Fork.
- The extracted project tree is visible; the repository is not a ZIP-only upload. · تظهر بنية ملفات المشروع المستخرجة، ولا يقتصر المستودع على ملف ZIP.
- The final notebook opens and runs from `C0` to `C29` on Colab Free CPU with `LLM_MODE=stub`. · يفتح الدفتر النهائي ويعمل من `C0` إلى `C29` على Colab Free CPU بوضع `LLM_MODE=stub`.
- `C9_DAY1_GATE` and `C20_DAY2_GATE` each report `all_passed=true`, and the enabled final C29 run prints `FINAL_EXPORT_CREATED`. · تعرض كل من `C9_DAY1_GATE` و`C20_DAY2_GATE` القيمة `all_passed=true`، ويطبع تشغيل C29 النهائي بعد تفعيله `FINAL_EXPORT_CREATED`.
- The project report, security assessment, sanitized trace, assessment results, monitoring dashboard, and manifest are visible and mutually consistent. · تقرير المشروع والتقييم الأمني والأثر المنقح ونتائج التقييم ولوحة المراقبة وبيان التسليم ظاهرة ومتسقة.
- The final checkpoint commit is present and its link is recorded. · يوجد Commit النهائي ومسجل رابطه.
- The repository contains no real data, credentials, private links, copied solutions, instructor material, recovery answers, grades, or hidden tests. · يخلو المستودع من البيانات الحقيقية وبيانات الدخول والروابط الخاصة والحلول المنسوخة ومواد المدربة وإجابات الاستعادة والدرجات والاختبارات الخفية.

## 12. Ask for help efficiently · اطلب المساعدة بكفاءة

Provide only these six items:

قدّم هذه العناصر الستة فقط:

1. Cell ID. · رقم الخلية.
2. Last passed gate. · آخر بوابة ناجحة.
3. First useful error line. · أول سطر خطأ مفيد.
4. Expected behavior. · السلوك المتوقع.
5. Actual behavior. · السلوك الفعلي.
6. Runtime type and whether it reset. · نوع البيئة وهل أعيد ضبطها.

Remove all private values before posting. Never paste a password, token, API key, private repository link, real record, or full browser screenshot.

احذف جميع القيم الخاصة قبل النشر. لا تلصق كلمة مرور أو Token أو مفتاح API أو رابط مستودع خاص أو سجلًا حقيقيًا أو لقطة كاملة للمتصفح.

Official GitHub help: [GitHub Docs](https://docs.github.com/)
