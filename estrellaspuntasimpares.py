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

    turtle.end_fill()
    turtle.done()
    
if __name__ == '__main__':
    start = int(input("¿Cuantas puntas quieres que tenga tu estrella?(tiene que ser un numero impar):"))
    estrella(start)