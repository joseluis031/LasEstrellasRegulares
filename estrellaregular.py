import turtle #es como un puntero que se va desplazando y dibujando a su vez
def estrella(start):
    turtle.color('grey')
    turtle.fillcolor("yellow")
    turtle.begin_fill()

    while True:
        turtle.forward(200)
        if start % 4 == 0:
            turtle.right(180 - (360/start))
        if start % 3 == 0:
            turtle.right((360/start) + 120)
        else:
            break
        if abs(turtle.pos()) < 1: #para que el puntero se pare una vez dibujado toda la estrella
            break
    turtle.end_fill()        
    turtle.done() #para que no se cierre la pantalla turtle
if __name__ == '__main__':
    start= int(input("¿Cuántas puntas quieres que tenga tu estrella?: "))
    estrella(start)
