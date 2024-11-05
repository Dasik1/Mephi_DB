# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Sun Nov  3 12:56:16 2024
in Tims II Lab

@author: Stark
"""


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
from bs4 import BeautifulSoup as bs
from datetime import date as d
from time import time
from time import sleep as zzz



class HomeMephiParser:
    def __init__(self):
        
        options = Options()
        # options.page_load_strategy = 'none'
        options.page_load_strategy = 'eager'
        # options.page_load_strategy = 'normal'
        self.driver = webdriver.Firefox(options=options)
            
    
    def login(self, username, password):
        self.driver.get("https://auth.mephi.ru/login")
        self.driver.find_element("id", "username").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        self.driver.find_element("name", "commit").click()
    
    def logout(self):
        self.driver.close()
    
    
    def ping_Groups(self, level_range = range(3+1),term_id=19):
        
        source = []
        for lvl in level_range:
            self.driver.get(f"https://home.mephi.ru/study_groups?level={lvl}&term_id=19")
            source.append(self.driver.page_source)
            zzz(0.5)
        return source
    
    def parse_Groups(self, pages):

        group_links = {}
        for page in pages:
            for i in re.findall('\d{5}/schedule">\w\d{2}-\d{3}',page):
                group_links[i[-7:]] = int(i[:5])
        return group_links
    
    
    
    def ping_Users_per_Group(self, group_id):
        while True:
            self.driver.get(f"https://home.mephi.ru/study_groups/{group_id}")
            source = self.driver.page_source
            if source.find("Forbidden")>=0:
                zzz(5)
                print("FORBIDDEN - RETRY")
            else:
                break
        return source
    
    def parse_Users_per_Group(self, page):
        users = {}
        
        #in here re cant solve it (it breaks on letter seq) so here it comes - BS
        s = bs(page,"html.parser")
        lines = s.findAll('div', attrs={'class' : 'list-group-item'})
        if lines == []:print("No Users - No horny")
        for student in lines:
            
            link = student.find('a')
            if link is None: #Б24-205 have a user without account
                name = student.find('span').next_sibling[1:-1]
                link = -time()
            else:
                name = link.text
                link = student.find('a')['href']
                link = re.findall('\d+',link)[0]
                
            sn, fn, *ln = name.split(' ')
            ln = ' '.join(ln)
            #нет отчества Б24-161
            if ln == '':ln = '-'
            users[int(link)] = {"second":sn, "first":fn, "last":ln}
        return users
    
    
    def ping_Teachers(self,letter):
        while True:
            self.driver.get(f"https://home.mephi.ru/tutors?char={letter}&organization_id=1&term_id=19")
            source = self.driver.page_source
            if source.find("Forbidden")>=0:
                zzz(5)
                print("FORBIDDEN - RETRY")
            else:
                break
        return source
    
    def ping_Teacher(self, sch_ID):
        while True:
            self.driver.get(f"https://home.mephi.ru/tutors/{sch_ID}?locale=")
            schedule = self.driver.page_source
            if schedule.find("Forbidden")>=0:
                zzz(5)
                print("FORBIDDEN - RETRY")
            else:
                break
        
        
        
        s = bs(schedule,"html.parser")
        link = s.findAll('h1', attrs={'class' : 'light'})[0].find("a")
        if link is None: return -1, ''
        link = link["href"]
        ID = re.findall('\d+',link)[0]
        
        
        while True:
            self.driver.get(f"https://home.mephi.ru/users/{ID}")
            page = self.driver.page_source
            if page.find("Forbidden")>=0:
                zzz(5)
                print("FORBIDDEN - RETRY")
            else:
                break
        return ID, page
    
    def parse_Teacher(self, page):
        #those who wrote home mephi must kill themselves
        #even re cant hold that theq pooped....
        s = bs(page,"html.parser")
        kaf = s.find('div', attrs={'class' : 'text-muted'}).find("small").text
        kaf = re.findall('\d+',kaf)
        if kaf == []:kaf = -1
        else: kaf = kaf[0]
        
        date = re.findall('в МИФИ с \d+',page)[0][-4:]
        
        
        return int(kaf), int(date)
        
    
    def parse_Teachers(self, page):
        
        teachers = {}
        
        s = bs(page,"html.parser")
        lines = s.findAll('a', attrs={'class' : 'list-group-item'})
            
        for teacher in lines:
            link = teacher['href'][-5:]
            name = teacher.contents[0]
                
            sn, fn, *ln = name.split(' ')
            ln = ' '.join(ln)
            #нет отчества 
            if ln == '':ln = '-'
            
            teachers[int(link)] = {"second":sn, "first":fn, "last":ln}
        
        return teachers


