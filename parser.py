from collections import deque

class City(object):
    def __init__(self, size, vehicles, num_rides, bonus, steps, rides):
        self.size = size
        self.vehicles = vehicles
        self.num_rides = num_rides
        self.bonus = bonus
        self.steps = steps
        self.rides = rides

    def __repr__(self):
        return "City: \n \
Size: {} \n \
Vehicles: {} \n \
Number of rides: {} \n \
Bonus: {} \n \
Steps: {} \n \
Rides: {} \n".format(self.size, self.vehicles, self.num_rides, self.bonus, self.steps, self.rides)

class Ride(object):
    def __init__(self, id, start_from, end_at, earliest_start, latest_finish):
        self.id = id
        self.start_from = start_from
        self.end_at = end_at
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

    def __repr__(self):
        return "Ride {}: \n \
From: {} \n \
To: {} \n \
Earliest start: {} \n \
Latest_finish: {} \n".format(self.id, self.start_from, self.end_at, self.earliest_start, self.latest_finish)

class Vehicle(object):
    def __init__(self):
        self.current_position = (0, 0)
        self.current_time = 0
        self.ride_queue = deque()

    def __repr__(self):
        return "Vehicle: \n \
Position: {} \n \
Queued Rides: {} \n".format(self.current_position, self.ride_queue)


def load_solution(solution_path, city):
    lines = get_lines_from_file(solution_path)
    tours = [[city.rides[int(tour_id)] for tour_id in line.split()[1:]] for line in lines]

    if len(tours) != len(city.vehicles):
        raise Exception("Length of tours %s does not match number of vehicles %s." % (len(tours), len(city.vehicles)))

    for i, vehicle in enumerate(city.vehicles):
        vehicle.ride_queue = deque(tours[i])

    return city

def save_solution(solution_path, city):
    output = [str(len(vehicle.ride_queue)) + " " + " ".join(map(lambda ride: str(ride.id), vehicle.ride_queue)) for vehicle in city.vehicles]

    with open(solution_path, 'w') as file:
        file.write("\n".join(output))


def get_lines_from_file(path):
    with open(path, 'r') as file:
        content = file.read()

    return [line for line in content.split("\n") if len(line) > 0]


def interpret_lines(lines):
    # get attributes from first line
    first_line_numbers = [int(number_str) for number_str in lines[0].split()]
    city_size = (first_line_numbers[0], first_line_numbers[1])
    vehicles = [Vehicle() for i in range(first_line_numbers[2])]
    num_rides = first_line_numbers[3]
    bonus = first_line_numbers[4]
    steps = first_line_numbers[5]

    # get rides from rest of lines
    rides = []
    for ride_id, line in enumerate(lines[1:]):
        line_numbers = [int(number_str) for number_str in line.split()]
        start_from = (line_numbers[0], line_numbers[1])
        end_at = (line_numbers[2], line_numbers[3])
        earliest_start = line_numbers[4]
        latest_finish = line_numbers[5]
        rides.append(Ride(ride_id, start_from, end_at, earliest_start, latest_finish))

    return City(city_size, vehicles, num_rides, bonus, steps, rides)


def load_problem(path):
    lines = get_lines_from_file(path)
    city = interpret_lines(lines)
    return city