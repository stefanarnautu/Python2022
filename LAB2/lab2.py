
print("1------------------------");

def first_n_fibo(n):
    fib = [];
    fib.append(0);
    fib.append(1);
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2]);

    return fib;

print(first_n_fibo(6));

print("\n2------------------------");

def only_prime(my_numbers):
    prim = [];

    for a in my_numbers:
        ok = 1;
        if a > 1:
            for d in range(2,a//2):
                if a%d == 0:
                    ok =0;

        if a > 1 and ok == 1:
            prim.append(a);

    return prim;


print(only_prime([1,12,13,56,3,2,29]));

print("\n3------------------------");

def ex3(a,b):
    return list(set(a) & set(b)),list(set(a) | set(b)), list(set(a) - set(b)),list(set(b) - set(a));

print(ex3([1,2,3,4,5,6],[4,5,6,7,8]));

print("\n4------------------------");

def note_muzicale(note,pozitii,start):
    rez = []
    rez.append(note[start])
    for i in range(0,len(pozitii)):
        rez.append(note[(start+pozitii[i])%(len(note))])
        start = start + pozitii[i]
    return rez
print(note_muzicale(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

print("\n5------------------------");

def main_diagonal(M):
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            if(i>j):
                M[i][j] = 0;
    return M;


mat = [
       [1,4,3,2,1],
       [3,3,6,3,2],
       [5,7,3,6,8],
       [3,6,9,1,3],
       [5,9,3,2,5]
      ]

print(main_diagonal(mat));

print("\n6------------------------")

def exaclty_n(n,*lists):
    i= 0
    frecventa = {}
    for lista in lists:
        for element in lista:
            if element in frecventa:
                frecventa[element] += 1
            else:
                frecventa[element] = 1

    rez = []
    for key, value in frecventa.items():
        if value == n:
            rez.append(key)
    return rez

print(exaclty_n(2, [1,2,3], [2,3,4],[4,5,6],[4,1,"list"]))

print("\n7------------------------")

def palindroms(numbers):
    how_many = 0;
    maxim = 0;
    for el in numbers:
        print(el)
        count=0
        copy = el
        while copy>0:
            copy= copy//10
            count=count+1
        i=0
        ok = 1;
        while i < count/2:
           if el%pow(10,i+1)//pow(10,i) != el//pow(10,count-(i+1))%10:
               ok = 0;
           i= i + 1
        if ok == 1:
            how_many = how_many + 1;
        if el > maxim and ok == 1:
            maxim = el;

    return [how_many,maxim]

a = [121,56765,1213,343]
print(palindroms(a))

print("\n8------------------------")

def ex8(div,words,flag):
    result = []
    for i in words:
        list_of_letters = []
        for c in i:
            if ord(c)%2 == 0 and flag == True:
                list_of_letters.append(c)
            elif ord(c)%2 != 0 and flag == False:
                list_of_letters.append(c)
        result.append(list_of_letters)
    return result

print(ex8(2,["test", "hello", "lab002"],False))

print("\n9------------------------")

def ex9(tribuna):
    rez = []
    for i in range(0,len(tribuna[0])):
        for j in range(1,len(tribuna)):
            for x in range(0,j):
                if tribuna[j][i] <= tribuna[x][i]:
                    rez.append([j,i])
                    break

    return rez

print(ex9([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]]))

print("\n10-----------------------")

def ex10(*lists):
    i = 0;
    rez = []
    for k in range(0, len(lists[i])):
        new_list = []
        for l in lists:
            new_list.append(l[i])
        rez.append(new_list)
        i = i + 1
    return rez

print(ex10([1,2,3], [5,6,7], ["a", "b", "c"]))

print("\n11-----------------------")

def ex11(tuples):
    copy = tuples
    for i in range(0,len(tuples)):
        for j in range(i+1,len(tuples)):
            if tuples[i][1][2] > tuples[j][1][2]:
                aux = copy[i]
                copy[i] = copy[j]
                copy[j] = aux
    return copy


a = [('abc', 'bcd'),('abc', 'zza'),('abc', 'zzb')]
print(ex11(a))

print("\n12-----------------------")
def group_by_rhyme(words):
    rez = {}
    for w1 in words:
        if w1[-2:] in rez:
            rez[w1[-2:]].append(w1)
        else:
            rez[w1[-2:]] = []
            rez[w1[-2:]].append(w1)
    return rez

print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
