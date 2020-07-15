import pandas as pd

outpath='/Users/igortitov/mod_b/metro_nielsen/ready/'

print('начали читать файл с отчетом')
df1 = pd.read_excel(io='/Users/igortitov/mod_b/metro_nielsen/incomming/Total Mixed Chains ST.xlsx', header=0, dtype='str')
print('прочитали файл с отчетом')

print('начали читать базу шк')
df2 = pd.read_excel(io='/Users/igortitov/mod_b/metro_nielsen/base/FNF_base.xlsx', header=0, dtype='str')
print('прочитали базу шк')
print('начали мерджить строки')
df3 = df1.merge(df2,left_on='EAN',right_on='sell_ean_no',how='left')
# df3.to_csv(outpath+'merged.csv')
# df3=pd.read_csv(outpath+'merged.csv')
print('смерджили строки')

num_cols=['MAT LY','MAT TY','Jun 2019','Jul 2019','Aug 2019','Sep 2019','Oct 2019','Nov 2019','Dec 2019','Jan 2020','Feb 2020','Mar 2020','Apr 2020','May 2020']
int_cols=['sell_ean_no', 'art_no', 'subsys_art_no', 'group_art','EAN']

for col in num_cols+int_cols:
    print('начинаем менять формат num',col)
    try:
        df3[col]=pd.to_numeric(df3[col])
    except:
        print(col, 'cant cast to num!!!')
        exit()
print(df3.info())
for col in int_cols:
    print('начинаем менять формат инт',col)
    try:
        df3[col] = df3[col].astype('Int64')
    except:
        print(col, 'cant cast to int!!!')
print(df3.info())

def dedouble(df3):
    dedouble_list = ['PRODUCT NAME','MAT LY','MAT TY','Jun 2019','Jul 2019','Aug 2019','Sep 2019','Oct 2019','Nov 2019','Dec 2019','Jan 2020','Feb 2020','Mar 2020','Apr 2020','May 2020']
    rsize=df3.shape[0]
    print('дедуплицируем по', str(dedouble_list)[1:-1],'до дедупликации было:',rsize)
    df3_dedoubled = df3.drop_duplicates(subset=dedouble_list, keep='first')
    print('закончили дедупликацию, стало:',df3_dedoubled.shape[0])
    print('в отчете должно быть:',df1.shape[0])
    return df3_dedoubled

ready = dedouble(df3)

def write(dflist):
    print('\n   начало функции write')
    # , options={'strings_to_urls': False}
    writer = pd.ExcelWriter(outpath+'_Report.xlsx', engine='xlsxwriter')
    for df in dflist:
        s_name='1'
        print('     начинаем запись в ексель',s_name)
        df.to_excel(writer, sheet_name=s_name, na_rep='', index=False)
        worksheet = writer.sheets[s_name]
        print(worksheet.get_name())
    

        cl_data_format_num = writer.book.add_format({'num_format': '0.0'})
        cl_data_format_int = writer.book.add_format({'num_format': '0'})
        FORMATS = ['MAT LY','MAT TY','Jun 2019','Jul 2019','Aug 2019','Sep 2019','Oct 2019','Nov 2019','Dec 2019','Jan 2020','Feb 2020','Mar 2020','Apr 2020','May 2020']
        FORMATS_ = ['sell_ean_no', 'art_no', 'subsys_art_no', 'group_art','EAN']
        ALL_FORMATS=FORMATS+FORMATS_
        for j, header in enumerate(df):
            print(j,header)
            if header not in ALL_FORMATS:
                continue

            for i, value in enumerate(df[header]):
                if header in FORMATS:
                    if pd.notna(value):
                        try:
                            worksheet.write_number(i+1, j, value, cl_data_format_num)
                        except:
                            print('WRITING NOT A NUMBER',header,value)
                            worksheet.write_string(i+1, j, value)
                    else:
                        continue
                elif header in FORMATS_:
                    if pd.notna(value):
                        try:
                            worksheet.write_number(i+1, j, value, cl_data_format_int)
                        except:
                            print('WRITING NOT A NUMBER',header,value)
                            worksheet.write_string(i+1, j, value)
                    else:
                        continue
    writer.save()

write([ready])

print('готово')