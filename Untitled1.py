#!/usr/bin/env python
# coding: utf-8

# In[3]:


if (10 < 0) and (0 < -10):
     print("A")

elif (10 > 0) or False:
     print("B")

else:
     print("C")


# In[4]:


if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
       print('B')
    else:
      print('C')
else:
     print('D')


# In[ ]:


n=int(input())
c=1
sum=0
while c<=n:
    if c%2==0:
        sum=sum+c
        c=c+1
print(sum)


# In[ ]:


n=int(input())
c=1
sum=0
while c<=n:
    if c%2==0:
        sum=sum+c
        c=c+1
print(sum)


# In[ ]:




