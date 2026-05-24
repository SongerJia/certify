// ielts-order.js —— 雅思子话题配置
//
// 调整顺序：拖动数组条目
// 隐藏子话题：设置 visible: false
// 新增子话题：添加条目 + 创建对应文件夹
//
// dir 路径前缀相同的条目归到同一个卡片分组：
//   ielts/listening → 听力卡片
//   ielts/reading   → 阅读卡片
//   ielts/writing   → 写作卡片
//   ielts/speaking  → 口语卡片

export const ieltsTopics = [
  { text: "听力技巧", dir: "ielts/listening/skills",   visible: true },
  { text: "听力真题", dir: "ielts/listening/practice", visible: true },
  { text: "阅读技巧", dir: "ielts/reading/skills",     visible: true },
  { text: "阅读真题", dir: "ielts/reading/practice",   visible: true },
  { text: "小作文",   dir: "ielts/writing/task1",       visible: true },
  { text: "大作文",   dir: "ielts/writing/task2",       visible: true },
  { text: "Part 1",  dir: "ielts/speaking/part1",      visible: true },
  { text: "Part 2",  dir: "ielts/speaking/part2",      visible: true },
  { text: "Part 3",  dir: "ielts/speaking/part3",      visible: true },
  { text: "恶搞单词", dir: "ielts/vocab-meme", visible: true },
];
