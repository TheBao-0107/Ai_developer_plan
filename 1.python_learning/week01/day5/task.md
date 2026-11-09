# W1D5 · 复习 + Git 基础

> 计划日期：2026-11-06（周五）　｜　实际日期：2026-11-06
> 对应：书第 2–4 章复习 + Git 基础　｜　预计用时：60 分钟
> 针对：内置名称遮蔽、排序是否修改原列表及返回值、`del` 与方法调用的区别。

## 今日目标

- [ ] 用列表、统计、排序、切片和循环完成一份小报告。
- [ ] 自查变量名，能说明 `sort()`、`sorted()`、`del` 的作用。
- [ ] 理解工作区、暂存区、本地提交和远端仓库，自己完成一次提交与推送。

今天按日历的工具日安排：**一道综合小题 + Git 操作任务**。学习 30 分钟、练习 25 分钟、小结 5 分钟；有余力再订正旧代码，不额外增加必做题。

可用知识：W1D1–W1D4 已学内容。本题不需要 `if`、字典、函数定义或导入库。

---

## 一、学习（约 30 分钟）

### 1. Python 复习与手敲（12 分钟）

按主题翻看书第 2–4 章：变量命名、列表排序、统计、切片和遍历。选 **两个最不熟的小例子** 手敲到本目录的 `examples.py` 并运行，不必重敲整章。

最后留 3 分钟完成下面的简短自查。针对：W1D3、W1D4 的遗留薄弱点。

1. `sort()` 和 `sorted()` 各自是否修改原列表？各自返回什么？
2. `del` 是用点号调用的方法吗？删除一个元素并保留被移出的值时，你会选择哪种已学操作？
3. 为什么不宜把变量命名为 `list` 或 `round`？以后多个英文单词组成的变量名准备怎样写？

**我的答案：**

1. sort()会修改原列表，返回None，sorted()不会修改原列表，返回排序后的列表
2. del不是用点号调用的；我会选择pop()
3. 因为list或round这种是python已经有的类型名，用它们来做变量的名称会容易引起误解；打算用驼峰命名法

**C++ 对照：** Python 的列表赋值要分清“两个名称指向同一个列表”和“创建副本”；遍历时用缩进表示循环体。本题循环后的输出位置也要留意。

### 2. Git 概念与命令（18 分钟）

先理解这条流程：**编辑文件（工作区）→ `add`（暂存区）→ `commit`（本地提交）→ `push`（远端仓库）**。

| 命令                     | 这一步在检查或改变什么                                    |
| ---------------------- | ---------------------------------------------- |
| `git status`           | 查看分支，以及已暂存、未暂存、未跟踪的文件。                         |
| `git diff`             | 查看已跟踪文件在工作区与暂存区之间的差异。新建但尚未 `add` 的文件通常不会显示在这里。 |
| `git add 路径`           | 把指定路径当前的改动放入暂存区。之后再编辑文件，需要再次 `add` 才能把新改动也暂存。  |
| `git diff --cached`    | 查看暂存区与上次提交之间的差异，也就是准备提交的内容。                    |
| `git commit -m "提交说明"` | 把暂存区的内容记录成一次本地提交。                              |
| `git log --oneline -5` | 查看最近 5 次提交，每次显示一行。                             |
| `git push`             | 把本地提交推送到已配置的远端分支。尚未提交的文件改动不会随之上传。              |

本仓库当前分支为 `master`，已关联 `origin/master`。后面的命令都在仓库根目录运行。

用 VS Code 打开根目录的 `.gitignore`，只看 `__pycache__/` 和 `*.pyc` 两条规则：它们用于忽略 Python 生成的缓存。`.gitignore` 主要影响未跟踪文件，不会自动让已经跟踪的文件退出跟踪。今天无需修改这个文件。

**用自己的一句话解释：忽略这两类缓存文件有什么好处？**

> 我的理解：这些缓存文件没有参考价值，不需要上传

---

## 二、练习（约 25 分钟）

### 练习 1（综合基础，约 10 分钟）：相机耗时小报告 → `ex1_capture_report.py`

一次相机采集测试依次记录了 4 次耗时，单位为毫秒：**42、30、36、52**。请按以下要求生成报告。

1. 在一个列表里按采集顺序保存这 4 个数，初始数据只写一次。
2. 用已学的统计操作算出平均耗时。
3. 得到一份按耗时从小到大排列的新列表，保留原始列表的顺序；再用切片取得最快的两次。
4. 完成计算、排序和切片之后，再按下方示例统一输出。第一行必须打印原始列表，不能另外重新构造一份。
5. 最后两行用 `for` 循环逐条打印最快的两次耗时。平均值和最快两次的数据必须由程序算出，不直接写死结果。
6. 变量采用小写加下划线命名，不使用 `list`、`round`、`sum`、`min`、`max`、`sorted` 等内置名称作为变量名。

**示例输出（要逐字符一致）：**

```text
原始耗时：[42, 30, 36, 52] ms
平均耗时：40.0 ms
最快两次：[30, 36] ms
逐条查看：
30 ms
36 ms
```

中文冒号使用 `：`，`ms` 前有一个普通空格；不要额外输出空行。平均值直接输出计算结果即可，本题无需新的小数格式语法。

**运行验证（在仓库根目录的 PowerShell 中）：**

```powershell
python 1.python_learning/week01/day5/ex1_capture_report.py
```

**验收：**

- [x] 正常运行，6 行输出与示例逐字符一致。
- [x] 原始数据只写一次，排序后原始列表仍保持采集顺序。
- [x] 平均值来自统计计算，最快两次来自排序结果的切片。
- [x] 最后两行由循环生成，标题与汇总没有在循环中重复打印。
- [x] 没有把内置名称当变量名，也没有直接写死计算结果。

<details><summary>提示（卡住 10 分钟再看）</summary>

先分清“原始记录”和“按耗时排序的结果”。选择排序操作时，分别检查它会不会改动原列表、会返回什么。平均值需要总耗时和记录数量；切片从排好序的结果中取出前两个元素。最后再安排输出和循环的缩进。

</details>

### 练习 2（Git 操作，约 15 分钟）：整理并推送本周学习记录

这部分由你亲自执行。Git 的提交编号、改动内容和输出会随仓库状态变化，**请粘贴真实输出**，不要求它们与固定示例一致。

#### A. 检查工作区

保存已经写好的文件，运行：

```powershell
Set-Location D:\Code\Ai_developer_plan
git status
git diff
```

阅读输出，区分已有文件的修改和新文件。`git diff` 进入分页显示时，按 `q` 返回命令行。已有的 `progress.md` 改动、W1D4 批改记录和今天的新文件都属于本周学习记录。

**粘贴 `git status` 输出，以及 `git diff` 中你看懂的一小段差异；若差异输出为空，就写“无输出”并说明原因：**

```text
// 在这之前由于我手快了，直接git add + git commit + git push推上去了，因此显示没有要提交的内容了
PS D:\Code\Ai_developer_plan> Set-Location D:\Code\Ai_developer_plan\
PS D:\Code\Ai_developer_plan> git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
PS D:\Code\Ai_developer_plan> git diff
//什么输出内容都没有
```

#### B. 检查暂存内容

先填写本文第三节的今日小结，再回到这里收尾；这 5 分钟计入小结时间。保存文件后运行：

```powershell
git add -- 1.python_learning/week01 progress.md
git diff --cached
git status
```

核对暂存区包含本周练习、题目、批改记录和已有的进度更新。比较 `git diff` 与 `git diff --cached`，理解两者看的差异不同。

**粘贴暂存后的 `git status` 输出，并用一句话说明这次准备提交哪些内容：**

```text
//理由和A中的理由一样，由于我手快了，写完ex1_capture_report.py验证通过就直接提交上去了，因此显示nothingtocommit
PS D:\Code\Ai_developer_plan> git diff --cached
PS D:\Code\Ai_developer_plan> git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean我准备提交：
```

#### C. 提交、推送和验证

上一步填写记录又改动了 `task.md`，保存后再次暂存，再提交：

```powershell
git add -- 1.python_learning/week01 progress.md
git commit -m "W1D5: 本周复习与 Git 练习"
git push
git log --oneline -5
git status
```

每条命令成功后再执行下一条。打开 GitHub 上的本仓库，确认能看到今天提交的 `ex1_capture_report.py`。

**粘贴本次 `git commit`、`git push`、`git log --oneline -5` 和最后一次 `git status` 的输出：**

```text
//在A之前就提交了，这些是当时命令执行的结果
PS D:\Code\Ai_developer_plan> git add .
warning: in the working copy of '1.python_learning/week01/day5/ex1_capture_report.py', LF will be replaced by CRLF the next time Git touches it
PS D:\Code\Ai_developer_plan> git commit -m "day5"
[master 8917c69] day5
 1 file changed, 10 insertions(+)
PS D:\Code\Ai_developer_plan> git push
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 869 bytes | 869.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/TheBao-0107/Ai_developer_plan
   5dbaf68..8917c69  master -> master
PS D:\Code\Ai_developer_plan> git log --oneline -5
8917c69 (HEAD -> master, origin/master) day5
5dbaf68 day5
f4b9beb day4
6eba149 day3
4e1c92d day2
PS D:\Code\Ai_developer_plan> git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

粘贴这些验证输出会再次修改 `task.md`，所以之后它显示为“未暂存”是正常的。本次记录保留在本地，批改后和 `review.md` 一起提交即可，不必为了记录状态反复提交。

**验收：**

- [x] 能用自己的话区分工作区、暂存区、本地提交和远端仓库。
- [x] 已查看两种 `diff`，确认准备提交的内容。
- [x] 本周练习和已有批改记录已自行提交、推送，GitHub 上能看到今天的代码。
- [x] 已粘贴提交、推送及最近 5 次提交的真实输出。
- [x] 能说明 `.gitignore` 中两条缓存规则的作用。

如果命令报错，保留原样输出，说明卡在哪一步再来问我；排查时间计入今天的实际用时。

---

## 三、今日小结（5 分钟，我自己填）

- 实际用时：40分钟
- 今天学会了：轻微复习了一下之前的内容，git的相关操作，在今天之前我已经自学掌握
- 还不太懂的：无
- 遇到的报错（贴最后一行）及原因：无

**另外（可选，不算在 60 分钟内）：** 按 W1D4 的批改建议，订正旧代码中遮蔽内置名称的变量及 W1D3 的排序笔记；改完代码再运行，确认输出保持正确。

---

✅ 完成代码、自查和 Git 操作后，对 AI 说：**「批改 W1D5」**。
