from interest import calculate_interest, calculate_total

principal = float(input('Principal: '))
rate = float(input('Interest rate (%): '))
years = float(input('Years: '))

interest = calculate_interest(principal, rate, years)
total = calculate_total(principal, interest)

print(f'Interest: {interest:.2f}')
print(f'Total: {total:.2f}')
