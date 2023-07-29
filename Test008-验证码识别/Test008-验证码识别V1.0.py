import ddddocr #导入模块
ocr=ddddocr.DdddOcr() #实例化
with open("1.do", 'rb') as f: #打开图片
    image = f.read() 
res = ocr.classification(image)
print(res) #识别
a = int(res[0])
b = int(res[2])
if(res[1] == '+' or '十'):
    c = int(a + b)
    print(c)