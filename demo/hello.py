import webbrowser
import time
import sys

url = 'https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=fb81b2437ed54b1baa0bd95ac8fa8379&roleId=6769824&to=sale.jd.com/act/lqf7gvle84v.html&'

while 1==1:
    tt = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if int(tt) > 20170601095959:
        webbrowser.open(url)
        print('chenggong')
    else:
        time.sleep(0.5)
        print(tt)
