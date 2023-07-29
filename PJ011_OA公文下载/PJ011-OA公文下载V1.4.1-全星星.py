# -*- coding: utf-8 -*-
import time,lxml.html
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  #这段代码并没有起作用
import tkinter as tk
from tkinter import messagebox

def run_program():
    # 获取输入框中的内容
    password.config(show="*")
    name = username.get()
    pwd = password.get()
    # 在这里编写程序的运行逻辑
    #1、打开网页登陆
    option = Options()#这段代码并没有起作用
    option.add_argument('--disable-blink-features=AutomationControlled') #这段代码并没有起作用
    web = Chrome(options=option)#这段代码并没有起作用
    #web = Chrome()
    web.implicitly_wait(5)
    web.get("http://oa.gmcc.net/oa/login?gourl=/client")
    time.sleep(2)
    web.find_element(by=By.XPATH,value='//*[@id="UserName"]').send_keys(name)
    web.find_element(by=By.XPATH,value='//*[@id="Password"]').send_keys(pwd)
    web.find_element(by=By.XPATH,value='//*[@id="linkeyform_value"]/div[4]/input[1]').click()
    time.sleep(4)
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]//a/li/div/span'))) #等待显示左边待办文件就继续执行
    time.sleep(3)
    html = web.page_source
    time.sleep(2)
    doc = lxml.html.fromstring(html)
    title_list = doc.xpath('//td[@class="el-table_2_column_13  cell-ellipsis el-table__cell"]//span/text()') #获取到标题内容
    OAnum = len(title_list) #得到标题数量
    #2、将所有标题放到txt
    data = []
    for title in title_list:
        data.append(f'{len(data)+1}、'+title) 
    with open(f'OAtitle.txt', 'w') as f:
        for item in data:
            f.write(str(item) + '\n') 

    #3、点击一篇公文并下载
    def get1OA(i):
        time.sleep(2)
        wait = WebDriverWait(web, 10)
        new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]//a/li/div/span'))) #等待显示左边待办文件就继续执行
        web.find_element(by=By.XPATH,value=f'//*[@id="app"]/div/div[4]/div[1]/section/section/div/div[2]/div/div[3]/table/tbody/tr[{i}]/td[5]').click() #点击更多
        time.sleep(2)
        #以下切换浏览器视界，然后点击另存为
        web.switch_to.window(web.window_handles[-1])
        wait = WebDriverWait(web, 10)
        time.sleep(1)
        new_page_loaded2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="formContent"]'))) #等待显示某个元素就继续执行
        web.find_element(by=By.XPATH,value='//*[@id="app"]/section/div/div/div[1]/div[1]/div/div[1]/ul/li[7]/div').click()  #点更多
        time.sleep(2)
        web.find_element(by=By.XPATH,value='/html/body/div[4]/ul/li[1]').click() #点另存为
        time.sleep(3)
        wait = WebDriverWait(web, 40)
        element_disappeared = wait.until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[4]'))) #等待不显示某个元素就继续执行
        time.sleep(1)
        web.close()
        time.sleep(1)
        web.switch_to.window(web.window_handles[0])

    if __name__ == '__main__':
        for i in range(1,OAnum+1):
            get1OA(i)
        web.quit
        # 弹出对话框，提示已下载完毕
        messagebox.showinfo("提示", "OA公文已下载完毕。")
        # 关闭主窗口
        root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("OA公文下载——by Fish")
# 创建标签和输入框——用户名
label = tk.Label(root, text="用户名：")
label.pack()
username = tk.Entry(root, width=20)
username.pack()
# 创建标签和输入框——密码
label = tk.Label(root, text="密码：")
label.pack()
#password = tk.Entry(root, width=20) 
password = tk.Entry(root, width=20, show="*") # 设置show选项为"*"，表示输入的内容将用"*"代替 ，注意直接用这段代码就会全部变成*
password.pack()
# 创建“运行程序”按钮
button = tk.Button(root, text="执行下载", command=run_program)
button.pack()
# 创建提示语
tip1 = tk.Label(root, text="**请耐心等待一下。", justify="left",highlightbackground="yellow")
tip1.pack(side="bottom")
'''
# 定义函数，延时6秒将密码文本框中的文本替换为"*"
def hide_password(event):
    password.insert(0, password.cget("show"))
    password.after(6000, lambda: password.config(show="*"))
# 绑定<KeyRelease>事件，当用户松开键盘时调用hide_password函数
password.bind("<KeyRelease>", hide_password)
'''
# 点击按钮后将密码框设置为显示"*"
# 进入消息循环
root.mainloop()