#!/bin/sh
# -*- coding: UTF-8 -*-

# Author: leylee

a=`which python3`
if [ -z "$a" ]
then
	echo "您没有安装 Python3. 是否通过 Homebrew 安装 Python3? [y/n]"
	read ans
	if [[ ans = "n" || ans = "N" ]]
	then
		echo "安装失败."
		exit
	fi

	echo "安装 Homebrew..."
	a=`which brew`
	if [ -z "$a" ]
	then
		/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	fi

	echo "安装 Python3..."
	brew install python3
fi
echo "安装 requests 库..."
pip3 install requests

echo "配置文件"
echo '#!'`which python3` > wlan_login.py
./config_wlan_login_script.py

echo "复制文件 (需要 root 权限)"
sudo cp ./com.leylee.wlanAutoLogin.plist /Library/LaunchDaemons/
sudo mkdir -p /usr/local/wlan_login
sudo cp -f ./wlan_login.py /usr/local/wlan_login/wlan_login.py
sudo chmod +x /usr/local/wlan_login/wlan_login.py
rm ./wlan_login.py

echo "重新启动守护进程..."
a=`launchctl list |grep leylee`
if [ "$a" ]
then
	launchctl unload com.leylee.wlanAutoLogin.plist
fi
launchctl load com.leylee.wlanAutoLogin.plist

echo "是否禁用 WiFi 验证的系统弹窗? [y/n]"
read ans
if [[ ans = "y" || ans = "Y" ]]
then
	sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean false
else
	sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean true
fi

echo "配置完成. 如不能自动登录, 请重新运行安装程序."
