import os
#nu cred ca pot sa vin(intru online) la seminarul de vineri dimineata(voi fi in tren si nu voi avea laptopul cu mine)
#daca sunt nelamuriri, as putea sa le clarific seminarul urmator, daca se poate
print("1-------------------------------------")

def ex1(path):
    rez = list()
    for f in os.listdir(path):
        if len(os.path.splitext(f)[-1]) > 0:
            if os.path.splitext(f)[-1][1:] not in rez:
                rez.append(os.path.splitext(f)[-1][1:])
    return sorted(rez)
print(ex1((os.path.join("D:\\","a.FACULTATE","x.An2Sem2","SGBD"))))

print("\n2-----------------------------------")

def ex2(director, fisier):
    fd = open(fisier, "w")
    for f in os.listdir(director):
        if f.startswith("A"):
            fd.write(os.path.join(director,f)+"\n")
ex2("D:\\a.FACULTATE","D:\\a.FACULTATE\PYTON\LAB4\ex2.txt")

print("\n3-----------------------------------")

lista_recursiva = list()
def parcurge_recursiv(my_path):
    if os.path.isfile(my_path):
        ok = 0
        for i in range(0,len(lista_recursiva)):
            if os.path.splitext(my_path)[-1] == lista_recursiva[i][0]:
                temp_list = list(lista_recursiva[i])
                temp_list[1] = temp_list[1] + 1
                lista_recursiva[i] = tuple(temp_list)
                ok = 1
        if ok == 0:
            lista_recursiva.append((os.path.splitext(my_path)[-1],1))
        return True

    for f in os.listdir(my_path):
        parcurge_recursiv(os.path.join(my_path,f))

def ex3(my_path):
    if os.path.isfile(my_path):
        return open(my_path,"r").read(20)
    if os.path.isdir(my_path):
        parcurge_recursiv(my_path)
        rez = lista_recursiva
        rez.sort(key=lambda x:x[1],reverse=True)
        return rez


print("Exemplul 1\n",ex3("D:\\a.FACULTATE\PYTON\LAB4\ex2.txt"))
print("Exemplul 2\n",ex3("D:\\a.FACULTATE\\x.An2Sem2\Engleza"))

print("\n4-----------------------------------")

def ex4(path):
    rez = list()
    for f in os.listdir(path):
        if os.path.splitext(f)[-1][1:] not in rez and len(os.path.splitext(f)[-1][1:])>1:
            rez.append(os.path.splitext(f)[-1][1:])
    return sorted(rez)

while True:
    path = input("Please enter a path:\n")
    if os.path.exists(path):
        break
#D:\a.FACULTATE\x.An2Sem2\Engleza
print(ex4(path))

print("\n5-----------------------------------")

class Gresit(Exception):
    pass


def ex5(target, to_search, lista_fisiere):
    if os.path.isfile(target):
        ok = 0
        if os.path.splitext(target)[-1][1:] == "txt":
            with open(target, 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    if to_search in line:
                        lista_fisiere.append(target)
                        break
        return True
    if not os.path.isfile(target):
        for f in os.listdir(target):
            ex5(os.path.join(target,f),to_search,lista_fisiere)
        return lista_fisiere

lista_fisiere = list()
target = "D:\\a.FACULTATE\\x.An2Sem2\Engleza"
try:
  if os.path.isdir(target) == False and os.path.isfile(target) == False:
      raise Gresit
  print(ex5(target,"degrees",lista_fisiere))
except Gresit:
        print ("Nu este fisier sau director")

print("\n6-----------------------------------")

from typing import List, Callable

def print_error(t,s):
    print("Programul s-a terminat cu instanta:",t," ",s)

def ex6(target, to_search, lista_fisiere,callback):
    try:
        if os.path.isdir(target) == False and os.path.isfile(target) == False:
            raise Exception
    except Exception as e:
        callback(target,to_search)
        return
    if os.path.isfile(target):
        ok = 0
        if os.path.splitext(target)[-1][1:] == "txt":
            with open(target, 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    if to_search in line:
                        lista_fisiere.append(target)
                        break
        return True
    if not os.path.isfile(target):
        for f in os.listdir(target):
            try:
                if os.path.isdir(target) == False and os.path.isfile(target) == False:
                    raise Exception
                ex6(os.path.join(target,f),to_search,lista_fisiere,callback)
            except Exception as e:
                print(e)
        return lista_fisiere

lista_fisiere = list()
#target = "D:\\a.FACULTATE\\x.An2Sem2\Engleza"
print(ex6("D:\\a.FACULTATE\\x.An2Sem2\Engleza","degrees",lista_fisiere,print_error))

print("\n7-----------------------------------")

def ex7(path):
    try:
        if os.path.isfile(path):
            rez = dict()
            rez.update({"full_path" : path})
            file_size = os.stat(target)
            rez.update({"file_size" : file_size.st_size})
            rez.update({"file_extension" : os.path.splitext(path)[-1][1:]})
            rez.update({"can_read": os.access(path, os.R_OK)})
            rez.update({"can_write": os.access(path, os.W_OK)})
            return rez
        else:
            raise Exception("Nu este fisier")
    except Exception as e:
        return e

print(ex7("D:\\a.FACULTATE\PYTON\LAB4\ex2.txt"))
print(ex7("D:\\a.FACULTATE\PYTON\LAB4\exsfasf.txt"))

print("\n8-----------------------------------")

def ex8(dir_path):
    try:
        if not os.path.isdir(dir_path):
            raise Exception("Nu este director")
        rez = list()
        for f in os.listdir(dir_path):
            rez.append(os.path.abspath(f))
    except Exception as e:
        print(e)
        return ""
    return rez


print(ex8("D:\\a.FACULTATE\PYTON"))