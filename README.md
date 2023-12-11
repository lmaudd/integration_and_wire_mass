# integration_and_wire_mass

The file titled integration.py is able to solve single, double, and triple integrals. I wrote the code with cartesion functions in mind have not presently
explored applying it to others. I imagine it should be able to handle polar, cylindrical, and spherical with minimal modifications, however. 

One limitation (maybe more of an annoyance) is that all of the inputs for triple_integral() are requried to be written as an equality statement. This is so that my code can differentiate
between x, y, and z bounds. I do imagine, though, that it would be pretty easy to rewrite it to avoid that; you would need to replace fun(inp1) with something mroe specific for each axis
of integration; I chose to leave it as is so the one function could handle all three.

Mass of wire, as far as I can tell, does it's job without any noticeable limitations. You need to input the parametrization of x and y with respect to time, a density function in terms
x and y, and bounds of integration for the line integral. In return, the function will output the mass of the wire.
