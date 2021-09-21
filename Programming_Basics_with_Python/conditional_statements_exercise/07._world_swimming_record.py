record = float(input())
distance = float(input())
swimming_time = float(input())
all_swimming_time = swimming_time * distance
slower_distance = distance // 15
slower_time = slower_distance * 12.5
ivan_swimming_time = (all_swimming_time + slower_time)
missing_seconds = ivan_swimming_time - record
if ivan_swimming_time < record:
    print(f" Yes, he succeeded! The new world record is {ivan_swimming_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {missing_seconds:.2f} seconds slower.")