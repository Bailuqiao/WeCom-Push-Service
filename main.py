# -*- coding = utf-8 -*-
# @Time : 2022/2/10 16:08
# @Author : wpz
# @File : main.py
# @Software : PyCharm
# 若需要在短时间内大量推送消息，请自行更改代码，把获取的access_token保存起来使用
# access_token有效期目前是7200s，可以通过api返回信息查到有效时间
# 不要频繁调用api获取，会被腾讯拉黑的
import requests

def push_service(message=""):
    # 以下参数必填
    corpid=""
    corpsecret=""
    Agentid=""
    
    if corpid == "" or corpsecret == "" or Agentid == "":
        print("必要参数为空")
        return
    
    # 获取access_token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+ corpid +"&corpsecret=" + corpsecret
    r = requests.get(url).json()
    if r["errcode"] != 0:
        print(r["errmsg"])
        print("access_token获取失败！")
        return
    else:
        access_token = r["access_token"]
    
    # 发送消息
    # 更多内容 https://developer.work.weixin.qq.com/document/path/90236
    data = {
    "touser": "@all",
    "msgtype": "text",
    "agentid": int(AgentId),
    "text": {
        "content": message
            },
    "safe": 0
    }
    
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + assess_token
    r = requests.post(url, json=data).json()
    if r["errcode"] == 0:
        print("推送成功")
    else:
        print(f"推送失败\n{r}")

if __name__ == "__main__":
    push_service("测试")
