from pandas import DataFrame
import xlsxwriter

def export_date_excel(request):
    
  header = [ 'A', 'B', 'C' ]
  dataF = DataFrame(detail_list, columns=header)
  filename = 'excel_.xlsx'
  dataF.to_excel(filename, 'Sheet1', index=False, engine='xlsxwriter')

# pip install pandas
# pip install XlsxWriter
# 출처: https://wangin9.tistory.com/entry/python-csv-excel-export-much-faster [잉구블로그]
