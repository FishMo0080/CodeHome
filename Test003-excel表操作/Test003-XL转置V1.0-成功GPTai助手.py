import pandas as pd

# 读取Excel文件
df = pd.read_excel('U-learning（1~4月）V4.xlsx')

# 通过reshape函数将A列单元格按照要求转换为多列，注意表头要改为A，即A1单元格的值为A
df_new = pd.DataFrame(df['A'].values.reshape(-1, 6))

# 给新生成的列命名，并连接到原始数据框中
df_new.columns = [f'{chr(65+i)}1' for i in range(df_new.shape[1])]
df = pd.concat([df.drop('A', axis=1), df_new], axis=1)

# 写入转换后的结果到新的Excel文件中
writer = pd.ExcelWriter('U-learning（1~4月）V4-new.xlsx')
df.to_excel(writer, index=False)
writer.close()