import os
import glob
import openpyxl
# 创建新的工作簿
new_workbook = openpyxl.Workbook()
new_sheet = new_workbook.active
# 遍历Ptest文件夹下的所有excel文件
for file_path in glob.glob("D:/Ptest/*.xlsx"):
    # 打开excel文件
    workbook = openpyxl.load_workbook(file_path)
    # 获取sheet1
    sheet = workbook["Sheet1"]
    # 获取A1和A2单元格的数据
    a1_data = sheet["A1"].value
    a2_data = sheet["A2"].value
    # 将数据添加到新的工作簿中
    new_sheet.append([a1_data, a2_data])
# 保存新的工作簿
new_workbook.save("D:/Ptest/summary.xlsx")