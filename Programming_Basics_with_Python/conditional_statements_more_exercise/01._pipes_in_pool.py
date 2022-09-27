def pool_condition(pool_capacity, first_pipe, second_pipe, missing_hours):
    first_pipe_water = first_pipe * missing_hours
    second_pipe_water = second_pipe * missing_hours
    total_water_from_two_pipes = first_pipe_water + second_pipe_water
    pool_water_percent = (total_water_from_two_pipes / pool_capacity) * 100
    first_pipe_water_percent = (first_pipe_water / total_water_from_two_pipes) * 100
    second_pipe_water_percent = (second_pipe_water / total_water_from_two_pipes) * 100
    overflows_water = abs(pool_capacity - total_water_from_two_pipes)

    if pool_capacity >= total_water_from_two_pipes:
        return f'The pool is {pool_water_percent:.2f}% full. Pipe 1: {first_pipe_water_percent:.2f}%. Pipe 2: {second_pipe_water_percent:.2f}%."'
    else:
        return f'For {missing_hours:.2f} hours the pool overflows with {overflows_water:.2f} liters.'


pool_capacity = int(input())
first_pipe = int(input())
second_pipe = int(input())
missing_hours = float(input())

print(pool_condition(pool_capacity, first_pipe, second_pipe, missing_hours))