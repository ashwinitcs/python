#!/usr/bin/env python

def insertionsort(sample):
   length = len(sample)
   for i in range(1,length):
      value = sample[i]
      j = i -1
      while j>=0:
         if(value < sample[j]):
            sample[j+1] = sample[j]
            sample[j] = value
            j = j -1
         else:
            break
     
   print(" sorted list:", sample)
sample = [6,3,2,5,7,1]
insertionsort(sample)  
   
