

''' Configure your username and password. '''
user = '$USERNAME$'
password = '$PASSWORD$'


import requests
import urllib
import os
import subprocess

''' Check if connected to HIT-WLAN. Only works on Mac OS. '''
process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I'], stdout=subprocess.PIPE)
out, err = process.communicate()
process.wait()
out = str(out)
if not 'HIT-WLAN' in out:
	print("You have not connected to HIT-WLAN.")
	os._exit(0)

''' Check if logged in. '''
response = requests.get("http://202.118.253.94:8080")
if not response.ok:
	print("Error:", response.status_code)
	os._exit(0)
if 'success' in response.url:
	print("You have already logged in.")
	os._exit(0)

''' Get url paraments. '''
print("Get http://123.123.123.123...")
response = requests.get("http://123.123.123.123")
if not response.ok:
	print("Error:", response.status_code)
	os._exit(0)
else:
	print("Attempt to login...")

headers = {
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': response.text.strip().lstrip("<script>top.self.location.href='").rstrip("'</script>"),
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
url = "http://202.118.253.94:8080/eportal/InterFace.do?method=login"
prefix = "<script>top.self.location.href='http://202.118.253.94:8080/eportal/index.jsp?"
suffix = "'</script>"
paraments = urllib.parse.quote(response.text.strip().lstrip(prefix).rstrip(suffix))
paraments = urllib.parse.quote(paraments)
form_data = "userId=" + user + "&password=" + password + "&service=&queryString=" + \
			paraments + "&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"
response = requests.post(url, data=form_data, headers=headers)
response.encoding = 'utf-8'

if not response.ok:
	print("Error:", response.status_code)
	os._exit(0)

if response.json()['result'] == "success":
	print("Login succeeded.")
else:
	print("Login failed:", response.json()['message'])