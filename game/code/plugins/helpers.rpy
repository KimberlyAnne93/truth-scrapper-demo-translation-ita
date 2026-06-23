############## HELPER FUNCTIONS #########################
init -1 python:
    import math

    ## Makes A move toward B at a decay rate. Used to smooth mouse movement/parallax.
    def expDecay(a, b, decay, dt):
        return b+(a-b)*math.exp(-decay*dt)
    
    ## Clamps X to a range. Example: If the minimum is 0 and x is -1, then it will return 0. If the maximum is 10 and x is 11, it will return 10.
    def clamp(minimum, x, maximum):
        return max(minimum, min(x, maximum))
    
    ## Returns the value between A and B in the T percentage. Good to smooth/interpolate values
    def lerp(a, b, t):
        return (1.0 - t) * a + t * b
    
    ## If given a number, returns -1 if it's negative, 1 if it's positive.
    def sign(a):
        return (a > 0) - (a < 0)