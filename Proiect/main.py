import matplotlib.pyplot as plt
import numpy as np

def proj_29(list_with_dots):
    if type(list_with_dots)!=list:
        print("Input-ul trebuie sa fie de tip list")
        return 0
    else:
        for t in list_with_dots:
            if type(t)!=tuple:
                print("Nu toate elementele listei sunt tuple de integer")
                return 0
    if len(list_with_dots)==0:
        print("Lista este nula")
        return 0
    try:
        x,y = zip(*list_with_dots)
        x_square = list(map(lambda e: e*e,x))
        xy = list(map(lambda a,b:a*b,x,y))
        m = ((len(list_with_dots) * sum(xy)) - (sum(x) * sum(y))) / ((len(list_with_dots) * sum(x_square)) - (sum(x) * sum(x)))
        b = (sum(y) - (m * sum(x))) / len(list_with_dots)
        return round(m,4),round(b,4)
    except ValueError:
        print("Trebuie cel putin un nod pentru a afisa graficul si cel putin doua noduri pentru a afisa ecuatia grafic")
    except ZeroDivisionError:
        print("Nu putem reprezenta axa cu doar un punct")
"""
def project_29(list_with_dots):
    x = list()
    y = list()
    for el in list_with_dots:
        x.append(el[0])
        y.append(el[1])
    x_square = list(map(lambda e: e*e,x))
    xy = list(map(lambda a,b:a*b,x,y))
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_square= sum(x_square)
    sum_xy= sum(xy)
    n = len(list_with_dots)
    m = ((n*sum_xy)-(sum_x*sum_y))/((n*sum_x_square)-(sum_x*sum_x))
    b = (sum_y-(m*sum_x))/n
    return round(m,4),round(b,4)
"""

proj_29([])
proj_29([(1.21,1.69), (3,5.89)])
proj_29([(1.21,1.69)])
proj_29([(1.21,1.69), (3,5.89), (5.16,4.11), (8.31,5.49), (10.21,8.65)])
proj_29("Asa nu")
proj_29([(1.21,1.69), "A", (5.16,4.11), (8.31,5.49), (10.21,8.65)])
proj_29([(1.21,1.69), (5.16,4.11), (8.31,5.49), 100])
proj_29([(1.21,1.69), ("b","A"), (8.31,5.49), 100])

def represent(list_with_dots):
    if type(list_with_dots)!=list:
        print("Input-ul trebuie sa fie de tip list")
        return 0
    else:
        for t in list_with_dots:
            if type(t)!=tuple:
                print("Nu toate elementele listei sunt tuple de integer")
                return 0
    if len(list_with_dots)==0:
        print("Lista nu contine noduri")
        return 0
    try:
        m,b = proj_29(list_with_dots)
        max_x = max(list_with_dots, key=lambda item: item[0])[0]
        min_x = min(list_with_dots, key=lambda item: item[0])[0]
        x = np.linspace(min_x-2, max_x+2, 100)
        y = m * x + b
        plt.plot(x, y,color='blue')
        x2, y2 = zip(*list_with_dots)
        plt.plot(x2, y2, color='green', linestyle='dashed', linewidth=2,marker='o', markerfacecolor='blue', markersize=6)
        plt.title("Graph of y="+ str(m) +"x+"+str(b))
        for i  in range(0,len(x2)):
            plt.annotate("("+str(x2[i])+","+str(y2[i])+")", (x2[i], y2[i]))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.show()
    except ValueError:
        print("Trebuie cel putin un nod pentru a afisa graficul si cel putin doua noduri pentru a afisa ecuatia grafic")
    except ZeroDivisionError:
        print("Nu putem reprezenta axa cu doar un punct")
        x2, y2 = zip(*list_with_dots)
        plt.plot(x2, y2, color='green', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='blue',markersize=6)
        for i in range(0, len(x2)):
            plt.annotate("(" + str(x2[i]) + "," + str(y2[i]) + ")", (x2[i], y2[i]))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.show()
    except TypeError:
        print("Eroare provocate de faptul ca algoritmul de generare a axei returneaza 0")

represent([])
represent([(1.21,1.69), (3,5.89)])
represent([(1.21,1.69)])
represent([(1.21,1.69), (3,5.89), (5.16,4.11), (8.31,5.49), (10.21,8.65)])
represent("Asa nu")
represent([(1.21,1.69), "A", (5.16,4.11), (8.31,5.49), (10.21,8.65)])
represent([(1.21,1.69), (5.16,4.11), (8.31,5.49), 100])
represent([(1.21,1.69), ("b","A"), (8.31,5.49), 100])



















