# Always UI

[English](README.md) · [简体中文](README.zh-CN.md) · [MIT 开源协议](LICENSE)

**先把布局想对，再把别扭的地方改掉。**

聊天软件不该硬套数据看板的布局。一个选中状态，也不需要外框、复选框和勾号反复强调。

**Always UI** 是给编程 Agent 用的界面设计 Skill：帮它判断软件适合什么布局，也帮它看出界面哪里不合理、不好用。你定产品风格，它不擅自替你换一套模板。

## 主要功能

### `design` — 先想清楚怎么布局

从用户在软件里**实际要做什么**出发，再决定导航、页面分区、信息层级和不同屏幕的布局。

内置 **11 类界面方向**，包括聊天、SaaS 工作台、数据分析、项目管理、电商、编辑器、社区、文件管理、金融、管理后台和预约服务。混合型产品也不必被塞进一种模板。

```text
$always-ui design 帮我规划一款桌面聊天软件的主界面。
先比较两种布局，再决定用哪种。
```

[查看 11 类布局指南](references/design-archetypes.md)

### `check` — 找出哪里不好看、不合理

框套框、重复勾选、满屏都在抢眼球的主按钮、不合适的开关和复选框、看不清的焦点、没有退路的错误提示……

Always UI 会检查 **20 类常见 UI 问题**，说清楚问题在哪里、为什么影响使用、怎么做最小修改。刻意选择的视觉风格，不会因为“不够标准”就被判错。

```text
$always-ui check 检查这个设置页面的框套框、
重复选中标记和控件误用，不要改变现有视觉风格。
```

[查看 20 类检查规则](references/check-catalog.md)

## 安装

**不想敲命令？直接对你的编程 Agent 说：**

> 在当前项目安装 Always UI，运行 `npx skills add handFOOLed/always-ui`，然后用 `$always-ui design` 帮我规划界面。

允许 Agent 执行安装命令，就可以开始使用。

**命令行安装** — 在项目目录运行：

```bash
npx skills add handFOOLed/always-ui
```

希望所有项目都能用？

```bash
npx skills add handFOOLed/always-ui -g
```

**习惯用 npm 全局安装命令行工具？**

```bash
npm install -g skills
skills add handFOOLed/always-ui
```

以上使用的是 [Skills CLI](https://github.com/vercel-labs/skills)，通过 GitHub 安装 Skill，**并不是**从 npm 下载一个单独的 `always-ui` 包。

安装完成后，在 Agent 中输入 `$always-ui design` 或 `$always-ui check` 即可。

---

由 [handFOOLed](https://github.com/handFOOLed) 维护。欢迎反馈问题与贡献改进。
