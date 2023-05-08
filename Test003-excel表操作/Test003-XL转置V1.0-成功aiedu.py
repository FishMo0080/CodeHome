import pandas as pd
# 读取Excel文件
df = pd.read_excel('U-learning（1~4月）V4.xlsx', header=None)
# 将数据按每6行一组进行分组
grouped = df.groupby(df.index // 6)
# 对每组数据进行转置
transposed_data = []
for _, group in grouped:
    transposed_data.append(group.transpose().values.reshape(-1))
# 将转置后的数据保存为Excel文件
new_df = pd.DataFrame(transposed_data)
new_df.to_excel('U-learning（1~4月）V4-new.xlsx', index=False, header=False)