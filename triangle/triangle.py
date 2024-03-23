def triangle(sides):

    return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1]) and (sides[0] + sides[1] + sides[2] != 0)
        
    
   

def equilateral(sides):

    return triangle(sides)==True and sides[0]==sides[1]==sides[2]
     
    


def isosceles(sides):

    return triangle(sides) == True and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])
     
     


def scalene(sides):

    return triangle(sides) == True and sides[0] != sides[1] != sides[2] != sides[0]