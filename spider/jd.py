"""
              ┏┓      ┏┓
            ┏━┛┻━━━━━━┛┻━┓
                                       ┃      ☃      ┃
            ┃   ┳┛   ┗┳  ┃
            ┃      ┻     ┃
            ┗━━━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑     ┣━━┓
                ┃　永无BUG!  ┏━┛
                ┗━┓┓┏━━┳┓┏━┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛

"""
import urllib
import urllib.request
import http.cookiejar

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
postdata = urllib.parse({
			'loginname':'15289479566',
			'nloginpwd':'*'
		})
#登录教务系统的URL
loginUrl = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fhome.jd.com%2F'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'https://sale.jd.com/act/Lqf7gVlE84v.html'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print(result.read())
