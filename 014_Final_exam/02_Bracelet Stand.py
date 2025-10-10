Teresa_day_budget = float(input())
sum_per_day = float(input())
minus_budget = float(input())
present_price = float(input())

Teresa_day_budget_saved = Teresa_day_budget * 5
winned_sum = sum_per_day * 5
total = winned_sum + Teresa_day_budget_saved
minus_budget_operation = total - minus_budget

if minus_budget_operation >= present_price:
    print(f"Profit: {minus_budget_operation:.2f} BGN, the gift has been purchased.")
else:
    needed = present_price - minus_budget_operation
    print(f"Insufficient money: {needed:.2f} BGN.")
