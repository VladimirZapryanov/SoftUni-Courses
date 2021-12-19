def is_password_length_valid(password):
    if 6 <= len(password) <= 10:
        return True


def is_password_alphanumeric(password):
    return password.isalnum()


def does_password_have_at_least_two_digits(password):
    digits_cnt = 0
    for ch in password:
        if ch.isdigit():
            digits_cnt += 1
    if digits_cnt >= 2:
        return True
    else:
        return False


def validate_password(password):
    is_valid = True
    if not is_password_length_valid(password):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not is_password_alphanumeric(password):
        print("Password must consist only of letters and digits")
        is_valid = False
    if not does_password_have_at_least_two_digits(password):
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


password_input = input()
validate_password(password_input)
