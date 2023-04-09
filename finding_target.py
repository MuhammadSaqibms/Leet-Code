#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main_func():
    num=[1,2,4,6,8,9,14,15]
    target=13
    left=0
    right=len(num)-1
    
    while left < right:
        result=num[left]+num[right]
        
        if result == target:
            return True
        if result > target:
            right -= 1
        else:
            left += 1
    return False
main_func()

