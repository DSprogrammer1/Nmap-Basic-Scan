#!/usr/bin/env python
# -*- coding utf-8 -*-

import os 

def maps():
	print("""
	-----------
	Welcome to Nmap Tools
	-----------
	Please Choose The Command
	-------------------------
	-s		Simply Scan
	-v		Version Info
	-S		System Info
	-sS		Port Scan
	-sV -sS		Port & Version Scan
	++++++++++++++++++++++++++++
	----------------------------
	""")
	key_word=input("Please Input Your Key Word: ")
	
	if(key_word=="-s"):
		ip=input("Please Input Target ip Adsress: ")
		os.system("nmap "+ip)
	if(key_word=="-v"):
		ip=input("Please Input Target ip Adsress: ")
		os.system("nmap -sV " +ip)
	if(key_word=="-S"):
		ip=input("Please Input Target ip Adsress: ")
		os.system("nmap -sS "+ip)
	if(key_word=="-sV -sV"):
		ip=input("Please Input Target ip Adsress: ")
		os.system("nmap -sS -sV "+ip)
maps()
