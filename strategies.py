import sys

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


def vehicle_can_accept_ride(vehicle, ride, city):
    vehicle_to_start, _, total_duration, _, _= get_ride_times(ride, vehicle)
    start_time = get_start_time(ride, vehicle)
    time_finish = start_time + total_duration

    can_finish_before_world_ends = time_finish <= city.steps
    can_finish_before_tour_is_old = time_finish <= ride.latest_finish

    return can_finish_before_tour_is_old and can_finish_before_world_ends


def get_start_time(ride, vehicle):
    return vehicle.current_time if vehicle.current_time > ride.earliest_start else ride.earliest_start


def best_score(city):
    for ride in sorted(city.rides, key=lambda ride: ride.earliest_start):
        max_vehicle_score = float("-inf")
        best_vehicle = None
        for vehicle in city.vehicles:
            if not vehicle_can_accept_ride(vehicle, ride, city):
                continue

            vehicle_to_start, ride_duration, total_duration, start_time, time_finish = get_ride_times(ride, vehicle)
            start_time = get_start_time(ride, vehicle)
            waiting_duration = start_time - vehicle.current_time

            bonus = city.bonus if waiting_duration >= 0 else 0
            vehicle_score = -vehicle_to_start - waiting_duration + ride_duration + bonus

            if vehicle_score > max_vehicle_score:
                max_vehicle_score = vehicle_score
                best_vehicle = vehicle

        if best_vehicle is None:
            continue

        vehicle_to_start, _, total_duration, start_time, time_finish = get_ride_times(ride, best_vehicle)
        best_vehicle.ride_queue.append(ride)
        best_vehicle.current_position = ride.end_at
        best_vehicle.current_time = time_finish

    return city


def get_ride_times(ride, vehicle):
    vehicle_to_start = distance(vehicle.current_position, ride.start_from)
    ride_duration = distance(ride.start_from, ride.end_at)
    total_duration = vehicle_to_start + ride_duration
    start_time = get_start_time(ride, vehicle)
    time_finish = start_time + total_duration
    return vehicle_to_start, ride_duration, total_duration, start_time, time_finish
