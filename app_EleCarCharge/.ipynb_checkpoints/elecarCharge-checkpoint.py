import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def save_excel(df):
    excel = pd.ExcelWriter('data/elecarCharge.xlsx')
    df.to_excel(excel, '.', index=False)
    excel.save()

api_key = 'ncNjy6RQJMeD8HlGJpo15iXufyCLgziGOcg0PtE8xCwEiMO0topNrA0fx%2Bptpf3%2Ba%2FZ4%2Bsxtf%2FtbVces7FiIBw%3D%3D'
df = pd.DataFrame({'충전소명': [], '충전소ID': [], '충전기ID': [], '충전기터입': [], '주소': [], '위도': [], '경도': [],
                   '이용가능시간': [], '기관ID': [], '기관명': [], '기관연락처': [], '충전기상태': [], '갱신일시': [], '충전량': []})
temp_list = []

for page_n in range(1,3):
    url = 'http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?serviceKey=' \
          + api_key + '&pageSize=' + str(120000) +'&pageNo=' + str(page_n)

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find_all('item')

    for item in data:
        temp_list.append(pd.DataFrame({'충전소명':[item.find('statnm').text], '충전소ID':[item.find('statid').text],
                                       '충전기ID':[item.find('chgerid').text], '충전기터입':[item.find('chgertype').text],
                                       '주소':[item.find('addr').text], '위도':[item.find('lat').text],
                                       '경도':[item.find('lng').text], '이용가능시간':[item.find('usetime').text],
                                       '기관ID':[item.find('busiid').text], '기관명':[item.find('businm').text],
                                       '기관연락처':[item.find('busicall').text], '충전기상태':[item.find('stat').text],
                                       '갱신일시':[item.find('statupddt').text], '충전량':[item.find('powertype').text]}))

df = pd.concat(temp_list)
df.reset_index(drop=True, inplace=True)

print(df)
save_excel(df)

df_check = pd.read_excel('data/elecarCharge.xlsx')
print(df_check)