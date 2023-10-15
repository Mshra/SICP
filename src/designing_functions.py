def pressure(v, t, n=6.022e23):
    """Compute the pressrue in pascals of an ideal gas.

    Applies the ideal gas law: https://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas
    """
    k = 1.38e-23 # boltzmann's constant
    return n * k * t / v 

if __name__ == '__main__':
    help(pressure) # can see docstring of a function with help method
    pressure(1, 273.15) # default value of n is used as mentioned in function arguments
    pressure(1, 273.15, 3 * 6.022e23) # default value is over rided