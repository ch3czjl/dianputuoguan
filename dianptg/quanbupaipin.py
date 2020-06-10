# GET /api/shop/v2/shopItem/queryShopItemFirstPage?orderByType=6&shopId=69954&itemType=3&pageIndex=1&pageSize=20 HTTP/1.1
# /api/shop/v2/shopItem/queryShopItemFirstPage?orderByType=6&itemType=3&shopId=83271&pageIndex=1&pageSize=10'
# https://h5.wanwudezhi.com/mall-web/shop/index?shopId=83271&__HgWtwYU=1591668118226&rtp=bw0.w0.0.0.Ikt6oB1591668115216&token=Wwdz%20eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxZXk4cHMiLCJjcmVhdGVkIjoxNTkxNjY4MDYxMjM4LCJleHAiOjE1OTIyNzI4NjF9.HA0VQnOC939V_T8Jw2kycZl5uN6g2Sbb38GOPMh9jFr-dQAUqgJmJxTjQNnfplZsYdII3Ya7eCIRdHOpJ7E34A&__nh=64.00',
# GET /api/shop/v2/shopItem/queryShopItemFirstPage?orderByType=4&shopId=19007&itemType=3&pageIndex=1&pageSize=20 HTTP/1.1

#coding:utf-8
import json
import requests
import datetime,time
import ceshiurl_dianpuming

dianpuming0 = "玉之典一号店工作室"

dianpuid = str(ceshiurl_dianpuming.dianpuid(dianpuming0))

print(dianpuid)

url = 'https://api.wanwudezhi.com/api/shop/v2/shopItem/queryShopItemFirstPage?orderByType=6&itemType=3&shopId=' + dianpuid + '&pageIndex=1&pageSize=3000'
# print(url)
# r = requests.get(url,headers=header,verify=False)
r = requests.get(url,verify=False)
rr = json.loads(r.content.decode())
# print(r.text)
# print(type(r.text),type(rr))
allpaipinlist = rr['result']['dataList']
# print(len(rr),rr['result']['dataList'])
print(allpaipinlist[0])
print (type(allpaipinlist),len(allpaipinlist),allpaipinlist[0]['title'])
for x in range(0,len(allpaipinlist)):
    print(allpaipinlist[x]['title'])
# print(len(r.text))
# rrr = rr['result']['dataList']
# print(rrr[0]['name'],type(rrr[0]))
