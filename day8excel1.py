import pymysql
import xlrd
from sql_ff import select
from sql_ff import update
yue = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
wb = xlrd.open_workbook(filename=r"D:\数据库\day09【xlrd的excel表的读写】\2020年每个月的销售情况.xlsx",encoding_override=True)
for o in yue:
    sheet = wb.sheet_by_name("1月")
    rows = sheet.nrows#获取多少行
    cols = sheet.ncols#获取多少列
    print(rows,"行",cols,"列")
    for i in range(0,rows):
        data = sheet.row_values(i)
        print(data)
        sql3 = "insert into clothes values(%s,%s,%s,%s,%s)"
        param3 = [data[0],data[1],data[2], data[3],data[4]]
        update(sql3, param3)








