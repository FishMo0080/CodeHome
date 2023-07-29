# -*- coding: utf-8 -*-
import time,lxml.html
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
#from selenium import webdriver #这段代码并没有起作用
#from selenium.webdriver.common.action_chains import ActionChains #这段代码并没有起作用
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  #这段代码并没有起作用

#from selenium.webdriver.common.keys import Keys #这段代码并没有起作用
option = Options()#这段代码并没有起作用
option.add_argument('--disable-blink-features=AutomationControlled') #这段代码并没有起作用
web = Chrome(options=option)#这段代码并没有起作用
#1、打开网页登陆
#web = Chrome()
web.implicitly_wait(10)
web.get("https://u.gmcc.net/login/")
time.sleep(2)
web.find_element(by=By.XPATH,value='//*[@id="loginName"]').send_keys("mowenyu")
web.find_element(by=By.XPATH,value='//*[@id="swInput"]').send_keys("Zq*332211")
time.sleep(5) #这段时间停留给用户输入验证码
web.find_element(by=By.XPATH,value='//*[@id="securityCode"]').click()
time.sleep(5) #这段时间用于停留等待登陆后的页面加载
wait = WebDriverWait(web, 10)
new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/aside/div[2]/ul/li[6]/span'))) #等待显示考试中心元素就继续执行
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[1]/aside/div[2]/ul/li[6]/span').click() #这里点击考试中心，要将页面全屏
time.sleep(2)
web.switch_to.window(web.window_handles[-1])#切换到考试中心界面
wait = WebDriverWait(web, 10)
new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="longUserEmsRightPanel"]/div/div[2]//div[1]/div'))) #等待试卷出现
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="longUserEmsRightPanel"]/div/div[2]/a[1]/div[1]/div').click() #这里点击点击试卷，多份试卷a有下标，1份试卷a没有下标
time.sleep(3)
#1、第一次做题并获取答案
def firstA():
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shortUserEmsRightPanel"]/div[2]/div[3]/button'))) #等待进入考试出现
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="shortUserEmsRightPanel"]/div[2]/div[3]/button').click() #这里点击进入考试
    time.sleep(2)
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="no_1"]/ul/li[1]/label/div'))) #等待选项出现
    web.find_element(by=By.XPATH,value='//*[@id="no_1"]/ul/li[1]/label/div').click() #这里点击A选项
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="no_2"]/ul/li[1]/label/div').click() #这里点击A选项
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="no_3"]/ul/li[1]/label/div').click() #这里点击A选项
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="no_4"]/ul/li[1]/label/div').click() #这里点击A选项
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="no_5"]/ul/li[1]/label/div').click() #这里点击A选项
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="examForm"]/div/div/div[1]/div[4]/button').click() #提交交卷
    time.sleep(1)
    web.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/button[2]').click() #确认交卷
    time.sleep(1)
    web.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/button').click() #确认交卷
    
#2、查看答案，记录答案
def viewA():
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="longUserEmsRightPanel"]/div/div[2]//div[1]/div'))) #等待试卷出现
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="longUserEmsRightPanel"]/div/div[2]/a[1]/div[1]/div').click() #这里点击点击试卷，多份试卷a有下标，1份试卷a没有下标
    time.sleep(3)
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="viewAnsweiButton"]/button'))) #等待查看答案
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="viewAnsweiButton"]/button').click() #这里点击查看答案
    #2.1、进入页面后，拿到网页源码

    #2.2、拿到源码后，进行数据解析，然后A~D，转换成1~4，用于改选项下标
    

#进入考试的xpath //*[@id="shortUserEmsRightPanel"]/div[2]/div[3]/button
#A选项xpath //*[@id="no_1"]/ul/li[1]/label/div
#B选项xpath //*[@id="no_1"]/ul/li[2]/label/div
#3、第二次用获取到的答案去正确做题
def TrueA():
    pass

if __name__ == '__main__':
    firstA()
    time.sleep(30)
    web.quit

#//*[@id="viewAnsweiButton"]/button 查看答卷
'''
time.sleep(2)
wait = WebDriverWait(web, 10)
new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tab-myTodo"]'))) #等待显示我的待办元素就继续执行
time.sleep(2)
html = web.page_source
doc = lxml.html.fromstring(html)
title_list = doc.xpath('//div[1]/div/div[1]/div[2]/div[1]/div/div/div[3]/table/tbody//td[1]/div/span/text()') #获取到标题内容
#//*[@id="tab-myTodo"]
#//*[@id="tab-0"]
#/html/body/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/span 我的待办完整xpath
#/html/body/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/span 我的项目完整xpath ，要区分2者区别
#//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/span
#//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/span
#//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/span
myTodonum = len(title_list) #得到标题数量
#2、将所有标题放到txt
data = []
for title in title_list:
    data.append(f'{len(data)+1}、'+title) 
with open(f'myTodotitle.txt', 'w') as f:
    for item in data:
        f.write(str(item) + '\n')


#def my1Todo():
def my1Todo(i):
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tab-myTodo"]'))) #等待显示我的待办元素就继续执行
    #web.find_element(by=By.XPATH,value='//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr/td[5]/div/button').click() #只有1个待办的时候，tr是没有下标的，不过1个待办也不会使用自动化来处理
    web.find_element(by=By.XPATH,value=f'//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr[{i}]/td[5]/div/button').click()
    time.sleep(2)
    #以下切换浏览器视界，然后点击提交
    web.switch_to.window(web.window_handles[-1])
    wait = WebDriverWait(web, 10)
    time.sleep(2)
    new_page_loaded2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]'))) #等待显示某个元素就继续执行
    web.find_element(by=By.XPATH,value='//*[@id="app"]/div/div/div[1]/div[4]/button[1]').click()  #点击提交
    time.sleep(2)
    web.find_element(by=By.XPATH,value='/html/body/div[2]/div/div[3]/button[2]').click() #点确认
    time.sleep(2)
    web.switch_to.window(web.window_handles[0])

if __name__ == '__main__':
    for i in range(1,myTodonum+1):
    #for i in range(1,2):
        my1Todo(i)
        #print(i)
    web.quit

'''
#//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr[1]  2个位置的Xpath
#//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr[2]

#//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr/td[5]/div/button
#//*[@id="pane-0"]/div/div/div[3]/table/tbody/tr #只剩下一个的时候，竟然不带下标了

'''
time.sleep(4)
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
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]'))) #等待显示某个元素就继续执行
    web.find_element(by=By.XPATH,value=f'//*[@id="app"]/div/div[4]/div[1]/section/section/div/div[2]/div/div[3]/table/tbody/tr[{i}]/td[5]').click()
    time.sleep(2)
    #以下切换浏览器视界，然后点击另存为
    web.switch_to.window(web.window_handles[-1])
    wait = WebDriverWait(web, 10)
    time.sleep(1)
    new_page_loaded2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="formContent"]'))) #等待不显示某个元素就继续执行
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
        #print(i)
    #web.quit
'''
    
'''
这个代码片段中，click 方法被用于单击 id 为 "myButton" 的按钮。
与 clickAndWait 方法相对应的是 WebDriverWait 类，它提供了等待指定的时间或者直到指定条件为真的方法。
例如，如果您需要等待新页面加载完成，可以使用以下代码：
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
web = Chrome()
web.get("http://www.example.com")
elem = web.find_element_by_xpath('//*[@id="myLink"]')
elem.click()
wait = WebDriverWait(web, 10)
new_elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="someElement"]')))
'''

#以上暂时成功打开
#//*[@id="app"]/div/div[4]/div[1]/section/section/div/div[2]/div/div[3]/table/tbody/tr[1]/td[5]                   标题第一份文外一层框架的xpath
#//*[@id="app"]/div/div[4]/div[1]/section/section/div/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div/div/div/span  标题第一份文标题xpath
#//*[@id="app"]/div/div[4]/div[1]/section/section/div/div[2]/div/div[3]/table/tbody/tr[2]/td[5]                   标题第二份文外一层框架的xpath
#//*[@id="app"]/div/div[4]/div[1]/section/section/div/div[2]/div/div[3]/table/tbody/tr[2]/td[5]
#/html/body/div[4]/ul/li[1]/span #打开第一份文另存为的Xpath
#/html/body/div[4]/ul/li[1]      #打开第一份文另存为外一层的Xpath
#//*[@id="app"]/section/div/div/div[1]/div[1]/div/div[1]/ul/li[7]/div #打开第一份文的更多
#<svg viewBox="25 25 50 50" class="circular"><circle cx="50" cy="50" r="20" fill="none" class="path"></circle></svg> #这个是加载旋转的圈圈的元素以及接下的2个都是
#<div class="el-loading-mask is-fullscreen" style="z-index: 2006; display: none;"><div class="el-loading-spinner"><svg viewBox="25 25 50 50" class="circular"><circle cx="50" cy="50" r="20" fill="none" class="path"></circle></svg><!----></div></div>
#<div class="el-loading-spinner"><svg viewBox="25 25 50 50" class="circular"><circle cx="50" cy="50" r="20" fill="none" class="path"></circle></svg><!----></div>
#/html/body/div[4]  #这个是点击完另存为以后，出现了加载圈圈，然后右键圈圈，copy xpath（等待这个转圈加载元素消失是正确的）
#/html/body/div[4]/div/svg （等待这个转圈加载元素消失不正确，可能原因是这个元素在某个时刻会消失，猜测可能是圈圈出现了又消失，消失的时候程序认定已经加载完，其实未加载完）

#用CLASS_NAME，不成功
#X = web.find_elements(by=By.CLASS_NAME,value='el-table_2_column_13  cell-ellipsis el-table__cell').__getitem__()
#print(X)

#web = Chrome()
#web.get("http://www.baidu.com")
#print(web.title)

#option=webdriver.ChromeOptions（）
#option.add_experimental_option（“detach”，True）