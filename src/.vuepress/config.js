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

  // 自定义插件：构建后注入蓝色 accent CSS（lightningcss 会去重 CSS bundle 中的 :root 变量）
  plugins: [
    () => ({
      name: "accent-color-override",
      onGenerated: async (app) => {
        // bundler-vite 输出到项目根 dist/，非 .vuepress/dist/
        const dest = join(app.dir.source(), "..", "dist");
        console.log("[accent-override] dest:", dest);
        const files = findHtmlFiles(dest);
        console.log("[accent-override] Found", files.length, "HTML files");
        const styleTag = '<style>:root{--vp-c-accent:#3b82f6!important;--vp-c-accent-bg:#3b82f6!important;--vp-c-accent-hover:#1d4ed8!important;--vp-c-accent-soft:#3b82f624!important}[data-theme=dark]{--vp-c-accent:#60a5fa!important;--vp-c-accent-bg:#3b82f6!important;--vp-c-accent-hover:#1d4ed8!important;--vp-c-accent-soft:#3b82f624!important}</style>';
        for (const file of files) {
          let html = readFileSync(file, "utf-8");
          if (!html.includes("vp-c-accent:#3b82f6")) {
            html = html.replace("</head>", styleTag + "\n</head>");
            writeFileSync(file, html);
          }
        }
        console.log("[accent-override] Done injecting into", files.length, "files");
      },
    }),
  ],
};
