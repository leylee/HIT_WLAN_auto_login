# HIT_WLAN_auto_login
Mac OS 自动登录哈工大校园网的脚本

## 功能
用 Mac 登录校园网的朋友都知道, Mac 不会记住你的登录用户名和密码, 每次连接都要重新输入. 为了实现自动化, 特写此脚本 (写的很难看). 

每五秒检查是否已登录校园网, 若未登录则登录.

## 实现
使用 Python3 requests 库登录, 每五秒检查使用 Mac OS 的 launchd 进程.

## Requirements
python3
python3-requests

## 安装
安装需在联网的状态下进行. 

```sh
git clone https://github.com/leylee/HIT_WLAN_auto_login
cd HIT_WLAN_auto_login
./auto_config.sh
```

安装脚本会询问您的学号与校园网密码.

若未安装 python3, 安装脚本会引导您安装 homebrew, 然后安装 python3.

拷贝文件时, 可能需要用户密码.

安装过程中, 可选择是否关闭 WiFi 登录的系统弹窗. ~~**此项功能仅在关闭 SIP 后生效, [点击查看如何关闭 SIP](https://zhuanlan.zhihu.com/p/35780058).**~~ **目前此功能无效, 欢迎 PR.**

## 移除
```sh
./remove.sh
```
