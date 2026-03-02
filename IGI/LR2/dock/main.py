import geometric_lib.square as square
import geometric_lib.circle as circle
import os

radius = float(os.environ.get("R", 0))
a = float(os.environ.get("A", 0))

print("Square area: ", circle.area(radius))
print("Rectangle area:", square.area(a))

