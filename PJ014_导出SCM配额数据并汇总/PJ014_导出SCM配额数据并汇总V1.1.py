# -*- coding: utf-8 -*-
import requests,json,asyncio,aiohttp,aiofiles   # 第三方库
from openpyxl import load_workbook, Workbook
# 1:目标网址
#尝试获取quotaId
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Cookie": "SHAREJSESSIONID=ead3177e-ede7-4538-bd86-7f431e3eda67",
    }
'''
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "iPlanetDirectoryPro1=C8iTptTY1dkK3elnHu6jt6C_Fauzfj0pK8in6_0-ucmnKNpgJUcqaxNN222rlysBQKk7MgonbUb01xYm70ZFQlE6WayA3eBErFuHn2cgELBDpRSIlV0ODZgS8IPTJLHd; LtpaToken=AAECAzY0MzEzRUFFNjQzMTc2RUVDTj0TxKoTzsQT6KQvT1U9WlEvTz1HTUNDXaXKvNcDk53V3h4aWb7mn38zcPY=; iPlanetDirectoryPro=C8iTptTY1dkK3elnHu6jt6C_Fauzfj0pK8in6_0-ucmnKNpgJUcqaxNN222rlysBQKk7MgonbUb01xYm70ZFQlE6WayA3eBErFuHn2cgELBDpRSIlV0ODZgS8IPTJLHd; LtpaToken1=AAECAzY0MzEzRUFFNjQzMTc2RUVDTj0TxKoTzsQT6KQvT1U9WlEvTz1HTUNDXaXKvNcDk53V3h4aWb7mn38zcPY=; rememberme_username=1+x5GCBZ21Q3VrikZD8qJQ==; pmis.session.id=a987effd6c204b1cbfee4b7cd1bb4cf5",
    }
    '''
#1、通过quotaName获取到quotaId
async def getqid(quotaName): 
    url = 'http://gdscm.gmcc.net/scm/quotaSearch/searchQuotaList?isCitySearch=true'
    payload = dict(quotaName = quotaName)       
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,data=payload,headers=headers) as resp:
            if resp.status == 200:            
                result = await resp.read()
                data = json.loads(result)
                id = data["rows"][0]["id"]
                #print(id)
    return id

#2、通过quotaId导出quota的excel表
async def getqxl():
    pass


loop = asyncio.get_event_loop()
def idmain():
    quotaName_wb = load_workbook("quotaName.xlsx")
    quotaName_ws = quotaName_wb.active
    quotaNames = [cell.value for cell in quotaName_ws["A"]]
    tasks = [loop.create_task(getqid(quotaName)) for quotaName in quotaNames[0:2]]
    result = loop.run_until_complete(asyncio.gather(*tasks))
    id_list = result
    print(id_list)
    

def xlmain():
    pass

if __name__ == '__main__':
    idmain()
    #id_list = []
    #print(id)


'''
import json
# 将JSON数据解析为字典
data = json.loads(r.text)
# 获取ID后面的数据
id = data["rows"][0]["id"]
# 输出结果
print(id)
'''
'''
if r.status_code == 200:
    # 打开一个新文件，将文件流写入其中
    with open('C23302137AA3002-01.xlsx', 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
r.close
'''