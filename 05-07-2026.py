# circle manager
class Circle:
    def __init__(self, radius):
        if(radius > 0):
            self.radius = radius
        else:
            raise ValueError("Invalid radius..!")
        
    def area(self):
        return 22/7 * (self.radius * self.radius)

    def circumference(self):
        return 2 * (22/7 * self.radius )
    
    def __str__(self):
        return f"Radius is : {self.radius}"

radius_objects = []
Radius = list(map(int, input("Enter radius : ").split()))
radius_list = []

#store objects in radius_object=[]
for circle_objects in Radius:
    circle = Circle(circle_objects)
    radius_objects.append(circle)

for circle_details in radius_objects:
    print(circle_details)
    print("Area : ", circle_details.area())
    radius_list.append(round(circle_details.area(), 2))
    print("Circumference : ", circle_details.circumference())
    print()


largest_circle = radius_objects[0]

for circle in radius_objects:
    if(circle.area() > largest_circle.area()):
        largest_circle = circle

print("\nLargest Area Circle")
print(largest_circle)
print("Area : ", round(largest_circle.area(), 2))
print("Circumference", round(largest_circle.circumference(), 2))