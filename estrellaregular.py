import turtle #es como un puntero que se va desplazando y dibujando a su vez

def estrella():
    turtle.color('grey')
    turtle.fillcolor("yellow")
    turtle.begin_fill()

    while True:
        turtle.forward(200)
        turtle.left(200)
        if abs(turtle.pos()) < 1: #para que el puntero se pare una vez dibujado toda la estrella
            break
    turtle.end_fill()        

estrella()
turtle.done() #para que no se cierre la pantalla turtle

if __name__ == '__main__':
    start = int(input("¿Cuántas puntas quieres que tenga tu estrella?: "))
