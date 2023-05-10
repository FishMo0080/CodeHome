#1、请求走通，获取1份试卷的内容
#2、获取历史试卷列表的链接，循环第1步多次请求多份试卷
#3、将试卷保存到txt
import requests
from bs4 import BeautifulSoup
url = ' https://u.gmcc.net/ems/html/examCenter/myExamPaperView.do'      # 具体试卷地址
#url = ' https://u.gmcc.net/ems/html/examCenter/newMyExamList.do'         #历史试卷列表
kw = {'examId':'f84f2b30cf63415884aa6712f28b47a5'}                     #试卷ID参数
#kw = {'current_app_id':'8a80826f5e16e1ba015e4c3c03c606f0'}                #试卷列表ID参数
headers = {    
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "eln_session_id=elnSessionId.19ec4f42cd7f49c7873b4daf62bf387c",    
    }
r = requests.get(url=url,params = kw,headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
qnum=[1,2,3,4,5]
data = []
for num in qnum:
    questionmain=soup.find('div', {'class': 'question-panel-middle','data-index':num})
    # 获取题目
    question = questionmain.find('div', {'class': 'name'}).text.split('.')[-1].strip()
    data.append(question)
    #print(question)
    # 获取选项和答案
    options = questionmain.find_all('div', {'class': 'item-detail'})
    for option in options:
        data.append(option.text.strip())
        #print(option.text.strip()) # 打印选项    
    # 获取标准答案
    answer = questionmain.find('div', {'class': 'true-answer'}).text.split('：')[-1].strip()
    data.append("标准答案："+answer)    
    #print("标准答案："+answer)
with open('每日一练.txt', 'w',encoding='utf-8-sig') as f:
    # 遍历data数组，将每个元素写入TXT文件中
    for item in data:
        f.write(str(item) + '\n')
    print("over!")
'''
#抓取五道题
qnum=[1,2,3,4,5]
for num in qnum:
    print(num)
'''
'''
# 获取题目
question = soup.find('div', {'class': 'name'}).text.strip()
print(question)

# 获取选项和答案
options = soup.find_all('div', {'class': 'item-detail'})

for option in options:
    print(option.text.strip()) # 打印选项
    
# 获取标准答案
answer = soup.find('div', {'class': 'true-answer'}).text.split('：')[-1].strip()
print(answer)
'''
'''
#用写到csv的方法，由于写出来的数据全部分了单元格所以不用这种方法
import csv
#f = open("每日一练试题.csv",mode="w",encoding='utf-8-sig')
#csvwriter = csv.writer(f)
#csvwriter.writerow(question)
#csvwriter.writerow(option.text.strip())
#csvwriter.writerow("标准答案："+answer)
#f.close()

'''