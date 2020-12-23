import xlrd
import xlwt
#提取指定excel某一列
def get_one_col_list(xlsx,sheet,col,raw_s,raw_e):
    workbook = xlrd.open_workbook(xlsx)
    sheet = workbook.sheet_by_index(sheet)
    colum = sheet.col(col, start_rowx=raw_s, end_rowx=raw_e)
    value = []
    for colum_index in colum:
        value.append(colum_index.value)
    return value

#把一个list写入指定excel某一列
def write_one_col_to_excel(result,sheet,colum,list,raw_s):
    #tempworkbook = xlrd.open_workbook(result,formatting_info=True)
    tempworkbook = xlrd.open_workbook(result)
    from xlutils.copy import copy
    workbook = copy(tempworkbook)
    worksheet = workbook.get_sheet(sheet)
    for temp in list:
        worksheet.write(raw_s,colum,temp)
        raw_s = raw_s + 1
    workbook.save(result)

xlsx = xlrd.open_workbook('即时库存12.22.xls')
table = xlsx.sheet_by_index(3)

code_inventory = get_one_col_list('即时库存12.22.xls',3,0,1,None)
amount_inventory = get_one_col_list('即时库存12.22.xls',3,17,1,None)
code_need = get_one_col_list('需求.xlsx',1,1,2,None)
amount_need = get_one_col_list('需求.xlsx',1,11,2,None)
#提取出需求表中的物料编码一列，与即时库存表中的物料编码列匹配。如匹配到，取库存数列的同一行。如果未匹配到.....
#暂时把匹配不到的删掉了
amount_inventory_t = []
gap = []
for code in code_need:
    amount_inventory_t.append(amount_inventory[code_inventory.index(code)])
    gap.append(amount_inventory[code_inventory.index(code)] - amount_need[code_need.index(code)])

write_one_col_to_excel('需求.xlsx',1,12,amount_inventory_t,2)
write_one_col_to_excel('需求.xlsx',1,13,gap,2)
