import concurrent.futures
import requests
from openpyxl import load_workbook, Workbook     
import time
import re
def fetch(url):
    pattern = re.compile(r'projectCode=(.*)')
    proj_id = pattern.search(url).group(1) 
    r = requests.post(url=url,headers=headers)
    if r.status_code == 200:
    # 打开一个新文件，将文件流写入其中
        with open(f"{proj_id}.xlsx", 'wb') as f:
            f.write(r.content) 

def main():
    ready_wb = load_workbook("ready/ready.xlsx")
    ready_ws = ready_wb.active
    proj_ids = [cell.value for cell in ready_ws["A"]]
    urls = [
        f"http://pmis.iim.gmcc.net/a/portal/overview/exportProjectTasks?projectCode={proj_id}"
        for proj_id in proj_ids
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(fetch, urls)


if __name__ == '__main__':   
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "pmis.session.id=22d213c46f5c43b98416f03c29dc6480",
    }
    start = time.time()
    main()
    end = time.time()
    print("使用时间",end-start)