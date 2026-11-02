# AI 应用开发转型 · 8 个月学习项目

> 2026.11 ～ 2027.6，从 Python 零基础到 AI 应用开发工程师（偏 Agent）。
> 计划详情见 `0.ai-dev-plan/00-总览.md`。

---

## 目录

| 路径 | 内容 |
|---|---|
| `AGENTS.md` | **给 AI 看的工作说明**：怎么出题、怎么批改、文件放哪 |
| `progress.md` | 学习进度，AI 根据它决定今天出什么题 |
| `0.ai-dev-plan/` | 8 个月计划；`11-第1月每日日历.md` 是每天的任务表；`templates/` 是题目和批改的格式 |
| `1.python_learning/` | 第 1 个月的练习代码，按 `weekNN/dayX/` 存放 |

---

## 每天怎么用（3 步）

### 1. 让 AI 出题

```
今天是 2026-11-02。请先阅读 AGENTS.md，再按里面的必读顺序读 progress.md 和日历，然后出今天的题。
```

### 2. 自己做

- 打开 `1.python_learning/weekNN/dayX/task.md`，按顺序学习、做题，最后填写"今日小结"
- 卡住 10 分钟以上再看提示，20–30 分钟以上再问 AI（只要提示）
- 做完提交：

  ```bash
  git add .
  git commit -m "W1D1: 环境和第一个程序"
  git push
  ```

### 3. 让 AI 批改

```
我做完 W1D1 了，请按 AGENTS.md 第 5 节批改，并更新 progress.md。
```

其他常用说法：「今天没学」、「周总结」、「月度考核」、「给提示」、「给我答案」，见 `AGENTS.md` 第 3 节。

---

## 用哪种 ChatGPT？

**A. 能读写本地文件的（Codex CLI / Codex IDE 插件 / ChatGPT 桌面版连接本地文件夹）**：推荐。
在 `D:\Code\Ai_developer_plan` 目录下打开，它会自动读取 `AGENTS.md`，能直接创建 task.md、运行代码、写 review.md、更新 progress.md。

**B. 网页版 ChatGPT（Projects 项目功能）**：
1. 新建项目，把 `08-ChatGPT使用指南.md` 里的"背景说明"粘贴进项目指令，并加一句：「严格按照项目文件 AGENTS.md 工作」
2. 上传这些文件到项目：`AGENTS.md`、`0.ai-dev-plan/01-第1月-Python基础.md`、`0.ai-dev-plan/11-第1月每日日历.md`、`0.ai-dev-plan/templates/` 里的两个模板
3. **每天出题时把最新的 `progress.md` 内容贴进对话**（项目文件不会自动更新）
4. 它没法直接写文件：把它给出的 task.md 内容保存到指定路径；批改时把代码和 task.md 贴给它，再把它给出的进度更新手动改进 `progress.md`
