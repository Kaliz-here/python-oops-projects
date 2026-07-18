class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return 22/7 * (self.radius ** 2)
    
    def circle_circumference(self):
        return 2 * (22/7 * self.radius)
    
circle = Circle(5)
print("Area is : ", circle.circle_area())
print("Circumference is ", circle.circle_circumference())