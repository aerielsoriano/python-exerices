import turtle

def square(draw):
  squareCount = 0
  
  while squareCount != 4:
    draw.forward(100)
    draw.right(90)
    squareCount += 1

def powerCircle():
  pen = turtle.Turtle()
  pen.shape("turtle")
  pen.speed(4)
  penCount = 0
  
  while penCount != 36:
    square(pen)
    pen.right(10)
    penCount += 1
    
  pen.right(90)
  pen.forward(200)
  
powerCircle()
