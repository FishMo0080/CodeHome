import asyncio
import aiohttp
import aiofiles
from openpyxl import load_workbook, Workbook
import time

async def aiodownload(proj_id):
    url = "http://pmis.iim.gmcc.net/a/portal/overview/exportProjectTasks" 
    payload = dict(projectCode=proj_id)
    async with aiohttp.ClientSession() as session:
        async with session.post(url,data=payload,headers=headers) as resp:
            if resp.status == 200:            
                result = await resp.read()
                async with aiofiles.open(f"{proj_id}.xlsx", 'wb') as f:
                    await f.write(result)

async def main():
        ready_wb = load_workbook("ready/ready.xlsx")
        ready_ws = ready_wb.active
        proj_ids = [cell.value for cell in ready_ws["A"]]
        tasks = [asyncio.create_task(aiodownload(proj_id)) for proj_id in proj_ids]
        await asyncio.wait(tasks)

if __name__ == '__main__':
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "pmis.session.id=53a8413faa4848a0ac756459175bbc8d",
    }
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("使用时间",end-start)