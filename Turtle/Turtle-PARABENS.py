import turtle

# Configuração inicial da tela
tela = turtle.Screen()
tela.bgcolor("white")

# Configuração da tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("red")
tartaruga.pensize(5)
tartaruga.speed(10)

# Desenhar a letra P
tartaruga.penup()
tartaruga.goto(-250,0)
tartaruga.pendown()
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.circle(33,-180)
tartaruga.penup()
tartaruga.goto(-250,0)
tartaruga.left(0)
tartaruga.forward(45)

# Desenhar a letra A
tartaruga.pendown()
tartaruga.left(76)
tartaruga.forward(120)
tartaruga.right(152)
tartaruga.forward(120)
tartaruga.back(45)
tartaruga.right(104)
tartaruga.forward(35)
tartaruga.penup()
tartaruga.goto(-128,0)
tartaruga.pendown()

# Desenhar a letra R
tartaruga.left(270)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.circle(30,-180)
tartaruga.right(60)
tartaruga.forward(68)
tartaruga.penup()
tartaruga.left(60)
tartaruga.forward(20)
tartaruga.pendown()

# Desenhar a letra A
tartaruga.pendown()
tartaruga.left(76)
tartaruga.forward(120)
tartaruga.right(152)
tartaruga.forward(120)
tartaruga.back(45)
tartaruga.right(104)
tartaruga.forward(35)
tartaruga.penup()
tartaruga.goto(-128,0)
tartaruga.left(180)
tartaruga.forward(127)
tartaruga.pendown()

# Desenhar a letra B
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.circle(30,-180)
tartaruga.left(180)
tartaruga.circle(30,-180)
tartaruga.penup()
tartaruga.left(0)
tartaruga.forward(47)
tartaruga.pendown()

# Desenhar a letra E
tartaruga.forward(35)
tartaruga.back(35)
tartaruga.left(90)
tartaruga.forward(60)
tartaruga.right(90)
tartaruga.forward(35)
tartaruga.back(35)
tartaruga.left(90)
tartaruga.forward(60)
tartaruga.right(90)
tartaruga.forward(35)
tartaruga.penup()
tartaruga.goto(100,0)
tartaruga.pendown()

# Desenhar a letra N
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.right(160)
tartaruga.forward(127)
tartaruga.left(160)
tartaruga.forward(120)
tartaruga.penup()
tartaruga.back(120)
tartaruga.right(90)
tartaruga.forward(40)
tartaruga.pendown()

# Desenhar a letra S
tartaruga.forward(15)
tartaruga.circle(30,180)
tartaruga.left(170)
tartaruga.circle(30,-180)
tartaruga.left(-170)
tartaruga.forward(15)

# Esconder a tartaruga
tartaruga.hideturtle()

# Manter a tela aberta
turtle.done()