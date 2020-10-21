import turtle

class Square:

    # constructor
    def __init__(self, l, c):
        self.length = l
        self.color = c


    def appear(self, x, y):
        barry = turtle.Turtle()
        barry.color( self.color )
        for i in range(4):
            barry.fd( self.length )
            barry.rt(90)
