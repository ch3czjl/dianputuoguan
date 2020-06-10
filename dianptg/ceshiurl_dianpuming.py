#coding:utf-8
import json
import requests
import datetime,time

# def __init__(self):
#     pass
def dianpuid(dianpuming):
    data = {'key': dianpuming, 'pageSize': 20,"pageIndex": 1}
    data_json = json.dumps(data)
    # payload = {'json_payload': data_json, 'key': "淘工厂工作室", 'pageSize': 20,"pageIndex": 1}   XXXXXX
    requests.packages.urllib3.disable_warnings()
    # time_stamp = '{0:%Y-%m-%d-%H-%M}'.format(datetime.datetime.now())
    time_stamp0 = time.time()
    # print(time_stamp0)
    time_stamp = str(int(round(time_stamp0*1000)))
    # time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    # time_stamp = datetime.struct_time()
    # print(time_stamp)
    header = {'Accept-Encoding': 'gzip',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              'User-Agent': 'okhttp-okgo/jeasonlzy',
              'Content-Length': '69',
              'Content-Type': 'application/json;charset=utf-8',
              'androidId': '408d5c17a3a55963',
              'appversion': '2.8.0',
              'deviceinfo': 'Android',
              'deviceNum': 'db28729e-4e88-3dec-99f4-9a8b76fca329',
              'imei': '355757600616318',
              'mac': '40:8D:5C:17:A3:A5',
              'sign': 'fd28b1c4ddb075c1758ce55f5f137169',
              'source': 'Android-MAWbdpz01',
              'systemversion': '5.1.1',
              'timestamp': time_stamp,
              'Authorization': 'Wwdz eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxZXk4cHMiLCJjcmVhdGVkIjoxNTkxMzIxMDc1MTgxLCJleHAiOjE1OTE5MjU4NzV9.UU6Yr-qRwlxh7m4XUr63ZvMuCGO79pGjjxnnE60cYwGK_rfJM9dT-bOGVWNdvfHIb7JvTHzEJe0iEYIVEeFwBw',
              'Connection': 'Keep-Alive',
              'Host': 'api.wanwudezhi.com'}
    # header = {'Client':{'Accept-Encoding': 'gzip','Accept-Language': 'zh-CN,zh;q=0.8','User-Agent': 'okhttp-okgo/jeasonlzy',},
    #           'Entity':{'Content-Length': '69','Content-Type': 'application/json;charset=utf-8',},
    #          'Miscellaneous':{'androidId': '408d5c17a3a55963','appversion': '2.8.0','deviceinfo': 'Android','deviceNum': 'db28729e-4e88-3dec-99f4-9a8b76fca329','imei': '355757600616318','mac': '40:8D:5C:17:A3:A5','sign': 'fd28b1c4ddb075c1758ce55f5f137169','source': 'Android-MAWbdpz01','systemversion': '5.1.1','timestamp': time_stamp,},
    #          'security':{'Authorization': 'Wwdz eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxZXk4cHMiLCJjcmVhdGVkIjoxNTkxMzIxMDc1MTgxLCJleHAiOjE1OTE5MjU4NzV9.UU6Yr-qRwlxh7m4XUr63ZvMuCGO79pGjjxnnE60cYwGK_rfJM9dT-bOGVWNdvfHIb7JvTHzEJe0iEYIVEeFwBw',},
    #          'Transport':{'Connection': 'Keep-Alive','Host': 'api.wanwudezhi.com',}}

    # header2 = {
    #     POST /api/shop/v2/shop/findShop HTTP/1.1
    #     Accept-Language: zh-CN,zh;q=0.8
    #     User-Agent: okhttp-okgo/jeasonlzy
    #     deviceinfo: Android
    #     appversion: 2.8.0
    #     systemversion: 5.1.1
    #     timestamp: 1591661818681
    #     deviceNum: db28729e-4e88-3dec-99f4-9a8b76fca329
    #     androidId: 408d5c17a3a55963
    #     mac: 40:8D:5C:17:A3:A5
    #     imei: 355757600616318
    #     source: Android-MAWbdpz01
    #     sign: f9ea4da837887809077b9e349e0e0d19
    #     Authorization: Wwdz eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxZXk4cHMiLCJjcmVhdGVkIjoxNTkxNjYxNzYwMjAyLCJleHAiOjE1OTIyNjY1NjB9.7Sr-PwPMT9QBAdKIltUMedE5mTTZwxQE486x2ZVjP2jnaYAMOiRCM5n_lnEgDnVHXl_EtGz7gEJPvFhcJGz0vA
    #     Content-Type: application/json;charset=utf-8
    #     Content-Length: 69
    #     Host: api.wanwudezhi.com
    #     Connection: Keep-Alive
    #     Accept-Encoding: gzip}
    #
    # }
    # header3 = {'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'User-Agent': 'okhttp-okgo/jeasonlzy',
    # 'deviceinfo': 'Android',
    # 'appversion': '2.8.0',
    # 'systemversion': '5.1.1',
    # 'timestamp': time_stamp,
    # 'deviceNum': 'db28729e-4e88-3dec-99f4-9a8b76fca329',
    # 'androidId': '408d5c17a3a55963',
    # 'mac': '40:8D:5C:17:A3:A5',
    # 'imei': '355757600616318',
    # 'source': 'Android-MAWbdpz01',
    # 'sign': 'fd28b1c4ddb075c1758ce55f5f137169',
    # 'Authorization': 'Wwdz eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxZXk4cHMiLCJjcmVhdGVkIjoxNTkxMzIxMDc1MTgxLCJleHAiOjE1OTE5MjU4NzV9.UU6Yr-qRwlxh7m4XUr63ZvMuCGO79pGjjxnnE60cYwGK_rfJM9dT-bOGVWNdvfHIb7JvTHzEJe0iEYIVEeFwBw',
    # 'Content-Type': 'application/json;charset=utf-8',
    # 'Content-Length': '69',
    # 'Host': 'api.wanwudezhi.com',
    # 'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    # }
    # r = requests.post('https://api.wanwudezhi.com/api/shop/v2/shop/findShop',data=payload,headers=header,verify=False)   xxxxx
    r = requests.post('https://api.wanwudezhi.com/api/shop/v2/shop/findShop',data=data_json,headers=header,verify=False)
    rr = json.loads(r.content.decode())
    # print(r.status_code,type(r.text),r.text)
    # print(r.text['result'])
    # print(type(rr),type(rr['result']),rr['result'])
    rrr = rr['result']['dataList']
    # print(rrr[0],type(rrr[0]))
    return rrr[0]['shopId']
# print(rr)
dianpuming = "淘工厂工作室"
x = dianpuid(dianpuming)
# print(x)