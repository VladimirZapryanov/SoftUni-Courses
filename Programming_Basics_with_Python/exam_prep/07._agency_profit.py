name = input()
adults_tickets = int(input())
kids_tickets = int(input())
adult_ticket_price = float(input())
service_fee = float(input())

adult_ticket_price_with_fee = adult_ticket_price + service_fee
kid_ticket_price = adult_ticket_price - adult_ticket_price * 0.7
kid_ticket_price_with_fee = kid_ticket_price + service_fee

total_price_for_all_tickets = adult_ticket_price_with_fee * adults_tickets + kid_ticket_price_with_fee * kids_tickets

print(f"The profit of your agency from {name} tickets is {total_price_for_all_tickets * 0.2:.2f} lv.")
