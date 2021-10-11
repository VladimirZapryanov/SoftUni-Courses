from errors import NameTooShortError, MustContainAtSymbolError, InvalidDomainError
valid_domain = ["com", "bg", "org", "net"]

email = input()

while not email == "End":
    email_details = email.split("@")
    email_name = email_details[0]
    domain_name = email_details[-1]
    needed_key = domain_name.split(".")

    if len(email_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif len(email_details) <= 1:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(needed_key) <= 1 or needed_key[-1] not in valid_domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()
