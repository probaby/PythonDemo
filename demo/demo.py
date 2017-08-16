import re
from _overlapped import NULL

str = '黄彪1'
str2 = '黄彪2'
style = re.compile('<(.*?)>')
print(style.search(str)!=None)
strCon = 'cxt"<cxt@smtp.telek.com.cn>,"乔祥耀"<qiao-xiangyao@smtp.telek.com.cn>,"张忠洋"<zhang-zhongyang@smtp.telek.com.cn>,"张念祥"<zhang-nianxiang@smtp.telek.com.cn>,"张琛"<zhang-chen@smtp.telek.com.cn>,"王家波"<wang-jiabo@smtp.telek.com.cn>,"王帅"<wang-shuai@smtp.telek.com.cn>,"王树国"<wang-shuguo@smtp.telek.com.cn>,"王浩洋"<wang-haoyang@smtp.telek.com.cn>,"莫庆峰"<mo-qingfeng@smtp.telek.com.cn>,"许轲"<xu-ke@smtp.telek.com.cn>,"程翔"<chengxiang@smtp.telek.com.cn>,"陈顺吉"<chen-shunji@smtp.telek.com.cn>,"陈思敏"<chen-simin@smtp.telek.com.cn>,"黎佳朋"<li-jiapeng@smtp.telek.com.cn>,"刘奇男"<liu-qinan@smtp.telek.com.cn>,"罗川"<luo-chuan@smtp.telek.com.cn>,"潘佳浩"<pan-jiahao@smtp.telek.com.cn>,"汤智帅"<tzs@smtp.telek.com.cn>,"王攀峰"<wang-panfeng@smtp.telek.com.cn>,"赵静"<zhao-jing@smtp.telek.com.cn>,"刘雷"<liu-l@smtp.telek.com.cn>'
# print(str[0:-1]==str[0:-1])
# print('黄慌晃' in '黄慌晃虎')
list = style.findall(strCon)
stt = ''
for i in list:
    if stt != '':
        stt += ','
    stt += i
print(stt)