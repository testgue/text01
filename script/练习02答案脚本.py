# 导包
import requests
#***********************查询接口调用start***********************
# 学院信息查询接口的调用
# 1.1
# 定义地址
url11 = "http://127.0.0.1:8000/api/departments/"
# 发送请求
res11 = requests.get(url11)
# 输出结果
print("1.1响应：",res11.text)

# 1.2
# 定义地址
url12 = "http://127.0.0.1:8000/api/departments/T01/"
# 发送请求
res12 = requests.get(url12)
# 输出结果
print("1.2响应：",res12.text)

# 1.3
# 定义地址
url13 = "http://127.0.0.1:8000/api/departments/"
# url13 = "http://127.0.0.1:8000/api/departments/?$dep_id_list=T01,T02,T03"
# 定义参数列表
para13 = {"$dep_id_list":"T01,T02,T03"}
# 发送请求
res13 = requests.get(params=para13,url=url13)
# res13 = requests.get(url=url13)
# 输出结果
print("1.3响应：",res13.text)

# 1.4
# 定义地址
url14 = "http://127.0.0.1:8000/api/departments/"
# 定义参数列表
para14 = {"$dep_id_list":"T01,T02,T03","$slogan_list":"Here is Slogan"}
# 发送请求
res14 = requests.get(params=para14,url=url14)
# 输出结果
print("1.4响应：",res14.text)

# 1.5
# 定义地址
url15 = "http://127.0.0.1:8000/api/departments/"
# 定义参数列表
para15 = {"master_name":"222"}
# 发送请求
res15 = requests.get(params=para15,url=url15)
# 输出结果
print("1.5响应：",res15.text)

# 1.6
# 定义地址
url16 = "http://127.0.0.1:8000/api/departments/"
# 定义参数列表
para16 = {"master_name":"222","slogan":"333"}
# 发送请求
res16 = requests.get(params=para16,url=url16)
# 输出结果
print("1.6响应：",res16.text)

# 1.7
# 定义地址
url17 = "http://127.0.0.1:8000/api/departments/"
# 定义参数列表
para17 = {"master_name":"2","blur":"1"}
# 发送请求
res17 = requests.get(params=para17,url=url17)
# 输出结果
print("1.7响应：",res17.text)

# 1.8
# 定义地址
url18 = "http://127.0.0.1:8000/api/departments/"
# 定义参数列表
para18 = {"master_name":"2","blur":"1","slogan":"3"}
# 发送请求
res18 = requests.get(params=para18,url=url18)
# 输出结果
print("1.8响应：",res18.text)

#***********************查询接口调用end***********************

#***********************新增接口调用start***********************
# 新增单个
# 自己做
# 新增两个

# 定义地址
url22 = "http://127.0.0.1:8000/api/departments/"
# 定义消息体数据
data22 = {"data":[{"dep_id":"T21","dep_name":"Test学院","master_name":"Test-Master","slogan":"HereisSlogan"},{"dep_id":"T22","dep_name":"Test学院","master_name":"Test-Master","slogan":"HereisSlogan"}]}
# 发送请求
res22 = requests.post(url=url22,json=data22)
# 输出结果
print("2.2响应：",res22.text)

#***********************新增接口调用end***********************

#***********************更新接口调用start***********************


# 定义地址
url31 = "http://127.0.0.1:8000/api/departments/T22/"
# 定义消息体数据
data31 = {"data":[{"dep_id":"T22","dep_name":"吐槽学院","master_name":"爱谁谁，谁谁","slogan":"这里不是口号"}]}
# 发送请求
res31 = requests.put(url=url31,json=data31)
# 输出结果
print("31响应：",res31.text)

#***********************更新接口调用end***********************


#***********************删除接口调用start***********************


# 4.1
# 定义地址
url41 = "http://127.0.0.1:8000/api/departments/T03/"
# 发送请求
res41 = requests.delete(url=url41)
# 输出结果
print("41响应状态码：",res41.status_code)

# 4.2
# 定义地址
url42 = "http://127.0.0.1:8000/api/departments/"
# 定义参数列表
para42 = {"$dep_id_list":"T21,T22"}
# 发送请求
res42 = requests.delete(url=url42,params=para42)
# 输出结果
print("42响应状态码：",res42.status_code)

#***********************删除接口调用end***********************

