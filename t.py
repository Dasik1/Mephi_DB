# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Mon Nov 11 15:34:15 2024
in Tims II Lab

@author: Stark
"""

import requests

q = requests.get("https://home.mephi.ru/study_groups/19468/schedule.ics")
q.encoding = 'utf-8'

print(q.text)