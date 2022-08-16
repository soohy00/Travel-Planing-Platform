#https://korean.visitkorea.or.kr/list/ms_list.do?areacode=1
import requests
import os
from bs4 import BeautifulSoup
import re

url = 'https://korean.visitkorea.or.kr/list/ms_list.do?areacode=1'
res = requests.get("http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=035720")

if res.status_code != 200:
    print("접속 코드가 200이 아닙니다 확인해주시기 바랍니다")
    exit()

soup = BeautifulSoup(res.text, 'html.parser')

print(res.text)
