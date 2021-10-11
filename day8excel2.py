import xlwt
from sql_ff import select
wb = xlwt.Workbook()
st = wb.add_sheet("t_dept")

sql = "select * from clothes "
param = []
f = select(sql,param)
for i in range(0,len(f)):
    for j in range(0,len(f[0])):
        st.write(i,j,f[i][j])

wb.save("三国集团.xls")







