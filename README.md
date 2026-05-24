<p align="center">
  <a href="https://songerjia.github.io/certify/">
    <img src="https://img.shields.io/badge/Certify-证书知识库-blue?style=for-the-badge" alt="Certify">
  </a>
</p>

<p align="center">
  <a href="https://songerjia.github.io/certify/"><img src="https://img.shields.io/badge/在线阅读-立即访问-green?style=flat-square"></a>
  <a href="https://github.com/SongerJia/certify"><img src="https://img.shields.io/github/stars/SongerJia/certify?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/SongerJia/certify/actions"><img src="https://img.shields.io/github/actions/workflow/status/SongerJia/certify/deploy.yml?style=flat-square" alt="Deploy"></a>
  <a href="https://github.com/SongerJia/certify/blob/main/LICENSE"><img src="https://img.shields.io/github/license/SongerJia/certify?style=flat-square" alt="License"></a>
</p>

# Certify · 证书知识库

> **Certify** —— 系统化备考，高效上岸。

一份**个人证书备考知识库**，覆盖**雅思 IELTS** 和 **软考高级系统架构师**。使用 VuePress 2 + vuepress-theme-hope 构建，GitHub Pages 自动部署。

- 🏠 **在线地址**：[songerjia.github.io/certify](https://songerjia.github.io/certify/)

---

## 🗂️ 内容概览

### 📝 雅思 IELTS

| 模块 | 说明 | 状态 |
|------|------|:---:|
| 听力 | 题型技巧 + 真题练习 | 🚧 |
| 阅读 | 题型技巧 + 真题练习 | 🚧 |
| 写作 | Task 1 + Task 2 模板与范文 | 🚧 |
| 口语 | Part 1/2/3 话题库 | 🚧 |
| **恶搞单词** | 谐音+拆词趣味背单词 | ✅ 7/50 本 |

### 🎓 软考系统架构师

| 模块 | 说明 | 状态 |
|------|------|:---:|
| 综合知识 | 计算机基础 / 网络 / OS / 数据库 / 软件工程 | 🚧 |
| 案例分析 | 架构设计 + 系统设计真题 | 🚧 |
| 论文写作 | 模板 + 范文 + 写作技巧 | 🚧 |
| 备考策略 | 时间规划 + 资料推荐 | 🚧 |

---

## 🛠️ 技术栈

<p>
  <img src="https://img.shields.io/badge/VuePress-2.0-3eaf7c?style=flat-square&logo=vue.js" alt="VuePress">
  <img src="https://img.shields.io/badge/Vite-5.x-646cff?style=flat-square&logo=vite" alt="Vite">
  <img src="https://img.shields.io/badge/Theme_Hope-3498db?style=flat-square" alt="Hope Theme">
  <img src="https://img.shields.io/badge/GitHub_Pages-Deployed-222?style=flat-square&logo=github" alt="GitHub Pages">
</p>

- **框架**：VuePress 2 + Vite
- **主题**：vuepress-theme-hope
- **部署**：GitHub Actions → GitHub Pages，推送即部署

---

## 🚀 本地运行

```bash
npm install          # 安装依赖
npm run dev          # 启动开发服务器（热更新）
npm run build        # 构建生产版本
```

---

## 📝 如何丰富知识库 —— 傻瓜式指南

知识库的操控分为 **四个层级**，从粗到细：大主题 → 小主题 → 文件夹 → 文件。

---

### 层级一：操作大主题（在导航栏出现 / 消失）

> **只管一件事：整个板块要不要显示在网站导航栏上。**

**操作文件**：`src/.vuepress/themes.js`

```js
export const themes = [
  { id: "ielts",            text: "📝 雅思",     link: "/ielts/",             visible: true },
  { id: "system-architect",  text: "🎓 软考架构", link: "/system-architect/",  visible: true },
];
```

| 你想做什么 | 怎么改 |
|---|---|
| **隐藏某个板块** | 把对应的 `visible` 改成 `false` |
| **恢复某个板块** | 把 `visible` 改回 `true` |
| **调整导航栏顺序** | 拖动数组中的整行 |
| **新增一个板块** | 添加一行 + 创建对应的 `{id}-order.js`（见层级二） |

---

### 层级二：操作小主题（卡片页里的子话题）

> **只管一件事：当前板块的卡片页里展示哪些子话题，以及侧边栏显示什么。**

**操作文件**：`src/.vuepress/{id}-order.js`（如 `ielts-order.js`、`sysarch-order.js`）

```js
// 以 ielts-order.js 为例
export const ieltsTopics = [
  { text: "听力",     dir: "ielts/listening",  visible: true },
  { text: "恶搞单词", dir: "ielts/vocab-meme", visible: true },
  // ... 更多
];
```

| 你想做什么 | 怎么改 |
|---|---|
| **隐藏某个子话题** | `visible: false` |
| **恢复某个子话题** | `visible: true` |
| **调整子话题顺序** | 拖动数组中的行 |
| **新增一个子话题** | 添加 `{ text, dir, visible }` |

> `dir` 同时决定三件事：属于哪个卡片分组、侧边栏扫描哪个文件夹、上下文感知（点进卡片后侧边栏只显示该卡片下的内容）。

---

### 层级三：操作子主题文件夹

> **只管一件事：在子话题里创建/删除文件夹分组。**

**不需要改任何配置文件**，直接操作文件系统。侧边栏的 `flattenFiles()` 会自动扫描所有 `.md` 文件（跳过 `README.md`）。

| 你想做什么 | 怎么操作 |
|---|---|
| **新建一个分组** | 在对应目录下新建文件夹，放 `.md` 文件 |
| **删除一个分组** | 删掉对应文件夹 |
| **重命名/设定分组标题** | 去 `*-order.js` 添加/修改 `{ text, dir }` 条目 |

---

### 层级四：写实际内容

> **只管一件事：在文件夹里写 `.md` 文件。**

| 你想做什么 | 怎么操作 |
|---|---|
| **写一篇新文章** | 新建 `xxx.md` |
| **改一篇文章** | 直接编辑 |
| **删一篇文章** | 删掉文件 |
| **调整文章顺序** | 用 `01-` `02-` 前缀控制文件名排序 |

```markdown
# 这是我的文章标题

正文，支持标准 Markdown 语法。
```

> ⚠️ 文件夹下的 `README.md` 是目录默认页面，**不会**出现在侧边栏。普通文章不要叫 `README.md`。

---

### 🎨 特殊玩法：恶搞单词卡片

`vocab-meme` 子项目使用自定义 HTML 卡片模板，支持 6 种记忆法标签：

| 标签 | 颜色 | 说明 |
|------|------|------|
| `<span class="vm-label-xieyin">` | 🟢 蓝色 | 谐音记忆 |
| `<span class="vm-label-chaic">` | 🟣 紫色 | 拆词记忆 |
| `<span class="vm-label-duanzi">` | 🟠 橙色 | 段子记忆 |
| `<span class="vm-label-lianx">` | 🔵 青色 | 联想记忆 |
| `<span class="vm-label-xingjin">` | ⚪ 灰色 | 形近词 |
| `<span class="vm-label-koujue">` | 🟡 金色 | 口诀记忆 |

**核心原则**：每个单词以谐音为基本，其他记忆法为辅助扩展。样式定义在 `src/.vuepress/styles/index.scss`（`vm-` 前缀）。

---

## 🔄 改动生效流程

```
你改文件 → git push → GitHub Actions 自动构建 → 几分钟后网站自动更新
```

本地预览：

```bash
npm run dev
# 浏览器打开 http://localhost:8080/certify/
# 改任何 .md 文件都会热更新
```

---

## ⚡ 常见操作速查

| 场景 | 改哪里 |
|---|---|
| 整个板块不想让人看见 | `themes.js` → `visible: false` |
| 某个子话题还没写完 | `*-order.js` → `visible: false` |
| 调整导航栏顺序 | `themes.js` → 拖动行 |
| 调整侧边栏分组顺序 | `*-order.js` → 拖动行 |
| 新文章侧边栏没出现 | 检查文件名是不是 `README.md` |
| 新文件夹没出现在侧边栏 | 去 `*-order.js` 加一条 `{ text, dir }` |
| 卡片页点了没反应 | 检查 `src/README.md` 中卡片的 `onclick` 路径 |
| 单词卡渲染不出来 | 检查 HTML 之间有没有空行（会触发 `<pre>` 包裹） |

---

## 📈 更新日志

| 日期 | 内容 |
|---|---|
| 2026-05-24 | 项目初始化，完成恶搞单词 1-7 本（#001-#700），GitHub Pages 部署上线 |

持续更新中，欢迎 **Star ⭐** 关注！

---

*Built with ❤️ by [SongerJia](https://github.com/SongerJia)*
