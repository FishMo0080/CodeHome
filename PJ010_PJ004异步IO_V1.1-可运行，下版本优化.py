import asyncio
import aiohttp
import aiofiles
import re
from openpyxl import load_workbook, Workbook
import time

async def aiodownload(url):
    pattern = re.compile(r'projectCode=(.*)')
    proj_id = pattern.search(url).group(1)    
    async with aiohttp.ClientSession() as session:
        async with session.post(url,headers=headers) as resp:
            if resp.status == 200:            
                result = await resp.read()
                async with aiofiles.open(f"{proj_id}.xlsx", 'wb') as f:
                    await f.write(result)

async def main():
        ready_wb = load_workbook("ready/ready.xlsx")
        ready_ws = ready_wb.active
        proj_ids = [cell.value for cell in ready_ws["A"]]
        urls = [
            f"http://pmis.iim.gmcc.net/a/portal/overview/exportProjectTasks?projectCode={proj_id}"
            for proj_id in proj_ids
        ]
        tasks = [asyncio.create_task(aiodownload(url)) for url in urls]
        await asyncio.wait(tasks)

if __name__ == '__main__':
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "pmis.session.id=22d213c46f5c43b98416f03c29dc6480",
    }
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("使用时间",end-start)