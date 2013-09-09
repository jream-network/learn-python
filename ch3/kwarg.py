# KWARG = KeyWord Arguments

def sublime(rating, color = None, other = None):
    if color is not None:
        print color
    if other is not None:
        print other

    return rating

print sublime(10, other = "life")