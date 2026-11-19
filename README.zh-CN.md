# Always UI

**先判断怎样设计，再检查哪里不合理。Guardrails, not taste.**

**Always UI** 是一套开源 AI Agent 界面设计 Skill，采用两种模式：

| 模式 | 解决的问题 | 输出 |
| --- | --- | --- |
| **design** | 这类软件适合怎样的布局和交互？ | 产品任务分析、布局类型、导航与信息层级、响应式方案、取舍 |
| **check** | 现有页面哪里不好看、不合理、不好用？ | 有证据的问题清单、优先级、最小修复建议、验收方法 |

核心原则：**提升设计判断力，不把所有产品变成同一种模板。** 不默认指定颜色、字体、圆角、组件库或极简风格。

## 安装

仓库根目录就是 Skill 目录，**调用名为 `always-ui`**。

Codex 用户级安装示例：

```bash
git clone https://github.com/handFOOLed/always-ui.git ~/.agents/skills/always-ui
```

项目级安装：将仓库复制到 `<项目>/.agents/skills/always-ui/`，确保 `SKILL.md` 位于目录内。不要直接覆盖已有的定制文件。其他 Agent 的识别路径以对应宿主文档为准。

## 使用方式

### Design 模式：先分析，再设计

```text
$always-ui design 设计一款团队聊天软件的主界面。
先分析用户核心任务，比较两种桌面布局并给出移动端适配。
保留现有紫色品牌，不要直接套用通用 SaaS 仪表盘。
```

```text
$always-ui design 我要开发一个销售分析 SaaS。
先判断用户需要观察、比较和操作什么，再决定导航和图表布局。
```

### Check 模式：检查不合理设计

```text
$always-ui check 检查当前设置页的框套框、重复选中标记、
复选框和开关是否被滥用，以及主次视觉层级。保留整体品牌风格。
```

```text
$always-ui check 审查文件传输侧栏的长文件名、省略号、失败反馈、
键盘焦点与操作按钮拥挤问题，优先报告五个最重要的问题。
```

不指定模式时，创建/规划界面默认 **design**；检查/修复现有界面默认 **check**。

## Design：11 类产品布局方向

不是看见 SaaS 就生成侧栏加四张数据卡，而是根据 **用户主要任务** 选择结构。

| 产品类型 | 主要任务 |
| --- | --- |
| SaaS / 综合工作台 | 跨模块继续工作 |
| 聊天 / 协作 | 阅读会话、发送消息 |
| 项目 / 任务管理 | 管理事项、进度和责任人 |
| 数据分析 / 监控 | 对比指标、排查变化 |
| 电商 / 交易市场 | 搜索、比较、购买 |
| 编辑器 / 知识库 | 创建和整理内容 |
| 社交 / 社区 | 阅读帖子、交流 |
| 媒体 / 文件管理 | 查找、预览和组织资源 |
| 金融 / 交易 | 审核精确数据、执行操作 |
| 管理后台 / 运维 | 查询记录、处理异常 |
| 预约 / 服务流程 | 选时间、资源、确认 |

每类都包括适用场景、桌面与移动端布局、重要操作与状态、常见误区及替代方案，详见 [`references/design-archetypes.md`](references/design-archetypes.md)。混合型产品可以采用一个主类型和一个辅助类型，不要把全部导航都叠在一个页面里。

## Check：20 类界面反模式

重点检查你可能最讨厌的设计问题：

- **框套框**：卡片描边、内层描边、按钮描边层层嵌套，重复表达同一边界。
- **重复选中信号**：选中卡片外框、内部复选框、独立对勾、主题色标签同时出现。
- **控件语义不对**：互斥选项使用多个复选框；尚未提交的表单设置使用即时开关；命令与选值混淆。
- **视觉层级失衡**：所有按钮都抢主视觉，重要内容与辅助时间戳一样突出。
- **冗余装饰与密度失控**：无目的渐变、阴影、发光、过度留白或拥挤工具栏。
- **交互缺陷**：焦点不可见、保存反馈不真实、错误恢复困难、响应式布局失效、展开后焦点和动效不正确。

完整规则见 [`references/check-catalog.md`](references/check-catalog.md)。检查结果明确区分 **确定缺陷、较有把握的设计问题、可选审美建议**。有意设计且符合产品定位的特殊风格，不应被当作错误。

## 文件结构

- [`SKILL.md`](SKILL.md)：双模式选择和基本执行流程。
- [`references/design-archetypes.md`](references/design-archetypes.md)：11 类设计方向。
- [`references/check-catalog.md`](references/check-catalog.md)：20 类界面反模式。
- [`references/implementation-notes.md`](references/implementation-notes.md)：按需查阅的技术细节。
- [`references/visual-guidance.md`](references/visual-guidance.md)：可选的克制/微明度审美建议，不强制启用。
- [`tests/evaluation-cases.md`](tests/evaluation-cases.md)：双模式人工 A/B 评估场景。
- [`scripts/validate.py`](scripts/validate.py)：离线结构与链接检查。

## 从 v0.1.0 迁移

**调用名有破坏性变更**：`$interaction-design-rules` → **`$always-ui`**。请同步重命名本地 Skill 安装文件夹，以及项目 `AGENTS.md` 和脚本中的调用引用。旧名称**不会**自动成为别名。

以前的规则都可以在 `check` 模式中继续使用；`design` 负责规划而不强行替换原有产品设计系统。

## 验证与贡献

```bash
python scripts/validate.py
```

校验脚本检查安装结构与文档链接，不证明 Agent 一定更有设计能力。请使用 [人工测试场景](tests/evaluation-cases.md) 对比开关 Skill 的差异，尤其评估 **是否降低界面缺陷，同时保留设计创造力**。

欢迎提交有明确场景、可复现问题、适用条件及验收标准的新规则，不要把个人审美偏好升级为通用硬性规则。

协议：[MIT](LICENSE)。

[English README](README.md)
