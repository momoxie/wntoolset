#/usr/bin/env python
#coding=utf8

import sys
import httplib
import hashlib
import urllib
import random
import json
try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET
import config_path

reload(sys)
sys.setdefaultencoding('utf8')

# 百度翻译开发者平台申请 appid和secreKey 并改为自己的，默认的访问频率受限
appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'

httpClient = None
myurl = '/api/trans/vip/translate'

def translate_baidu(q,fromLang,toLang):
    salt = random.randint(32768, 65536)

    sign = "%s%s%s%s"%(appid,q,str(salt),secretKey)
    m1 = hashlib.md5()
    m1.update(sign)
    sign = m1.hexdigest()

    turl = "%s%s%s%s%s%s%s%s%s%s%s%s%s"%(myurl,'?appid=',appid,'&q=',urllib.quote(q),'&from=',fromLang,'&to=',toLang,'&salt=',str(salt),'&sign=',sign)
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', turl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        returnJson = response.read()
        print returnJson
        return returnJson
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    return q


def translate_xml(filePath,fromLang,toLang):
    try:
        tree = ET.parse(filePath)  # 打开xml文档
        root = tree.getroot()  # 获得root节点
        for name in root:  # 找到root节点下的所有name节点
            value = name.text  # 子节点下属性name的值
            jsonValue = translate_baidu(value.encode('utf-8'),fromLang,toLang)
            jsonDic = json.loads(jsonValue)
            print jsonDic["trans_result"][0]["dst"]
            name.text = jsonDic["trans_result"][0]["dst"];
        tree.write(filePath.replace('.xml',"_"+toLang+".xml"),"utf-8")

    except Exception, e:
        print "Error:cannot parse file: %s"%e
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 3:
        translate_xml(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) > 1:
        translate_xml(sys.argv[1],"zh","en")
    else:
        translate_xml("%s/plugins/fanyibaidu/strings.xml"%config_path.g_project_dir,"zh","en")
