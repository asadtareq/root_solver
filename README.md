# Dynamic Root Finding Solver

## Description
This project implements numerical methods to solve nonlinear equations dynamically using Python.

The user can input any mathematical function, and the program computes the root using different numerical methods. It also compares the performance of each method.

## Methods Implemented
- Bisection Method
- Newton-Raphson Method
- Secant Method

## Features
- Dynamic function input using SymPy
- Automatic derivative calculation for Newton method
- Iteration tracking
- Error analysis
- Time comparison
- Convergence plot (log scale)

## Technologies Used
- Python
- SymPy
- NumPy
- Matplotlib

## Example

Input:any non linear function by user
Output:
- Root values 
- Iterations
- Error
- Time taken
- Convergence graph

## Project Structure
root_solver.py
README.md
requirements.txt
output_result.PNG
root_solver_plot.png

## How to Run
1. Install required libraries(bash)
   - pip install numpy
   - pip install sympy
   - pip install matplotlib
3. Run the program
   - python root_solver.py

## Motivation
This project was developed as part of my research preparation in numerical analysis and computational mathematics. The goal is to provide a robust tool for solving nonlinear equations while evaluating the efficiency, accuracy, and convergence rates of classic numerical techniques—specifically the Newton-Raphson, Bisection, and Secant methods.

## Author
Md Asaduzzaman
