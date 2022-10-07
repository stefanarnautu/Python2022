import math
import re
#1
def gcd(number_list):
    for x in range(len(number_list)-1):
        gcd=math.gcd(number_list[x],number_list[x+1])
    return gcd
#number_list=list(map(int, input("Enter numbers: ").split()))

#print(gcd(number_list));

#2
def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1

    print("No. of vowels :", count)

str = "Python"
vowel_count(str)

#3
string = "asa si asa"
substring = 'asa'
res = len(re.findall(substring, string))
print("Number of substrings", res)

#4
test_str = "UpperCamelCase"
upperalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
j=0
for i in test_str:
    if i in upperalpha:
        result += '_'
        result += test_str[j].lower()
        j=j+1
    else:
        result += test_str[j]
        j=j+1

print("The uppercase characters in string are : " + result)

#5

#6
def palindrom(num):
    count=0
    copy = num
    while copy>0:
        copy/=10
        count=count+1
    i=0
    while i<count/2:
       if num%pow(10,i+1) != num/pow(10,count-i-1):
           return 0
       i= i + 1
    return 1

print(palindrom(121))

