(() => {
  "use strict";

  const LANGUAGE_KEY = "rafeeq-preview-language";
  const STEP_KEY = "rafeeq-preview-step";
  const root = document.documentElement;
  const languageButtons = [...document.querySelectorAll("[data-lang-switch]")];

  const setupSteps = [
    {
      icon: "◉",
      titleEn: "Create account",
      titleAr: "إنشاء الحساب",
      bodyEn: "Create a personal GitHub account, verify your email, and choose a professional username.",
      bodyAr: "أنشئ حساب GitHub شخصيًا، ووثّق بريدك، واختر اسم مستخدم مهنيًا.",
    },
    {
      icon: "⑂",
      titleEn: "Use template",
      titleAr: "استخدام القالب",
      bodyEn: "Create your own public repository from the approved course template. Use the template—not a fork.",
      bodyAr: "أنشئ مستودعك العام من قالب الدورة المعتمد. استخدم القالب، لا الـFork.",
    },
    {
      icon: "☁",
      titleEn: "Prepare Colab",
      titleAr: "تجهيز كولاب",
      bodyEn: "Open the verified notebook, save a working copy in Drive, and keep the standard CPU runtime.",
      bodyAr: "افتح الدفتر بعد التحقق منه، واحفظ نسخة عمل في Drive، واستخدم بيئة CPU القياسية.",
    },
    {
      icon: "✓",
      titleEn: "Reach C0 READY",
      titleAr: "الوصول إلى C0 READY",
      bodyEn: "Run C0_ENV_DOCTOR and continue only when every check passes and all_passed=true.",
      bodyAr: "شغّل C0_ENV_DOCTOR، ولا تتابع حتى تنجح جميع الفحوص وتظهر all_passed=true.",
    },
  ];

  function safeRead(key) {
    try {
      return localStorage.getItem(key);
    } catch (_error) {
      return null;
    }
  }

  function safeWrite(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (_error) {
      // Local preferences are optional; the portal remains usable without storage.
    }
  }

  function applyLanguage(language) {
    const allowed = ["en", "both", "ar"];
    const next = allowed.includes(language) ? language : "both";
    root.dataset.language = next;
    root.lang = next === "ar" ? "ar" : "en";
    root.dir = next === "ar" ? "rtl" : "ltr";
    languageButtons.forEach((button) => {
      const active = button.dataset.langSwitch === next;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    safeWrite(LANGUAGE_KEY, next);
  }

  const savedLanguage = safeRead(LANGUAGE_KEY);
  const defaultLanguage = savedLanguage || (window.matchMedia("(max-width: 760px)").matches ? "ar" : "both");
  applyLanguage(defaultLanguage);
  languageButtons.forEach((button) => button.addEventListener("click", () => applyLanguage(button.dataset.langSwitch)));

  const board = document.querySelector("[data-setup-board]");
  if (board) {
    const stepButtons = [...board.querySelectorAll("[data-step]")];
    const progress = board.querySelector(".setup-progress");
    const progressBar = progress?.querySelector("span");
    const icon = board.querySelector("[data-step-icon]");
    const countEn = board.querySelector("[data-step-count-en]");
    const countAr = board.querySelector("[data-step-count-ar]");
    const titleEn = board.querySelector("[data-step-title-en]");
    const titleAr = board.querySelector("[data-step-title-ar]");
    const bodyEn = board.querySelector("[data-step-body-en]");
    const bodyAr = board.querySelector("[data-step-body-ar]");
    const nextButton = board.querySelector("[data-next-step]");
    const savedStep = Number.parseInt(safeRead(STEP_KEY) || "0", 10);
    let activeStep = Number.isFinite(savedStep) ? Math.min(Math.max(savedStep, 0), setupSteps.length - 1) : 0;

    function renderStep(index) {
      activeStep = Math.min(Math.max(index, 0), setupSteps.length - 1);
      const step = setupSteps[activeStep];
      stepButtons.forEach((button, buttonIndex) => {
        button.classList.toggle("current", buttonIndex === activeStep);
        button.classList.toggle("done", buttonIndex < activeStep);
        button.setAttribute("aria-selected", String(buttonIndex === activeStep));
      });
      if (progressBar) progressBar.style.width = `${((activeStep + 1) / setupSteps.length) * 100}%`;
      if (progress) progress.setAttribute("aria-valuenow", String(activeStep + 1));
      if (icon) icon.textContent = step.icon;
      if (countEn) countEn.textContent = `STEP ${activeStep + 1} OF ${setupSteps.length}`;
      if (countAr) countAr.textContent = `الخطوة ${activeStep + 1} من ${setupSteps.length}`;
      if (titleEn) titleEn.textContent = step.titleEn;
      if (titleAr) titleAr.textContent = step.titleAr;
      if (bodyEn) bodyEn.textContent = step.bodyEn;
      if (bodyAr) bodyAr.textContent = step.bodyAr;
      if (nextButton) {
        nextButton.innerHTML = activeStep === setupSteps.length - 1
          ? "Return to first preview · عُد إلى المعاينة الأولى <span aria-hidden=\"true\">↺</span>"
          : "Preview next step · عاين الخطوة التالية <span aria-hidden=\"true\">→</span>";
      }
      safeWrite(STEP_KEY, String(activeStep));
    }

    stepButtons.forEach((button) => button.addEventListener("click", () => renderStep(Number(button.dataset.step))));
    nextButton?.addEventListener("click", () => renderStep(activeStep === setupSteps.length - 1 ? 0 : activeStep + 1));
    renderStep(activeStep);
  }

  const copyButton = document.querySelector("[data-copy-help]");
  const toast = document.querySelector("[data-toast]");
  const helpTemplate = [
    "Rafeeq Mini — Safe help request",
    "Cell / الخلية:",
    "Expected / المتوقع:",
    "Observed / الفعلي:",
    "Error code only / رمز الخطأ فقط:",
    "Steps tried / المحاولات:",
    "No passwords, tokens, private links, or real customer data.",
  ].join("\n");

  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const field = document.createElement("textarea");
    field.value = text;
    field.setAttribute("readonly", "");
    field.style.position = "fixed";
    field.style.opacity = "0";
    document.body.append(field);
    field.select();
    document.execCommand("copy");
    field.remove();
  }

  copyButton?.addEventListener("click", async () => {
    try {
      await copyText(helpTemplate);
      if (toast) {
        toast.hidden = false;
        window.setTimeout(() => { toast.hidden = true; }, 2600);
      }
    } catch (_error) {
      if (toast) {
        toast.textContent = "Copy unavailable · تعذر النسخ";
        toast.hidden = false;
        window.setTimeout(() => {
          toast.hidden = true;
          toast.textContent = "Copied safely · تم النسخ بأمان";
        }, 2600);
      }
    }
  });
})();
