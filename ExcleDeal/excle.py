import openpyxl

file = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\查找基础数据.txt')
log = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\新建文本文档log.txt','w+')


wb = openpyxl.load_workbook('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\实体表_5.xlsx')

sheet1 = wb.get_sheet_by_name('能源域')
name = ''
numAll = 0
snum = 0;
x = set()
def check():
    global numAll
    global snum
    star = 3
    while sheet1['D'+str(star)].value!=None and sheet1['D'+str(star)].value not in '年月':
        valueCell = sheet1['D'+str(star)].value
        line = file.readline()
        snum = 0
        while line and line not in '':
            snum+=1
            k = len(x)
            x.add(line)
            if (k+1) !=len(x) and star==3:
                print('炸裂 ： '+line)
            if '#' in line:
                name = line.replace('#','')
            if line.replace('\n','').strip() in valueCell.replace('\n','').strip() or valueCell.replace('\n','').strip() in line.replace('\n','').strip() and sheet1['C'+str(star)].value==None:
                #print(name + ' : ' + str(star)+' : '+valueCell+' line '+ line)
                print(str(star)+' : '+line.replace('\n','')+' ： '+ valueCell.replace('\n','')+' : '+name)
                sheet1['C'+str(star)] = name
                numAll += 1
            line = file.readline()

        file.seek(0)
        star = star+1
    print(str(numAll))  
    print('txt共'+'snum'+str(snum))
    
      
check()
#wb.save('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\实体表_6.xlsx')