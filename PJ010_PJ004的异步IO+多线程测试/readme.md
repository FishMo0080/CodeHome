写python一段代码，用于读取文件夹ready里面的“ready.xlsx”A列的数据，按照A列的数据到PMIS导出表格，然后对数据进行汇总。cookie会改变，需要定期更新，更新方法：PORTAL登陆后进入PMIS，直接查看cookie里面的pmis.session.id即可。
<hr>

# 代码说明

## 用了3种方法对比：
    单线程、多线程、异步。
    1、119个项目导出时间：多线程（12s）>异步（14s）>>单线程（5min）
    2、注意异步模块获取内容的方式是read().