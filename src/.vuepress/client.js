import { defineClientConfig } from "vuepress/client";

export default defineClientConfig({
  setup() {
    // 仅在浏览器端运行（SSR 期间无 document）
    if (typeof document === "undefined") return;

    const style = document.createElement("style");
    style.id = "accent-color-override";
    style.textContent = [
      ":root{",
      "--vp-c-accent:#3b82f6!important;",
      "--vp-c-accent-bg:#3b82f6!important;",
      "--vp-c-accent-hover:#1d4ed8!important;",
      "--vp-c-accent-soft:#3b82f624!important",
      "}",
      "[data-theme=dark]{",
      "--vp-c-accent:#60a5fa!important;",
      "}",
    ].join("");
    document.head.appendChild(style);
  },
});
