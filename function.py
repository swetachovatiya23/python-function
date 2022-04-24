def max_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest

print(max_num(10,20,30))

def mul_list(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
     
lists = [1, 2, 3]
print(mul_list(lists))

def rev_string(str):  
    str1 = ""    
    for i in str:  
        str1 = i + str1  
    return str1  
str = "sweta"  
print(rev_string(str))

def num_within(num, start_num, end_num):
    return start_num < num < end_num
print(num_within(3,2,4))


def choose(n, k): 
    if k in (0, n):
        return 1
    return choose(n-1, k-1) + choose(n-1, k)
def pascal(n):
    for row in range(n):
        for k in range(row + 1):
            print(choose(row, k), end=' ') 
        print()
print(pascal(5))