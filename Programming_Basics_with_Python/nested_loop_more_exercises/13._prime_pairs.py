start_number_for_first_couple = int(input())
start_number_for_second_couple = int(input())
difference_number_for_first_couple = int(input())
difference_number_for_second_couple = int(input())

end_number_for_first_couple = start_number_for_first_couple + difference_number_for_first_couple
end_number_for_second_couple = start_number_for_second_couple + difference_number_for_second_couple

for nums1 in range(start_number_for_first_couple, end_number_for_first_couple + 1):
    counter_one = 0
    for nn1 in range(1, end_number_for_first_couple + 1):
        if nums1 % nn1 == 0:
            counter_one += 1
    for nums2 in range(start_number_for_second_couple, end_number_for_second_couple + 1):
        counter_two = 0
        for nn2 in range(1, end_number_for_second_couple + 1):
            if nums2 % nn2 == 0:
                counter_two += 1
        if counter_one == 2 and counter_two == 2:
            print(f'{nums1}{nums2}')
