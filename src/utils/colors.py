class Color:
    def __init__(self, r=0, g=0, b=0, a=0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def rgb(self):
        return (self.r, self.g, self.b)

    @property
    def rgba(self):
        return (self.r, self.g, self.b, self.a)

    def __str__(self):
        return "(r={r}, g={g}, b={b}, a={a})".format(r=self.r, g=self.g, b=self.b, a=self.a)


white = Color(r=255, g=255, b=255, a=255)
red = Color(r=255, g=0, b=0, a=255)
green = Color(r=0, g=255, b=0, a=255)
blue = Color(r=0, g=0, b=255, a=255)
yellow = Color(r=255, g=255, b=0, a=255)
black = Color(r=0, g=0, b=0, a=255)
light_green = Color(r=102, g=255, b=51, a=255)
brown = Color(r=135, g=84, b=8, a=255)
