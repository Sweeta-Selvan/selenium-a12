'''
xlrd    :   To read excel files, we use xlrd

TO install xlrd
    Go to command prompt -->    pip install xlrd==1.2.0


    STEP1   :   import xlrd
    STEP2   :   Open the excel file
                workbook = xlrd.open_workbook("path_of_excel_file")             ## Book object
    STEP3   :   Open the worksheet
                worksheet = workbook.sheet_by_name("SheetName")                 ## Sheet object
    STEP4   :   Convert the sheet object to the generator object
                rows = worksheet.get_rows()                                     ## generator object
    STEP5   :   Traversing on the generator object and fetch the data


'''

import xlrd

path = r'C:\Users\Ramya\PycharmProjects\Sel-A12-June16-2025\files\candidate_info.xlsx'

## open the excel file
workbook = xlrd.open_workbook(path)
# print(workbook)         ## Book object

## open the worksheet
worksheet = workbook.sheet_by_name('data')
# print(worksheet)        ## Sheet object

## Convert sheet object to the generator object
rows = worksheet.get_rows()
# print(rows)             ## generator object

##-------------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele)
#
# ## [text:'name', text:'place', text:'phone_num']
# ## [text:'Gayathri', text:'Mysore', number:8976541230.0]
# ## [text:'Someshwar', text:'Hyderabad', number:7896541236.0]
# ## [text:'Keerthan', text:'Chennai', number:9874563214.0]
# ## [text:'Pooja', text:'Delhi', number:9865320147.0]


##-------------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0], ele[1], ele[2])
#
# ## text:'name' text:'place' text:'phone_num'
# ## text:'Gayathri' text:'Mysore' number:8976541230.0
# ## text:'Someshwar' text:'Hyderabad' number:7896541236.0
# ## text:'Keerthan' text:'Chennai' number:9874563214.0
# ## text:'Pooja' text:'Delhi' number:9865320147.0

##-------------------------------------------------------------------------------------------
# for ele in rows:
#     print(ele[0].value, ele[1].value, ele[2].value)
#
# ## name place phone_num
# ## Gayathri Mysore 8976541230.0
# ## Someshwar Hyderabad 7896541236.0
# ## Keerthan Chennai 9874563214.0
# ## Pooja Delhi 9865320147.0


##-------------------------------------------------------------------------------------------

d = {}

for ele in rows:
    d[ele[0].value]= (ele[1].value, ele[2].value)

print(d)







































