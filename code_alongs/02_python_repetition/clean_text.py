
import re
from pathlib import Path

print("Thie is path of this script.")     # 这是该脚本的路径。

data_path = Path(__file__).parent/"data"

with open(data_path / "ml_text_raw.txt", 'r') as file:
    raw_text = file.read()

text_fixed_spacing = re.sub(r"\s+", " ", raw_text)

# similar code as in jupyter notebook for cleaning the rest of the text. 
# 与 jupyter notebook 中类似的代码，用于清理其余文本。

print(text_fixed_spacing)
























