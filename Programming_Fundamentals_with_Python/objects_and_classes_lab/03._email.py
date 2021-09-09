class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
data = input()
while not data == "Stop":
    sender, receiver, content = data.split()
    my_email = Email(sender, receiver, content)
    emails.append(my_email)
    data = input()

indexes = [int(el) for el in input().split(", ")]
for index in indexes:
    emails[index].send()

for my_email in emails:
    print(my_email.get_info())
