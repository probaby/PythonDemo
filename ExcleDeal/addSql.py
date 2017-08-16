import openpyxl
import re


wb = openpyxl.load_workbook('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\副本实体表_1.4.xlsx')
log = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\log.txt','w')
projectSql = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\projectSql.sql','w+')
energySql = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\energySql.sql','w+')
deleteSql = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\deleteSql.sql','w+')
repeatLog = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\repeat.log','w+')
sheetXiangMuYu = wb.get_sheet_by_name('项目域')
sheetNengYuan = wb.get_sheet_by_name('能源域')
sheetShiti = wb.get_sheet_by_name('实体清单')


def readShiTi(star,end):
    log.write('开始读取实体表\n')
    columsName = ''
    entry = {}
    while star<end:
        if sheetShiti['B'+str(star)].value!= None:
            columsName = sheetShiti['B'+str(star)].value[:sheetShiti['B'+str(star)].value.index('(')].replace('\n','').strip()
        name =  columsName+sheetShiti['D'+str(star)].value
        entry[name] = sheetShiti['E'+str(star)].value
        entry[name+'annotation'] = sheetShiti['H'+str(star)].value
        #log.write('readShiTi的行号: '+str(star)+'\n')
        star += 1
    log.write('读取实体表成功\n')
    return entry

def writeSql(sheet,entry,sql):
    #总共建表张数
    numTable = 0
    lineNum = 3
    tableName = ''
    b = False
    sqlContent = ''
    annotationContent = ''
    
    log.write('开始读取'+str(sheet)+'\n')
    while sheet['D'+str(lineNum)].value != None:
        aName = ''
        if sheet['A'+str(lineNum)].value != None:
            aName = sheet['A'+str(lineNum)].value
        #当B不为空时为合并行的第一行
        if sheet['B'+str(lineNum)].value != None:
            b = True

            #查表名
            for k,v in entry.items():
                if 'annotation' in k:
                    continue
                rngx = aName+sheet['B'+str(lineNum)].value+'|'+aName+sheet['B'+str(lineNum)].value[:-1]
                if re.compile('情况').search(sheet['B'+str(lineNum)].value) !=None :
                    rngx += '|'+aName+sheet['B'+str(lineNum)].value[:-3]
                if re.compile(rngx).search(k) != None :
                    tableName = v
                    log.write("开始创建表 :" + tableName+'\n')
                    sqlContent = 'create table ' + tableName+' (\n'
                    annotationContent = 'COMMENT ON TABLE ' + tableName +' IS \'' + k +'、'+entry[k+'annotation']+'\';\n'
                    numTable += 1
        
        sqlContent += '\t'+sheet['E'+str(lineNum)].value.strip()
        sqlContent += ' '+sheet['F'+str(lineNum)].value.strip().replace('（','(').replace('）',')')
        if sheet['G'+str(lineNum)].value != None and ('Y' in sheet['G'+str(lineNum)].value) and b:
            sqlContent += ' PRIMARY KEY'
            b = False
        sqlContent += ',\n'
        
        annotationContent += 'COMMENT ON COLUMN ' +  tableName+'.'+ sheet['E'+str(lineNum)].value.strip()
        annotationContent += ' IS \'' + sheet['D'+str(lineNum)].value
        if sheet['J'+str(lineNum)].value != None:
            annotationContent += '、'+sheet['J'+str(lineNum)].value.replace("\n", "")
        annotationContent += '\';\n'
        #log.write('writeSql的行号 '+str(lineNum))
        lineNum += 1
        
        #此时一张表完，把sql写入sql.txt
        if sqlContent != '' and (sheet['B'+str(lineNum)].value != None or sheet['D'+str(lineNum)].value == None):
            sqlContent = sqlContent[:-2]+');\n'
            sql.write('/*创建表'+tableName+'*/'+'\n')
            sql.write(sqlContent+'\n')
            sql.write(annotationContent+'\n')
            deleteSql.write('drop table '+tableName+';\n')
    
    log.write('建表数**'+str(numTable))
        
#检查每张表中的重复字段
def checkRepeat(sheet):
    Repeat = True
    lineNum = 3
    #记录每张表的每个字段，查看是否重复，并输出 
    columsContents = {}   
    while sheet['D'+str(lineNum)].value != None:
        addColumn = False
        #当B不为空时为合并行的第一行
        if sheet['B'+str(lineNum)].value != None:
            columsContents = {}
            columsContents['star'] = sheet['B'+str(lineNum)].value
        for k,v in columsContents.items():
            if  sheet['E'+str(lineNum)].value.replace('\n','').strip() ==  k.replace('\n','').strip():
                repeatLog.write(columsContents['star'].replace('\n','')+' ： \t'+sheet['E'+str(lineNum)].value)
                repeatLog.write('\n' + v +'\t' +sheet['D'+str(lineNum)].value+'\n\n')
                Repeat = False
                break
            else:
                addColumn = True
        if addColumn :
            columsContents[sheet['E'+str(lineNum)].value] = sheet['D'+str(lineNum)].value
        #log.write('checkRepeat: '+str(lineNum))
        lineNum += 1
    return Repeat
            
            
# readShiTi(83,129)
                
# writeSql(sheetXiangMuYu,readShiTi())
# 能源域 73 83 项目域结束83 ， 129
print('开始')
if checkRepeat(sheetXiangMuYu) and checkRepeat(sheetNengYuan) :
    writeSql(sheetXiangMuYu,readShiTi(83,129),projectSql)
    deleteSql.write('/*能源域删除表*/\n')
    writeSql(sheetNengYuan,readShiTi(73,83),energySql)
    print('结束')
else:
    print('执行失败')

           




