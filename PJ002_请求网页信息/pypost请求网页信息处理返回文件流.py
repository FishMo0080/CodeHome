import requests     # 第三方库
# 1:目标网址
url = ' http://pmis.iim.gmcc.net/a/portal/overview/exportProjectTasks'
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)",
    "Cookie": "iPlanetDirectoryPro1=C8iTptTY1dkK3elnHu6jt6C_Fauzfj0pK8in6_0-ucmnKNpgJUcqaxNN222rlysBQKk7MgonbUb01xYm70ZFQlE6WayA3eBErFuHn2cgELBDpRSIlV0ODZgS8IPTJLHd; LtpaToken=AAECAzY0MzEzRUFFNjQzMTc2RUVDTj0TxKoTzsQT6KQvT1U9WlEvTz1HTUNDXaXKvNcDk53V3h4aWb7mn38zcPY=; iPlanetDirectoryPro=C8iTptTY1dkK3elnHu6jt6C_Fauzfj0pK8in6_0-ucmnKNpgJUcqaxNN222rlysBQKk7MgonbUb01xYm70ZFQlE6WayA3eBErFuHn2cgELBDpRSIlV0ODZgS8IPTJLHd; LtpaToken1=AAECAzY0MzEzRUFFNjQzMTc2RUVDTj0TxKoTzsQT6KQvT1U9WlEvTz1HTUNDXaXKvNcDk53V3h4aWb7mn38zcPY=; rememberme_username=1+x5GCBZ21Q3VrikZD8qJQ==; pmis.session.id=a987effd6c204b1cbfee4b7cd1bb4cf5",
    }
payload = dict(projectCode="C23302137AA3002-01")
r = requests.post(url=url, data=payload,headers=headers)
if r.status_code == 200:
    # 打开一个新文件，将文件流写入其中
    with open('C23302137AA3002-01.xlsx', 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
r.close