# 03 — MVC / MVP / MVVM 与表现层模式

> **对应计划**：第 1 周周四（5/29）| **学习时间**：2~3 小时 | **题量目标**：20 道

---

## 一、学习目标

完成本章后，你将能够：
1. 画图解释 MVC、MVP、MVVM 三种模式的组件交互关系
2. 说出三种模式的核心区别（谁持有 View 引用、数据流向）
3. 在案例分析中根据场景选择合适的表现层模式
4. 了解 PAC、Front Controller 等其他表现层模式

---

## 二、核心概念

### 2.1 为什么需要表现层模式？

**核心问题**：用户界面逻辑和业务逻辑耦合 → 难测试、难维护、难复用。

**解决思路**：分离关注点（Separation of Concerns）——把"展示什么"（View）、"怎么展示"（逻辑）、"数据是什么"（Model）拆开。

```
          表现层架构演进
              │
    ┌─────────┼─────────┐
    │         │         │
   MVC      MVP      MVVM
 (1970s)  (1990s)  (2005)
    │         │         │
 Smalltalk  Dolphin  WPF/Knockout
  Web:      Android  Vue/Angular
  Spring   原生MVP   React(单向)
```

---

### 2.2 MVC（Model-View-Controller）

#### 经典结构

```
         ┌──────────┐
         │   Model   │  ← 数据 + 业务逻辑
         └────┬─────┘
        ↑     │ 通知数据变化
   查询/更新  ↓
   ┌──────────┴─────┐
   │     View        │  ← 展示 + 用户交互
   └────────┬───────┘
        ↑   │ 用户输入
        │   ↓
   ┌────┴───────────┐
   │  Controller     │  ← 协调者：接收输入→更新Model→选择View
   └────────────────┘
```

#### 交互流程

```
用户点击按钮
    ↓
Controller.handleClick()
    ↓
Model.updateData()
    ↓
Model.notifyObservers()  ← 观察者模式
    ↓
View.refresh()
```

#### MVC 变体

| 变体 | Model→View 通信方式 | 典型框架 |
|:---|:---|:---|
| **经典 MVC** | 观察者模式（Push） | Smalltalk |
| **Web MVC** | Controller 推数据到 View | Spring MVC / ASP.NET MVC |
| **被动 MVC** | View 主动 Pull | — |

> **考试重点**：Web MVC 中 Controller 是核心协调者，与经典 MVC 的区别在于 Model 不直接通知 View。

#### MVC 优缺点

| 优点 | 缺点 |
|:---|:---|
| 职责分离清晰 | Controller 可能臃肿（"胖控制器"） |
| Model 可独立测试 | View 和 Controller 通常耦合（框架层面） |
| 一对多（一个 Model 多个 View） | 复杂交互场景下事件流难追踪 |

---

### 2.3 MVP（Model-View-Presenter）

#### 结构

```
  ┌──────────┐          ┌──────────────┐
  │  Model    │ ←──────→│  Presenter    │  ← 所有逻辑在 Presenter
  └──────────┘          └──────┬───────┘
                               │ 接口（IView）
                        ┌──────┴───────┐
                        │     View      │  ← 被动视图，只管渲染
                        └──────────────┘
```

#### 核心变化

**View 和 Presenter 通过接口通信**，View 不知道 Presenter 的存在，Presenter 通过 `IView` 接口操作 View。

```
用户点击登录按钮
    ↓
View: IView.onLoginClicked("admin", "123456")
    ↓
Presenter: Model.authenticate("admin", "123456")
    ↓
Presenter: 判断结果
    ↓
Presenter: IView.showHome() 或 IView.showError("密码错误")
```

#### MVP vs MVC 核心区别

| | MVC | MVP |
|:---|:---|:---|
| **View 知道 Controller/Presenter 吗？** | 知道 Controller | **不知道** Presenter（只暴露接口） |
| **谁持有 View 引用？** | Controller 可选持有 | Presenter 持有 IView |
| **View 可测试性** | 较差（依赖 Controller） | **极好**（可 Mock IView） |
| **适用场景** | Web 应用 | Android / 复杂 UI 逻辑 |

> **记忆口诀**：MVP = "Presenter 当家，View 当哑巴"

---

### 2.4 MVVM（Model-View-ViewModel）

#### 结构

```
  ┌──────────┐          ┌──────────────┐          ┌──────────┐
  │  Model    │ ←──────→│  ViewModel    │ ←──────→│   View    │
  └──────────┘          └──────────────┘          └──────────┘
                              ↑                        ↑
                        数据绑定（双向）───────────────┘
```

#### 核心机制：数据绑定（Data Binding）

```
用户在输入框输入 "Hello"
    ↓ (自动)
ViewModel.name = "Hello"          ← View → ViewModel
    ↓ (自动)
View 上显示 "Hello" 的地方全部更新  ← ViewModel → View
```

**不需要手动写 `onTextChanged()` 和 `setText()`！**

#### ViewModel 的职责

- 暴露数据（Observable Property）
- 暴露命令（Command）
- 处理展示逻辑（格式化、校验）
- **不持有 View 引用**（这是与 Presenter 的关键区别！）

```
ViewModel: 日期格式化逻辑
  Model.date = 2026-05-27
     ↓ ViewModel 转换
  ViewModel.displayDate = "2026年5月27日"
     ↓ 自动绑定
  View 显示 "2026年5月27日"
```

#### 三大模式对比

| 特性 | MVC | MVP | MVVM |
|:---|:---|:---|:---|
| **数据流** | Controller→Model→View | Presenter↔View(接口) | ViewModel↔View(绑定) |
| **View 角色** | 主动（拉数据） | 被动（接口定义） | 声明式（绑定） |
| **逻辑位置** | Controller | Presenter | ViewModel |
| **测试性** | 中 | 高 | 高 |
| **代码量** | 少 | 多（接口定义） | 少（绑定自动） |
| **学习曲线** | 低 | 中 | 中（需理解绑定） |
| **典型框架** | Spring MVC | Android MVP | Vue / Angular / React+Redux |

---

### 2.5 PAC（Presentation-Abstraction-Control）

```
┌─────────────────────────────────┐
│         顶层 PAC Agent            │
│   ┌─────┐ ┌─────┐ ┌─────┐      │
│   │  P  │ │  A  │ │  C  │      │  P=Presentation(展示)
│   └──┬──┘ └──┬──┘ └──┬──┘      │  A=Abstraction(数据)
│      │       │       │          │  C=Control(协调)
│  ┌───┴───────┴───────┴───┐      │
│  │      中层 PAC Agent     │      │
│  │   ┌───┐ ┌───┐ ┌───┐   │      │
│  │   │ P │ │ A │ │ C │   │      │
│  │   └─┬─┘ └─┬─┘ └─┬─┘   │      │
│  │     │     │     │     │      │
│  │ ┌───┴─────┴─────┴───┐ │      │
│  │ │  底层 PAC Agent    │ │      │
│  │ └───────────────────┘ │      │
│  └───────────────────────┘      │
└─────────────────────────────────┘
```

**要点**：
- **树形结构**：每个 Agent 是独立的 P-A-C 三元组
- **只与上下级通信**：同级 Agent 不直接通信
- **适用**：大型交互式系统（如 IDE、CAD 工具、交通控制系统）

> **真题关联**：2019 年案例分析曾考 PAC 与 MVC 的区别。

---

### 2.6 Front Controller（前端控制器）

```
                  ┌──────────────┐
  所有请求 ─────→ │Front Controller│ ──→ 调度到具体Handler
                  └──────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
    ┌──────────┐  ┌──────────┐  ┌──────────┐
    │Handler 1 │  │Handler 2 │  │Handler 3 │
    └──────────┘  └──────────┘  └──────────┘
```

**统一入口处理**：认证、日志、路由、编码等横切关注点。

| 框架 | 前端控制器 |
|:---|:---|
| Spring MVC | `DispatcherServlet` |
| ASP.NET | `HttpHandler` |
| Express.js | `app` 对象（中间件链） |

---

## 三、考试重点聚焦

### 3.1 高频考点

| 考点 | 出现频率 | 出题形式 |
|:---|:---:|:---|
| MVC 三组件职责 | ★★★★★ | 综合选择、案例分析 |
| MVP 与 MVC 的区别 | ★★★★ | 综合选择 |
| MVVM 数据绑定原理 | ★★★★ | 综合选择、论文 |
| 表现层模式选型 | ★★★ | 案例分析 |
| PAC 树形层次结构 | ★★ | 综合选择 |

### 3.2 2025 新考纲关联

MVVM 与前端的 Vue/React 生态紧密关联，云原生架构中的**前后端分离**设计也依赖合理的表现层模式选型。论文题若涉及"微服务架构下的前端架构设计"，MVVM 是必写内容。

---

## 四、记忆辅助卡

### 一句话区分

| 模式 | 一句话 |
|:---|:---|
| MVC | Controller 是交通警察，指挥 Model 和 View |
| MVP | Presenter 是傀儡师，View 是木偶 |
| MVVM | ViewModel 是翻译官，View 和数据自动同步 |

### MVP vs MVVM 速判

```
问：View 需要定义接口（IView）吗？
  ├── 需要 → MVP
  └── 不需要（数据绑定）→ MVVM
```

---

## 五、章节练习（20 题）

### 单选题（12 题）

**1.** MVC 模式中，Model 发生变化后如何通知 View 更新？

- A. Controller 轮询 Model
- B. Model 通过观察者模式主动通知 View
- C. View 定时拉取 Model 数据
- D. 用户手动刷新

<details><summary>答案</summary>B — 经典 MVC 中 Model 使用观察者模式通知 View。Web MVC 中则由 Controller 推数据。</details>

**2.** 以下关于 MVP 的描述，错误的是？

- A. Presenter 持有 IView 接口引用
- B. View 知道 Presenter 的存在
- C. View 可以直接访问 Model
- D. MVP 中 View 的测试性优于 MVC

<details><summary>答案</summary>C — MVP 中 View 只能通过 Presenter 间接访问 Model（通过 IView 接口），不能直接访问。</details>

**3.** MVVM 中 ViewModel 与 Presenter 的关键区别是？

- A. ViewModel 负责更多业务逻辑
- B. ViewModel 不持有 View 引用，通过数据绑定通信
- C. ViewModel 只能用于前端
- D. ViewModel 必须用 TypeScript 编写

<details><summary>答案</summary>B — Presenter 持有 IView 引用；ViewModel 完全不知道 View 的存在，通过双向绑定自动同步。</details>

**4.** 一个 Android 应用需要对 UI 逻辑做充分的单元测试，推荐使用？

- A. MVC
- B. MVP
- C. PAC
- D. Front Controller

<details><summary>答案</summary>B — MVP 的 IView 接口可被 Mock，使得 Presenter 可以脱离真实 UI 进行单元测试。</details>

**5.** Vue.js 的核心架构模式是？

- A. MVC
- B. MVP
- C. MVVM
- D. PAC

<details><summary>答案</summary>C — Vue 的响应式数据 + 模板语法就是典型的 MVVM 数据绑定。</details>

**6.** Front Controller 模式的主要优点是？

- A. 减少类数量
- B. 统一处理横切关注点（认证、日志、编码）
- C. 提高数据库性能
- D. 减少前端代码量

<details><summary>答案</summary>B — 所有请求经过统一入口，集中处理认证、日志、路由等通用逻辑。</details>

**7.** Spring MVC 的 DispatcherServlet 实现了什么模式？

- A. MVC（经典）
- B. Front Controller + Web MVC
- C. MVP
- D. MVVM

<details><summary>答案</summary>B — DispatcherServlet 是 Front Controller（统一入口），Handler+ModelAndView 构成 Web MVC。</details>

**8.** PAC 模式中，同级 Agent 之间的通信方式是？

- A. 直接通信
- B. 通过共享内存
- C. 通过上级 Agent 转发
- D. 通过消息队列

<details><summary>答案</summary>C — PAC 严格遵循树形层级，同级不直接通信，只能通过父 Agent 协调。</details>

**9.** 关于 MVC 和 MVP，描述正确的是？

- A. MVC 的 View 比 MVP 的 View 更"被动"
- B. MVP 中 View 通过接口与 Presenter 解耦
- C. MVC 中 Model 一定不知道 View
- D. MVP 出现时间早于 MVC

<details><summary>答案</summary>B — MVP 的核心创新就是通过 IView 接口解耦 View 和 Presenter。MVP 出现于 1990s，晚于 MVC（1970s）。</details>

**10.** 以下哪个不是 MVVM 数据绑定的常见实现方式？

- A. 脏检查（Dirty Checking）
- B. Getter/Setter 劫持
- C. Proxy 代理
- D. 观察者模式轮询数据库

<details><summary>答案</summary>D — 数据绑定是 View ↔ ViewModel 的同步机制，不涉及数据库轮询。脏检查（AngularJS）、属性劫持（Vue 2）、Proxy（Vue 3）都是数据绑定实现方式。</details>

**11.** 一个 IDE（如 VS Code）需要支持大量第三方插件扩展，最适合的表现层架构是？

- A. MVC
- B. PAC
- C. MVP
- D. Front Controller

<details><summary>答案</summary>B — PAC 的树形 Agent 结构天然适合 IDE 这类复杂交互系统，每个工具窗口可以是一个 Agent，通过父 Agent 协调。但注意：VS Code 本身用的是微内核架构（插件体系）+ 部分 MVVM。</details>

**12.** "当用户修改了购物车中商品数量，总价自动更新"——这种场景最适合？

- A. MVC 的观察者通知
- B. MVP 的 Presenter 命令
- C. MVVM 的双向数据绑定
- D. PAC 的层级通信

<details><summary>答案</summary>C — MVVM 的自动数据绑定最简洁：购物车数据变化 → ViewModel 计算总价 → View 自动更新。</details>

---

### 多选题（3 题）

**13.**（多选）以下属于表现层架构模式的是？

- A. MVC
- B. MVP
- C. 管道-过滤器
- D. MVVM
- E. Front Controller

<details><summary>答案</summary>A、B、D、E — 管道-过滤器属于架构风格层面（数据流风格），不是表现层模式。</details>

**14.**（多选）关于 MVC 和 MVVM，以下说法正确的是？

- A. MVC 的 Controller 处理用户输入
- B. MVVM 的 ViewModel 不持有 View 引用
- C. MVC 中 View 总是可以直接访问 Model
- D. MVVM 用数据绑定替代了 MVC 中 Controller 的手动同步

<details><summary>答案</summary>A、B、D — C 错误：Web MVC 中 View 通常通过 Controller 获取数据，不直接访问 Model。</details>

**15.**（多选）选择表现层模式时需要考虑的因素包括？

- A. 团队的测试策略（单元测试覆盖率要求）
- B. 前端框架的生态（如 Vue 自带响应式）
- C. 数据库类型（关系型 vs NoSQL）
- D. UI 复杂度（简单表单 vs 复杂交互）

<details><summary>答案</summary>A、B、D — 数据库类型与表现层模式选型无关。</details>

---

### 简答题（3 题）

**16.** 请用数据流向图描述 MVC、MVP、MVVM 三种模式中"用户点击按钮"这一操作的完整数据流。

<details><summary>参考</summary>

- **MVC**：用户点击 → Controller.handleClick() → Model.update() → Model.notifyObservers() → View.refresh()
- **MVP**：用户点击 → View 调用 IView.onClick() → Presenter.handleClick() → Model.update() → Presenter 判断结果 → IView.showResult() → View 更新
- **MVVM**：用户点击 → View 触发 Command → ViewModel.execute() → Model.update() → ViewModel 属性变化 → 自动绑定 → View 自动更新

核心差异：MVC 用观察者通知，MVP 用接口回调，MVVM 用数据绑定自动同步。
</details>

**17.** 某团队从 MVC 迁移到 MVP 后，单元测试覆盖率从 30% 提升到 80%。请解释 MVP 为什么能提升可测试性。

<details><summary>参考</summary>

MVP 提升测试性的两个关键机制：
1. **IView 接口抽象**：Presenter 依赖 IView 接口而非具体 View。测试时用 Mock View 替代真实 View，不需要启动 UI 环境。
2. **逻辑集中**：所有 UI 逻辑都在 Presenter 中，View 只负责渲染。Present 是纯逻辑类，可以直接用 JUnit/Mockito 测试，不需要 Espresso/UI Automator。

对比 MVC：Controller 通常与 View 紧耦合（如通过 findViewById），测试 Controller 必须启动 Activity/View，测试成本高。
</details>

**18.** 解释 Front Controller 模式和 MVC 的 Controller 之间的关系：它们是同一个概念吗？为什么 Spring MVC 同时使用了这两种模式？

<details><summary>参考</summary>

不是同一个概念：
- **MVC 的 Controller**：负责处理特定请求的业务协调（如 UserController 处理用户相关请求）
- **Front Controller**：是架构模式层面的统一入口，负责请求分发

Spring MVC 同时使用两者：
- `DispatcherServlet` 作为 Front Controller：统一接收所有 HTTP 请求，完成认证/日志等通用处理
- `@Controller` 类作为 MVC Controller：处理具体的业务请求协调

前端控制器解决"横切关注点"，业务控制器解决"具体业务协调"，两者互补。
</details>

---

### 情景分析（2 题）

**19.** 某公司开发一款实时协作文档编辑器（类似 Google Docs），需求如下：
- 多人同时编辑同一文档，变更实时同步
- 支持 Web、iOS、Android 三端
- 需要离线编辑能力（网络恢复后自动合并冲突）
- 界面复杂：富文本工具栏、评论面板、版本历史侧栏

请从表现层架构角度回答：
1. 你会为主编辑器选用哪种表现层模式？为什么？
2. 评论面板和版本历史是否需要同一种模式？

<details><summary>参考</summary>

1. **MVVM** 是最佳选择：
   - 数据驱动：文档内容变化 → ViewModel 状态更新 → 所有视图自动同步（配合 OT/CRDT 冲突解决）
   - 多端统一：同一套 ViewModel 逻辑可复用于 Web（Vue/React）、iOS（SwiftUI）、Android（Jetpack Compose）
   - 离线支持：ViewModel 管理本地 Draft 状态，网络恢复后同步

2. 不同模块可以用不同策略：
   - 主编辑器：MVVM（复杂数据绑定）
   - 评论面板：MVP（评论列表交互简单，MVP 的 IView 接口足够）
   - 版本历史：MVC（只读展示，简单的请求-响应模式即可）
</details>

**20.** 某金融 App 的登录模块需要支持：
- 密码登录、指纹登录、人脸登录三种方式
- 登录失败 3 次锁定 5 分钟
- 登录成功/失败需要上报埋点
- 所有交互逻辑需要 90% 以上的单元测试覆盖率

请设计这个登录模块的表现层架构，画出组件关系图并说明各组件职责。

<details><summary>参考</summary>

推荐 **MVP** 模式：

```
   FingerprintLogin         PasswordLogin        FaceLogin
         ↓                      ↓                   ↓
         └──────────────────────┴───────────────────┘
                               ↓
                    ┌─────────────────────┐
                    │   ILoginView 接口    │  ← Mock 接口
                    │  - showLoading()    │
                    │  - showError(msg)   │
                    │  - navigateHome()   │
                    │  - lockLogin(sec)   │
                    └─────────┬───────────┘
                              │
                    ┌─────────┴───────────┐
                    │   LoginPresenter     │  ← 单元测试目标
                    │  - login(cred)       │
                    │  - checkLockState()  │
                    │  - reportAnalytics() │
                    └─────────┬───────────┘
                              │
                    ┌─────────┴───────────┐
                    │   AuthModel          │
                    │  - authenticate()    │
                    │  - getLockState()    │
                    └─────────────────────┘
```

各组件职责：
- **ILoginView**：定义 UI 操作接口（加载、错误提示、跳转、锁定倒计时）
- **LoginPresenter**：处理所有登录逻辑、锁定策略、埋点上报（纯逻辑，100% 可测）
- **AuthModel**：封装认证 API 调用和锁定状态管理
- **View 层**：三种登录方式的具体 UI 实现，只负责收集用户输入和渲染

为什么不用 MVVM：密码输入、指纹触发是一次性操作（非持续数据绑定），MVP 的接口回调更自然。
</details>

---

## 六、学习检查清单

- [ ] 能独立画出 MVC、MVP、MVVM 三张交互图
- [ ] 能一句话区分三种模式的核心差异
- [ ] 知道 MVP 的 IView 接口的作用
- [ ] 理解 MVVM 数据绑定的两种方向
- [ ] 了解 PAC 的树形层级通信规则
- [ ] 知道 Front Controller 解决了什么问题
- [ ] 能在给定场景中选择合适的表现层模式并阐述理由
- [ ] 完成 20 道练习，正确率 ≥ 75%
