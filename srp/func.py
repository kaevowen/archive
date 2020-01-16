#-*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup
from datetime import date
from time import strftime, strptime
import re

date_regex = re.compile(r"(\w{3} \d{2}, \d{4})")
date_regex2 = re.compile(r"(\d{4}-\d{2}-\d{2})")
kill_regex = re.compile(r"(/kill/\d*/)")
price_regex = re.compile(r"[\d.]*")

def name() : 
	names = input("name : ")
	findcharname = "https://api.eveonline.com/eve/CharacterID.xml.aspx?names={}".format(names)
	charid = BeautifulSoup(get(findcharname).content, "lxml")
	charid = charid.row['characterid']

	if charid <= '0' :
		print("잘못되거나 없는 캐릭터 이름 입니다.")
		return name()
	else : 
		return charid

def target_date() :
	inp = input("date (YYYY-MM-DD) : ")
	today = strftime("%Y-%m-%d",date.today().timetuple())

	if date_regex2.search(inp) == None:
		print("형식이 다릅니다.")
		return target_date()

	elif(inp[-2:] > "31" or inp[5:-3] > "12" or inp[-2:] < "0" or inp[5:-3] < "0"
		):	
			print("날짜가 아닌 것 같습니다.")
			return target_date()

	elif today < inp :
		print("지정일은 오늘보다 클 수 없습니다.")
		return target_date()

	else :
		return inp

def srp_calc(charid, target_date) :
	txt = open("srplist.txt", "w")
	total = 0
	page = 0

	while True :
		page += 1
		site = "https://zkillboard.com/character/{}/losses/page/{}/".format(charid, page)
		site = get(site).content

		bs = BeautifulSoup(site, "html.parser")
		km = bs.find('table', {"class" : "table table-condensed table-striped table-hover"})

		for i in km.tbody:
			try :
				if bool(date_regex.search(i.text)) :
					date_conv = (strftime("%Y-%m-%d" ,
						strptime(date_regex.findall(i.text)[0], "%b %d, %Y")))
					if date_conv < target_date :
						break
					else :
						print("{}".format(date_conv))

				elif (
					bool(kill_regex.search(i.a['href'])) and 
					i.find_all('a')[1].text != "10.00k" and
					float(i.span.text) < 0.5
				) :
					link = "zkillboard.com{}".format(kill_regex.findall(i.a['href'])[0])
					price = i.find_all('a')[1].text

					# m = 1,000,000 / b = 100,000,000
					if price[-1] == 'm' :
						price = float((price_regex.findall(i.find_all('a')[1].text)[0])) * 1000000
						if price >= 800000000 :
							print("{} ".format(link) + "{:>12,.0f}".format(price))
							price = 800000000
							data = ("{} ".format(link) + "{:>12,.0f}\n".format(price))

						else :
							print("{} ".format(link) + "{:>12,.0f}".format(price))
							data = ("{} ".format(link) + "{:>12,.0f}\n".format(price))
						total += price
						txt.write(data)

					elif price[-1] == 'b' :
						price = 800000000
						print("{} ".format(link) + "{:>12,.0f}".format(price))
						data = ("{} ".format(link) + "{:>12,.0f}\n".format(price))					
						total += price
						txt.write(data)

			except AttributeError :
				pass

		if date_conv < target_date :
			break

	print("\n\ntotal : {:0,.0f}".format(total))
	data = "\n\ntotal : {:0,.0f}\n{}".format(total, date_conv)
	txt.write(data)
	txt.close()