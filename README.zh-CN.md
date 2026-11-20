# Always UI

[English](README.md) · [简体中文](README.zh-CN.md) · [MIT 开源协议](LICENSE)

**先把布局想对，再把别扭的地方改掉。**

聊天软件不该硬套数据看板的布局。一个选中状态，也不需要外框、复选框和勾号反复强调。

**Always UI** 是给桌面 Agent 用的UI/UX设计 Skill：它会在开工之前先判断软件适合什么布局，也会在完工后检查界面哪里不合理、不好用。

## 主要功能

### `design` — 先想清楚怎么布局

“这里不要用选择器，那里换成卡片”。受够了在一滩烂泥中修修改改？

**Always UI**从分析用户软件行为出发，再决定导航、页面分区、信息层级和不同尺寸屏幕的布局。

内置 **11 类界面方向**，包括聊天、SaaS 工作台、数据分析、项目管理、电商、编辑器、社区、文件管理、金融、管理后台和预约服务。混合界面也不会生搬硬套某种模板。

```text
$always-ui design 帮我规划一下软件的主界面。
```

[查看 11 类布局指南](references/design-archetypes.md) · [查看分类数值预设表](references/value-presets.md)

### `check` — 找出哪里不好看、不合理

框套框、重复勾选、主次不分的按钮、不合适的开关和复选框……

Always UI 会检查 **24 类常见 UI 问题**，指出问题在哪里、为什么不合适、怎么做最小修改。而用户依然可以保留软件的个性，不会因为“不够标准”就被判错。

```text
$always-ui check 检查这个页面，不要改变现有视觉风格。
```

[查看 24 类检查规则](references/check-catalog.md)

## 安装

**不想敲命令？直接对你的编程 Agent 说：**

> 在当前项目安装 Always UI，运行 `npx skills add handFOOLed/always-ui`，然后用 `$always-ui design` 帮我规划界面。

一句话就可以开始使用。

**命令行安装** — 在项目目录运行：

  **项目安装**

```bash
npx skills add handFOOLed/always-ui
```

  **全局安装**

```bash
npx skills add handFOOLed/always-ui -g
```

  **npm 全局安装**

```bash
npm install -g skills
skills add handFOOLed/always-ui
```

npm命令使用的是 [Skills CLI](https://github.com/vercel-labs/skills)，通过 GitHub 安装 Skill。安装完成后，在 Agent 中输入 `$always-ui design` 或 `$always-ui check` 即可。

---

由 [handFOOLed](https://github.com/handFOOLed) 维护。欢迎反馈问题与贡献改进。
