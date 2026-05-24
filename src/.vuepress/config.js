import viteBundler from "@vuepress/bundler-vite";
import theme from "./theme.js";
import { writeFileSync, readFileSync, readdirSync, statSync } from "fs";
import { join } from "path";

function findHtmlFiles(dir) {
  let results = [];
  const list = readdirSync(dir);
  for (const item of list) {
    const full = join(dir, item);
    if (statSync(full).isDirectory()) {
      results = results.concat(findHtmlFiles(full));
    } else if (item.endsWith(".html")) {
      results.push(full);
    }
  }
  return results;
}

const ACCENT_STYLE =
  '<style>:root{--vp-c-accent:#3b82f6!important;--vp-c-accent-bg:#3b82f6!important;--vp-c-accent-hover:#1d4ed8!important;--vp-c-accent-soft:#3b82f624!important}[data-theme=dark]{--vp-c-accent:#60a5fa!important}</style>';

export default {
  base: "/certify/",

  lang: "zh-CN",
  title: "Certify · 证书知识库",
  description: "雅思 · 软考高级系统架构师 备考知识库",

  head: [
    ["meta", { name: "theme-color", content: "#3b82f6" }],
  ],

  bundler: viteBundler(),

  theme,

  // 构建后在所有页面注入蓝色 accent CSS 变量（覆盖 Theme Hope 默认绿色）
  // lightningcss 会去重 CSS bundle 中 :root 的重复变量声明，因此只能在构建后注入
  plugins: [
    () => ({
      name: "accent-color-override",
      onGenerated: async (app) => {
        const dest = join(app.dir.source(), "..", "dist");
        const files = findHtmlFiles(dest);
        for (const file of files) {
          let html = readFileSync(file, "utf-8");
          if (!html.includes("vp-c-accent:#3b82f6")) {
            html = html.replace("</head>", ACCENT_STYLE + "\n</head>");
            writeFileSync(file, html);
          }
        }
      },
    }),
  ],
};
