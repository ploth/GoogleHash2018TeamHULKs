class Pizza(object):
    def __init__(self, size, min_ingredient, max_cells, toppings):
        self.size = size
        self.min_ingredient_per_slice = min_ingredient
        self.max_cells_per_slice = max_cells
        self.toppings = toppings
        self.slices = []

    def __repr__(self):
        return "Pizza: \n \
Size: {} \n \
Min_ingredients: {} \n \
Max_cells_in_slice: {} \n \
Toppings: {}".format(self.size, self.min_ingredient_per_slice, self.max_cells_per_slice, self.toppings)


def get_lines_from_file(path):
    with open(path, 'r') as file:
        content = file.read()

    return [line for line in content.split("\n")]

def interpret_lines(lines):
    # get attributes from first line
    first_line_numbers = [int(number_str) for number_str in lines[0].split()]
    pizza_size = (first_line_numbers[0], first_line_numbers[1])
    min_ingredient_per_slice = first_line_numbers[2]
    max_cells_per_slice = first_line_numbers[3]

    # get toppings from rest of lines
    toppings = [[0 for i in range(pizza_size[1])] for j in range(pizza_size[0])]
    for i, line in enumerate(lines[1:]):
        for j, char in enumerate(line):
            toppings[i][j] = char

    return Pizza(pizza_size, min_ingredient_per_slice, max_cells_per_slice, toppings)

