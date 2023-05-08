from bs4 import BeautifulSoup

# 定义一个函数，用于解析HTML页面中的数据
def parse_data(html):
    # 使用BeautifulSoup库解析HTML页面
    soup = BeautifulSoup(html, 'html.parser')
    
    # 查找所有class为panel-content的a标签
    links = soup.find_all('div', {'class': 'item-middle'})
    
    # 遍历每个a标签，查找data-id属性值，并将其添加到列表中
    id_list = []
    for link in links:
        id_list.append(link.get('data-id'))
    
    return id_list

# 将HTML代码作为参数传入parse_data()函数中，获取data-id并打印输出
html = '''
        <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=82c93a0b03024bc9b5b928564ab7ac27&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="82c93a0b03024bc9b5b928564ab7ac27">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0104
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-04 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-05 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-04 12:26</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=694443bc3e544e58991a97f8478f23f2&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="694443bc3e544e58991a97f8478f23f2">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0103
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-03 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-04 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-03 10:14</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            '''
id=parse_data(html)
print(id) # 输出：694443bc3e544e58991a97f8478f23f2