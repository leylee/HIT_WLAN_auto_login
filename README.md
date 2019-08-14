# HIT_WLAN_auto_login

## 功能
每五秒检查是否已登录校园网, 若未登录则登录.

## 实现
使用 Python3 requests 库登录, 每五秒检查使用 Mac OS 的 launchd 进程.

## Requirements
python3
python3-requests

## 安装
安装需在联网的状态下进行. 

```sh
cd ${DOWNLOADS}
unzip HIT_WLAN_auto_login.zip
cd HIT_WLAN_auto_login
./auto_config.sh
```

其中 `${DOWNLOADS}` 为你的下载路径.

安装脚本会询问您的学号与校园网密码.

若未安装 python3, 安装脚本会引导您安装 homebrew, 然后安装 python3.

拷贝文件时, 可能需要用户密码.