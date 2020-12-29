# -*-codeing = utf-8 -*-
# @Time : 2020/12/21
# @Author : 山与河　qq 2900180755
# @FIle ： follow.py.py
# @Software : PyCharm
import requests
from multiprocessing.dummy import Pool
import re
import time
import argparse
import random
import os

########自定义定义logo############
logo = """
                                      __       _ _               
                                     / _| ___ | | | _____      __
                                    | |_ / _ \| | |/ _ \ \ /\ / /
                                    |  _| (_) | | | (_) \ V  V / 
                                    |_|  \___/|_|_|\___/ \_/\_/  Author：SHANYUHE  北京 海淀 2020/12/22 

"""
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
def ua():
    header = [
        'Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html',
        'Baiduspider-image+(+http://www.baidu.com/search/spider.htm)',
        'Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SCH-N719 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 YisouSpider/1.0.0 Mobile Safari/533.1',
        'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider(compatible;',
        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko)Version/4.0 Mobile Safari/534.30; 360Spider',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'AdsBot-Google-Mobile (+http://www.google.com/mobile/adsbot.html) Mozilla (iPhone; U; CPU iPhone OS 3 0 like Mac OS X) AppleWebKit (KHTML, like Gecko) Mobile Safari',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        'Sosoimagespider+(+http://help.soso.com/soso-image-spider.htm)',
        'Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)',
        'Mozilla/5.0 (compatible; Bytespider; https://zhanzhang.toutiao.com/) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; Bytespider; https://zhanzhang.toutiao.com/)',
        'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko)Version/4.0 Mobile Safari/534.30; 360Spider']
    i = random.randint(0,len(header)-1)
    user_agent = header[i]
    header = {}
    header['User-Agent'] = user_agent
    return header

## 请求返回返回一个列表 主域名 状态码 urls
file_txt = ''
urls_200_set = []
########返回主域名#######
def Name_url(url):
    ex = '[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?'
    name = re.search(ex, url, re.S)
    name_list = name[0].split('.')
    name_url = name_list[-2] + '.' + name_list[-1]
    return name_url
#####正则出连接#####
def rqueset(url):
    try:
        user_list = []
        # 正则出url主域名
        name_url = Name_url(url)
        global file_txt
        file_txt = name_url
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), "    ", '目标主域 ==> ',file_txt,proxy_name)
        user_list.append(name_url)
        url_bool = apk_exe(url)
        if url_bool == False:
            html_text = requests.get(url=url, headers=header,timeout=5,proxies=proxies,verify=False)
            ## 转换编码
            html_text.encoding = html_text.apparent_encoding
            html_text = html_text.text
            ## 正则1
            ex = '''href *= *['"]*(\S+)["']'''
            text1_url = re.findall(ex, html_text, re.S)
            ## 正则2
            ex = '''[a-zA-z]+://[^\s]*'''
            text2_url = re.findall(ex, html_text, re.S)
            user_list.append(text1_url + text2_url)
            return user_list
    except Exception as a:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), "    ", '主域名访问失败 ==> ',file_txt,proxy_name)
######## 去除特殊字符 ########
def a(url):
    if url.find('"') != -1:
        i = url.find('"')
        url_name = url[:i]
        return url_name
    else:
        return url  #

def b(url):
    if url.find(':', 7) != -1:
        i = url.find(':', 7)
        url_name = url[:i]
        return url_name
    else:
        return url

def c(url):
    if url.find("'") != -1:
        i = url.find('"')
        url_name = url[:i]
        return url_name
    else:
        return url

def d(url):
    if url.find(')') != -1:
        i = url.find(')')
        url_name = url[:i]
        return url_name
    else:
        return url

def e(url):
    if url[-2:] == '//':
        return url[:-2]
    else:
        return url

def f(url):
    if url[-1:] == '/':
        return url[:-1]
    else:
        return url

def urls(url):
    a1 = a(url)
    b1 = b(a1)
    c1 = c(b1)
    d1 = d(c1)
    e1 = e(d1)
    f1 = f(e1)
    return f1

######存活保存到list#####
hg_jc = 0
urls_200 = []
# 过滤 资源
def apk_exe(url):
    if url[-3:] == 'apk':
        urls_200.append(url)
        return True
    elif url[-3:] == 'exe':
        urls_200.append(url)
        return True
    elif url[-3:] == 'mp4':
        urls_200.append(url)
        return True
    elif url[-3:] == 'mp3':
        urls_200.append(url)
        return True
    else:
        return False
def code(url):
    try:
        if apk_exe(url) == False:
            url_bool = url in urls_200_set
            if url_bool == False:
                long = len(Name_url(url).split('.')[-1])
                if long < 6:
                    code = requests.head(url, headers=ua(), timeout=1,proxies=proxies,verify=False).status_code
                    if code != 404:
                        urls_200.append(url)
                        global hg_jc
                        hg_jc += 1
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), "    ", hg_jc, '——', url,proxy_name, " ⇆ ",code)
    except Exception as a:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), "    ", url,proxy_name, "==>", "访问失败!!!")

######多线程验证存活#########
def thread(url_list):
    pool = Pool(50)
    pool.map(code, url_list)
    pool.close()
    pool.join()
    repeat()
#######数据清洗 存活验证#######
########取合格url 返回 urls_list###########
def clean(url):
    try:
        urls_list = []
        url_list = rqueset(url)
        for name_url in url_list[1]:
            if name_url.find(url_list[0]) == -1:
                name_urls = url + name_url
                if len(name_urls) < 200:
                    if name_urls.count('http') < 2:
                        if name_urls.find('http') == -1:
                            name_urls1 = 'http:' + name_urls
                            name_urls1 = urls(name_urls1)
                            urls_list.append(name_urls1)
                            name_urls1 = 'https:' + name_urls
                            name_urls1 = urls(name_urls1)
                            urls_list.append(name_urls1)
                        else:
                            name_urls = urls(name_urls)
                            urls_list.append(name_urls)
            else:
                if len(name_url) < 200:
                    if name_url.count('http') < 2:
                        if name_url.find('http') == -1:
                            name_url1 = 'http:' + name_url
                            name_url1 = urls(name_url1)
                            urls_list.append(name_url1)
                            name_url1 = 'https:' + name_url
                            name_url1 = urls(name_url1)
                            urls_list.append(name_url1)
                        else:
                            name_url = urls(name_url)
                            urls_list.append(name_url)

        q = len(urls_list)
        h = set(urls_list)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), "     去重前： ", q, " 去重后：", len(h))
        thread(urls_list)
    except Exception as a:
        print(a)
###########去重复操作########
def repeat():
    try:
        urls_200_txt = []
        for url_name in urls_200:
            url_bool = url_name in urls_200_set
            if url_bool == True:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', '去除重复 ==>', url_name)
            if url_bool == False:
                urls_200_set.append(url_name)
                urls_200_txt.append(url_name)
        file_url(urls_200_txt)
        urls_200.clear()
    except Exception as a:
        print(a)

#####文件操作##############
def file_url(url_list):
    try:
        file_txt_name = file_txt.replace('.', '_') + '.txt'
        with  open(file_txt_name, 'a', encoding='utf-8') as fp:
            for url_name in url_list:
                url_bool = url_name in urls_200_set
                if url_bool == True:
                    fp.write(url_name + '\n')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), "    ", '保存成功 ==> ', file_txt_name)
    except Exception as a:
        print(a)

#######递归操作#########
dg_jc = 0
def recursion():
    try:
        global dg_jc
        while dg_jc < len(urls_200_set):
            url = urls_200_set[dg_jc]
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'   ',"➤" * 70,'\n')
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'   ','║',' 总:',len(urls_200_set), "余:",len(urls_200_set)-dg_jc, '现:',dg_jc,'⇆','',url,'\n')
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'   ', "➤" * 70)
            clean(url)
            dg_jc += 1
    except Exception as a:
        print(a)

# 返回全局代理
def proxy(proxie):
    global proxies
    proxies = proxie
    if proxies != '':
        proxies = {'http': proxies, 'https': proxies}
        global proxy_name
        proxy_name = ' ⇆  ' + proxies['http']
    if proxies == '':
        proxy_name = ''
if __name__ == '__main__':
        print(logo)
        time.sleep(3)
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', help='单个url进行爬取')
        parser.add_argument('-f', help='导入文本批量爬取')
        parser.add_argument('--xray', help='启动xray')
        parser.add_argument('--proxy', help='启用代理转发')
        args = parser.parse_args()
        if (args.u) != None and (args.proxy) == None:
            print(1)
            proxy('')
            clean(args.u)
            recursion()
        elif (args.proxy) != None and (args.u) != None and (args.xray) == None :
                print(2)
                proxy(args.proxy)
                clean(args.u)
                recursion()
        elif (args.proxy) != None and (args.u) != None and (args.xray) !=None:
            print(3)
            ip_i = args.proxy.find('//') + 2
            ip = args.proxy[ip_i:]
            proxy(args.proxy)
            os.system('start cmd /k "d: & cd d:/test/ & ' + args.xray + ' webscan --listen ' + ip + ' --html-output bai.html ')
            time.sleep(5)
            clean(args.u)
            recursion()
        elif(args.f) != None and (args.proxy) == None:
            try:
                print(4)
                with  open(args.f, 'r', encoding='utf-8') as fp:
                    z = len(fp.readlines())
                i = 1
                with  open(args.f, 'r', encoding='utf-8') as fp:
                    for url_name in fp:
                        url = url_name.strip()
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', "➤" * 70, '\n')
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', '║', ' 文本: ',args.f,' 总：',z,'现：',i,url,'\n')
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', "➤" * 70)
                        proxy('')
                        clean(url)
                        recursion()
                        i += 1
            except Exception as a:
                print(a)
        elif(args.f) != None and (args.proxy) != None and (args.xray) == None:
            try:
                print(5)
                with  open(args.f, 'r', encoding='utf-8') as fp:
                    z = len(fp.readlines())
                i = 1
                with  open(args.f, 'r', encoding='utf-8') as fp:
                    for url_name in fp:
                        url = url_name.strip()
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', "➤" * 70, '\n')
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', '║', ' 文本: ',args.f,' 总：',z,'现：',i,url,'\n')
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', "➤" * 70)
                        proxy(args.proxy)
                        clean(url)
                        recursion()
                        i += 1
            except Exception as a:
                print(a)
        elif (args.f) != None and (args.proxy) != None and (args.xray) != None :
            try:
                print(a)
                ip_i = args.proxy.find('//') + 2
                ip = args.proxy[ip_i:]
                os.system('start cmd /k "d: & cd d:/test/ & ' + args.xray + ' webscan --listen '+ ip +' --baidu.html ')
                time.sleep(5)
                print('6')
                with  open(args.f, 'r', encoding='utf-8') as fp:
                    z = len(fp.readlines())
                i = 1
                with  open(args.f, 'r', encoding='utf-8') as fp:
                    for url_name in fp:
                        url = url_name.strip()
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', "➤" * 70, '\n')
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', '║', ' 文本: ',args.f,' 总：',z,'现：',i,url,'\n')
                        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), '   ', "➤" * 70)
                        proxy(args.proxy)
                        clean(url)
                        recursion()
                        i += 1
            except Exception as a:
                print(a)