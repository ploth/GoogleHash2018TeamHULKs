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
    def __init__(self, start_from, end_at, earliest_start, latest_finish):
        self.start_from = start_from
        self.end_at = end_at
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish

    def __repr__(self):
        return "Ride: \n \
From: {} \n \
To: {} \n \
Earliest start: {} \n \
Latest_finish: {} \n".format(self.start_from, self.end_at, self.earliest_start, self.latest_finish)

class Vehicle(object):
    def __init__(self):
        self.current_position = (0, 0)
        self.ride_queue = deque()

    def __repr__(self):
        return "Vehicle: \n \
Position: {} \n \
Queued Rides: {} \n".format(self.current_position, self.ride_queue)

def get_lines_from_file(path):
    with open(path, 'r') as file:
        content = file.read()

    return [line for line in content.split("\n") if len(line) > 0]

def interpret_lines(lines):
    # get attributes from first line
    print(lines)
    first_line_numbers = [int(number_str) for number_str in lines[0].split()]
    city_size = (first_line_numbers[0], first_line_numbers[1])
    vehicles = [Vehicle() for i in range(first_line_numbers[2])]
    num_rides = first_line_numbers[3]
    bonus = first_line_numbers[4]
    steps = first_line_numbers[5]

    # get rides from rest of lines
    rides = []
    for line in lines[1:]:
        print(line)
        line_numbers = [int(number_str) for number_str in line.split()]
        start_from = (line_numbers[0], line_numbers[1])
        end_at = (line_numbers[2], line_numbers[3])
        earliest_start = line_numbers[4]
        latest_finish = line_numbers[5]
        rides.append(Ride(start_from, end_at, earliest_start, latest_finish))

    return City(city_size, vehicles, num_rides, bonus, steps, rides)

