import math
i = 0
while i <= 345:
    rads = (i * math.pi)/180
    print("The sin value of", i, "degrees is", math.sin(rads))
    print("The cos value of", i, "degrees is", math.cos(rads))
    i += 15