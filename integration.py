# Write code to solve single, double, and triple integrals

from scipy.integrate import quad, dblquad, tplquad

# Single
def s_int(function, l, u):
    
    """
    SINGLE INTEGRAL
    function: function to integrate. Wrap in quotation marks. Must be in form of "y=..."
    l / u: lower and upper bounds of integration. May not be a function. Do not wrap in quotation marks.
    """
    
    def integrand(x):
        return eval(function)

    return quad(integrand, l, u)[0]

# Double
def d_int(function, llx, ulx, lly, uly):

    """
    DOUBLE INTEGRAL
    function: function in terms of z. Enclosed in quotation marks.
    llx / ulx: x lower and upper bounds of integration (outer integral) - CANNOT BE VARIABLE. Is NOT enclosed in quotation marks.
    lly / uly: y lower and upper bounds of integration (inner integral) - CAN BE VARIABLE. Enclosed in quotation marks.
    
    """
    
    def integrand(y, x):
        return eval(function)
    
    def upper_limit_y(x):
        return eval(uly)
    
    def lower_limit_y(x):
        return eval(lly)

    return(dblquad(integrand, llx, ulx, lower_limit_y, upper_limit_y)[0])

# Triple
def triple_integral(f, xl='x=0', xu='x=5', yl='y=0', yu='y=5', zl='z=0', zu='z=5'):
    
    """
    Everything must be wrapped as string. 
    
    Only works in cartesian coordinate system with order of integration being 'dx dy dx'.
    
    Write everything as an equality; 
      -  'f = ...' for function (does not need to be f)
      -  'x, y, or z = ... ' for bounds of integration
    
    Due to nature of triple integral, ... 
     - x must be a constant
     - y can be constant or a function in terms of x
     - z can be a constant, a function in terms of y, a function in terms of x, or a function in terms y and x
    """
    
    def func(inp1): # Functon to make inputs useable for tplquad

        inp = inp1.replace(" ", "").lower()               # Lowercase the string and remove all empty space (allows equality statements to work)

        if inp.split('=')[0] == 'x':                      # If left side of equals sign is [x] (means it is the [x] bound for integration)
            return eval(inp.split("=")[1])                # Bound for [x] must be a constant, so return a constant

        elif inp.split('=')[0] == 'y':                    # If left side of equals sign is [y] (means it is the y bound for integration)
            return lambda x: eval(inp.split("=")[1])      # Bound for [y] must be in terms of [x] with no other variables -> return that function

        elif inp.split('=')[0] == 'z':                    # If left side of equals sign is [z] (means it is the x bound for integration)
            return lambda x,y: eval(inp.split("=")[1])    # Bound for [z] must be in terms of [x] with no other variables -> return that function

        else:                                             # If left side of equals sign equals anything else, treat it as though it is the function
            return lambda z,y,x: eval(inp.split("=")[1])  # Return a function with three variables bc it is the function (not bound of integration)
    
    # Using conversion function; Input as string -> Output as useable function

    F  = func(f)

    XL = func(xl)
    XU = func(xu)

    YL = func(yl)
    YU = func(yu)

    ZL = func(zl)
    ZU = func(zu)

    # Plug function and bounds of integration into tplquad for computation

    print(tplquad(F, XL, XU, YL, YU, ZL, ZU)[0])