import turtle

def drawShape ():
  window = turtle.Screen()
  window.bgcolor("red")
  
  square = turtle.Turtle()
  squareCount = 0
  
  while squareCount != 4:
    turtle.forward (100)
    turtle.right(90)
    squareCount += 1

  Circle = turtle.Turtle()
  Circle.circle(100)
  
  triangle = turtle.Turtle()
  triangleCount = 0
  
  while triangleCount != 3:
    triangle.forward (90)
    triangle.left (120)
    triangleCount += 1

  window.exitonclick()
  
drawShape()
  
  