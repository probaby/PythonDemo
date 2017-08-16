import openpyxl
import re

roll = ['A','B','C','D','E','F','G','H','I','J','K','L']

wb = openpyxl.load_workbook('E:\\工作\\材料整理\\read.xlsx')
log = open('E:\\工作\\材料整理\\log.txt','w')
sheet1 = wb.get_sheet_by_name('Sheet1')
sheet2 = wb.get_sheet_by_name('区域表')

#J C区域编码
#K D区域名称
#F 单位名称
#3164 甘肃省
#3275 青海
#积石山保安族东乡族撒拉族自治县 阿克塞哈萨克族自治县 肃北蒙古族自治县
special = ['积石山保安族东乡族撒拉族自治县','阿克塞哈萨克族自治县','肃北蒙古族自治县','东乡族自治县','肃南裕固族自治县']
place = {}
#读取区域表中的区域编码和区域名称
lineQuyu = 3164
valueQ = ''
keyQ = ''
print('开始')
style1 = re.compile('自治')
while lineQuyu < 3275:
    keyQ = sheet2['C'+str(lineQuyu)].value
    valueQ = sheet2['D'+str(lineQuyu)].value
    placeAll = [keyQ,valueQ]
    if valueQ in special[0]:
        valueQ = '积石山'
    elif valueQ in special[1]:
        valueQ = '阿克塞'
    elif valueQ in special[2]:
        valueQ = '肃北'
    elif valueQ in special[3]:
        valueQ = '东乡'
    elif valueQ in special[4]:
        valueQ = '肃南'
    elif style1.search(valueQ)!=None:
        valueQ = valueQ[0:-5]
    else:
        valueQ = valueQ[0:-1]
    place[valueQ] = placeAll
    lineQuyu = lineQuyu+1
log.write('读取完毕\n')
log.write('\n')
print('准备写入')
i = 3 
while i<201 :
    for v,k in place.items():
        if re.compile(str(v)).search(sheet1['F'+str(i)].value)!=None:
            sheet1['J'+str(i)] = str(k[0])
            log.write('J'+str(i)+' 成功插入: '+str(k[0])+'\n')
            sheet1['K'+str(i)] = str(k[1])
            log.write('K'+str(i)+' 成功插入: '+str(k[1])+'\n')  
    i = i+1

wb.save('E:\\工作\\材料整理\\test.xlsx')#保存     
log.close()
print('结束')