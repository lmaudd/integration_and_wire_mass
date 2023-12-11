from sympy import *
non = symbols('non')
init_printing(use_unicode=True)

from scipy.integrate import quad
from numpy import sin, cos, tan, pi

def mass_wire(xt, yt, density=1, lower_bound=0, upper_bound=pi):
          
    # Compute derivatives of x(t) and y(t)
    
    x_non = xt.replace("t", "non")  # Replace 't' with 'non' bc I can replace 'non' w/out needing to differentiate between eat and sqr[t] and [t]an
    dx_non = str(diff(x_non, non))  # Compute derivative of x(t) (or x(non))

    y_non = yt.replace("t", "non")  # Replace 't' with 'non'
    dy_non = str(diff(y_non, non))  # Compute derivative of y(t) (or y(non))

    # I have the density function, x(t), x'(t), y(t), and y'(t); now I need to combine them into a line integral for mass of wire
    
    root = f'(({str(dx_non)})**2 + ({str(dy_non)})**2)'  # Piece together the square root part of integral
    comb_func = f'{density} * sqrt{root}'                #  Combine density and square root

    comb_func = comb_func.replace("x", "(" + str(x_non) + ")")  # Change of coordinates – replace 'x' with 'x(t)'
    comb_func = comb_func.replace("y", "(" + str(y_non) + ")")  # Change of coordinates – replace 'y' with 'y(t)'
    comb_func = comb_func.replace("non", "x")                   # Replace 'non' with 'x' to allow quad function to integrate

    # Compute and print
    
    def integrand(x): # Turn function to integrate into a proper function
        return eval(comb_func)
    
    print(quad(integrand, lower_bound, upper_bound)[0]) # Integrate on bounds and print answer
