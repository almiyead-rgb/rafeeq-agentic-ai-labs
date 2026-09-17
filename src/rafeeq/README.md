# Rafeeq runtime package · حزمة تشغيل رفيق

| English | العربية |
|---|---|
| This package is the reusable, offline-first core shared by the cumulative notebook, public tests, and command-line checks. | هذه الحزمة هي النواة القابلة لإعادة الاستخدام والمشتركة بين الدفتر التراكمي والاختبارات العامة وفحوص سطر الأوامر. |
| The mandatory path supports only `LLM_MODE=stub`; it needs no network connection, model API key, GPU, or paid service. | يدعم المسار الإلزامي الوضع `LLM_MODE=stub` فقط، ولا يحتاج شبكة أو مفتاح نموذج أو GPU أو خدمة مدفوعة. |

## Components · المكونات

- `state.py`, `config.py`: typed state and hard limits `6/12/2/1` · الحالة المحددة والحدود الصلبة.
- `graph.py`, `agents.py`, `approval.py`: bounded supervisor, two specialists, refund and approval gates · المنسق والوكيلان وبوابتا الاسترداد والموافقة.
- `memory.py`, `retrieval.py`: scoped recall and current-policy retrieval · استرجاع مقيّد وسياسات سارية.
- `mcp_client.py`: real local `stdio` adapter and subprocess lifecycle · عميل MCP محلي وإدارة العملية الفرعية.
- `guards.py`, `tracing.py`: deterministic controls and redacted operational evidence · حواجز وأدلة تشغيلية منقحة.
- `assessment.py`: public, inspectable evaluation helpers · أدوات تقييم عامة قابلة للفحص.

The code records routes, results, risk flags, counters, and short operational reasons. It never records raw prompts or private chain-of-thought.

يسجل الكود المسارات والنتائج وعلامات المخاطر والعدادات والأسباب التشغيلية القصيرة، ولا يسجل الأوامر الخام أو سلسلة التفكير الخاصة.

Reference answers, hidden tests, grades, instructor notes, and real credentials are prohibited in this public package.

يُمنع وضع الإجابات المرجعية أو الاختبارات الخفية أو الدرجات أو ملاحظات المدربة أو بيانات الاعتماد الحقيقية داخل هذه الحزمة العامة.
