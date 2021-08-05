#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import re
import json
from multiprocessing.dummy import Pool as asshole

# color area
r = '\x1b[31m'
g = '\x1b[32m'
y = '\x1b[33m'
b = '\x1b[34m'
m = '\x1b[35m'
c = '\x1b[36m'
w = '\x1b[37m'

# clear func
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][(os.name == 'nt')])

# database for number
database = []

#global middle number 
babe = []

# middle code genarator
def midman():
	global babe
	for x in range(10):
		if x == 1 or x == 0:
			pass
		else:
			for x2 in range(10):
				for x3 in range(10):
					babe.append(str(x)+str(x2)+str(x3))

# grab number from adresses.com
def addresses(username):
	global database
	baifost = requests.Session()
	username = username.replace("\n","").replace("\r","").replace(" ","+")
	headers = {
	"Host": "www.addresses.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
	"Upgrade-Insecure-Requests": "1",
	"Sec-Fetch-Dest": "document",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-Site": "none",
	"Sec-Fetch-User": "?1",
	"Connection": "keep-alive"}
	for num in range(50):
		page = "p"+str(num)
		api = "https://www.addresses.com/people/"+username+"/"+page
		response = baifost.post(api, headers=headers).content
		#error key
		if "This page may have been moved or doesn't exist." in response or "Oops! 404 Page Not Found Error" in response:
			break
		else:
			#you can change this regex + code if you want
			junk = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",response)
			if len(junk) == 0:
				pass
			else:
				for junknum in junk:
					if "(" in junknum:
						gotnumber = "+"+junknum.replace("(","").replace(")","").replace("\r","").replace(" ","").replace("-","")
						if gotnumber not in database:
							database.append(gotnumber)
							# you can change num output style if you want
							print y + "[x.x] Number Found : " + w + gotnumber + y + " [owner] : "+ w + username
							open('grabnum.txt','a').write(gotnumber+'\n')
						else:
							pass
					else:
						pass


def preadresses():
	clear()
	userlist = open(raw_input(g + 'Username list : ' + w),'r').readlines()
	th = raw_input(g + 'Threads : ' + w)
	pool = asshole(int(th))
	pool.map(addresses,userlist)
	pool.close()
	pool.join()

# grab number from 411.com
def fouroneone(midnum):
	midnum = midnum.replace('\n','').replace('\r','')
	baifost = requests.Session()
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
	res = baifost.get("https://www.411.com/",headers=headers)
	cookies = res.cookies
	for xs in range(10):
		for xs2 in range(10):
			lnum = str(xs)+str(xs2)
			api = "https://www.411.com/phone/1-"+acode+"-"+str(midnum)+"-"+str(lnum)+"XX"
			response = baifost.post(api,headers=headers,verify=False,cookies=cookies).content
			if '<h1 class="display-3 mb-5">Sorry!</h1>' in response:
				pass
			else:
				getnum = re.findall(r"itemsData:(.*),pageType:",response)[0]
				junk = json.loads(getnum)
				for num in junk:
					sp = '1-'+acode
					try:
						fcode = num.split(sp)[1]
						fcode = fcode.replace('-','')
						lfnum = '+1'+acode+fcode
						# you can change num output style if you want
						print y + "[x.x] Number Found : " + w + lfnum + y + " [AreaCode] : "+ w + acode
						open('grabnum.txt','a').write(lfnum+'\n')
					except:
						break

	

def prefouroneone():
	midman()
	global acode
	acode = raw_input(g + 'Area code : ' + w)
	if len(acode) == 3:
		th = raw_input(g + 'Threads : ' + w)
		pool = asshole(int(th))
		pool.map(fouroneone,babe)
		pool.close()
		pool.join()
	else:
		prefouroneone()

# grab number from whitepages.com
def whitepages(midnum):
	midnum = midnum.replace('\n','').replace('\r','')
	baifost = requests.Session()
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
	res = baifost.get("https://www.whitepages.com/",headers=headers)
	cookies = res.cookies
	for xs in range(10):
		for xs2 in range(10):
			lnum = str(xs)+str(xs2)
			api = "https://www.whitepages.com/phone/1-"+acode+"-"+str(midnum)+"-"+str(lnum)+"XX"
			response = baifost.post(api,headers=headers,verify=False,cookies=cookies).content
			if '<h1 class="display-3 mb-5">Sorry!</h1>' in response:
				pass
			else:
				getnum = re.findall(r"itemsData:(.*),pageType:",response)[0]
				junk = json.loads(getnum)
				for num in junk:
					sp = '1-'+acode
					try:
						fcode = num.split(sp)[1]
						fcode = fcode.replace('-','')
						lfnum = '+1'+acode+fcode
						# you can change num output style if you want
						print y + "[x.x] Number Found : " + w + lfnum + y + " [AreaCode] : "+ w + acode
						open('grabnum.txt','a').write(lfnum+'\n')
					except:
						break

	

def prewhitepages():
	midman()
	global acode
	acode = raw_input(g + 'Area code : ' + w)
	if len(acode) == 3:
		th = raw_input(g + 'Threads : ' + w)
		pool = asshole(int(th))
		pool.map(whitepages,babe)
		pool.close()
		pool.join()
	else:
		prewhitepages()

# number genarator 
def numgen():
	numcount = 1
	clear()
	seads = raw_input(g + "Area Code : " + w)
	midman()
	for z in range(10):
		for z2 in range(10):
			for z3 in range(10):
				for z4 in range(10):
					for midnum in babe:
						lastnum = str(z) + str(z2) + str(z3) + str(z4)
						# you can change num output style.if you want "-" then just add + "-" +
						fnum = "+1" + seads + str(midnum) + lastnum
						print b + "[" + str(numcount) + "]" + y + "[x.x] Number Genarated : " + w + fnum + y + " [AreaCode] : "+ w + seads
						open('GenNumber.txt','a').write(fnum + "\n")
						numcount = numcount + 1

# help func
def help():
	clear()
	print """\x1b[31m


_____________________________________
               help
-------------------------------------
For address.com use name as combo
example:
jonathon james
jhon
Mia khalifa
-------------------------------------
For 411 just give USA area code as
input
example:
201
332
-------------------------------------
For whitepages just give USA area
code as input
example:
201
332
-------------------------------------
For number genarator just give USA 
area code as input
example:
201
332
_____________________________________\x1b[37m"""

# main func
def main():
	clear()
	want = raw_input("""\x1b[37m
          ,-~-. _.---._ ,-~-x.
         / .- ,'       `. -. x
         x ` /`          x ' / \x1b[35m[PhoneBook Eater v1]\x1b[37m
          `-/   'A___A`   x-'     \x1b[35m[Author : xTheOneAboveAll]\x1b[37m
            |   ,'(_)`.   |    \x1b[35m[Not for sell bro !]\x1b[37m
            x  ( ._|_. )  /
             x  `.___,'  /
            .-`._     _,'-.
          ,'  ,' `---' `.  `.[use usa vpn]
      \x1b[35m-----------------------------\x1b[37m
      [1] \x1b[31mGrab Number From Addresses.com\x1b[37m
      [2] \x1b[31mGrab Number From 411.com\x1b[37m
      [3] \x1b[31mGrab Number From Whitepages.com\x1b[37m
      [4] \x1b[31mNumber Genarator(USA)\x1b[37m
      [5] \x1b[31mHelp!\x1b[37m

      \x1b[35m[root@Eater]  \x1b[31m""")
	if want == '1':
		preadresses()
	elif want == '2':
		prefouroneone()
	elif want == '3':
		prewhitepages()
	elif want == '4':
		numgen()
	elif want == '5':
		help()
	else:
		main()

main()
