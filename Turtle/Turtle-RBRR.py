import turtle

# Configuração inicial da tela
tela = turtle.Screen()
tela.bgcolor("white")

# Configuração da tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("blue")
tartaruga.pensize(10)
tartaruga.speed(10)

#Tartaruga mexe
tartaruga.penup()
tartaruga.goto(-120,0)
tartaruga.pendown()

#R
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.circle(30,-180)
tartaruga.right(60)
tartaruga.forward(68)

#Espaço
tartaruga.penup()
tartaruga.left(60)
tartaruga.forward(20)
tartaruga.pendown()

#B
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.circle(30,-180)
tartaruga.left(180)
tartaruga.circle(30,-180)

#Espaço
tartaruga.penup()
tartaruga.left(0)
tartaruga.forward(50)
tartaruga.pendown()

#R
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.circle(30,-180)
tartaruga.right(60)
tartaruga.forward(68)

#Espaço
tartaruga.penup()
tartaruga.left(60)
tartaruga.forward(20)
tartaruga.pendown()

#R
tartaruga.left(90)
tartaruga.forward(120)
tartaruga.left(90)
tartaruga.circle(30,-180)
tartaruga.right(60)
tartaruga.forward(68)


# Esconder a tartaruga
tartaruga.hideturtle()

# Manter a tela aberta
turtle.done()