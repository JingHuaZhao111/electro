import os
import csv

input_folder = 'data'
output_folder = 'out'

# 获取输入文件夹中的所有文件名
file_names = os.listdir(input_folder)

for file_name in file_names:
    # 去掉扩展名
    file_name_without_ext = os.path.splitext(file_name)[0]
    input_file = os.path.join(input_folder, file_name)
    output_file = os.path.join(output_folder, file_name)
    fixed_value = file_name_without_ext

    with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)

        for row in reader:
            # 在每一行的第一列前插入文件名（不包括扩展名）
            row.insert(0, fixed_value)
            writer.writerow(row)
