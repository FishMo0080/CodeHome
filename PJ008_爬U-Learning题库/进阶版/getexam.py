import requests
from bs4 import BeautifulSoup
headers = {    
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "eln_session_id=elnSessionId.a1c6385d51854ac7833110e16b50327d",    
    }
def get1exam(id,name):
    url2 = ' https://u.gmcc.net/ems/html/examCenter/myExamPaperView.do'
    kw2 = {'examId':f'{id}'}
    r2 = requests.get(url=url2,params = kw2,headers=headers)
    qnum=[1,2,3,4,5]
    data = []
    for num in qnum:
        soup = BeautifulSoup(r2.text, 'html.parser')
        questionmain=soup.find('div', {'class': 'question-panel-middle','data-index':num})
        if questionmain is None:
            continue #为空则跳出循环
        # 查找标签
        true_answer_tag = questionmain.find('div', {'class': 'true-answer'})
        # 判断"true-answer"标签是否存在
        if true_answer_tag is None:
            continue
        # 获取题目
        question = questionmain.find('div', {'class': 'name'}).text.split('.')[-1].strip()
        data.append(question)        
        # 获取选项和答案
        options = questionmain.find_all('div', {'class': 'item-detail'})
        for option in options:
            data.append(option.text.strip())              
        # 获取标准答案
        answer = true_answer_tag.text.split('：')[-1].strip()
        data.append("标准答案："+answer)                
        with open(f'output/{name}.txt', 'w',encoding='utf-8-sig') as f:
        # 遍历data数组，将每个元素写入TXT文件中
            for item in data:
                f.write(str(item) + '\n')  
    return