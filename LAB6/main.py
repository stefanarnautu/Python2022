import re
"""
1.Write a function that extracts the words from a given text as a parameter.
A word is defined as a sequence of alpha-numeric characters.
"""
print("1-----------------------------------------------------")
def ex1(text):
    return re.split(" ",text)
print(ex1("orice as zice"))

"""
2.Write a function that receives as a parameter a regex string, a text string and a whole number x,
and returns those long-length x substrings that match the regular expression.
"""
print("\n2---------------------------------------------------")
def ex2(reg,text,l):
    return list(filter(lambda x: len(x)==l, re.findall(reg,text)))

print(ex2("\d+", "Price is 123 USD 345, 45673",3))

"""
3.Write a function that receives as a parameter a string of text characters and a list of regular
 expressions and returns a list of strings that match on at least one regular expression given as a parameter.

"""
print("\n3---------------------------------------------------")
def ex3(text,list_regex):
    rezultat = list()
    for l in list_regex:
        rezultat += re.findall(l,text)
    return rezultat

print(ex3("nu stiu ce sa mai zic 23486 adsd 345",["[0-9]{3}\s+","\w+"]))
"""
4.Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns
 those elements that have as attributes all the keys in the dictionary and values the corresponding values.
  For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be
  those tags whose attributes are class="url" si name="url-form" si data-id="item".
"""
print("\n4---------------------------------------------------")
def ex4(path,d):
    f = open(path,"r")
    rez = list()
    lines = f.readlines()
    k=0
    for key,value in d.items():
        if k == 0:
            for l in lines:
                if re.search(f"{key}=\s*\"{value}\"",l):
                    rez.append(l)
        else:
            for l in rez:
                if not re.search(f"{key}=\s*\"{value}\"", l):
                    rez.remove(l)
        k = k+1
    return rez

print(ex4("D:\\a.FACULTATE\PYTON\LAB6\data\ex4_data.xml",{"class": "url", "name": "url-form", "data-id": "item"}))
"""
5.Write another variant of the function from the previous exercise that returns those elements that have at least
 one attribute that corresponds to a key-value pair in the dictionary.
"""

print("\n5---------------------------------------------------")
def ex5(path,d):
    f = open(path,"r")
    rez = list()
    lines = f.readlines()
    k=0
    for key,value in d.items():
            for l in lines:
                if re.search(f"{key}=\s*\"{value}\"",l) and l not in rez:
                    rez.append(l)
    return rez
print(ex5("D:\\a.FACULTATE\PYTON\LAB6\data\ex4_data.xml",{"class": "url", "name": "url-form", "data-id": "item"}))

"""
6.Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
 Censorship means replacing characters from odd positions with *.
"""
print("\n6---------------------------------------------------")
def ex6(text):
    s = re.split(" ",text)
    for i in range(0,len(s)):
        if re.match("^[aeiouAEIOU].*[aeiouAEIOU]$",s[i]):
            s[i] = "*" * len(s[i])
    return " ".join(map(str,s))
print(ex6("afdhdfhfdhe agh bhe AkO ooo "))
"""
7.Verify using a regular expression whether a string is a valid CNP.
"""
print("\n7---------------------------------------------------")
def get_control_digit(digits):
    checksum_number = "279146358279"
    checksum = 0
    for i, j in zip(checksum_number, str(digits)):
        checksum += int(i) * int(j)
    checksum %= 11
    if checksum == 10:
        checksum = 1
    print(checksum)
    return str(checksum)
def ex7(cnp):
    if re.match("^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$",cnp) and get_control_digit(cnp)==cnp[12]:
        return True
    return False

print(ex7("5010208270041"))
"""
8.Write a function that recursively scrolls a directory and displays those files whose name matches a regular
 expression given as a parameter or contains a string that matches the same expression. Files that satisfy
 both conditions will be prefixed with ">>"
"""
print("\n8---------------------------------------------------")
import os

def ex8(path,reg):
    rez = list()
    for(root,d,f) in os.walk(path):
        for file_name in f:
            full_file_name = os.path.join(root, file_name)
            if re.match(".*(\\\\\w+\..*)$",full_file_name):
                if re.match(reg,re.split("\.",file_name)[0]):
                    rez.append(full_file_name)
    return rez
print(ex8(".","comp"))















