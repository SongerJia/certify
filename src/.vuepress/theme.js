import { hopeTheme } from "vuepress-theme-hope";
import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({
  hostname: "https://songerjia.github.io",

  author: {
    name: "SongerJia",
    url: "https://github.com/SongerJia",
  },

  repo: "SongerJia/certify",
  repoDisplay: true,
  repoLabel: "GitHub",

  // Logo 配置
  logo: "/logo.svg",
  logoDark: "/logo.svg",

  // 页脚配置
  displayFooter: true,
  footer: `MIT License © 2026 SongerJia | Powered by <a href="https://v2.vuepress.vuejs.org/" target="_blank">VuePress</a> & <a href="https://theme-hope.vuejs.press/" target="_blank">Theme Hope</a> · <span id="busuanzi_value_site_pv">-</span> 次访问`,

  // 注入不蒜子访问统计脚本
  head: [
    ["script", { async: true, src: "https://busuanzi.ibruce.info/busuanzi/2.3.0/busuanzi.pure.min.js" }],
  ],

  // 导航栏
  navbar,

  // 侧边栏
  sidebar,

  // 面包屑配置
  breadcrumb: false,
  breadcrumbIcon: false,

  // 主题色（蓝色）
  themeColor: {
    blue: "#3b82f6",
    lightblue: "#60a5fa",
    darkblue: "#1d4ed8",
  },

  // ===== 插件配置 =====
  plugins: {
    // PWA 支持
    pwa: {
      manifest: {
        name: "Certify · 证书知识库",
        short_name: "Certify",
        start_url: "/",
        display: "standalone",
        background_color: "#ffffff",
        theme_color: "#3b82f6",
        icons: [
          {
            src: "/logo.svg",
            sizes: "any",
            type: "image/svg+xml",
            purpose: "any",
          },
        ],
      },
      cacheHTML: true,
      cacheImage: true,
      update: "available",
    },

    // 搜索
    slimsearch: {},

    // 代码复制
    copyCode: {},
  },
});
