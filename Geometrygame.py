class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.low_left.x < self.x < rectangle.up_right.x \
                and rectangle.low_left.y < self.y < rectangle.up_right.y:
            return True
        else:
            return False

class Rectangle:
    def __init__(self, low_left, up_right):
        self.low_left = low_left
        self.up_right = up_right

    def area(self):
        return (self.up_right.x - self.low_left.x) * (self.up_right.y - self.low_left.y)

from random import randint

rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10,19), randint(10, 19)))
print("Rectangle co-ordinates:")
print(f"( {rectangle.low_left.x}, {rectangle.low_left.y}) and ({rectangle.up_right.x},{rectangle.up_right.y})")

user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))
if user_point.falls_in_rectangle(rectangle) == True:
  print("YOU WON")
else:
  print('Try again')

user_area = input("Enter rectangle area:")
print("Your area was off by:", rectangle.area() - int(user_area), "units")
if rectangle.area() - int(user_area) == 0:
    print("YOU HAVE WON THIS GAME TOO")

else:
    print('OOPS! NICE TRY')