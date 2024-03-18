from turtle import *

#forward faz o desenho ser feito na direção apontada
forward(100)
#left faz o cursor dar um giro de x Graus, mudando assim sua rota
left(120)
forward(100)
#backward faz o contrario do forward, dando uma ré
backward(130)
#right faz o inverso do left, fazendo um giro na direção oposta
right(120)
backward(115)

#color muda a cor da reta
color("Blue")
left(88)
forward(200)

#width muda a largura da linha
color("red")
width(3)
left(20)
forward(70)

#up e down para mover a caneta sem desenhar(Utilizar sempre primeiro o up para levantar a caneta)
up()
color("Grey")
forward(30)
down()
forward(20)

#Home para trazer ao seu local de origem
up()
home()
down()

