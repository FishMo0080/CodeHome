from bs4 import BeautifulSoup
from lxml import etree
import re

html = '''
<input type="hidden" id="current-user-id" value=68e1a093392c4cacab5ed901f503d95a/>
<div class="selector-corner">
    <select name="" class="select-year" data-tom="">
        <option value=2023
            selected
        >2023</option>
        <option value=2022
            
        >2022</option>
        <option value=2021
            
        >2021</option>
        <option value=2020
            
        >2020</option>
        <option value=2019
            
        >2019</option>
        <option value=2018
            
        >2018</option>
        <option value=2017
            
        >2017</option>
        <option value=2016
            
        >2016</option>
        <option value=2015
            
        >2015</option>
        <option value=2014
            
        >2014</option>
        <option value=2013
            
        >2013</option>
        <option value=2012
            
        >2012</option>
        <option value=2011
            
        >2011</option>
        <option value=2010
            
        >2010</option>
        <option value=2009
            
        >2009</option>
        <option value=2008
            
        >2008</option>
    </select>
    <select name="" class="select-type">
        <option value="all"  >全部</option>
        <option value="up"   >线上</option>
        <option value="down" >线下</option>
    </select>
    <select name="" id="" class="select-month">
        <option value="ALL"class="choose">全部月份</option>
        <option value="Jan" class="choose">一月</option>
        <option value="Feb"  class="choose">二月</option>
        <option value="Mar"  class="choose">三月</option>
        <option value="Apr"  class="choose">四月</option>
        <option value="May"  >五月</option>
        <option value="Jun"  >六月</option>
        <option value="Jul"  >七月</option>
        <option value="Aug"  >八月</option>
        <option value="Sep"  >九月</option>
        <option value="Oct"  >十月</option>
        <option value="Nov"  >十一月</option>
        <option value="Dec"  >十二月</option>
    </select>
</div>
<a class="back-top iconfont">&#xe61f;</a>
<div class="main-panel history-exam-list">
        <div class="panel-title">
            <h2 class="title-name" id="month_4">4月</h2>
        </div>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=56a1f68e17bf463aa381aaaaf8c25f13&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="56a1f68e17bf463aa381aaaaf8c25f13">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0426
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-26 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-27 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-26 08:33</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=6ef1f62cc0234a278bfad80ef274392f&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="6ef1f62cc0234a278bfad80ef274392f">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0425
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-25 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-26 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-25 08:40</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=f84f2b30cf63415884aa6712f28b47a5&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="f84f2b30cf63415884aa6712f28b47a5">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0424
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-24 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-25 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-24 08:46</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=753833a47f7b434ca4f2db2b61d7c858&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="753833a47f7b434ca4f2db2b61d7c858">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0423
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-23 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-24 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-23 08:28</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=333bac2535314c8b8a3264faea048e81&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="333bac2535314c8b8a3264faea048e81">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0421
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-21 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-22 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-21 08:58</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=4e7a006a87af41ba84cb56c0c76a2a2c&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="4e7a006a87af41ba84cb56c0c76a2a2c">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0420
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-20 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-21 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-20 08:41</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=ba80dd6b21af43eb922cf9c2fb1ad6fa&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="ba80dd6b21af43eb922cf9c2fb1ad6fa">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0419
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-19 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-20 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-19 08:32</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=40eb42c598b14de19d89b7ed50482778&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="40eb42c598b14de19d89b7ed50482778">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0418
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-18 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-19 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-18 08:37</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=097c8cabfb0b4446924f226a40b70188&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="097c8cabfb0b4446924f226a40b70188">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0417
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-17 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-18 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-17 08:47</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=a471e0d5fb4c487c9006ae9e80b1e82e&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="a471e0d5fb4c487c9006ae9e80b1e82e">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0414
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-14 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-15 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-14 09:01</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=67400b9cd79c437db673a43c3a429f84&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="67400b9cd79c437db673a43c3a429f84">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0413
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-13 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-14 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-13 08:43</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=e2fd575e920548c2b3928427debe524c&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="e2fd575e920548c2b3928427debe524c">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0412
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-12 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-13 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-12 08:50</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=5bd821812114498883124447030580fb&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="5bd821812114498883124447030580fb">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0411
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-11 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-12 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-11 09:32</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=569e7d2705c746c7a9448f6fb4e6aed4&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">50</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="569e7d2705c746c7a9448f6fb4e6aed4">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0410
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-10 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-11 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-10 09:18</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=a39d9a65660a44b786e92c88d68e2a53&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="a39d9a65660a44b786e92c88d68e2a53">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0407
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-07 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-08 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-07 08:39</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=aa8d9795f5e34bb08fe0ab37e18803ef&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="aa8d9795f5e34bb08fe0ab37e18803ef">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0406
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-06 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-07 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-06 20:55</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=1e81c11c4cae45148e926c85b61f4fdc&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="1e81c11c4cae45148e926c85b61f4fdc">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0404
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-04 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-05 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-04 08:38</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=63c1153947ec45c0ac543595a01c77e4&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="63c1153947ec45c0ac543595a01c77e4">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0403
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-04-03 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-04 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-04-03 08:45</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
        <div class="panel-title">
            <h2 class="title-name" id="month_3">3月</h2>
        </div>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=344a071b482146a4b25ce7c64887893f&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="344a071b482146a4b25ce7c64887893f">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0331
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-31 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-04-01 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-31 08:23</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=fc543a5801fd4d2cb7b4f882ec654a1e&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="fc543a5801fd4d2cb7b4f882ec654a1e">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0330
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-30 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-31 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-30 08:36</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=69b5322e9e6143e4801e9c9342092a98&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="69b5322e9e6143e4801e9c9342092a98">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0329
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-29 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-30 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-29 08:53</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=b35d4ea2af54422b91c1dfc422f06002&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="b35d4ea2af54422b91c1dfc422f06002">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0328
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-28 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-29 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-28 08:48</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=58b2dd9e79754bc383adab7aff46284d&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="58b2dd9e79754bc383adab7aff46284d">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0327
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-27 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-28 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-27 11:01</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=424f2b3ff8b246fea59a0f7a31bd8dbc&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="424f2b3ff8b246fea59a0f7a31bd8dbc">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0324
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-24 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-25 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-24 09:18</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=77f67c665d1e41ddb96c8735b48f1597&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="77f67c665d1e41ddb96c8735b48f1597">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0323
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-23 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-24 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-23 08:57</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=cdbbe8c674954af58448c4acdf97509c&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="cdbbe8c674954af58448c4acdf97509c">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0322
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-22 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-23 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-22 09:10</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=204d5e31ae614f40ba79d1cf27b02f13&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="get-no-score gray">缺考</div>
                    </div>
                    <div class="item-middle" data-id="204d5e31ae614f40ba79d1cf27b02f13">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0321
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-21 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-22 00:00</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=201676d657c74be1a71d14ce527e8b36&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="201676d657c74be1a71d14ce527e8b36">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0320
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-20 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-21 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-20 11:42</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=4985157afec343c8a24da385db1862d4&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="4985157afec343c8a24da385db1862d4">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0317
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-17 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-18 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-17 09:28</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=5a66f69436ae46b4a5f60659d2250db5&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="get-no-score gray">缺考</div>
                    </div>
                    <div class="item-middle" data-id="5a66f69436ae46b4a5f60659d2250db5">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0316
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-16 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-17 00:00</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=7db3497568964beda0f2c2bd26ec74be&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="7db3497568964beda0f2c2bd26ec74be">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0315
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-15 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-16 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-15 09:40</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=d07c91b0c16c4ce58f40e04eb0b867b5&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="get-no-score gray">缺考</div>
                    </div>
                    <div class="item-middle" data-id="d07c91b0c16c4ce58f40e04eb0b867b5">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0314
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-14 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-15 00:00</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=8bc1104570054a22acfae6eea5ea5f9c&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="8bc1104570054a22acfae6eea5ea5f9c">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0313
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-13 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-14 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-13 08:39</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
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
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=a3ab4132a5d4426eaa63e6bfbe1df425&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="a3ab4132a5d4426eaa63e6bfbe1df425">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0306
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-06 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-07 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-06 09:14</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=4a552822055740e8bfeb4d57066aeade&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="4a552822055740e8bfeb4d57066aeade">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0303
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-03 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-04 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-03 08:49</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=8e2f602181c14f1ca00f65d9ef327e25&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="8e2f602181c14f1ca00f65d9ef327e25">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0302
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-02 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-03 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-02 09:30</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=eb8d81c6e7e94233a073b580d4aaac95&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="eb8d81c6e7e94233a073b580d4aaac95">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0301
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-03-01 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-02 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-03-01 09:32</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
        <div class="panel-title">
            <h2 class="title-name" id="month_2">2月</h2>
        </div>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=259d29761b4349e79e5b7ad867499088&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="259d29761b4349e79e5b7ad867499088">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0228
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-28 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-03-01 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-28 18:54</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=b20f7c20c4e740e0a551fca6ee62bf75&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="b20f7c20c4e740e0a551fca6ee62bf75">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0227
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-27 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-28 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-27 08:54</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=422cab476059485984276fde7cde2bb1&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="get-no-score gray">缺考</div>
                    </div>
                    <div class="item-middle" data-id="422cab476059485984276fde7cde2bb1">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0224
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-24 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-25 00:00</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=68f3cdeced8246d49a502ed047ae5918&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="68f3cdeced8246d49a502ed047ae5918">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0223
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-23 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-24 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-23 09:34</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=b670b6a148554457af7e05d4206b194f&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="b670b6a148554457af7e05d4206b194f">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0222
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-22 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-23 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-22 10:22</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=c59fdac4bec2468bb54410d50cb8e335&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="c59fdac4bec2468bb54410d50cb8e335">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0221
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-21 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-22 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-21 08:51</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=4b64cefca8ac4e89b3cde839bb82ca8c&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="4b64cefca8ac4e89b3cde839bb82ca8c">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0220
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-20 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-21 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-20 11:55</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=2369fb1e947d40829bf06ea549ed9939&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="2369fb1e947d40829bf06ea549ed9939">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0217
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-17 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-18 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-17 08:41</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=8c6fc0ae37484ee1a3829a4bd0e188cd&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="8c6fc0ae37484ee1a3829a4bd0e188cd">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0216
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-16 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-17 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-16 08:44</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=cb29bd7c38974b3aa9b9affd5c13a160&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="cb29bd7c38974b3aa9b9affd5c13a160">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0215
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-15 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-16 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-15 11:53</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=f79ed326b72e4f16ab0ae4e855190475&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="f79ed326b72e4f16ab0ae4e855190475">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0214
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-14 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-15 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-14 08:52</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=9db08e850a6b4e59bc015fd5ae64a77c&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="9db08e850a6b4e59bc015fd5ae64a77c">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0213
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-13 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-14 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-13 09:19</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=028d18392f3f4ca291d19ffd1503baed&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="028d18392f3f4ca291d19ffd1503baed">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0210
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-10 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-11 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-10 14:53</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=0cc19f81d1ff4248a62b2b9df30159a7&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="get-no-score gray">缺考</div>
                    </div>
                    <div class="item-middle" data-id="0cc19f81d1ff4248a62b2b9df30159a7">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0209
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-09 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-10 00:00</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=7341a0d2338a477d8b9049f22cf07014&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="7341a0d2338a477d8b9049f22cf07014">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0208
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-08 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-09 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-08 09:59</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=8ea60b18834648d093a43b8d29d3b287&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="8ea60b18834648d093a43b8d29d3b287">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0207
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-07 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-08 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-07 09:12</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=773b75e702d644ecba85966701953306&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="773b75e702d644ecba85966701953306">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0206
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-06 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-07 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-06 08:33</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=dc9e91183c6e48daa621f6431ab2b17d&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="dc9e91183c6e48daa621f6431ab2b17d">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0203
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-03 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-04 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-03 11:20</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=80b81bf2849d4d7b9d2a3b84764caf6c&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="80b81bf2849d4d7b9d2a3b84764caf6c">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0202
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-02 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-03 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-02 08:55</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=0d6284db3e3e4457841e4481dc6c5bad&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="0d6284db3e3e4457841e4481dc6c5bad">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0201
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-02-01 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-02-02 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-02-01 10:57</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
        <div class="panel-title">
            <h2 class="title-name" id="month_1">1月</h2>
        </div>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=1c69b28211754064afb5073e4e3998e3&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="1c69b28211754064afb5073e4e3998e3">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0117
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-17 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-18 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-17 11:16</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=c60eaf1ec5db4eb9b102ec80142c2e06&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="c60eaf1ec5db4eb9b102ec80142c2e06">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0116
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-16 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-17 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-16 09:01</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=3d4eee188b3e42bf9f2af61d2d1b949e&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="3d4eee188b3e42bf9f2af61d2d1b949e">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0113
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-13 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-14 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-13 08:45</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=148c93527a934a56af9af810f1d7203d&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="148c93527a934a56af9af810f1d7203d">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0112
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-12 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-13 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-12 09:09</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=b935dc5bf7f74948928f3f69c23739b2&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="b935dc5bf7f74948928f3f69c23739b2">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0111
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-11 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-12 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-11 14:38</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=d4a87f749c5549b1876c61f4e19ab0a6&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="d4a87f749c5549b1876c61f4e19ab0a6">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0110
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-10 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-11 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-10 09:29</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=3ee4bee426b54c17be6c55c0b00f8c86&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="3ee4bee426b54c17be6c55c0b00f8c86">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0109
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-09 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-10 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-09 14:31</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=76ec664aeaba42c68a555b7cc6b24aa1&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="76ec664aeaba42c68a555b7cc6b24aa1">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0106
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-06 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-07 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-06 10:26</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
            <a class="panel-content"
               href="/ems/html/examCenter/examDetailLeft.do?examId=d1e2c253c2214dc6bd87277df9138298&thisEnterType=historyExam">
                <div class="item-panel">
                    <div class="item-left">
                            <div class="item-top pass">100</div>
                            <div class="item-down pass">通过</div>
                    </div>
                    <div class="item-middle" data-id="d1e2c253c2214dc6bd87277df9138298">
                        <div class="item-top">
                            <div class="overflow-div">
                            工程每日一练0105
                            </div>
                        </div>
                        <div class="item-down">
                            <div class="item-time">
                                <div class="item-time-l fl start-time">考试时间:2023-01-05 00:00</div>
                                <div class="item-time-m fl"></div>
                                <div class="item-time-r fl end-time">2023-01-06 00:00</div>
                                    <div class="item-time-l fl start-time">交卷时间：2023-01-05 09:07</div>
                            </div>
                        </div>
                    </div>
                    <div class="item-right clearF">

                                <button type="button" class="btn-white fr view-exam-paper">查看答卷</button>

                    </div>
                </div>
            </a>
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
</div>`
<script type="text/javascript">
    $(function () {
        baseEms.historyExamInt.init();
    })
</script>
'''

'''
tree = etree.HTML(html)
result= tree.xpath("//div/@data-id")
r2= tree.xpath("//div[@class='overflow-div']/text()")
#print(result)
#r3= r2[1].text.split('.')[-1].strip()
#print(r3)
# 定义正则表达式
pattern = r'<div class="overflow-div">\s*(.*?)\s*</div>'
# 使用正则表达式匹配
result2 = re.findall(pattern, html)
# 输出结果
#print(result2)
#测试循环打印2正确了，用函数调用的方法
def getIN(id,name):
    print(id,name)
    return

L=list(range(0,len(result2)))
for i in L:
    getIN(result[i],result2[i])


#<div class="item-middle" data-id="6ef1f62cc0234a278bfad80ef274392f">

#<div class="overflow-div">
'''

soup = BeautifulSoup(html, 'html.parser')
# 获取题目ID
examlistget=[]
examlist = soup.find_all('div', {'class': 'item-middle'})
for value in examlist:
    examlistget.append(value['data-id'])
print(examlistget[0])

#以上通过3种数据解析方法获取了试卷ID等信息，RE模块的正则表达式，BS4,Xpath
#测试循环打印1错误了
'''
for id in result:
    for name in result2:
        print(id,name)
    break
'''