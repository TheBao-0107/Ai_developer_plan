# W1D1 · 环境准备 + 第一个程序

> 计划日期：2026-11-02（周一）　｜　实际日期：2026-11-02
> 教材：《Python 编程：从入门到实践（第 3 版）》第 1 章　｜　预计用时：60 分钟

## 今日目标

- [x] 能指出终端和 VS Code 各自使用的 Python 解释器。
- [x] 能在交互模式下运行一行 Python，也能从终端和 VS Code 运行自己保存的 `.py` 文件。
- [ ] 能读懂一次真实报错，修好程序，再把今天的练习提交到本项目。

## 一、学习（30 分钟）

### 1. 核对终端环境（7 分钟）

用 VS Code 的「文件 → 打开文件夹」打开 `D:\Code\Ai_developer_plan`。选「终端 → 新建终端」，使用 PowerShell。以下终端命令都从这个仓库根目录运行。

```powershell
python --version
where.exe python
git --version
git config --global user.name
```

在 PowerShell 里要写全 `where.exe`。对照环境记录，Python 版本应为 3.14.7，路径列表第一项应为 `D:\myApp-Python\python\python3.14.7\python.exe`。如果后面还有一项 `WindowsApps`，看第一项即可。

**我的终端记录**（在下面粘贴四条命令和各自的实际输出）

```text
PS D:\Code\Ai_developer_plan> python --version
Python 3.14.7
PS D:\Code\Ai_developer_plan> where.exe python
D:\myApp-Python\python\python3.14.7\python.exe
C:\Users\24170\AppData\Local\Microsoft\WindowsApps\python.exe
PS D:\Code\Ai_developer_plan> git --version
git version 2.56.0.windo-0107
PS D:\Code\Ai_developer_plan> git config --global user.name  
Bao
```

### 2. 选好 VS Code 解释器（6 分钟）

按 `Ctrl+Shift+X` 打开扩展，逐项确认下面两个 Microsoft 扩展已安装并启用，缺哪项就补哪项。打开今天目录里的 `examples.py`，按 `Ctrl+Shift+P`，执行 `Python: Select Interpreter`，选中上一步核对过的解释器。

- [x] Python（`ms-python.python`）
- [x] Pylance（`ms-python.vscode-pylance`）

- 我选中的解释器完整路径：`D:\myApp-Python\python\python3.14.7\python.exe`

### 3. 从一行命令到一个文件（17 分钟）

1. 读第 1 章中运行 Python 和第一个程序的部分。在 PowerShell 输入 `python` 并回车。看到 `>>>` 后，手敲 `print("Hello")` 并回车，再输入 `exit()` 回到 PowerShell。
2. 在 `examples.py` 里手敲书中第一个输出文字的例子，按 `Ctrl+S` 保存。如果教材还没到，就手敲刚才的交互示例。文件里只写 Python 代码，`>>>` 是终端的提示符。
3. 先在 PowerShell 运行下面的命令，再回到 `examples.py`，点编辑器右上角的「运行 Python 文件」按钮。对照两次输出。

```powershell
python .\1.python_learning\week01\day1\examples.py
```

- 我在交互模式看到的输出：`Hello`
- 我从文件运行看到的输出：`Hello`

- [x] 同一个文件用终端命令和运行按钮跑过，两次输出一致。

## 二、练习（动手 20 分钟，小结后另用 5 分钟提交）

### 练习 1（基础，12 分钟）· 相机采集日志 → `ex1_camera_log.py`

你要用三条日志记录一次相机采集。请只用 `print()` 和字符串，每条日志单独调用一次 `print()`，依次记录打开相机、采集第一帧、关闭相机。保存后，在 PowerShell 运行 `python .\1.python_learning\week01\day1\ex1_camera_log.py`。

**示例输出（逐字符一致）**

```text
[CameraHAL] OPEN
[CameraHAL] FRAME 001
[CameraHAL] CLOSE
```

**验收**

- [x] 恰好三行，顺序与示例相同，行首行尾没有多余空格。
- [x] 大小写、方括号和半角空格与示例一致，帧号保留为三位 `001`。

<details><summary>提示（卡住 10 分钟再看）</summary>

先让第一条日志单独跑通，再补后两条。核对第二行时，把帧号当成日志里要原样显示的一段文字。

</details>

### 练习 2（读报错，8 分钟）· 让最后一条日志出错

在刚跑通的文件里，把最后一条日志中 `print` 的首字母改成大写，保存，用练习 1 的命令再跑一次。把报错的最后一行原样粘到下面，写一句自己的解释。然后修好这一处，保存，再跑一次。

**报错的最后一行**

```text
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

Python 在哪一行遇到了什么问题？

**我的答案：**编译发生报错，存在没有定义过的函数名“Print”

- [x] 修好后重新运行，三条日志都和示例相同。

## 三、今日小结（5 分钟，我自己填）

- 实际用时：__10__ 分钟
- 今天我学会了 __________先前都已掌握的一些Python基础__________
- 还有哪一步需要再试一次？ __________无需再试__________

## 四、第一次提交（5 分钟，计入练习）

在仓库根目录运行下面的命令，核对今天的三个文件。把输出粘到下方，保存本页后再提交。

```powershell
git status --short --untracked-files=all -- 1.python_learning/week01/day1/
```

```text

```

亲自在 PowerShell 逐条执行，每条成功后再执行下一条。

```powershell
git add -- 1.python_learning/week01/day1/
git commit -m "W1D1: 环境和第一个程序"
git push
git log -1 --oneline
```

确认推送成功、最后一条命令显示今天的提交后，对我说 **「批改 W1D1」**。
