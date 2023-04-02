import turtle

# Ekranı ayarla
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")

# Kalem ayarları
pen = turtle.Turtle()
pen.pensize(4)
pen.speed(2)

# Başla çizim
pen.penup()
pen.goto(-80, -150)
pen.pendown()

# Şapka
pen.color("red")
pen.begin_fill()
pen.forward(160)
pen.left(90)
pen.circle(50, 180)
pen.left(90)
pen.forward(160)
pen.end_fill()

# Yüz
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Kaşlar
pen.penup()
pen.goto(-50, 50)
pen.pendown()
pen.right(60)
pen.forward(40)

pen.penup()
pen.goto(50, 50)
pen.pendown()
pen.left(120)
pen.forward(40)

# Gözler
pen.penup()
pen.goto(-35, 20)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

pen.penup()
pen.goto(35, 20)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

pen.penup()
pen.goto(-30, 10)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

pen.penup()
pen.goto(40, 10)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# Burun
pen.penup()
pen.goto(0, 10)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Ağız
pen.penup()
pen.goto(-30, -30)
pen.pendown()
pen.right(90)
pen.circle(30, 180)

# Boyunluk
pen.penup()
pen.goto(-80, -150)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.forward(160)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(160)
pen.left(90)
pen.forward(30)
pen.end_fill()

# Tamamlandı
pen.hideturtle()

turtle.done()
