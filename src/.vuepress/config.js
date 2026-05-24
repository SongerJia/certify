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

const STYLE =
  "<style>:root{--vp-c-accent:#3b82f6!important;--vp-c-accent-bg:#3b82f6!important;--vp-c-accent-hover:#1d4ed8!important;--vp-c-accent-soft:#3b82f624!important}[data-theme=dark]{--vp-c-accent:#60a5fa!important}</style>";

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

  plugins: [
    () => ({
      name: "accent-color-override",
      onGenerated: async (app) => {
        const dest = app.dir.dest();
        const files = findHtmlFiles(dest);
        for (const file of files) {
          let html = readFileSync(file, "utf-8");
          if (!html.includes("vp-c-accent:#3b82f6")) {
            html = html.replace("</head>", STYLE + "\n</head>");
            writeFileSync(file, html);
          }
        }
      },
    }),
  ],
};
