km = float(input())  # използваме float вместо int
fpw = km * 7.61
wpd = fpw * 0.18
fp = fpw - wpd
print(f"The final price is: {fp:.2f} lv.")
print(f"The discount is: {wpd:.2f} lv.")