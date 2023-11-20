import turtle

# Crear un objeto Turtle
t = turtle.Turtle()

# Definir la longitud de los lados del pentágono
lado = 100

# Definir el ángulo de cada vértice del pentágono
angulo = 360 / 5

# Dibujar el pentágono
for i in range(5):
    t.forward(lado)
    t.right(angulo)

# Esperar a que el usuario cierre la ventana
turtle.done()
