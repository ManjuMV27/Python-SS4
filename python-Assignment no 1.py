#!/usr/bin/env python
# coding: utf-8

# 
# # 1:Write a function to find the maximum element in a array

# In[4]:



def maximum(array):
    max=array[0]
    for i in range(1,len(array)):
        if array[i]>max:
            max=array[i]
    return max    
    
array=[]
n=int(input("enter the size of array"))
for i in range(n):
    x=int(input(""))
    array.append(x)
large=maximum(array)
print("largest element = ",large)




# # 2.Write a function to reverse a string x

# In[12]:


def stringReverse(name):
    string_rev=""
    for i in range(len(name)-1,-1,-1):  
       string_rev+=name[i]
    return string_rev


x=input("Enter the string = ")
y=stringReverse(x)
print("Reverse string is = ",y)


# # 3.Write a function to sort a array in ascending order

# In[19]:


def sort_array(array):
    array.sort()
    return array

x=list(map(int,input("enter elements of array = ").split()))
y=sort_array(x)
print("Sorted Array is = ",*y)


# # 4.Write a function to calculate the sum of all even numbers between 1 and n.

# In[4]:


def even_sum(n):
    sum=0
    for i in range(1,n+1):
        if (i%2==0):
            sum=sum+i
    return sum

n=int(input("enter the limit"))
sum=even_sum(n)
print("sum of even numbers between 1 and {}".format(n))
print(sum)
    


# # 5. Write a function to check if a given number is prime.

# In[26]:


def prime(n):
    for i in range(2,int(n/2+1)):
        if n%i==0:
            return 0
        else:
            return 1
n=int(input("enter the number "))
y=prime(n)
if(y==0):
    print("{} is not a prime number".format(n))
else:
    print("{} is a prime number".format(n))
        
        


# # 6. Write a function to find the second largest number in a array

# In[31]:


def second_large(array):
     array.sort(reverse=True)
     return array    
x=list(map(int,input("enter the elements of array ").split()))
y=second_large(x)
print("Second Largest = ",y[1])


# # 7.Write a function to remove duplicates from a array

# In[35]:


def remove_dupli(array):
    list=[]
    for i in array:
        if i not in list:
            list.append(i)
    return list
x=list(map(int,input("enter the elements of array ").split()))
y=remove_dupli(x)
print("old array= ", *x)
print("new array= ",*y)


# # 8.Write a function to calculate the sum of all numbers in an array
# 

# In[39]:


def sum_array(n):
    sum=0
    for i in n:
        sum=sum+i          
    return sum

x=list(map(int,input("enter the elements of array ").split()))
sum=sum_array(x)
print("sum of array = ",sum)


# # 9.Write a function to generate all prime numbers up to a given limit

# In[59]:


def prime_limit(n):
    list=[]
    for i in range(1,n+1):
            if i==1 or i==0:
                continue
            else:
                for j in range(2,int(i/2)+1):
                    if i%j==0:
                        break
                else:
                    list.append(i)
    print("prime numbers upto",list)
n=int(input("enter the limit "))
prime_limit(n)


# # 10.Write a program to find the maximum and minimum   elements in an array of integers.

# In[62]:


x=list(map(int,input("enter the elements of array ").split()))
print("maximum element = ",max(x))
print("minimum element = ",min(x))


# # 11.Write a function to calculate the factorial of a given number n

# In[66]:


def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)    
x=int(input("enter the number"))
factorial=fact(x)
print("factorial of {} is = ".format(x),factorial)


# # 12. Write a function to check given string is palindrome or not

# In[75]:


def palindrome(s):
    str=s[::-1]
    print("reverse string is = ", str)
    if(str==s):
        print("string is palindrome")
    else:
        print("string is not palindrome")
x=input("enter the string = ")
palindrome(x)


# # 13.Write a function to check if a given number is an Armstrong number.

# In[82]:


def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=int(temp/10)# or use temp//=10
    if n==sum:
        print("{} is an armstrong number".format(n))
    else:
        print("{} is not an armstrong number".format(n))
        
x=int(input("enter the number"))
arm=armstrong(x)    


# # 14. A program to print the Fibonacci series

# In[98]:


def fibonacci(n):
    list=[]
    for i in range(0,n):
        if i<=1:
            list.append(i)
        else:
            f=0
            f=list[-1]+list[-2]
            list.append(f)
    print(list)       
x=int(input("enter the limit "))
fibonacci(x)


# # 15. Write a program to find the sum of all prime numbers up to a given limit. 

# In[102]:


def prime_limit(n):
    list=[]
    sum=0
    for i in range(1,n+1):
           
            if i==1 or i==0:
                continue
            else:
                for j in range(2,int(i/2)+1):
                    if i%j==0:
                        break
                else:
                    list.append(i)
                    sum=sum+i
    print("prime numbers upto",list)
    print("sum = ", sum)
n=int(input("enter the limit "))
prime_limit(n)


# # 16.Write a program to find the sum of all the multiples of 3 or 5 below a given number.

# In[111]:


def multi(x):
    sum=0
    list=[]
    for i in range(1,x):
        if i%3==0 or i%5==0:
            list.append(i)
            sum=sum+i
    print(list)
    return sum
    

n=int(input("enter the limit "))
sum=multi(n)

print("sum of all the multiples of 3 or 5 below  {} = ".format(n),sum)


# # 17.Write a program to find the sum of all the even or odd numbers below a given number.

# In[114]:


def sum_even_odd(x):
    sum_odd=0
    sum_even=0
    list_odd=[]
    list_even=[]
    for i in range(1,x):
            if i%2==0:
                list_even.append(i)
                sum_even+=i
            else:
                list_odd.append(i)
                sum_odd+=i    
    print("list of even numbers = ", list_even)
    print("sum = ", sum_even)
    print("list of odd numbers = ", list_odd)
    print("sum = ", sum_odd)
n=int(input("enter the limit "))
sum=sum_even_odd(n)


# # 18.Write a program to find the union of two arrays of integers.

# In[123]:


a=[2,4,5,6,7]
b=[1,3,8,10]
union=[]
for i in a:
    if i not in union:
        union.append(i)
for j in b:
    if j not in union:
        union.append(j)
union.sort()        
print("union of arrays = ",union)


# # 19.Write a program to find the sum of the digits of a given number.

# In[126]:


def sum_digit(x):
    sum=0
    t=x
    while(t>0):
        rem=t%10
        sum=sum+rem
        t//=10
    print("sum = ",sum)   
x=int(input("enter the number"))
sum_digit(x)


# # 20.Write a program to count the number of vowels in a given string.

# In[132]:


x=input("enter the string ")
vowels=['a','e','i','o','u']
count=0
for i in x:
    if i in vowels:
        count+=1
print("no of vowels in {} is = ".format(x),count)


# In[ ]:




