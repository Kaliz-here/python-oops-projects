class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        # Rectangle formula is Area = length × width    
        return self.lenght * self.width

    def perimeter(self):
        # Perimeter = 2 × (length + width)
        return 2 * (self.lenght + self.width)

rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())