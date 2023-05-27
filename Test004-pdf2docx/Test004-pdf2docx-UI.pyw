from pdf2docx import parse
import tkinter as tk
from tkinter import messagebox
def run_program():
    # 获取输入框中的内容
    cinput = entry.get() 
    pdf_file = f'input/{cinput}.pdf'
    docx_file = f'output/{cinput}.docx'
    # convert pdf to docx
    parse(pdf_file, docx_file)
    # 弹出对话框，提示用户数据已导出
    messagebox.showinfo("提示", "你的文档可能已完成转换 (๑¯ิε ¯ิ๑) ")
        # 关闭主窗口
    root.destroy()
# 创建主窗口
root = tk.Tk()
root.title("PDF转换DOCX——by Fish")
# 创建标签和输入框
label = tk.Label(root, text="请你要转换的文件名不带后缀名：")
label.pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
# 创建“运行程序”按钮
button = tk.Button(root, text="执行转换", command=run_program)
button.pack(pady=5)
# 创建提示语
tip1 = tk.Label(root, text="**请耐心等待一下。", justify="left",highlightbackground="yellow")
tip2 = tk.Label(root, text="**执行时间根据文档大小而不同", justify="left")
tip2.pack(side="bottom")
tip1.pack(side="bottom")
# 进入消息循环
root.mainloop()