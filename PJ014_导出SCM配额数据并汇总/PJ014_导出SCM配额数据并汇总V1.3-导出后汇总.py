# -*- coding: utf-8 -*-
import json,asyncio,aiohttp,aiofiles,glob   # 第三方库
import pandas as pd
from openpyxl import load_workbook, Workbook
from datetime import datetime

# 1:目标网址
#尝试获取quotaId
key_cookie = "356d898a-d4e5-409f-bfd4-33f6f9a65fe5"
headers1 = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Cookie": f"SHAREJSESSIONID={key_cookie}",
    }
headers2 = {    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Cookie": f"SHAREJSESSIONID={key_cookie}",
    }
#1、通过quotaName获取到quotaId
async def getqid(quotaName): 
    url = 'http://gdscm.gmcc.net/scm/quotaSearch/searchQuotaList?isCitySearch=true'
    payload = dict(quotaName = quotaName)       
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,data=payload,headers=headers1) as resp:
            if resp.status == 200:            
                result = await resp.read()
                data = json.loads(result)
                id = data["rows"][0]["id"]
                #print(id)
    return id

#2、通过quotaId导出quota的excel表
async def getqxl(id):    
    url = 'http://gdscm.gmcc.net/scm/quotaSearch/venderQuotaUserStandListExport'
    payload = dict(quotaId = id) 
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url,data=payload,headers=headers2) as resp:
            result = await resp.read()
            #print (result)
            async with aiofiles.open(f"{id}.xls", 'wb') as f:
                await f.write(result)

loop = asyncio.get_event_loop()
def idmain():
    quotaName_wb = load_workbook("ready/quotaName.xlsx")
    quotaName_ws = quotaName_wb.active
    quotaNames = [cell.value for cell in quotaName_ws["A"]]
    tasks = [loop.create_task(getqid(quotaName)) for quotaName in quotaNames]
    result = loop.run_until_complete(asyncio.gather(*tasks))
    id_list = result
    #print(id_list)
    return id_list    

def xlmain(id_list):
    tasks = [loop.create_task(getqxl(id)) for id in id_list]
    loop.run_until_complete(asyncio.gather(*tasks))

if __name__ == '__main__':
    datet = datetime.now().strftime('%Y-%m-%d') # 获取当前日期以便用时间命名文件夹
    new_title = '配额数据汇总' + datet
    id_list = idmain()
    print(id_list)
    xlmain(id_list)
    # 获取所有xls后缀的文件路径
    file_paths = glob.glob('*.xls')
    # 创建一个空的DataFrame对象来保存汇总的数据
    merged_data = pd.DataFrame()
    # 遍历每个文件路径
    for file_path in file_paths:
        # 读取Excel文件
        df = pd.read_excel(file_path, skiprows=0)
        # 将当前文件的数据添加到汇总数据中
        merged_data = merged_data._append(df, ignore_index=True)
    # 保存汇总的数据到新的Excel文件
    merged_data.to_excel(f'{new_title}.xls', index=False, engine='openpyxl')