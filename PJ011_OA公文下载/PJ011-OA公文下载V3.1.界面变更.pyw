# -*- coding: utf-8 -*-
import time,lxml.html
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  #这段代码并没有起作用

#1、打开网页登陆
option = Options()#这段代码并没有起作用
option.add_argument('--disable-blink-features=AutomationControlled') #这段代码并没有起作用
web = Chrome(options=option)#这段代码并没有起作用
#web = Chrome()
web.implicitly_wait(5)
web.get("http://oa.gmcc.net/oa/login?gourl=/client")
time.sleep(1)
web.maximize_window()
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="UserName"]').send_keys("mowenyu")
web.find_element(by=By.XPATH,value='//*[@id="Password"]').send_keys("Zq*332211")
web.find_element(by=By.XPATH,value='//*[@id="linkeyform_value"]/div[4]/input[1]').click()
time.sleep(5)
wait = WebDriverWait(web, 10)
new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div[1]/section/section/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]'))) #等待文件标题就继续执行
html = web.page_source
time.sleep(1)
doc = lxml.html.fromstring(html)
title_list = doc.xpath('//td[@class="el-table_1_column_5  cell-ellipsis el-table__cell"]//span/text()') #获取到标题内容
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
    web.find_element(by=By.XPATH,value=f'//*[@id="app"]/div/div[4]/div[1]//div[2]//div[3]/table/tbody/tr[{i}]/td[5]').click() #点击公文
    #//*[@id="app"]/div/div[4]/div[1]/section/section/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/div/div/span 【20230711第一份公文的XPATH】
    time.sleep(2)
    #以下切换浏览器视界，然后点击另存为
    web.switch_to.window(web.window_handles[-1])
    wait = WebDriverWait(web, 10)
    time.sleep(1)
    new_page_loaded2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section//ul/li[last()]/div'))) #等待显示某个元素就继续执行
    web.find_element(by=By.XPATH,value='//*[@id="app"]/section//ul/li[last()]/div').click()  #点更多的xpath，有时候下标是[7]、有时候是[8]但每次都是最后，通过li[last()]来找到最后一个元素。       
    time.sleep(2)
    web.find_element(by=By.XPATH,value='/html/body/div[2]/ul/li[1]').click() #点另存为    
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


'''
如果网页源码变更获取不了标题，就要用这个下载网页源码分析
time.sleep(2)
with open(f'OA网页源码.txt', 'w') as f:
    f.write(html) 
'''