# -*- coding:utf-8 -*-

import win32com.client
import sys

if sys.getdefaultencoding() != "utf-8":
    reload(sys)
    sys.setdefaultencoding("utf-8")

# 加载RTXSAPIRootObj 创建RTX根对象
rootobj = win32com.client.Dispatch("RTXSAPIRootObj.RTXSAPIRootObj")

# 创建一个用户管理对象
um = rootobj.UserManager

# 创建一个部门管理对象
dm = rootobj.DeptManager

# AddUser 接收两个参数 第一个待添加的用户名字 第二个用户认证类型，该参数为0表示本地认证，为1表示第三方认证
isadd = um.AddUser("xxx".encode("gb2312"), 0)
print(isadd)
