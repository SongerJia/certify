// sidebar.js - 侧边栏配置
//
// 上下文感知：按路径前缀分组，点进某个卡片后侧边栏只显示当前卡片下的子文件夹
//
// 修复说明（2026-05-25）：
//   vocabMemeSidebar 改为由 flattenFiles 自动扫描，不再硬编码（新增 wordbook-8.md 无需改配置）

import { resolve, dirname, relative } from "path";
import { fileURLToPath } from "url";
import { readdirSync, statSync, existsSync } from "fs";

import { themes } from "./themes.js";
import { ieltsTopics } from "./ielts-order.js";
import { sysarchTopics } from "./sysarch-order.js";

const SRC_DIR = resolve(dirname(fileURLToPath(import.meta.url)), "..");

// ---------- 主题可见性 ----------
const visibleIds = new Set(
  themes.filter((t) => t.visible).map((t) => t.id)
);

// ---------- 子话题可见性过滤 ----------
function visibleTopics(allTopics) {
  return allTopics.filter((t) => t.visible !== false);
}

// ---------- 文件扫描 ----------
function flattenFiles(dirName) {
  const dir = resolve(SRC_DIR, dirName);
  if (!existsSync(dir) || !statSync(dir).isDirectory()) return [];

  const files = [];

  function walk(currentDir, depth) {
    if (depth > 10) return;
    const entries = readdirSync(currentDir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.name.startsWith(".")) continue;
      const fullPath = resolve(currentDir, entry.name);
      if (entry.isDirectory()) {
        walk(fullPath, depth + 1);
      } else if (entry.name.endsWith(".md") && entry.name !== "README.md") {
        const relPath =
          "/" + relative(SRC_DIR, fullPath).replace(/\\/g, "/").replace(/\.md$/, "");
        files.push(relPath);
      }
    }
  }

  walk(dir, 0);
  return files.sort();
}

function topic(text, dir) {
  const children = flattenFiles(dir);
  return { text, collapsible: true, collapsed: true, children };
}

/** 从 topics 中按目录前缀过滤子话题 */
function topicGroup(topics, themeId, prefix) {
  if (!visibleIds.has(themeId)) return null;
  return visibleTopics(topics)
    .filter((t) => t.dir.startsWith(prefix))
    .map((t) => topic(t.text, t.dir));
}

// ---------- 雅思各子话题侧边栏 ----------
const ieltsListeningSidebar = topicGroup(ieltsTopics, "ielts", "ielts/listening");
const ieltsReadingSidebar   = topicGroup(ieltsTopics, "ielts", "ielts/reading");
const ieltsWritingSidebar   = topicGroup(ieltsTopics, "ielts", "ielts/writing");
const ieltsSpeakingSidebar  = topicGroup(ieltsTopics, "ielts", "ielts/speaking");

// ---------- 恶搞单词侧边栏（自动扫描，不再硬编码）----------
const vocabMemeSidebar = flattenFiles("ielts/vocab-meme/wordbook").map((p) => ({
  text: p.replace(/^.*\//, "").replace(/-/g, "_"),
  link: p,
}));

// ---------- 软考各子话题侧边栏 ----------
const sysarchKnowledgeSidebar = topicGroup(sysarchTopics, "system-architect", "system-architect/knowledge");
const sysarchCaseSidebar      = topicGroup(sysarchTopics, "system-architect", "system-architect/case-study");
const sysarchEssaySidebar     = topicGroup(sysarchTopics, "system-architect", "system-architect/essay");
const sysarchStrategySidebar  = topicGroup(sysarchTopics, "system-architect", "system-architect/strategy");

// ---------- 路由分配 ----------
const routeConfig = {};

function assign(paths, sidebar) {
  if (!sidebar) return;
  for (const p of paths) routeConfig[p] = sidebar;
}

// 雅思
assign(["/ielts/", "/ielts/listening/",
        "/ielts/listening/skills/", "/ielts/listening/practice/"], ieltsListeningSidebar);
assign(["/ielts/reading/",
        "/ielts/reading/skills/", "/ielts/reading/practice/"], ieltsReadingSidebar);
assign(["/ielts/writing/",
        "/ielts/writing/task1/", "/ielts/writing/task2/"], ieltsWritingSidebar);
assign(["/ielts/speaking/",
        "/ielts/speaking/part1/", "/ielts/speaking/part2/",
        "/ielts/speaking/part3/"], ieltsSpeakingSidebar);

// 恶搞单词
assign(["/ielts/vocab-meme/",
        "/ielts/vocab-meme/wordbook/"], vocabMemeSidebar);

// 软考
assign(["/system-architect/", "/system-architect/knowledge/",
        "/system-architect/knowledge/computer-basics/",
        "/system-architect/knowledge/os/",
        "/system-architect/knowledge/database/",
        "/system-architect/knowledge/network/",
        "/system-architect/knowledge/software/"], sysarchKnowledgeSidebar);
assign(["/system-architect/case-study/",
        "/system-architect/case-study/architecture/",
        "/system-architect/case-study/system-design/"], sysarchCaseSidebar);
assign(["/system-architect/essay/",
        "/system-architect/essay/skills/",
        "/system-architect/essay/templates/"], sysarchEssaySidebar);
assign(["/system-architect/strategy/",
        "/system-architect/strategy/timeline/",
        "/system-architect/strategy/resources/"], sysarchStrategySidebar);

export default routeConfig;
