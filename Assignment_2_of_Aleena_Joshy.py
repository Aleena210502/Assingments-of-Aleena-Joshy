#!/usr/bin/env python
# coding: utf-8

# # Q1 Program to Guess the Secret Number

# In[1]:


s = int(input("Enter a secret number from 0 to 10:"))
m1 = str("Too low! Try again")
m2 = str("Too high! Try again")
m3 = str("Congratulations! You guessed the number correctly!")
while s<=10:
    if s < 7:
        print(m1)
        s = int(input("Enter a number again from 0 to 10 :"))
    elif s > 7:
        print(m2)
        s = int(input("Enter a number agin from 0 to 10 :"))
    elif s == 7:
        print(m3)
        break
    else:
        print("Execution is completed")


# # Q2 Program to find the Factorial of a Number

# In[2]:


num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
    print(" Factorial does not exist for negative numbers")    
elif num == 0:    
    print("The factorial of 0 is 1")    
else:    
    for i in range(1,num + 1):    
        factorial = factorial*i    
    print("The factorial of",num,"is",factorial)  


# # Q3 Program to Change Profile Picture on Facebook having some restriction over the dimension of picture 

# In[9]:


L=int(6)
N=int(1)
while N>0:
    W,H=map(int,input('Enter the Width and Height with a space: ').split(" "))

    if (W<L) or (H<L):

        print("UPLOAD ANOTHER")

    elif (W==L) and (H==L) and (W==H):

        print("ACCEPTED")
        break

    else:

        print("CROP IT")
    


# In[ ]:




