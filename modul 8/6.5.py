class Triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a and(self.a > 0, self.b > 0, self.c > 0):
            return True
        else:
            return False
    def get_triangle_area(self):
        is_tiangle
        if self.is_triangle():
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
