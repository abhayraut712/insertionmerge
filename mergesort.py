from mergesorting import mergesort
import random
from time import time
import matplotlib.pyplot as plt

randomnum=random.sample(range(100000),10000)
sortednum=sorted(randomnum)
merge_unsorted=[]
merge_bestcase=[]
merge_worstcase=[]
xdomain=[]
j=0
stepsize=1000
print("NORMAL CASE SCENARIO")
for i in range(1000,11000,stepsize):
    start_time=time()
    mergesort(randomnum[0:i])
    end_time=time()
    print(end_time-start_time)
    merge_unsorted.insert(j,end_time-start_time)
    xdomain.insert(j,i)
    j+=1

print("BEST CASE SCENARIO")
for i in range(1000,11000,stepsize):
    start_time=time()
    mergesort(sortednum[0:i])
    end_time=time()
    print(start_time-end_time)
    merge_bestcase.insert(j,end_time-start_time)
    j+=1


print("WORST CASE SCENARIO")
for i in range(1000,11000,stepsize):
    start_time=time()
    mergesort(sortednum[i:0:-1])
    end_time=time()
    print(end_time-start_time)
    merge_worstcase.insert(j,end_time-start_time)
    j+=1

print("**************")
plt.plot(xdomain,merge_unsorted,'y',label="Normal Case")
plt.plot(xdomain,merge_bestcase,'g',label="Best Case")
plt.plot(xdomain,merge_worstcase,'r',label="Worst Case")
plt.show()
