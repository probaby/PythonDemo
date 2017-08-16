import openpyxl
import re
import time


wb = openpyxl.load_workbook('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\demo1.xlsx')
log = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\log.txt','w')
sheet1 = wb.get_sheet_by_name('项目域')

'''得到包含信息的字典'''
def getInfo(list):
    place = {}
    readStar = list[1]
    readEnd = list[2]
    sheet2 = wb.get_sheet_by_name(str(list[0]))
    log.write('开始读取:'+str(list[0])+'\n')
    while readStar < readEnd:
        keyQ = sheet2['A'+str(readStar)].value
        valueQ = sheet2['C'+str(readStar)].value
        place[valueQ] = keyQ
        readStar = readStar+1
    place['star'] = sheet2['D2'].value
    log.write('读取完毕\n')
    return place



'''通过place写入'''
def writeInfo(place,list):
    writeStar = list[3]
    writeEnd = list[4]
    log.write('开始写入:'+str(list[0])+'\n')

    while writeStar<writeEnd:
        b = False
        # sheet1['D'+str(writeStar)].value in place.keys()
        for k,v in place.items():
            if (re.compile(str(sheet1['D'+str(writeStar)].value)).search(str(k))!=None or re.compile(str(k)).search(str(sheet1['D'+str(writeStar)].value))!=None) :
                sheet1['C'+str(writeStar)] = str(str(place['star'])+'的'+v)
            else:
                b=True
        if b :
            log.write(list[0]+' 在  '+str(place['star'])+' 未找到：'+str(sheet1['D'+str(writeStar)].value)+'\n')
        else:
            log.write('C'+str(writeStar)+' 成功插入: '+str(place['star'])+' 的 '+str(v)+'\n')
        writeStar = writeStar+1
    log.write('\n')






#分别为sheet名字开始和结束的行号
kuoJian110 = ['110扩建',2,48,138,179]
kuoJian35 = ['35扩建',2,43,242,278]
bianGai110 = ['110变电站改造',2,41,179,211]
bianGai35 = ['35变电站改造',2,36,278,304]
xianGai110 = ['110线路改造',2,43,211,242]
xianGai35 = ['35线路改造',2,38,304,329]
xinJian = ['8电网新建工程',2,40,329,390]
gaiZao = ['9电网改造',2,45,390,441]

allList = [kuoJian110,kuoJian35,bianGai110,bianGai35,xianGai110,xianGai35,xinJian,gaiZao]

#J C区域编码
#K D区域名称
#F 单位名称
#3164 甘肃省
#3275 青海
time1 = time.time()

print('开始')
for k in range(8):
    writeInfo(getInfo(allList[k]),allList[k])
print('写入完成'+str(time.time()-time1))

wb.save('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\demo'+str(3)+'.xlsx')#保存     
log.close()
print('结束'+str(time.time()-time1))