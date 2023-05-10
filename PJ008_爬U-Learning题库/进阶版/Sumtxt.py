import os
# 获取当前文件夹路径
def all_txt():
    folder_path = os.path.join(os.getcwd(), 'output')
    # 定义汇总后的文件名
    new_file_name = 'all.txt'
    # 打开汇总后的文件
    with open(new_file_name, 'w', encoding='utf-8') as f:
        # 遍历当前文件夹
        for filename in os.listdir(folder_path):
            # 判断是否为txt文件
            if filename.endswith('.txt'):
                # 打开txt文件
                with open(f'output/{filename}', 'r', encoding='utf-8') as f_txt:
                    # 读取txt文件内容，并写入汇总后的文件
                    f.write(f_txt.read())
                    f.write('\n')  # 每个txt文件之间添加空行
    return