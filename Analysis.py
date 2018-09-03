import matplotlib.pyplot as mt
import numpy as np
import matplotlib.dates as mdates
import datetime as dt
import re

datdict={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
arrowdict={'red_arrow.jpg':'v','grn_arrow.jpg':'^'}

def analyser(dat,com):
   shares=[]
   arrow=[]
   time=[]
   rt=datdict[dat[5:7]] + " " + dat[8:10]
   f = open( '/home/spanidea/.PyCharmCE2018.1/config/scratches/' + com + "_" + dat + '.txt', "r")
   line=f.readlines()
   for i in range(len(line)):
       p4 = re.findall(r'[\w\.{3}]+\s[\d\.{2}]+', line[i])
       if p4[0] == rt:
          try:
             p1=re.findall(r'^\D*?(\d+(\.\d+)?)',line[i])
             p2=re.findall(r'([\w\.-]+.jpg|[\w\.-]+.gif)',line[i])
             p3=re.findall(r'[\d\.{2}]+:[\d\.{2}]+',line[i])
             shares.append(p1[0][0])
             arrow.append(p2[0])
             time.append(str(p3[0]))
          except:
             continue

   x = np.array([v for v in range(len(time))])
   mt.figure(figsize=(17, 8))
   mt.xlabel("Time")
   mt.ylabel("Prices")
   mt.xticks(x, time, rotation=90)
   mt.plot(x,shares,marker='o')
   mt.title("Shares of " + com + " on " + dat)
   mt.grid()
#   mt.show()
   mt.savefig('/home/spanidea/.PyCharmCE2018.1/config/scratches/static/' + com + "_" + dat + '.jpg')
   f.close()

#if __name__=='__main__':
#   analyser('2018-08-20','Tata')