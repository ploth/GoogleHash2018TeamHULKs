from simulate import distance

def naive_strategy(city):
    # loop through rides and give a ride to next vehicle in line
    for ride in city.rides:
        vehicle = city.vehicles.pop(0)
        vehicle.ride_queue.append(ride)
        city.vehicles.append(vehicle)

    return city

def naive_check_strategy(city):
    # loop through rides and give a ride to next vehicle in line
    for ride in sorted(city.rides, key=lambda ride: ride.earliest_start):
        vehicle = city.vehicles.pop(0)

        vehicle_to_start = distance(vehicle.current_position, ride.start_from)
        ride_duration = distance(ride.start_from, ride.end_at)
        total_duration = vehicle_to_start + ride_duration

        start_time = vehicle.current_time if vehicle.current_time > ride.earliest_start else ride.earliest_start
        time_finish = start_time + total_duration

        can_finish_before_world_ends = time_finish <= city.steps
        can_finish_before_tour_is_old = time_finish <= ride.latest_finish

        if can_finish_before_world_ends and can_finish_before_tour_is_old:
            vehicle.ride_queue.append(ride)
            vehicle.current_position = ride.end_at
            vehicle.current_time = time_finish

        city.vehicles.append(vehicle)

    return city
