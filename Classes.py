###########  CLASSES  ###########
#################################


# Like in other languages: Classes in Python are blueprints for creating Objects

x = 1
print(type(x))
# prints  <class 'int'>   Integers are classes, same for lists, bool's strings etc
y = "derpify"
print(type(y))
# prints  <class 'str'>

# Create a 'point' class .. Pascal convention used for classes like in other languages


class Point:
    # Methods/Fields
    # MagicMethod Constructor (uses __init__) with x and y instance attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Below, default_color is a CLASS-LEVEL ATTRIBUTE: It will be the same value for all later instance objects
    default_color = "purple"
    second_color = "red"
    # method-function's by convention have at least 1 parameter, usually 'self'
    # NOTE 'self' is a reference to the current instantiated object of the class.. similar to 'this'

    def draw(self):
        print(F"Point ({self.x}, {self.y})")


# Object instantiation. Rather than using 'new' keyword as in other langs, simply assign the
# object to a function-call of the parent Class
point1 = Point(8, 10)

print(type(point1))
# prints  <class '__main__.Point'>

# IsInstance method to check inheritance of objects
print(isinstance(point1, Point))
# prints  True

##  CONSTRUCTORS  ##
####################
# Same as other languages. Used to bundle-initialize all initial data for an object instance of a class
# In our Point example the objects initial x and y coordinate values are initialized
point2 = Point(3, 8)

print(point2.x)
# prints  3

point1.draw()
# Recall when we defined this method on the Point class we passed 'self' to the draw method.
# It is not necessary to do so, but technically, what is happening is this point1.draw(point) referencing itself
# Point (8, 10)

##  INSTANCE ATTRIBUTES vs CLASS ATTRIBUTES ##
##########################
# NOTE All of the attributes/fields we have defined so far for the Point Class and all of its
# instantiated objects are Instance attributes: They belong to the Point instances
# NOTE Objects are DYNAMIC in Python, like in Javascript, and UNlike C#/Java
# CLASS Attributes however are defined at the Class level and ARE THE SAME for all later instances
point2.z = 13

print(point2.z)
# prints  13

# Print the Class attribute default_color which is the same for all objects instantiated from Point class
print(point2.default_color)
# prints  purple
point3 = Point(4, 4)
print(point3.default_color)
# also: purple
# With Class attributes you can also simply call the attribute on the class (capital P Point)
print(Point.default_color)
# prints purple
# Since Classes are reference types. If you change the value for a Class attribute, it will be visible
# to all object instances of that Class
Point.second_color = "black"
print(point1.second_color)
# prints  black (since we changed it from it's original value of red)


###  INSTANCE VS CLASS METHODS  ###
###################################

# On our above defined class Point. the Draw method is an instance method. Meaning. You wan't to
# Draw for a specific point instance object
point4 = Point(50, 90)

print(type(point4))
point4.draw()
