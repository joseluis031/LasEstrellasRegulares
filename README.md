# LasEstrellasRegulares

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/joseluis031/LasEstrellasRegulares.git)

Hemos conseguido un programa que, utilizando Turtle, es capaz de dibujar una estrella regular con el número de puntas que elija el usuario.

El diagrama de flujo es el siguiente:

![figma estrellas regulares](https://user-images.githubusercontent.com/91721888/146835899-d4e313f7-6087-4f6e-9eca-34dcfc0f897d.png)

El código de esta tarea es el siguiente:
```
import turtle #es como un puntero que se va desplazando y dibujando a su vez
def estrella(start):
    turtle.color('grey')
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.title('Tu estrella')
    while True:
        turtle.forward(200)
        if start == 5:
            turtle.right(144)
        
        elif start % 4 == 0:    #al dibujar estrellas, la suma de sus puntas siempre van a ser multiplo de 3 o de 4
            turtle.left(180 - (360/start))
        elif start % 3 == 0:
            turtle.right((360/start) + 120)
        else:
            break
            
        if start < 5:
            print("¡Recuerda que las estrellas mínimo tienen 5 puntass!!")
            turtle.write("No puedo dibujarte una estrella con esas puntas,lo siento")
            break
        if abs(turtle.pos()) < 1: #para que el puntero se pare una vez dibujado toda la estrella
            break
    turtle.end_fill()        
    turtle.done() #para que no se cierre la pantalla turtle

if __name__ == '__main__':
    start= int(input("¿Cuántas puntas quieres que tenga tu estrella?: "))
    estrella(start)
```

Código solo para puntas impares:
```
import turtle

def estrella(start):
    turtle.color('grey')
    turtle.begin_fill()
    turtle.title('Tu estrella')

    if start % 2 != 0:
        n = 180 - (360/(start*2))
        while True:
            turtle.forward(200)
            turtle.right(n)
            turtle.end_fill()
            if abs(turtle.pos()) < 1:
                break
    elif start % 2 == 0:
        pass
    turtle.end_fill()
    turtle.done()
    
if __name__ == '__main__':
    start = int(input("¿Cuantas puntas quieres que tenga tu estrella?(tiene que ser un numero impar):"))
    estrella(start)
```
