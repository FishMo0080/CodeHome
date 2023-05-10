#1、请求走通，获取1份试卷的内容
#2、获取历史试卷列表的链接，循环第1步多次请求多份试卷
#3、将试卷保存到txt
import requests
from bs4 import BeautifulSoup
from lxml import etree
#url = ' https://u.gmcc.net/ems/html/examCenter/myExamPaperView.do'      # 具体试卷地址
url1 = ' https://u.gmcc.net/ems/html/examCenter/historyExamList.do'
#url = ' https://u.gmcc.net/ems/html/examCenter/newMyExamList.do'         #历史试卷列表
#kw = {'examId':'f84f2b30cf63415884aa6712f28b47a5'}                     #试卷ID参数
#kw = {'_t':'1682580635509'} 
headers = {    
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "eln_session_id=elnSessionId.e816e1c67ebb4464bd3fc23991f862f2",    
    }
#r = requests.get(url=url,params = kw,headers=headers)
r = requests.get(url=url1,headers=headers) #获取试卷ID列表不用传参数就可以，直接请求网页可以
tree = etree.HTML(r.text)
result= tree.xpath("//div/@data-id")
for examId in result[0:50]:
    url2 = ' https://u.gmcc.net/ems/html/examCenter/myExamPaperView.do'
    kw2 = {'examId':f'{examId}'}
    r2 = requests.get(url=url2,params = kw2,headers=headers)
    qnum=[1,2,3,4,5]
    data = []
    for num in qnum:
        soup = BeautifulSoup(r2.text, 'html.parser')
        questionmain=soup.find('div', {'class': 'question-panel-middle','data-index':num})
        if questionmain is None:
            continue #为空则跳出循环
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
        with open(f'每日一练{examId}.txt', 'w',encoding='utf-8-sig') as f:
        # 遍历data数组，将每个元素写入TXT文件中
            for item in data:
                f.write(str(item) + '\n')            
    break   


'''
qnum=[1,2,3,4,5]
data = []
for num in qnum:
    questionmain=soup.find('div', {'class': 'question-panel-middle','data-index':num})
    # 获取题目
    question = questionmain.find('div', {'class': 'name'}).text.strip()
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