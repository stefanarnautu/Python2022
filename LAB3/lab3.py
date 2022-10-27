

print("1------------------------")
def ex1(a, b):
    #am pus union in loc de diferenta simetrica
    return [set(a | b), set(a.union(b)), set(a - b), set(b - a)]
print(ex1({1,2,3},{2,3,4,5}))

print("2------------------------")

def ex2(my_string):
    frecventa = {}
    for c in my_string:
        if c in frecventa:
            frecventa[c] = frecventa[c] + 1
        else:
            frecventa[c] = 1
    return frecventa

print(ex2("Ana are mere"))

print("3------------------------")

def rec(a,b):
    if len(a)!= len(b):
        return False
    for key in a:
        if key not in b:
            return False
        else:
            if a[key] != b[key]:
                return False
    return True


print(rec({1:"a",2:"b",3:"c"},{1:"a",2:"b",3:"c",4:"a"}))

print("4------------------------")

#am pus parametri variabili
def build_xml_element(tag,content,*args):
    rez = "<" + tag + " "
    for el in args:
        rez = rez + el + " "
    rez = rez + ">" + content + "</" + tag + ">"
    return rez

print(build_xml_element("a","Hello there","href=\"http://python.org\"", "_class=\"my-link\"", "id=\"someid\""))

print("5------------------------")

def validate_dict(rules, dict):
    for k in dict:
       ok = 0
       #am sters primul si ultimul cuvant din string pentru a face verificare
       string_for_check_midd = dict[k]
       string_for_check_midd = string_for_check_midd[string_for_check_midd.index(' ') + 1:string_for_check_midd.rindex(' ')]
       for rule in rules:
           if k == rule[0]:
               ok = 1
               if not (dict[k].startswith(rule[1]) and dict[k].endswith(rule[3]) and rule[2] in string_for_check_midd):
                   return False
       if ok == 0:
           return False
    return True

print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
      {"key1": "come inside, it's too cold out", "key2": "start this middle is not valid winter"}))
print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
      {"key1": "come inside, it's too cold out", "key2": "this is not valid winter"}))

print("6------------------------")

def ex6(s):
    #am pus initializarea corect
    uniq = set()
    dupli = set()
    for e in s:
        count = 0
        for e1 in s:
            if e == e1:
                count = count+1
        if count == 1:
            uniq.add(e)
        elif count > 1:
            dupli.add(e)
    return uniq , dupli


print(ex6(["a","a","b","cdfgfgjzdgfd","da","da","nu","d","d","e","f","k","b","d","aa","c","df",2,4,5,5]))

print("7------------------------")

def ex7(*sets):
    rez = {}

    for i in range(0,len(sets)):
        for j in range(i+1,len(sets)):
            name1 = str(sets[i]) + "|" + str(sets[j])
            name2 = str(sets[i]) + "&" + str(sets[j])
            name3 = str(sets[i]) + "-" + str(sets[j])
            name4 = str(sets[j]) + "-" + str(sets[i])
            rez[name1] = sets[i] | sets[j]
            rez[name2] = sets[i] & sets[j]
            rez[name3] = sets[i] - sets[j]
            rez[name4] = sets[j] - sets[i]
    return rez

print(ex7({1,2,3},{3,4,5},{11,12,3}))

print("8------------------------")

def loop(s):
    curent_key = "start"
    rez = []
    while True:
        if s[curent_key] in rez:
            return rez
        rez.append(s[curent_key])
        curent_key = s[curent_key]

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

print("9------------------------")

def my_function(*args,**kwargs):
    digits = list()
    for d in args:
        digits.append(d)
    print(digits)
    c = 0
    #cred ca asa trebuie facut cu kwargs
    for key,value in kwargs.items():
        if value in digits:
            c = c + 1
    return c
print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))