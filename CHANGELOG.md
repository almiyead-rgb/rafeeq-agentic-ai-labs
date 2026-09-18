# Changelog · سجل التغييرات

All notable changes to the learner repository are recorded here.

تُسجل هنا التغييرات المهمة في مستودع المتدرب.

## [0.9.0-rc2] — 2026-09-18

### Added · أضيف

- Bilingual submission-and-passing section with a 100-point rubric, a 70-point threshold, non-compensable safety gates, presentation expectations, and configurable deadline/form states.
- Ten-minute readiness check, Core/Stretch paths, an eight-step upload wizard, a Lab-versus-Production truth table, and a real sanitized `lab-help` issue form.
- Dependency-free preflight that separates seven automated checks from five manual hosted-Colab acceptance steps.
- Limited learner course-and-portfolio reuse permission with privacy, attribution, and instructor-material boundaries.
- Cryptographic submission receipt that binds the executed final notebook, manifest, assessment run, assessment hash, and export ID.
- Strict canonical 16-case assessment contract, named metrics/gates, exact risk-flag matching, and actionable seven-check validation.

### Changed · تغيّر

- GitHub setup is now one consistent policy: create an empty repository during preflight, leave it empty through C29, then upload the clean export and final notebook.
- Learner Actions now runs on any branch, requires a green `Learner submission quality` result, and uploads the validation receipt.
- Public identity fields now use a pseudonymous `learner_id`; real identity belongs only in the private hand-in form.
- Course and reference links are pinned to the `v0.9.0-rc2` tag instead of the moving `main` branch.

### Acceptance status · حالة القبول

- Automated repository checks, 47 public tests, notebook structure, compilation, static Pages checks, and the end-to-end temporary export/validation/receipt path pass.
- Promotion to `v1.0.0` remains blocked until the clean-account hosted-Colab C0–C29, runtime-recovery, browser upload, and green-Actions pilot is recorded.

- نجحت فحوص المستودع الآلية و47 اختبارًا عامًا وفحص بنية الدفتر والتجميع وفحوص Pages الثابتة ومسار التصدير والتحقق والإيصال المؤقت من البداية إلى النهاية.
- تبقى الترقية إلى `v1.0.0` معلقة حتى توثيق تجربة Colab المستضاف بحساب نظيف من C0 إلى C29، واختبار الاستعادة، والرفع من المتصفح، ونجاح Actions.

## [0.9.0-rc1] — 2026-09-17

### Added · أضيف

- One cumulative bilingual Colab notebook with the exact `C0–C29` learning path and 14 bounded TODOs.
- Dependency-light Rafeeq runtime: typed state, bounded graph, two specialists, scoped memory, current-policy retrieval, approval, guardrails, redacted tracing, and assessment.
- Real local MCP `stdio` subprocess with three narrow tools and trusted runtime context.
- Six versioned synthetic datasets, public contract/security tests, JSON schemas, day gates, reports, dashboard, and safe export.
- Beginner GitHub/Colab/recovery guides and an active Colab launch path.
- Live bilingual learner portal published through GitHub Pages and verified on 2026-09-18.
- Versioned, result-only reference contracts and a bilingual browser comparison page for learner evidence; no solution code or TODO answers are exposed. · عقود مرجعية ذات إصدار للنتائج فقط، وصفحة مقارنة ثنائية اللغة لأدلة المتدرب؛ بلا كود حلول أو إجابات مهام.

### Release note · ملاحظة الإصدار

This is a learner pilot, not a production system. The mandatory path was verified locally and in CI without credentials or network services; an actual hosted Colab runtime remains part of the instructor pilot acceptance.

هذا إصدار تجريبي للمتدربين وليس نظام إنتاج. جرى التحقق من المسار الإلزامي محليًا وفي CI بلا بيانات دخول أو خدمات شبكية، ويبقى تشغيل جلسة Colab مستضافة فعليًا ضمن قبول تجربة المدربة.

## [0.1.0-alpha] — 2026-09-17

### Added · أضيف

- Static bilingual GitHub Pages foundation derived from the approved design prototype.
- Explicit pre-release status and inactive lab/Colab actions.
- Public/private content boundary and security guidance.
- Reserved directories for the cumulative notebook, synthetic data, source, MCP server, public tests, reports, and recovery policy.
- Foundation validation script and lightweight GitHub Actions workflow.

### Not included · غير مشمول

- Runnable notebook, datasets, project source, tests, active Colab link, solutions, or hidden assessment material.
