# -*- coding: utf-8 -*-
import time,ddddocr,os
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--disable-blink-features=AutomationControlled') 
web = Chrome(options=option)
web.implicitly_wait(10)
web.get("https://u.gmcc.net/login/")
web.maximize_window() #页面最大化
time.sleep(2)
web.find_element(by=By.XPATH,value='//*[@id="loginName"]').send_keys("mowenyu")
web.find_element(by=By.XPATH,value='//*[@id="swInput"]').send_keys("Zq*332211")
#以下处理验证码
imgelement = web.find_element(by=By.XPATH,value='//*[@id="validateCodeImg"]')
# 获取当前文件的位置、并获取保存截屏的位置
current_location = os.path.dirname(__file__)
screenshot_path = os.path.join(current_location, "V_Code")
Code_Img = screenshot_path + '//' + 'printscreen.png'
imgelement.screenshot(Code_Img)
ocr=ddddocr.DdddOcr() #实例化
with open(Code_Img, 'rb') as f: #打开图片
    image = f.read() 
res = ocr.classification(image)
print(res) #识别
a = int(res[0])
b = int(res[2])
if(res[1] == '+' or '十'):
    c = int(a + b)
    print(c)

web.find_element(by=By.XPATH,value='//*[@id="identifyingCode"]').send_keys(c)
time.sleep(2) #这段时间停留给用户输入验证码
web.find_element(by=By.XPATH,value='//*[@id="securityCode"]').click()
time.sleep(5) #这段时间用于停留等待登陆后的页面加载，页面最大化
wait = WebDriverWait(web, 10)
new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/aside/div[2]/ul/li[6]/span'))) #等待显示考试中心元素就继续执行
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="app"]/div/div[1]/aside/div[2]/ul/li[6]/span').click() #这里点击考试中心，要将页面全屏
time.sleep(2)
web.switch_to.window(web.window_handles[-1])#切换到考试中心界面
wait = WebDriverWait(web, 10)
new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="longUserEmsRightPanel"]/div/div[2]//div[1]/div'))) #等待试卷出现
time.sleep(1)
web.find_element(by=By.XPATH,value='//*[@id="longUserEmsRightPanel"]/div/div[2]/a/div[1]/div').click() #这里点击点击试卷，多份试卷a有下标，1份试卷a没有下标
time.sleep(3)
#1、第1次随意做题
def firstA():
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shortUserEmsRightPanel"]/div[2]/div[3]/button'))) #等待进入考试出现
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="shortUserEmsRightPanel"]/div[2]/div[3]/button').click() #这里点击进入考试
    time.sleep(2)
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="no_1"]/ul/li[1]/label/div'))) #等待选项出现
    for i in range(1,6):
        time.sleep(0.2)
        web.find_element(by=By.XPATH,value=f'//*[@id="no_{i}"]/ul/li[2]/label/div').click() #这里点击A选项
    time.sleep(0.5)
    web.find_element(by=By.XPATH,value='//*[@id="examForm"]/div/div/div[1]/div[4]/button').click() #提交交卷
    time.sleep(0.5)
    web.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/button[2]').click() #确认交卷
    time.sleep(0.5)
    web.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/button').click() #再确认交卷
    
#2、查看答案，记录答案
def viewA():
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="longUserEmsRightPanel"]/div/div[2]//div[1]/div'))) #等待试卷出现
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="longUserEmsRightPanel"]/div/div[2]/a/div[1]/div').click() #这里点击点击试卷，多份试卷a有下标，1份试卷a没有下标
    time.sleep(3)
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="viewAnsweiButton"]/button'))) #等待查看答案
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="viewAnsweiButton"]/button').click() #这里点击查看答案
    #2.1、进入页面后，拿到网页源码,拿到源码后，进行数据解析，将A~D转换成1~4，用于改选项的下标
    html = web.page_source
    soup = BeautifulSoup(html, 'html.parser')
    answer = soup.findAll('div', {'class': 'true-answer'})
    answer_get = [i.text.split('：')[-1].strip() for i in answer]
    change_answer_get = [ord(c) - 64 for c in answer_get]
    print(answer_get)
    print(change_answer_get)
    time.sleep(0.5)
    web.find_element(by=By.XPATH,value='//*[@id="shortUserEmsRightPanel"]/div[1]/a[1]').click() #这里点击返回
    return change_answer_get    

#3、第二次用获取到的答案去正确做题
def TrueA(answer_list):
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shortUserEmsRightPanel"]/div[2]/div[3]/button'))) #等待进入考试出现
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="shortUserEmsRightPanel"]/div[2]/div[3]/button').click() #这里点击进入考试
    time.sleep(2)
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="no_1"]/ul/li[1]/label/div'))) #等待选项出现
    for i in range(1,6):
        time.sleep(0.2)
        web.find_element(by=By.XPATH,value=f'//*[@id="no_{i}"]/ul/li[{answer_list[i-1]}]/label/div').click() #这里点击之前获取的正确选项
    time.sleep(0.5)
    web.find_element(by=By.XPATH,value='//*[@id="examForm"]/div/div/div[1]/div[4]/button').click() #提交交卷
    time.sleep(0.5)
    web.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/button[2]').click() #确认交卷
    time.sleep(0.5)
    web.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/button').click() #再确认交卷

if __name__ == '__main__':
    firstA()
    time.sleep(2)
    answer_list = viewA()
    time.sleep(2)
    TrueA(answer_list)
    time.sleep(2)
    #最后，点进去试卷，看看是不是100分
    wait = WebDriverWait(web, 10)
    new_page_loaded = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="longUserEmsRightPanel"]/div/div[2]//div[1]/div'))) #等待试卷出现
    time.sleep(1)
    web.find_element(by=By.XPATH,value='//*[@id="longUserEmsRightPanel"]/div/div[2]/a/div[1]/div').click() #这里点击点击试卷，多份试卷a有下标，1份试卷a没有下标
    time.sleep(5)
    web.quit