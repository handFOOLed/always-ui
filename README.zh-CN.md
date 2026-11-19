# Always UI

**Guardrails, not taste. —— 约束交互缺陷，不规定审美。**

**Always UI** 是一个开源 Agent Skill，调用名为 `interaction-design-rules`，面向 AI 编码 Agent 的 Web 与桌面 UI 设计、实现和评审。

它负责避免控件语义错误、键盘焦点不可见、状态反馈不真实、折叠后控件仍可聚焦、长文件名显示不合理，以及原生窗口拖拽区域误伤交互等问题。

**它不负责告诉 Agent：页面必须长什么样。** 配色、字体、布局、品牌个性和组件外观，首先由你的产品决定。

## 设计哲学

原始版本来自中文界面设计准则。开源版将规则分成三类：

- **硬约束：** 控件表达真实状态，焦点可见，失败可处理，隐藏内容不能意外获取焦点；隐私与危险操作不能只靠颜色暗示。
- **情境建议：** 避免重复的视觉边框，合理保留文件扩展名，必要时使用等宽数字，尊重平台原生行为。
- **可选审美：** 微明度色阶、双环焦点、连续圆角、暗色字重光学校正等，仅在项目已有相应视觉方向时按需使用。

这些规则不是为了把所有产品做成同一种「极简风」。

## 安装

仓库根目录就是 Skill 目录。仓库名为 `always-ui`，Skill 名保持 `interaction-design-rules`，便于现有项目继续调用。

Codex 用户级安装：

```bash
git clone https://github.com/handFOOLed/always-ui.git ~/.agents/skills/interaction-design-rules
```

项目级安装：将仓库文件复制到 `<项目>/.agents/skills/interaction-design-rules/`，保证 `SKILL.md` 位于该目录下。

不同 Agent 的发现路径与调用机制可能不同，以宿主工具文档为准。

## 使用示例

```text
$interaction-design-rules 检查设置页的开关、勾选框、键盘焦点和保存反馈。
保留现有品牌风格，不要重设计整个页面。
```

```text
$interaction-design-rules 修复文件列表过窄时的截断问题。
优先保留扩展名，完整文件名仍须能查看和复制。
```

## 项目文件

- [`SKILL.md`](SKILL.md)：核心规则、适用范围、最小改动流程。
- [`references/implementation-notes.md`](references/implementation-notes.md)：按需加载的技术实现提示。
- [`references/visual-guidance.md`](references/visual-guidance.md)：**可选**审美建议，非全局设计系统。
- [`tests/evaluation-cases.md`](tests/evaluation-cases.md)：十个供 Agent A/B 对比的场景。
- [`scripts/validate.py`](scripts/validate.py)：结构与链接检查，无第三方依赖。

## 校验与贡献

运行 `python scripts/validate.py` 检查文件结构。静态检查通过不代表 Skill 已经证明提高设计质量。欢迎提交可复现的交互问题、平台适配改进和具备可观察验收结果的测试场景；不要把个人审美升级为通用硬约束。

协议：[MIT](LICENSE)。

[English README](README.md)
