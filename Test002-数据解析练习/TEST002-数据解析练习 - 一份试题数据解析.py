from bs4 import BeautifulSoup

html = '''<div class="question-panel-middle" id="myexa_quest_7d4d4bad39fc421f993954a936683647" data-index="4" questtype="SINGLE" >
            <div class="question-stem clearF">
                <span class="num fl">4</span>
                <div class="name">
                    <b>.</b> 根据中国移动企业标准，1000Ah以下的阀控式密封蓄电池，重量偏差应不超过标称值的（ ）。 （20&nbsp;分）
                </div>
            </div>
            <ul class="question-options" style="margin-left:24px;">
                <li class="form-cell">
                    <input type="radio" id="_item_716e508b6dd344e59760ef07afd34951" name="_item_7d4d4bad39fc421f993954a936683647" value="716e508b6dd344e59760ef07afd34951"/>
                    <label for="_item_716e508b6dd344e59760ef07afd34951">
                        <div class="item-detail">
                            A. 百分之五
                        </div>
                    </label>
                </li>
                <li class="form-cell">
                    <input type="radio" checked="checked" id="_item_5b89b641b1654779bf721cdf247e29ca" name="_item_7d4d4bad39fc421f993954a936683647" value="5b89b641b1654779bf721cdf247e29ca"/>
                    <label for="_item_5b89b641b1654779bf721cdf247e29ca">
                        <div class="item-detail">
                            B. 百分之八
                        </div>
                    </label>
                </li>
                <li class="form-cell">
                    <input type="radio" id="_item_bf5a80d0375e4640b3b5d1a8b63778d5" name="_item_7d4d4bad39fc421f993954a936683647" value="bf5a80d0375e4640b3b5d1a8b63778d5"/>
                    <label for="_item_bf5a80d0375e4640b3b5d1a8b63778d5">
                        <div class="item-detail">
                            C. 百分之十五
                        </div>
                    </label>
                </li>
                <li class="form-cell">
                    <input type="radio" id="_item_7c6bd7dcd6624eb7ae06d65b018b2f3d" name="_item_7d4d4bad39fc421f993954a936683647" value="7c6bd7dcd6624eb7ae06d65b018b2f3d"/>
                    <label for="_item_7c6bd7dcd6624eb7ae06d65b018b2f3d">
                        <div class="item-detail">
                            D. 百分之二十
                        </div>
                    </label>
                </li>
            </ul>
            <div class="true-answer-panel">
                <div class="fl">
                    <div class="true-answer" > 标准答案 ：B </div>
                </div>
                <div class="s fr">
                    <i class="iconfont right">&#xe7bf;</i>
                </div>
            </div>
        </div>'''

soup = BeautifulSoup(html, 'html.parser')

# 获取题目
question = soup.find('div', {'class': 'name'}).text.split('.')[-1].strip()
print(question)

# 获取选项和答案
options = soup.find_all('div', {'class': 'item-detail'})

for option in options:
    print(option.text.strip()) # 打印选项
    
# 获取标准答案
answer = soup.find('div', {'class': 'true-answer'}).text.split('：')[-1].strip()
print(answer)