n_a=float(input("escriba el numero a: "))
n_b=float(input("escriba el numero b: "))
n_c=float(input("escriba el numero c: "))
n_d=(((n_b**2)-(4*n_a*n_c))**1/2)
y1=(((-1*n_b)-(n_d**1/2))/2*n_a)
y2=(((-1*n_b)+(n_d**1/2))/2*n_a)
if n_d>0:
 print("Es negativo en:",y1 , "Es positivo en:",y2)
else:
    if n_d==0:
        print("El valor x1:", (-n_d/2*a), "es igual que x2: ", (-n_d/2*a))
    else:
        if n_d<0:
            print("no tiene solucion en los reales")