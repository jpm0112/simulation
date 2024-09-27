import simpy


def car(env, fuel_pump, name):
    while True:
        print(f'{name} starts driving at {env.now}')
        driving_duration = 5
        yield env.timeout(driving_duration)

        print(f'{name} requests fuel at {env.now}')
        with fuel_pump.request() as req:
            yield req
            print(f'{name} starts refueling at {env.now}')
            refueling_duration = 3
            yield env.timeout(refueling_duration)


def fuel_station(env):
    fuel_pump = simpy.Resource(env, capacity=1)  # Only 1 car can refuel at a time
    env.process(car(env, fuel_pump, 'Car 1'))
    env.process(car(env, fuel_pump, 'Car 2'))


# Create environment and run the simulation
env = simpy.Environment()
fuel_station(env)  # Call fuel_station without env.process
env.run(until=20)
