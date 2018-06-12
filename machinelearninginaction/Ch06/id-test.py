# _*_ coding: UTF-8 _*_
import os,sys
import ssl
reload(sys)
sys.setdefaultencoding('utf-8')

import time,json
import urllib,urllib2,base64,json,hashlib

app_key = 'xxxxxx'
app_secret = 'xxxxxx'
clitraid = 'clitraid21231'

id = '362532198705152927'
name = '李小菲'

time_now = time.strftime('%Y-%m-%d %H:%M:%S')

param = dict()
param.update(
        app_key = app_key,
        name = name,
        id = id,
        time = time_now,
        sign = hashlib.md5(app_key+id+time_now+app_secret).hexdigest(),
		clitraid = clitraid)

postdata = urllib.urlencode(param).encode('utf-8')
time_start = time.time()
ssl._create_default_https_context = ssl._create_unverified_context
res = urllib2.urlopen('https://45.120.243.194:8883/service/b2/check',postdata).read()
print res,'time:',time.time()-time_start,id
