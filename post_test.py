#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import requests
import json



# def post_test():
#
#     n=0
#     for i in range(1, 5):
#         params1 = {'gply': '',
#                    'wtcsjg': '',
#                    'jzmj':'',
#                    'ordertype':'',
#                    'fwyt':'',
#                    'hxs':'',
#                    'havepic':'',
#                    'xzqh':'',
#                    'starttime':'',
#                    'endtime':'',
#                    'keywords':'',
#                    'page': i,
#                    'xqid': '0'}
#         headers1 = {'Accept': 'text/html, */*; q=0.01',
#                     'Accept-Encoding':'gzip, deflate',
#                     'Accept-Language':'zh-CN,zh;q=0.9','Connection':'keep-alive','Content-Length':'100',
#                     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#                     'Cookie':'JSESSIONID=FEC87CBBA17C0E6FB101986950B22BED.lb8; ROUTEID=.lb8; Hm_lvt_70e93e4ca4be30a221d21f76bb9dbdfa=1522409239,1522456083,1522456947; Hm_lpvt_70e93e4ca4be30a221d21f76bb9dbdfa=1522456957',
#                     'Host':'jjhygl.hzfc.gov.cn',
#                     'Origin':'http://jjhygl.hzfc.gov.cn','Referer':'http://jjhygl.hzfc.gov.cn/webty/gpfy/gpfySelectlist.jsp',
#                     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#                     'X-Requested-With':'XMLHttpRequest'}
#         url= 'http://jjhygl.hzfc.gov.cn/webty/WebFyAction_getGpxxSelectList.jspx'
#         r = requests.post(url, data=params1,headers=headers1)
#         rrr = json.loads(r.text)#注意！！！后面必须加‘.text’否则报错！！！！！
#         print(rrr)
#         print(n)
#         n=n+1
#         print('\n')
#         print('\n')
#         for j in range(0,10): #注意实际只取了1到n-1！！！！
#             print(rrr['list'][j]['fczsh']) #放到jsonviewer里面分析提取路径
#
# post_test()

def post_test(n):  #n为页码数量
    with open(r'C:\Users\mcc\Desktop\price_data.csv', 'w', encoding='utf-8') as f:
        for i in range(1,n):
            params1 = {'gply': '','wtcsjg': '','jzmj':'','ordertype':'','fwyt':'','hxs':'','havepic':'','xzqh':'','starttime':'',
                       'endtime':'','keywords':'','page': i,'xqid': '0'}
            headers1 = {'Accept': 'text/html, */*; q=0.01','Accept-Encoding':'gzip, deflate',
                        'Accept-Language':'zh-CN,zh;q=0.9','Connection':'keep-alive','Content-Length':'100',
                        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                        'Cookie':'JSESSIONID=FEC87CBBA17C0E6FB101986950B22BED.lb8; ROUTEID=.lb8; Hm_lvt_70e93e4ca4be30a221d21f76bb9dbdfa=1522409239,1522456083,1522456947; Hm_lpvt_70e93e4ca4be30a221d21f76bb9dbdfa=1522456957',
                        'Host':'jjhygl.hzfc.gov.cn',
                        'Origin':'http://jjhygl.hzfc.gov.cn','Referer':'http://jjhygl.hzfc.gov.cn/webty/gpfy/gpfySelectlist.jsp',
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                        'X-Requested-With':'XMLHttpRequest'}
            url= 'http://jjhygl.hzfc.gov.cn/webty/WebFyAction_getGpxxSelectList.jspx'
            r = requests.post(url, data=params1,headers=headers1)
            r_json = json.loads(r.text)#注意！！！后面必须加‘.text’否则报错！！！！！
            for j in range(0,10): #注意实际只取了1到n-1！！！！#将r_json放到jsonviewer里面分析提取路径
                fwtybh = r_json['list'][j]['fwtybh']
                cqmc = r_json['list'][j]['cqmc']  #所属城区
                xqmc = r_json['list'][j]['xqmc']  # 小区
                jzmj = r_json['list'][j]['jzmj']  # 建筑面积
                wtcsjg = r_json['list'][j]['wtcsjg']  # 委托价格
                mdmc = r_json['list'][j]['mdmc']  # 挂牌机构
                scgpshsj = r_json['list'][j]['scgpshsj']  # 挂牌时间
                f.write("{},{},{},{},{},{},{}\n".format(fwtybh,cqmc,xqmc,jzmj,wtcsjg,mdmc,scgpshsj))
            print('当前第 %d 页'%(i))

post_test(529)


#--------以下为草稿----------
# jd = json.loads(r.text) #移除改var data=将其变为json数据
# print(r.text)
# json_str = re.compile(r"{.*}") # 非贪婪模式的最大匹配，获取整个json字符串
# json_str = json_str.search(r).group()
# food_dict = json.loads(json_str)
# json = demjson.encode(r) 怀疑服务器没有严格封装成json的格式，强制转换为json对象，但是输出了一串数字
# soup = BeautifulSoup(r,'html.parser')
# soup.prettify()

# json_obj = json.loads(r.text)
# json = json.dumps(r.text)
# print (json)
# print (json[15])
# c= r.json()
# print(c)


