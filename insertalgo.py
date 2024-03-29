from insertionsorting import insertionsort
import random
from time import time
import matplotlib.pyplot as plt

randomnum= random.sample(range(100000),10000)
sortednum=sorted(randomnum)
insertion_unsorted=[]
insertion_bestcase=[]
insertion_worstcase=[]
xdomain=[]
j=0
stepsize=1000
print("normal case scenario")
for i in range(1000,11000,stepsize):
    start_time=time()
    insertionsort(randomnum[0:i])
    end_time=time()
    print(end_time-start_time)
    insertion_unsorted.insert(j,end_time-start_time)
    xdomain.insert(j,i)
    j+=1
print("BEST CASE SCENARIO")
for i in range (1000,11000,stepsize):
    start_time=time()
    insertionsort(sortednum[0:i])
    end_time=time()
    print(end_time-start_time)
    insertion_bestcase.insert(j,end_time-start_time)
    j+=1
print("WORST CASE SCENARIO")
for i in range (1000,11000,stepsize):
    start_time=time()
    insertionsort(sortednum[i:0:-1])
    end_time=time()
    print(end_time-start_time)
    insertion_worstcase.insert(j,end_time-start_time)
    j+=1

print("****************")
plt.plot(xdomain,insertion_unsorted,'y',label="Normal Case")
plt.plot(xdomain,insertion_bestcase,'g',label="Best Case")
plt.plot(xdomain,insertion_worstcase,'y',label="Worst Case")
plt.show()
