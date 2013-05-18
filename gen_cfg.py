# -*- coding: utf-8 -*- 

import tenjin, re, ConfigParser
from tenjin.helpers import *
from tenjin.escaped import *
import xdrlib, sys, xlrd, datetime


ini_parser = ConfigParser.ConfigParser()
ini_parser.read("cfg.ini")
for sec in ini_parser.sections():
	tpl_file = sec
	excele_file = ini_parser.get(sec, 'excle_data')
	func_list =  ini_parser.get(sec, 'excle_sheets')
	func_list = eval(func_list)
	print func_list

