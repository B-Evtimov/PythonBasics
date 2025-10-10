people_count = int(input())
nights = int(input())
transport_cards_count = int(input())
museum_tickets_count = int(input())
night_price = 20
transport_card_price = 1.60
museum_ticket_price = 6


nights_price = nights * night_price
transport_price = transport_cards_count * transport_card_price
museum_price = museum_tickets_count * museum_ticket_price

total_per_person = nights_price + transport_price + museum_price
group_total = total_per_person * people_count
group_total += group_total * 0.25

print(f"{group_total:.2f}")
