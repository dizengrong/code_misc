# -*- coding: utf-8 -*- 

# from ArtMustache import *
# import ArtMustache 
# import xdrlib, sys, xlrd, datetime

# xml_data = xlrd.open_workbook(u"宠物.xlsx")
# table    = xml_data.sheet_by_name(u'宠物二级属性计算公式')
# attr_func = {'attr_func': []}
# for i in range(1, table.nrows):
#     attr_func['attr_func'].append([table.cell(i, 0).value, table.cell(i, 1).value, table.cell(i, 2).value])

# print attr_func
# ArtMustache.render_to_file("pet.tpl", "test.html", attr_func)

import tenjin, re
from tenjin.helpers import *
from tenjin.escaped import *
import xdrlib, sys, xlrd, datetime

def format(value):
    if isinstance(value, float):
        if int(value) == value: return int(value)
        else: return value
    else:
        return value

## create engine object
engine = tenjin.Engine()

xml_data = xlrd.open_workbook(u"宠物.xlsx")

table    = xml_data.sheet_by_name(u'宠物二级属性计算公式')
context = {'attr_func': [], 'pets': []}
for i in range(1, table.nrows):
    context['attr_func'].append(
        [table.cell(i, 0).value, 
         table.cell(i, 1).value, 
         table.cell(i, 2).value])

table = xml_data.sheet_by_name(u'宠物基本信息')
for i in range(1, table.nrows):
    context['pets'].append(
        [format(table.cell(i, 0).value), 
         format(table.cell(i, 1).value), 
         format(table.cell(i, 2).value),
         format(table.cell(i, 3).value),
         format(table.cell(i, 4).value),
         format(table.cell(i, 5).value),
         format(table.cell(i, 6).value),
         format(table.cell(i, 7).value),
         format(table.cell(i, 8).value),
         format(table.cell(i, 9).value),
         format(table.cell(i, 10).value),
         format(table.cell(i, 11).value)
        ])


print context
## render template with context data
html = engine.render('pet.pyhtml', context)
dest = open("test.html", "w")
html = html.replace("\r\n", "\n")
dest.write(html)
dest.close()
