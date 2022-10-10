import math
import re
print("\n1-------------");
#1
def gcd(number_list):
    for x in range(len(number_list)-1):
        gcd=math.gcd(number_list[x],number_list[x+1])
    return gcd
#jnumber_list=list(map(int, input("Enter numbers: ").split()))

#print(gcd(number_list));
print("\n2-------------");
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
print("\n3-------------");
#3
string = "asa si asa"
substring = 'asa'
res = len(re.findall(substring, string))
print("Number of substrings", res)
print("\n4-------------");
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
print("\n5-------------");
#5
def spiral (M):
  print(M);

MAT = [['f','i','r','s'],
       ['n','_','l','t'],
       ['o','b','a','_'],
       ['h','t','y','p']]




print("\n6-------------");
#6
def palindrom(num):
    count=0
    copy = num
    while copy>0:
        copy= copy//10
        count=count+1
    i=0
    while i < count/2:
       #print(" Nr 1 = ", num % pow(10, i + 1) // pow(10, i), "Nr 2 = ", num // pow(10, count - (i+1))%10)
       if num%pow(10,i+1)//pow(10,i) != num//pow(10,count-(i+1))%10:
           return 0
       i= i + 1
    return 1

print(palindrom(2223222))
print("\n7-------------");
#7
def extract_number(sir):
    ok=0;
    number_found=""
    for i in range(0, len(sir)):
        if(ok==1):
            break
        if(sir[i].isnumeric()):
            ok = 1;
            number_found = number_found + sir[i];
            j=1;
            if (i + j < len(sir) - 1):
                while(sir[i+j].isnumeric()):
                    number_found = number_found + sir[i+j];
                    j=j+1;
                    if (i + j > len(sir)-1):
                        break

    return number_found
    print("\n")

print(extract_number("abc123ab7"))
print("\n8-------------");
#8
def bits_count(nr):
    contor = 0;
    while(nr>0):
       if(nr%2==1):
           contor = contor + 1;
       nr = nr //2;
    return contor;

print(bits_count(24));
print("\n9-------------");
#9
def most_appearances(sir):
    s = sir.lower();
    frecventa = {}
    for element in s:
        if element in frecventa:
            frecventa[element] += 1
        else:
            frecventa[element] = 1

    max=0;

    for key, value in frecventa.items():
        if value > max:
            max  = value;
            letter = key;

    return letter;

    # s = sir.lower();
    # frecventa = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
    # for c in s:
    #     val = ord(c)-97;
    #
    #     frecventa[val] = frecventa[val] + 1;
    # frecventa[5] = 100;
    # for i in frecventa:
    #     print(frecventa[i], end=' ');

print(most_appearances("aadsgsdgAAAAAA"));
print("\n10-------------");
#10
# Am facut doua variante, una cu functii predefinite si una fara deoarece nu stiu daca avem voie sa folosim functii
#predefinite la aceasta tema.
def words_count(sir):
    list_words = sir.split();
    nr = len(list_words);
    return nr;

def word_count2(sir):
    count = 0;
    for c in range(0, len(sir)):
        if sir[c] == ' ':
            count = count + 1;
            if c == len(sir)-1:
                count = count - 1;

    count = count + 1;
    return count;

print(words_count("Nu stiu daca este bine asa "))

#Am pus doua ca sa vad daca merge bine atunci cand ultimul caracter este ' '
print(word_count2("Nu stiu daca este bine asa"))
print(word_count2("Nu stiu daca este bine asa "))





