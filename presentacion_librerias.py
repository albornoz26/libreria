#para la presentacion de librerias
import matplotlib.pyplot as plt
x,y,z,w,i=0,0,0,0,0

def menu():
    global x,y,z,w,i
    a='y'
    while a=='y':
        op=int(input('''que lenguaje de programacion es de su preferencia
    1- python
    2- javascript
    3- c++
    4- HTML
    5- otro \nOpcion: '''))
        if op==1:
            x=x+1
            print('\nsu voto se ha registrado para python\n')
        elif op==2:
            y=y+1
            print('\nsu voto se ha registrado para javascript\n')
        elif op==3:
            z=z+1
            print('\nsu voto se ha registrado para c++\n')
        elif op==4:
            w=w+1
            print('\nsu v-oto se ha registrado para HTML\n')
        elif op==5:
            i=i+1
            print('\nsu voto se ha registrado para otro\n')
        else:
            print('\ndigite una opcion correcta\n')
            menu()
            
        a=input('''desea volver a votar?
    y=si
    n=no \n''')
        if a=='n':
            break

menu()
## Declaramos valores para el eje x
eje_x = ['Python', 'javascript', 'c++', 'HTML','otro']
 
## Declaramos valores para el eje y
eje_y = [x,y,z,w,i]
 
## Creamos Gráfica
plt.bar(eje_x, eje_y)
 
## texto en el eje y
plt.ylabel('Cantidad de usuarios', fontdict = {'fontsize':15, 'fontweight':'bold', 'color':'tab:purple'})
 
## texto en el eje x
plt.xlabel('Lenguajes de programación', fontdict = {'fontsize':15, 'fontweight':'bold', 'color':'tab:blue'})
 
## Título de Gráfica
plt.title('Usuarios de lenguajes de programación', fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:green'})
 
## Mostramos Gráfica
plt.show()
