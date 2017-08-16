import openpyxl
import re
import time

wb = openpyxl.load_workbook('E:\\工作\\材料整理\\read.xlsx')
log = open('E:\\工作\\材料整理\\log.txt','w')
sheet1 = wb.get_sheet_by_name('Sheet1')
sheet2 = wb.get_sheet_by_name('区域表')

#J C区域编码
#K D区域名称
#F 单位名称
#3164 甘肃省
#3275 青海

place = {}
#读取区域表中的区域编码和区域名称
readStar = 2953
readEnd = 3037
writeStar = 201
writeEnd = 243
valueQ = ''
keyQ = ''
time1 = time.time()
print('开始')

while readStar < readEnd:
    keyQ = sheet2['C'+str(readStar)].value
    valueQ = sheet2['D'+str(readStar)].value
    placeAll = [keyQ,valueQ]
    if re.compile('地区').search(valueQ)!=None:
        valueQ = valueQ[0:-2]
    elif re.compile('自治区').search(valueQ)!=None:
        valueQ = valueQ[0:-3]
    else:
        valueQ = valueQ[0:-1]
    place[valueQ] = placeAll
    readStar = readStar+1
    
log.write('读取完毕\n')

print('准备写入')

 
while writeStar<(writeEnd+1):
    for v,k in place.items():
        if re.compile(str(v)).search(sheet1['F'+str(writeStar)].value)!=None:
            sheet1['J'+str(writeStar)] = str(k[0])
            log.write('J'+str(writeStar)+' 成功插入: '+str(k[0])+'\n')
            sheet1['K'+str(writeStar)] = str(k[1])
            log.write('K'+str(writeStar)+' 成功插入: '+str(k[1])+'\n')  
    writeStar = writeStar+1

wb.save('E:\\工作\\材料整理\\test2.xlsx')#保存     
log.close()
time1 -= time.time()
print('结束'+str(-time1))