def tickets_budget(budget, category, people_count, vip_ticket_price, normal_ticket_price):
    transport_budget = 0
    all_tickets_price = 0

    if 1 <= people_count <= 4:
        transport_budget = budget * 0.75
    elif 5 <= people_count <= 9:
        transport_budget = budget * 0.6
    elif 10 <= people_count <= 24:
        transport_budget = budget * 0.5
    elif 25 <= people_count <= 49:
        transport_budget = budget * 0.4
    elif 50 <= people_count:
        transport_budget = budget * 0.25

    if category == 'VIP':
        all_tickets_price = people_count * vip_ticket_price
    elif category == 'Normal':
        all_tickets_price = people_count * normal_ticket_price

    budget_difference = budget - (transport_budget + all_tickets_price)

    if budget_difference >= 0:
        return f'Yes! You have {budget_difference:.2f} leva left.'
    else:
        return f'Not enough money! You need {abs(budget_difference):.2f} leva.'


budget = float(input())
category = input()
people_count = int(input())

vip_ticket_price = 499.99
normal_ticket_price = 249.99

print(tickets_budget(budget, category, people_count, vip_ticket_price, normal_ticket_price))