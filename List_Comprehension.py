
#l=[v for v in range(1,10,2)]
#print l

#parsed=[]
#wipro="This mac address 00:0a:95:9d:68:16 was used to hack the network"
#parsed=wipro.split(" ")
#print parsed[3]

#ldesc=[]
#lasc=[]
# Python program for implementation of Bubble Sort

#def bubbleSort(arr):
#	n = len(arr)

	# Traverse through all array elements
#	for i in range(n):

		# Last i elements are already in place
#		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
#			if arr[j] > arr[j+1] :
#				arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
#arr = [64, 34, 25, 12, 22, 11, 90]

#bubbleSort(arr)

#print ("Sorted array is:")
#for i in range(len(arr)):
#	print ("%d" %arr[i]),


#xx="This mac address 00:0a:95:9d:68:16 was used to hack the network"
#mac = re.findall(r'[\w\.{2}]+:[\w\.{2}]+:[\w\.{2}]+:[\w\.{2}]+:[\w\.{2}]+:[\w\.{2}]+', xx)
#print mac


import pandas as pd
import numpy as np
import time

def my_dec(func):
    def rgen():
        count = 0
        N = 100000
        for k in range(N):
            r = np.random.randn()
            if r > -1 and r < 1:
                count += 1

        d = float(count) / N
        print "Normally distributed random numbers have the % probablity of " + "{:.2f}".format(d * 100) + "% everywhere"
        func()
    return rgen

@my_dec
def mindex():
    o=['G1','G1','G1','G2','G2','G2']
    l=[1,2,3,1,2,3]
    index=list(zip(o,l))
    index=pd.MultiIndex.from_tuples(index)
    df=pd.DataFrame(np.random.randn(6,6),index,['A','B','C','D','E','F'])
    df.index.names=['Groups','Num']
    print df
    print df.loc['G1'].loc[2]
    print df.xs(3,level='Num')


if __name__ == '__main__':
    start_time=time.time()
    mindex()
    print "Time taken:" + str(time.time()-start_time)
