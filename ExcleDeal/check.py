import openpyxl
from openpyxl.styles import Color, Font, Alignment  
from openpyxl.styles.colors import BLUE, RED, GREEN, YELLOW 


file = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\新建文本文档.txt')
log = open('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\新建文本文档log.txt','w+')


wb = openpyxl.load_workbook('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\副本实体表_1.4.xlsx')

sheet1 = wb.get_sheet_by_name('项目域')
sheetNengyuan = wb.get_sheet_by_name('能源域')
name = '首页_点击地区_点击项目列表_下拉箭头'

def checkSheet(sheet):
    num = 0
    num2 = 0
    star = 3
    while sheet['D'+str(star)].value != None:
        log.write(str(star)+'\n')
        line = file.readline()
        while line:
            log.write(line+' : '+ sheet['D'+str(star)].value.replace('\n','').strip())
            if sheet['D'+str(star)].value.replace('\n','').strip() in line and (sheet['D'+str(star)].value.replace('\n','').strip() not in '项目编码'):
                num2 += 1
                if sheet['C'+str(star)].value == None:
                    num += 1
                    cell = sheet.cell('C'+str(star))  
                    sheet['C'+str(star)] = name
                    cell.font = Font(name=u'宋体', size=10, color=BLUE, bold=False)  
                    cell.alignment = Alignment(horizontal='center', vertical='center')  
                    #sheet.cellstyle('C'+str(star), font, align)
                    print(str(star)+' : ' + line+'\n')
            line = file.readline()
        file.seek(0) 
        star += 1
    print('共找到：'+str(num2)+'\n')
    print('之前找到的 ：'+str(num2-num)+'\n')
    print('共写入：'+str(num)+'\n')


checkSheet(sheet1)
wb.save('E:\\工作\\pis2.0\\项目域_能源域\\实体表\\实体表_5.xlsx')#保存
