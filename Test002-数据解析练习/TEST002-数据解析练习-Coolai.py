import re

html = '''    <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=3a02c9727e0045139954837ccd0998fc&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="3a02c9727e0045139954837ccd0998fc">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0310
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-10 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-11 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-10 09:10</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=4723ace109b343038a7dced70d4cb2d8&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="4723ace109b343038a7dced70d4cb2d8">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0309
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-09 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-10 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-09 09:04</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=1b1311dda318413f9e2a696f2f9f89d0&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="1b1311dda318413f9e2a696f2f9f89d0">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0308
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-08 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-09 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-08 08:45</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=152e33b01a4248af995d6d5f3f26a8f5&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="152e33b01a4248af995d6d5f3f26a8f5">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0307
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-07 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-08 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-07 08:52</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">'''

pattern = r'<div class="item-middle" data-id="([a-zA-Z0-9]+)">'
result = re.findall(pattern, html)

print(result)

# 输出：['3a02c9727e0045139954837ccd0998fc', '4723ace109b343038a7dced70d4cb2d8', '1b1311dda318413f9e2a696f2f9f89d0', '152e33b