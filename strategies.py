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
    for ride in city.rides:
        vehicle = city.vehicles.pop(0)

        # check if the vehicle hast a ride
        if len(vehicle.ride_queue) > 0:
            time_vehicle_to_start = distance(vehicle.ride_queue[-1].end_at, ride.start_from)
            time_needed_ride = distance(ride.start_from, ride.end_at)
            time_available = ride.latest_finish - vehicle.current_time

            if time_available > (time_vehicle_to_start + time_needed_ride):
                vehicle.ride_queue.append(ride)
                vehicle.current_position = ride.end_at
                vehicle.current_time = vehicle.current_time + distance(ride.start_from, ride.end_at)
                city.vehicles.append(vehicle)
        else:
            vehicle.ride_queue.append(ride)
            vehicle.current_position = ride.end_at
            vehicle.current_time = vehicle.current_time + distance(ride.start_from, ride.end_at)
            city.vehicles.append(vehicle)

    return city
