# integration_and_wire_mass

The file titled integration.py can solve single, double, and triple integrals. I wrote the code with cartesian functions in mind and have yet to 
explore applying it to others. However, I think it would be able to handle polar, cylindrical, and spherical with minimal modifications. 

One limitation (maybe more of an annoyance) is that all of the inputs for triple_integral() must be written as an equality statement. This is so my code can differentiate
between x, y, and z bounds. It would be pretty easy to rewrite it to avoid that; you would need to replace fun(inp1) with something more specific for each integration axis. I left it as is so that one function could handle all three.

The mass_wire() function seems to do its job without any noticeable limitations. You need to input the parametrization of x and y with respect to time, a density function in terms
of x and y, and the bounds of integration for the line integral. In return, the function will output the mass of the wire.
