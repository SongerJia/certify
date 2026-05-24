// navbar.js - 导航栏配置
// 从 themes.js 动态生成导航项

import { themes } from "./themes.js";

export default themes
  .filter((t) => t.visible)
  .map((t) => ({ text: t.text, link: t.link }));
