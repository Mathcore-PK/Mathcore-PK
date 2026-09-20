# MathCore-PK | Numerical Analysis
# Bisection + Newton Raphson Method
# For BS Mathematics - Peshawar

def bisection_method(f, a, b, tol=0.0001):
    print("--- Bisection Method ---")
    if f(a) * f(b) >= 0:
        print("No root in [a,b]")
        return None
    
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

def newton_raphson(f, df, x0, tol=0.0001, max_iter=100):
    print("\n--- Newton Raphson Method ---")
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            print(f"Root found after {i} iterations: {x}")
            return x
        dfx = df(x)
        if dfx == 0:
            print("Derivative zero!")
            return None
        x = x - fx/dfx
    return x

# --- Example ---
if __name__ == "__main__":
    # Find root of x^3 - x - 2 = 0
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1

    root1 = bisection_method(f, 1, 2)
    print(f"Bisection Root: {root1}")

    root2 = newton_raphson(f, df, 1.5)
    print(f"Newton Root: {root2}")
