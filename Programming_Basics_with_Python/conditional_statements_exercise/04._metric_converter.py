conversion_number = float(input())
input_unit = input()
output_unit = input()
if input_unit == "mm" and output_unit == "m":
    print(f"{conversion_number / 1000:.3f}")
elif input_unit == "mm" and output_unit == "cm":
    print(f"{conversion_number / 10:.3f}")
elif input_unit == "cm" and output_unit == "m":
    print(f"{conversion_number / 100:.3f}")
elif input_unit == "cm" and output_unit == "mm":
    print(f"{conversion_number * 10:.3f}")
elif input_unit == "m" and output_unit == "cm":
    print(f"{conversion_number * 100:.3f}")
elif input_unit == "m" and output_unit == "mm":
    print(f"{conversion_number * 1000:.3f}")

