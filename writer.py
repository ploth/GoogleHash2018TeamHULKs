def write_solution_file(pizza):
    with open("output.txt", 'w') as file:

        lines = []
        for pizza_slice in pizza.slices:
            a, b, c, d = pizza_slice
            lines.append(f"{a} {b} {c} {d}\n")

        file.writelines(lines)

