#!/bin/sh
# -*- coding: UTF-8 -*-

# Author: leylee

echo "移除自动登录..."
launchctl unload com.leylee.wlanAutoLogin.plist
sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean true
sudo rm /Library/LaunchDaemons/com.leylee.wlanAutoLogin.plist
sudo rm -Rf /usr/local/wlan_login
echo "文件已移除."