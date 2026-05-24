import viteBundler from "@vuepress/bundler-vite";
import theme from "./theme.js";

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
};
