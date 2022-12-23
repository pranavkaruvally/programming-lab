def base_area(length, breadth):
    return 2*length*breadth

def lateral_surface_area(breadth, height):
    return 4*(breadth*height)

def total_surface_area(length, breadth, height):
    return base_area(length, breadth) + lateral_surface_area(breadth, height)

def volume(length, breadth, height):
    return length*breadth*height
