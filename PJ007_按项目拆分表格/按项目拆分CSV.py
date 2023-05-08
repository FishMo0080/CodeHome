
import pandas as pd
# 读取CSV文件
df = pd.read_csv('input.csv',low_memory=False, encoding='GBK')
# 获取所有项目编号
proj_ids = df['B'].unique()
# 按照项目编号分别拆分为多个表格
for proj_id in proj_ids:
    proj_df = df[df['B'] == proj_id]
    # 将每个表格保存为单独的CSV文件
    proj_df.to_csv(f'output_{proj_id}.csv', index=False, encoding='utf-8-sig')