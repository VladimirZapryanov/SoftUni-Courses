def find_platform(arr, dep, n):
    arr = sorted(arr)
    dep = sorted(dep)
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:
        if arr[i] < dep[j]:
            plat_needed += 1
            i += 1
            if plat_needed > result:
                result = plat_needed
        else:
            plat_needed -= 1
            j += 1

    return result


arrival_hours = [float(x) for x in input().split()]
departure_hours = [float(x) for x in input().split()]
n = len(arrival_hours)

print(find_platform(arrival_hours, departure_hours, n))

