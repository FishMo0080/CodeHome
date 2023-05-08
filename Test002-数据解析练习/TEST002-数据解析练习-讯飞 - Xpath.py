import lxml.html

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
# 读取HTML文件内容
#with open('example.html', 'r', encoding='utf-8') as f:
#    html = f.read()

# 将HTML内容转换成lxml对象
doc = lxml.html.fromstring(html)

# 使用XPath表达式查找所有class为panel-content的a标签，并获取其中的data-id属性值
ids = doc.xpath('//div[@class="item-middle"]/@data-id')

# 输出所有data-id属性值
print(ids)