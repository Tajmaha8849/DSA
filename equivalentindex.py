# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 00:55:14 2023

@author: shubham prajapati
"""

#find equivalent index from an array

arr=eval(input())
leftsum=0
rightsum=0
for i in range(len(arr)):
    index=i
    for j in range(0,index):
        leftsum+=arr[j]
    for k in range(index+1,len(arr)):
        rightsum+=arr[k]
    if(leftsum==rightsum):
        print("Equivalent index is:",i)
        break
    
    leftsum=0
    rightsum=0

    