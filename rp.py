from bs4 import BeautifulSoup

import re
import requests

regex = re.compile('[\t|\n|\r]')

url = 'http://www.compuzone.co.kr/product/product_list.htm? \
		actype=&listv=&BigDivNo=4&MediumDivNo=1014&DivNo=2036& \
		PreOrder=&ps_po=P&firstOpen=1&PageCount=100&StartNum=0& \
		PageNum=1&lvm=&splist_stm=hide&SelectProductNo=&orderlayerx=& \
		orderlayery=&splist_kw=%B0%CB%BB%F6%BE%EE%C0%D4%B7%C2& \
		splist_sbno%5B%5D=18088&splist_sbno%5B%5D=20841&splist_sbno%5B%5D=18087& \
		splist_sbno%5B%5D=14245&splist_sbno%5B%5D=1421#ProductList'


bs = BeautifulSoup(requests.get(url).content, 'html.parser')

''' 
for i in bs.find_all('ul', {'class' : 'product_list'}) :
	a = i.find_all('div', {'class' : 'prd_name'})
	b = i.find_all('dl', {'class' : 'prd_price'})
	for i in range(len(a)):
		print(regex.sub('', a[i].text), b[i].dd.text)
	#print(prd_name, )
'''

for i in bs.find_all('ul', {'class' : 'product_list'}) :
	for j in i.find_all('li') :
		print(j.select('div'))
		name = regex.sub('', j.select('div')[6].text)

		print(name)
