#!/usr/bin/python
# -*- coding: UTF-8 -*-

data = ''
with open('ori_wlan_login.py', 'rt') as f:
	data = f.read()

user = str(raw_input("学号: ")).strip()
password = str(raw_input("密码: ")).strip()

data = data.replace('$USERNAME$', user).replace("$PASSWORD$", password)
with open('wlan_login.py', 'at') as f:
	f.write(data)
