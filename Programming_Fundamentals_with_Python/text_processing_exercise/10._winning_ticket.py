# 10. WinningTickets
tickets = [t.strip() for t in input().split(', ') if not t.isspace()]

# 01. @@@@@@
winning_combo_at = '@' * 6
# 02. ######
winning_combo_hash = '#' * 6
# 03. $$$$$$
winning_combo_dollar = '$' * 6
# 04. ^^^^^^
winning_combo_circumflex = '^' * 6

for ticket in tickets:
    if len(ticket) != 20:
        # This way I insure that the ticket will always be 20 characters length
        print('invalid ticket')
        continue

    left_half = ticket[:10]
    right_half = ticket[10:]

    match_symbol = ''

    # There is at least 6 symbols combo
    if winning_combo_at in left_half and winning_combo_at in right_half:
        match_symbol = '@'
    elif winning_combo_hash in left_half and winning_combo_hash in right_half:
        match_symbol = '#'
    elif winning_combo_dollar in left_half and winning_combo_dollar in right_half:
        match_symbol = '$'
    elif winning_combo_circumflex in left_half and winning_combo_circumflex in right_half:
        match_symbol = '^'
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    # Here we have a matching ticket
    left_matches = left_half.count(match_symbol)
    right_matches = right_half.count(match_symbol)

    # In case we have different matches length in left and right half, we take the min
    min_matches = min(left_matches, right_matches)

    if min_matches == 10:
        # 10 matches we have - There is a Jackpot!!!
        print(f'ticket "{ticket}" - {min_matches}{match_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - {min_matches}{match_symbol}')
