import curses
from random import randint

def SnakeGame():
    ### Preparamos la ventana
    curses.initscr()
    ### Especificamos el tamaño de la ventana como 20y 60x 
    ventana = curses.newwin(20,60,0,0)
    ventana.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    ventana.border(0)
    ventana.nodelay(1)

    ### Necesitamos llevar un registro de la serpiente y de la comida
    snake=[(4,10),(4,9),(4,8)]
    fruta=(10,20)

    ventana.addch(fruta[0],fruta[1],'#')

    ### Lógica del juego
    ESC=27
    tecla = curses.KEY_RIGHT

    score = 0
    while tecla != ESC:
        ### Agregamos el puntaje en pantalla
        ventana.addstr(0,2,'Score: '+str(score))
        ventana.timeout(150)

        tecla_anterior=tecla
        event = ventana.getch()
        tecla = event if event != -1 else tecla_anterior

        ### Nos aseguramos de que se ingrese una de las teclas de control
        if tecla not in [curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_UP,curses.KEY_DOWN,ESC]:
            tecla = tecla_anterior

        ### Calculamos la siguiente posición
        y = snake[0][0]
        x = snake[0][1]
        if tecla == curses.KEY_DOWN:
            y+=1
        if tecla == curses.KEY_UP:
            y-=1
        if tecla == curses.KEY_RIGHT:
            x+=1
        if tecla == curses.KEY_LEFT:
            x-=1

        ### Actualizamos la posición de la serpiente
        snake.insert(0,(y,x))

        ### Revisamos si golpeamos un borde
        if y==0 or y==19 or x==0 or x==59: break

        ### Revisamos si nos golpeamos a sí mismos
        if snake[0] in snake[1:]:break

        ### Revisamos si golpeamos una fruta
        if snake[0] == fruta:
            ### Desaparece la fruta
            score+=1
            fruta=()
            while fruta == ():
                ### La colocamos en un lugar aleatorio
                fruta = (randint(1,18),randint(1,58))
                ### Siempre y cuando no sea sobre la serpiente
                if fruta in snake:
                    fruta = ()
            ventana.addch(fruta[0],fruta[1],'#')
        else:
            ### Movemos la serpiente
            last = snake.pop()
            ventana.addch(last[0],last[1],' ')

        for c in snake:
            ventana.addch(c[0],c[1],'O')

        ventana.addch(snake[0][0],snake[0][1],'O')

    curses.endwin()
    print(f"Puntaje final: {score}")