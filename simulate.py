def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def score_vehicle(city, vehicle):
    total_points = 0
    t = 0
    vehicle.current_position = (0, 0)

    for ride in vehicle.ride_queue:
        if t < ride.earliest_start:
            t = ride.earliest_start

        # durations
        vehicle_to_start = distance(vehicle.current_position, ride.start_from)
        ride_duration = distance(ride.start_from, ride.end_at)
        total_duration = vehicle_to_start + ride_duration
        is_punctual = t + vehicle_to_start == ride.earliest_start

        # update state
        t = t + total_duration
        vehicle.current_position = ride.end_at

        if t > city.steps:
            raise Exception("INVALID SOLUTION: Vehicle took to long with ride %s: %s, %s" % (ride.id, t, len(vehicle.ride_queue)))

        # calculate points per ride
        ride_points = ride_duration
        if is_punctual:
            ride_points = ride_points + city.bonus

        # add to points
        total_points = total_points + ride_points

    return total_points


def assert_unique_ride_assignment(city):
    ride_set = set()
    for vehicle in city.vehicles:
        for ride in vehicle.ride_queue:
            if ride.id in ride_set:
                raise Exception("Ride %s is assigned multiple times!" % ride.id)
            ride_set.add(ride.id)


def score_solution(city):
    assert_unique_ride_assignment(city)

    total_score = 0
    for vehicle in city.vehicles:
        total_score += score_vehicle(city, vehicle)

    return total_score
