class Rectangle:
    def __init__(self, length, width):
        if length > 0 and width > 0:
            self.length = length
            self.width = width
        else:
            raise ValueError("Integer must be positive..!")
        
    def rectangle_area(self):
        return self.length * self.width
    
    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width
        
    def __str__(self):
        return  f"Rectangle(Length : {self.length}, Width : {self.width})"
        
    def display(self):
        print(f"Area of rectangle is {self.rectangle_area()}")
        print(f"Perimeter of rectangle is {self.rectangle_perimeter()}")

rectangle = Rectangle(10, 20)
print(rectangle)
rectangle.display()
print(rectangle.is_square())