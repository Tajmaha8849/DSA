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



#In C language
#include <stdio.h>

int main()
{
    int size,ele;
    int leftsum=0;
    int rightsum=0;
    int i,j,k,index;
    printf("Enter size of an array:");
    scanf("%d",&size);
    int arr[size];
    printf("Enter the elements:");
    for(i=0;i<size;i++){
        scanf("%d",&ele);
        arr[i]=ele;
    }
    
    
    for(i=0;i<size;i++){
        index=i;
        for(j=0;j<index;j++){
            leftsum=leftsum+arr[j];
        }
        for(k=i+1;k<size;k++){
            rightsum=rightsum+arr[k];
        }
        if(leftsum==rightsum){
            printf("Equivalent index is %d",i);
            break;
        }
        leftsum=0;
        rightsum=0;
        
        
        
    }

    return 0;
}


    
