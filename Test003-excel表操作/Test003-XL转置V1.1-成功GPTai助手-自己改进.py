import pandas as pd
# 读取Excel文件
df = pd.read_excel('U-learning（1~4月）V4.xlsx')
# 通过reshape函数将A列单元格按照要求转换为多列，注意表头要改为A，即A1单元格的值为A
df_new = pd.DataFrame(df['A'].values.reshape(-1, 6))
df_new.to_excel('U-learning（1~4月）V4-new.xlsx', index=False, header=False)