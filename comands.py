# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Fri Nov  1 22:49:53 2024
in Tims II Lab

@author: Stark
"""

ALPHABET = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Э","Ю","Я",]



#init
def read_comand(path):
    with open(path, 'r', encoding="utf-8") as Comand:
        return Comand.read()

init = read_comand("sql/init.sql")

users_param = read_comand("sql/users_param.TIsp")#TI script part