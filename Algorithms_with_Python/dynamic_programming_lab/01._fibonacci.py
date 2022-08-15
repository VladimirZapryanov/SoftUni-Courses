def calc_fib(number, memory):
    if number in memory:
        return memory[number]
    if number <= 2:
        return 1
    result = (calc_fib(number - 1, memory) + calc_fib(number - 2, memory))
    memory[number] = result
    return result


number = int(input())

print(calc_fib(number, {}))
