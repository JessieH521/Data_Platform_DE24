# Solving 


# 0. User input for ETL Parameters - Ask the user for 2 inputs:
# source file path
# destination file path

from pathlib import Path

source_file_path = input("Enter source file absolute path:")
destination_file_path = input("Enter destination file absolute path:")

# /Users/apple/Data_Platform/github/Data_Platform_DE24/exercises/exercise_0/input_data.csv
# /Users/apple/Data_Platform/github/Data_Platform_DE24/exercises/exercise_0/output_data.csv

print(f"source: {source_file_path}")
print(f"destination: {destination_file_path}")

# 验证源文件路径是否存在
if not Path(source_file_path).exists():
    print("Error: The source file does not exist.")



# others

# print(f"source: {input_source} {'*exist*' if Path(input_source).exists() else '*does not exist*'}")
# print(f"destination: {input_destination} {'*exist*' if Path(input_destination).exists() else '*does not exist*'}")





