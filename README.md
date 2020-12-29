# follow

我的私藏,一个web安全深度爬虫，可以和漏扫软件进行联动，如 burp xray ,可以导入文本批量爬取，自动化你懂的，效果吊打已有的爬虫。

第一次 用python 编写脚本，不要看代码 代码很烂，要看功能。也可以用我的思路写一个更强的。 但是这一个就够我用了。

方法： follow.py -h 查看帮助文档

# 单个url操作命令

follow.py -u https://www.baidu.com    # 单个url爬取

follow.py -u https://www.baidu.com  --proxy  http://127.0.0.1:8080  # 单个url爬取 并使用代理 

follow.py -u https://www.baidu.com  --proxy  http://127.0.0.1:8080 --xray D:\xray\xray.exe   # 单个url爬取 并使用代理 自动启动xray

# 批量操作命令 

follow.py -f D:\url.txt  # 导入文本进行批量爬取

follow.py -f D:\url.txt --proxy http://127.0.0.1:8080 # 导入文本 平且使用代理

follow.py -f D:\url.txt --proxy http://127.0.0.1:8080 --xray D:\xray\xray.exe # 导入文本 平且使用代理 自动启动xray
