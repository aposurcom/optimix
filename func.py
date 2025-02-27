from ortools.linear_solver import pywraplp


def product_mix_optimization(product_A_material=4, product_B_material=2, material_max=60, product_A_labor=2, product_B_labor=3, labor_max=60, product_A_price=30, product_B_price=40):
    # Create solver
    solver = pywraplp.Solver.CreateSolver('GLOP')  # GLOP is for linear programming

    if not solver:
        return

    # Decision variables: Number of units to produce (continuous variables)
    # product_A and product_B are the number of units to produce.
    # They must be ≥ 0 (you can’t produce a negative amount).
    product_A = solver.NumVar(0, solver.infinity(), 'Product_A')
    product_B = solver.NumVar(0, solver.infinity(), 'Product_B')

    print("Number of variables =", solver.NumVariables())

    # Constraints (Available Resources)
    # Material Constraint: 4A + 6B ≤ 60
    solver.Add(product_A_material * product_A + product_B_material * product_B <= material_max) # Material Limit ProductA needs 4 and ProductB needs 6 max 60

    # Labor Constraint: 2A + 3B ≤ 30
    solver.Add(product_A_labor * product_A + product_B_labor * product_B <= labor_max) # Labor Limit ProductA needs 2h and productB needs 3 max 60h

    print("Number of constraints =", solver.NumConstraints())

    # Objective Function: Maximize Profit (30A + 40B)
    solver.Maximize(product_A_price * product_A + product_B_price * product_B) # ProductA $30 per unit and ProductB $40 per unit

    # Solve the problem
    status = solver.Solve()
    result = ""

    # Save and print Results
    if status == pywraplp.Solver.OPTIMAL:
        result = f"Optimal production of Product A: {product_A.solution_value():.2f}\n"
        result += f"Optimal production of Product B: {product_B.solution_value():.2f}\n"
        result += f"Maximum Profit: {solver.Objective().Value():.2f}\n"
    else:
        result = "No optimal solution found."

    print(result)
    
    return result

if __name__ == '__main__':
    # Run the function
    product_mix_optimization()
