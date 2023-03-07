# String Functions:

demo = "Aakash is a good boy"
print(demo.endswith("boy"))
# print(demo.count('o'))
print(demo.capitalize())
# print(demo.upper())
# print(demo.lower())
print(demo.find("is"))
# print(demo.find("good","nice"))

mystr = "Harry is a good bdoy"
# print(len(mystr))
# print(mystr[::-2])

print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.replace("is", "are"))


# F strings (Fast string) -- it simply means
import math

me = "Harry"
a1 =3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)


arr = []

#input values to list
arr = [23,45,67,32,98]

fun = sum(arr)

print ('Sum of the array is ',fun)



# def largest(arr, n):

#     max = arr[0]


# for i in range(1, n):
#     if arr[i] > max:
#          max = arr[i]
#  return max

#  n = len(arr)
# fun2 = largest(arr,n)
# print ("Largest no in given array is",fun2)
# Checking a number is palindrome 
# using math.log() + recursion + list comprehension 
import math 

# the recursive function to reverse 
def rev(num):
    return int(num != 0) and ((num % 10)* (10**int(math.log(num, 10))) + rev(num // 10)) 
	
# initializing number 
test_number = 6543
# test_number = 5462
# printing the original number 
print ("The original number is : " + str(test_number)) 

# using math.log() + recursion + list comprehension 
# for checking a number is palindrome 
res = test_number == rev(test_number) 

# printing result 
print ("Is the number palindrome ? : " + str(res)) 

