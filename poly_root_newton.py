# computation of a root of a real polynomial
# using Newton-Rhapson method
def eval_poly(poly, x):
    """
    Calculates value of polynomial given by coefficients, at value x
    """
    total = 0.00
    degree = len(poly)
    for i in range(0, degree):
        total += (x**i)* poly[i]
        #print "total: ", total
    return total

def deriv_poly(poly):
    # (x0, x1, x2, x3, x4) --> (x1* 1, x2*2, x3*3, x4*4)
    d_poly = []
    for i in xrange(1, len(poly)):
        d_poly.append(float(i * poly[i]))
    
    return d_poly

def compute_root(poly, guess, e):
    """
    Computes the root of a polynomial given a guess and an allowed epsilon
    """
    root = guess
    counter = 0
    while abs(eval_poly(poly, root)) >= e:
        root = (root - eval_poly(poly, root) /eval_poly(deriv_poly(poly), root))
        counter += 1
        print root, counter
    return [root, counter]
poly = [2, 3, 1]
root = compute_root(poly, 4, 1e-6)
root = round(root)
print root