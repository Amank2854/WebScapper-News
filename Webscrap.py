import requests
import lxml
import bs4
import os
from time import sleep
india = os.getcwd() + '\\india'
world = os.getcwd() + '\\world'
business = os.getcwd() + '\\business'
mai = os.getcwd() + '\\main'
os.mkdir(india)
os.mkdir(world)
os.mkdir(business)
os.mkdir(mai)
path = ''
title=''
date=''
text='' 
def ind():
  top=[]
  link=[]   
  li='' 
  j=0;   
  if(j==0):
      web_link= 'https://timesofindia.indiatimes.com/india/'
      path=india
  if(j==1):
      web_link= 'https://timesofindia.indiatimes.com/world/'
      path=world
  if(j==2):
      web_link= 'https://timesofindia.indiatimes.com/business/'
      path=business
  if(j==3):
      web_link= 'https://timesofindia.indiatimes.com/'
      path = mai
  req=requests.get(web_link)
  soup=bs4.BeautifulSoup(req.text,'lxml')
  topi=soup.find('div',{'class':'main-content'})
  topi=topi.find_all('span',{'class':'w_tle'})
  for i in range(len(topi)):
      top=topi[i].find('a').get('href')
      link.append('https://timesofindia.indiatimes.com'+top)
  for i in range(len(link)):
      rq=''
      c=0
      while(rq== ''):
        try: 
          rq=requests.get(link[i])
          break
        except:
            c=1
            break
      if(c!=0):
          break
      sp=bs4.BeautifulSoup(rq.text,'lxml')
      title=sp.find('h1',{'class':'_23498'})
      if(title!=None):
          title=title.getText()
          li=link[i]
      if(sp.find('div',{'class':'_3Mkg- byline'})!=None):
          date=sp.find('div',{'class':'_3Mkg- byline'}).getText()
      if(sp.find('div',{'class':'ga-headlines'})!=None):
          text=sp.find('div',{'class':'ga-headlines'}).getText()
      if(title!=None):
        os.chdir(path)
        file=open("scrape.txt",'a',encoding = 'utf-8')    
        file.write("Title:"+'\n'+'\n')
        file.write(title+'\n'+'\n')
        file.write("Link:"+'\n'+'\n')
        file.write(li+'\n'+'\n')
        file.write("Date and Time:"+'\n'+'\n')
        file.write(date+'\n'+'\n')
        file.write("Text:"+'\n'+'\n')
        file.write(text+'\n'+'\n')
def wor():
  li='' 
  top=[]
  link=[]  
  j=1;   
  if(j==0):
      web_link= 'https://timesofindia.indiatimes.com/india/'
      path=india
  if(j==1):
      web_link= 'https://timesofindia.indiatimes.com/world/'
      path=world
  if(j==2):
      web_link= 'https://timesofindia.indiatimes.com/business/'
      path=business
  if(j==3):
      web_link= 'https://timesofindia.indiatimes.com/'
      path = mai
  req=requests.get(web_link)
  soup=bs4.BeautifulSoup(req.text,'lxml')
  topi=soup.find('div',{'class':'main-content'})
  topi=topi.find_all('span',{'class':'w_tle'})
  for i in range(len(topi)):
      top=topi[i].find('a').get('href')
      link.append('https://timesofindia.indiatimes.com'+top)
  for i in range(len(link)):
      rq=''
      c=0
      while(rq== ''):
        try: 
          rq=requests.get(link[i])
          break
        except:
            c=1
            break
      if(c!=0):
          break
      sp=bs4.BeautifulSoup(rq.text,'lxml')
      title=sp.find('h1',{'class':'_23498'})
      if(title!=None):
          title=title.getText()
          li=link[i]
      if(sp.find('div',{'class':'_3Mkg- byline'})!=None):
          date=sp.find('div',{'class':'_3Mkg- byline'}).getText()
      if(sp.find('div',{'class':'ga-headlines'})!=None):
          text=sp.find('div',{'class':'ga-headlines'}).getText()
      if(title!=None):
        os.chdir(path)
        file=open("scrape.txt",'a',encoding = 'utf-8')    
        file.write("Title:"+'\n'+'\n')
        file.write(title+'\n'+'\n')
        file.write("Link:"+'\n'+'\n')
        file.write(li+'\n'+'\n')
        file.write("Date and Time:"+'\n'+'\n')
        file.write(date+'\n'+'\n')
        file.write("Text:"+'\n'+'\n')
        file.write(text+'\n'+'\n')    
def bus():
  li='' 
  j=2; 
  top=[]
  link=[]    
  if(j==0):
      web_link= 'https://timesofindia.indiatimes.com/india/'
      path=india
  if(j==1):
      web_link= 'https://timesofindia.indiatimes.com/world/'
      path=world
  if(j==2):
      web_link= 'https://timesofindia.indiatimes.com/business/'
      path=business
  if(j==3):
      web_link= 'https://timesofindia.indiatimes.com/'
      path = mai
  req=requests.get(web_link)
  soup=bs4.BeautifulSoup(req.text,'lxml')
  topi=soup.find('div',{'class':'main-content'})
  topi=topi.find_all('span',{'class':'w_tle'})
  for i in range(len(topi)):
      top=topi[i].find('a').get('href')
      link.append('https://timesofindia.indiatimes.com'+top)
  for i in range(len(link)):
      rq=''
      c=0
      while(rq== ''):
        try: 
          rq=requests.get(link[i])
          break
        except:
            c=1
            break
      if(c!=0):
          break
      sp=bs4.BeautifulSoup(rq.text,'lxml')
      title=sp.find('h1',{'class':'_23498'})
      if(title!=None):
          title=title.getText()
          li=link[i]
      if(sp.find('div',{'class':'_3Mkg- byline'})!=None):
          date=sp.find('div',{'class':'_3Mkg- byline'}).getText()
      if(sp.find('div',{'class':'ga-headlines'})!=None):
          text=sp.find('div',{'class':'ga-headlines'}).getText()
      if(title!=None):
        os.chdir(path)
        file=open("scrape.txt",'a',encoding = 'utf-8')    
        file.write("Title:"+'\n'+'\n')
        file.write(title+'\n'+'\n')
        file.write("Link:"+'\n'+'\n')
        file.write(li+'\n'+'\n')
        file.write("Date and Time:"+'\n'+'\n')
        file.write(date+'\n'+'\n')
        file.write("Text:"+'\n'+'\n')
        file.write(text+'\n'+'\n')
def mi():
  li=''
  top=[]
  link=[]  
  j=3;   
  if(j==0):
      web_link= 'https://timesofindia.indiatimes.com/india/'
      path=india
  if(j==1):
      web_link= 'https://timesofindia.indiatimes.com/world/'
      path=world
  if(j==2):
      web_link= 'https://timesofindia.indiatimes.com/business/'
      path=business
  if(j==3):
      web_link= 'https://timesofindia.indiatimes.com/'
      path = mai
  req=requests.get(web_link)
  soup=bs4.BeautifulSoup(req.text,'lxml')
  topi=soup.find('div',{'class':'main-content'})
  topi=topi.find_all('span',{'class':'w_tle'})
  for i in range(len(topi)):
      top=topi[i].find('a').get('href')
      link.append('https://timesofindia.indiatimes.com'+top)
  for i in range(len(link)):
      rq=''
      c=0
      while(rq== ''):
        try: 
          rq=requests.get(link[i])
          break
        except:
            c=1
            break
      if(c!=0):
          break
      sp=bs4.BeautifulSoup(rq.text,'lxml')
      title=sp.find('h1',{'class':'_23498'})
      if(title!=None):
          title=title.getText()
          li=link[i]
      if(sp.find('div',{'class':'_3Mkg- byline'})!=None):
          date=sp.find('div',{'class':'_3Mkg- byline'}).getText()
      if(sp.find('div',{'class':'ga-headlines'})!=None):
          text=sp.find('div',{'class':'ga-headlines'}).getText()
      if(title!=None):
        os.chdir(path)
        file=open("scrape.txt",'a',encoding = 'utf-8')    
        file.write("Title:"+'\n'+'\n')
        file.write(title+'\n'+'\n')
        file.write("Link:"+'\n'+'\n')
        file.write(li+'\n'+'\n')
        file.write("Date and Time:"+'\n'+'\n')
        file.write(date+'\n'+'\n')
        file.write("Text:"+'\n'+'\n')
        file.write(text+'\n'+'\n')
if __name__ == "__main__":
    wor()
    bus()
    mi()
    ind()
