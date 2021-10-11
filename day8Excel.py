import xlrd
wb = xlrd.open_workbook(filename=r"D:\数据库\day09【xlrd的excel表的读写】\2020年每个月的销售情况.xlsx",encoding_override=True)
yue = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
yifu = ["羽绒服","T血","衬衫","风衣","牛仔裤","皮衣","皮草","小西装","棉衣","卫衣","铅笔裤"]
jidu = [["1月","2月","12月"],["3月","4月","5月"],["6月","7月","8月"],["9月","10月","11月"]]

'''
#全年销售总额
sum = 0
for o in yue:
    sheet = wb.sheet_by_name(o)
    rows = sheet.nrows#获取多少行
    cols = sheet.ncols#获取多少列
    for i in range(1,rows):
        data2=sheet.row_values(i)
        sum = sum + data2[4] * data2[2]
print("工资总和",int(sum))
'''

'''
#各种销售量占比
sum1 = 0
sum2 = 0
for k in yifu:
    for i in yue:
        sheet = wb.sheet_by_name(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]
            if data[1] == k:
                sum2 = sum2 + data[4]
    print(k,"销量占比",sum2/sum1*100,"%")
print("销量总和",int(sum1))
'''

'''
#每件衣服月销售额占比
yue1 = str(input("输入你要的月份各销售占比"))
sum1 = 0
sum2 = 0
for k in yifu:
    sheet = wb.sheet_by_name(yue1)
    rows = sheet.nrows#获取多少行
    cols = sheet.ncols#获取多少列
    for j in range(1,rows):
        data=sheet.row_values(j)
        sum1 = sum1 + data[4]*data[2]
        if data[1] == k:
            sum2 = sum2 + data[4]*data[2]
    print(k,"销售额占比",sum2/sum1*100,"%")
print("销售额和",int(sum1))
'''

'''
#各种销售额占比
sum1 = 0
sum2 = 0
for k in yifu:
    for i in yue:
        sheet = wb.sheet_by_name(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]*data[2]
            if data[1] == k:
                sum2 = sum2 + data[4]*data[2]
    print(k,"销售额占比",sum2/sum1*100,"%")
print("销售额总和",int(sum1))
'''

'''
sum1 = 0
sum2 = 0
list1={}
for k in yifu:
    for i in yue:
        sheet = wb.sheet_by_name(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]
            if data[1] == k:
                sum2 = sum2 + data[4]
    list1[k]=sum2
print(list1)
i = max(list1, key=lambda x:list1[x])
o = min(list1, key=lambda x:list1[x])
print("最畅销的",i,"最不畅销的",o)
'''

sum1 = 0
sum2 = 0
list1={}
print("0.冬季 1.春季 2.夏季 3.秋季")
s = int(input("请输入你想知道的季度的序号"))
for k in yifu:
    for i in jidu[s]:
        sheet = wb.sheet_by_name(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data=sheet.row_values(j)
            sum1 = sum1 + data[4]
            if data[1] == k:
                sum2 = sum2 + data[4]
    list1[k]=sum2
i = max(list1, key=lambda x:list1[x])
o = min(list1, key=lambda x:list1[x])
print("最畅销的",i,"最不畅销的",o)