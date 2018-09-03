

from bs4 import BeautifulSoup
from googlesearch import search
import urllib3
import sched, time
from itertools import cycle as cy
import Flask as f
import requests
import html5lib
import re
bse=["Bse_Prc_tick_div","bse_upd_time","b_changetext"]
t=set()
s = sched.scheduler(time.time, time.sleep)
rept=[1,2,3,4,5,6,7,8,9,10]
rep=cy(rept)
#stoptime=["16:00","16:01","16:02","16:03","16:04","16:05","16:06","16:07","16:08","16:09","16:10"]
#rec=iter(stoptime)
def loop(rt,company,dat):
   l=[]
   f = open ( '/home/spanidea/.PyCharmCE2018.1/config/scratches/' + company + "_" + dat + '.txt',"r" )
   lineList = f.readlines()
   f.close()
   time=lineList[len(lineList)-1][20:25]
   t.add(time)
   k = (int(rt) > 5 and len(t)==1)



   if len(t) == 10:
      t.clear()
   if k:
       exit()


   query = company + " share advanced chart moneycontrol"

   for j in search(query, tld="com", num=1, stop=1, pause=2):
      s=j
   URL = str(s)
   http = urllib3.PoolManager()
   r = http.request('GET', URL)
   soup = BeautifulSoup(r.data, 'html5lib')
   soup.prettify()
   for k in bse:
       content=soup.find("div", {"id": k})
       l.append(str(content.text))
       for div in content.findAll('img'):
            l.append(str(div)[46:116])

   file = open('/home/spanidea/.PyCharmCE2018.1/config/scratches/' + company + "_" + dat + '.txt','a')
   file.write(str(l))
   file.write("\n")
   file.close()



def runner(company,date):
   for y in range(1,144):
       try:
           r=next(rep)
           s.enter(1,1,loop,(str(r),company,date))
           s.run()
           time.sleep(295)
       except:
           print("Share market closed")
           exit()


#if __name__=='__main__':
#    x=raw_input("Enter the name of the company: ")
#    runner('Tata')