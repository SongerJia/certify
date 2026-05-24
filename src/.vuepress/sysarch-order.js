// sysarch-order.js —— 软考系统架构师子话题配置
//
// 调整顺序：拖动数组条目
// 隐藏子话题：设置 visible: false
// 新增子话题：添加条目 + 创建对应文件夹
//
// dir 路径前缀相同的条目归到同一个卡片分组：
//   system-architect/knowledge   → 综合知识卡片
//   system-architect/case-study  → 案例分析卡片
//   system-architect/essay       → 论文卡片
//   system-architect/strategy    → 备考策略卡片

export const sysarchTopics = [
  { text: "计算机基础",   dir: "system-architect/knowledge/computer-basics", visible: true },
  { text: "操作系统",     dir: "system-architect/knowledge/os",              visible: true },
  { text: "数据库技术",   dir: "system-architect/knowledge/database",         visible: true },
  { text: "网络与安全",   dir: "system-architect/knowledge/network",          visible: true },
  { text: "软件工程",     dir: "system-architect/knowledge/software",         visible: true },
  { text: "架构设计",     dir: "system-architect/case-study/architecture",    visible: true },
  { text: "系统设计",     dir: "system-architect/case-study/system-design",   visible: true },
  { text: "写作技巧",     dir: "system-architect/essay/skills",               visible: true },
  { text: "范文模板",     dir: "system-architect/essay/templates",            visible: true },
  { text: "时间规划",     dir: "system-architect/strategy/timeline",          visible: true },
  { text: "备考资源",     dir: "system-architect/strategy/resources",         visible: true },
];
