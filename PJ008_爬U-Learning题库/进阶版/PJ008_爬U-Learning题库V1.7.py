import requests
from lxml import etree
import re
from getexam import get1exam
from Sumtxt import all_txt
url1 = ' https://u.gmcc.net/ems/html/examCenter/historyExamList.do'
headers = {    
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "eln_session_id=elnSessionId.a1c6385d51854ac7833110e16b50327d",    
    }
r = requests.get(url=url1,headers=headers) #获取试卷ID列表不用传参数就可以，直接请求网页可以
tree = etree.HTML(r.text)
result= tree.xpath("//div/@data-id") #获取试卷ID
pattern = r'<div class="overflow-div">\s*(.*?)\s*</div>' #定义正则表达式，获取试卷名称
result2 = re.findall(pattern, r.text)

L=list(range(0,len(result2))) #创建一个0~名称数量的列表，然后重复调用上面定义的函数
for i in L:
    #print((result[i],result2[i]))    
    get1exam(result[i],result2[i])
    #break
all_txt()
#思路：
#1、请求走通，获取1份试卷的内容
#2、获取历史试卷列表的链接，循环第1步多次请求多份试卷
#3、将试卷保存到txt,并汇总txt