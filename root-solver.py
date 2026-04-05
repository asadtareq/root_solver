import math
import time
import matplotlib.pyplot as plt
from sympy import symbols, sympify, diff, lambdify

# -------------------------
# User Input Function
# -------------------------
x = symbols('x')
func_input = input("Enter function f(x) (e.g., x**3 - x - 2): ")
func_expr = sympify(func_input)

f = lambdify(x, func_expr, 'math')
df_expr = diff(func_expr, x)
df = lambdify(x, df_expr, 'math')

# -------------------------
# Input Parameters
# -------------------------
tolerance = 0.0001
max_iter = 100

a = float(input("Enter interval start (a) for Bisection/Secant: "))
b = float(input("Enter interval end (b) for Bisection/Secant: "))
x0_newton = float(input("Enter initial guess for Newton: "))
x0_secant = float(input("Enter first guess for Secant: "))
x1_secant = float(input("Enter second guess for Secant: "))

# -------------------------
# Error storage
# -------------------------
errors_bis = []
errors_newton = []
errors_secant = []

# -------------------------
# Bisection Method
# -------------------------
iteration_bis = 0
start_time = time.time()

if f(a) * f(b) >= 0:
    print("\n❌ Bisection method fails. f(a) and f(b) must have opposite signs.")
    root_bis = None
    time_bis = 0
else:
    while (b - a)/2 > tolerance and iteration_bis < max_iter:
        c = (a + b) / 2
        iteration_bis += 1
        errors_bis.append(abs(f(c)))

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    root_bis = c
    time_bis = time.time() - start_time

# -------------------------
# Newton Method
# -------------------------
iteration_newton = 0
x_newton = x0_newton
start_time = time.time()

while iteration_newton < max_iter:
    if df(x_newton) == 0:
        print("\n❌ Newton method failed (derivative = 0).")
        break

    x_next = x_newton - f(x_newton) / df(x_newton)
    iteration_newton += 1
    errors_newton.append(abs(f(x_next)))

    if abs(x_next - x_newton) < tolerance:
        break

    x_newton = x_next

root_newton = x_next
time_newton = time.time() - start_time

# -------------------------
# Secant Method
# -------------------------
iteration_secant = 0
x0 = x0_secant
x1 = x1_secant
start_time = time.time()

while iteration_secant < max_iter:
    if f(x1) - f(x0) == 0:
        print("\n❌ Secant method failed (division by zero).")
        break

    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    iteration_secant += 1
    errors_secant.append(abs(f(x2)))

    if abs(x2 - x1) < tolerance:
        break

    x0 = x1
    x1 = x2

root_secant = x2
time_secant = time.time() - start_time

# -------------------------
# Output Results
# -------------------------
print("\n========== RESULTS ==========")

if root_bis is not None:
    print(f"Bisection Root: {root_bis:.6f} | Iterations: {iteration_bis} | Time: {time_bis:.6f}")
else:
    print("Bisection: Failed")

print(f"Newton Root: {root_newton:.6f} | Iterations: {iteration_newton} | Time: {time_newton:.6f}")
print(f"Secant Root: {root_secant:.6f} | Iterations: {iteration_secant} | Time: {time_secant:.6f}")

# -------------------------
# Final Errors
# -------------------------
print("\n========== FINAL ERRORS ==========")

if root_bis is not None:
    print("Bisection Error:", abs(f(root_bis)))

print("Newton Error:", abs(f(root_newton)))
print("Secant Error:", abs(f(root_secant)))

# -------------------------
# Comparison Table
# -------------------------
print("\n========== COMPARISON ==========")
print("Method\t\tRoot\t\tIterations\tTime\t\tError")

if root_bis is not None:
    print(f"Bisection\t{root_bis:.6f}\t{iteration_bis}\t\t{time_bis:.6f}\t{abs(f(root_bis)):.6e}")
else:
    print("Bisection\tFailed")

print(f"Newton\t\t{root_newton:.6f}\t{iteration_newton}\t\t{time_newton:.6f}\t{abs(f(root_newton)):.6e}")
print(f"Secant\t\t{root_secant:.6f}\t{iteration_secant}\t\t{time_secant:.6f}\t{abs(f(root_secant)):.6e}")

# -------------------------
# Plot Convergence
# -------------------------
plt.figure(figsize=(8,5))

if len(errors_bis) > 0:
    plt.plot(range(1, len(errors_bis)+1), errors_bis, marker='o', label="Bisection")

plt.plot(range(1, len(errors_newton)+1), errors_newton, marker='x', label="Newton")
plt.plot(range(1, len(errors_secant)+1), errors_secant, marker='s', label="Secant")

plt.yscale('log')
plt.xlabel("Iteration")
plt.ylabel("Absolute Error")
plt.title("Convergence of Root Finding Methods")
plt.legend()
plt.grid(True, which="both", ls="--")

plt.show()
