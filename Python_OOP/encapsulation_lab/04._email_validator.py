class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        data = email.split("@")
        name = data[0]
        data_1 = data[1].split(".")
        mail = data_1[0]
        domain = data_1[1]
        valid_email = True

        if not self.__is_name_valid(name):
            valid_email = False
        if not self.__is_mail_valid(mail):
            valid_email = False
        if not self.__is_domain_valid(domain):
            valid_email = False

        return valid_email


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
