# create class point to store point(x,y) inside it.
class point():
    def __init__(self, x_point, y_point):
        self.x = x_point
        self.y = y_point

# store first_point inside the class point
p1 = point(1, 2)
print(f"  X   of   First    Point   is:   {p1.x}")
print(f"  Y   of   First    Point   is:   {p1.y}")
print(" "*10 + "-"*10 + " "*10)#Just to separate the two parts.
# store second_point inside the class point
p2 = point(3, 4)
print(f"  X   of   Second   Point   is:   {p2.x}")
print(f"  Y   of   Second   Point   is:   {p2.y}")
