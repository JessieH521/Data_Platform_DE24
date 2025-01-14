import pandas as pd

from pathlib import Path

# __file__ 在 Jupyter Notebook 中不存在，所以下面语句不能使用。
# __file__ 是 Python 脚本中内置的一个变量，它存储的是当前脚本的文件路径。
  
data_path = Path(__file__).parent / "data"

df = pd.read_csv(data_path / "calories.csv")

print(df.head())



# data_path = Path(__file__).parent / "data" 是一种用 Python 的 pathlib 模块动态生成文件路径的方式，常用于构造指向特定目录或文件的路径。这种写法特别适合在脚本中使用，因为它不会受到工作目录的影响。














# 1. echo $VIRTUAL_ENV, 专门用于查看 当前激活的 Python 虚拟环境的路径。

# 输出内容:
# 如果虚拟环境被激活，它会直接输出虚拟环境的路径。
# 如果没有激活虚拟环境，则输出为空。

# 适用范围:
# 仅适用于基于 venv 或 virtualenv 创建的虚拟环境（它们会设置 $VIRTUAL_ENV 环境变量）。


# 2. which python, 用于查找当前 Shell 使用的 python 可执行文件的路径。

# 输出内容:
# 如果激活了虚拟环境，会输出虚拟环境中 python 的路径。
# 如果没有激活虚拟环境，会输出系统默认 python 的路径（通常是全局安装路径）。

# 适用范围:
# 适用于任何环境下，不仅限于虚拟环境。
# 它会返回 Python 可执行文件的实际路径，因此也可以用来判断是否处于虚拟环境中。








