def naive_strategy(city):
    # loop through rides and give a ride to next vehicle in line
    for ride in city.rides:
        vehicle = city.vehicles.pop(0)
        vehicle.ride_queue.append(ride)
        city.vehicles.append(vehicle)

    return city
