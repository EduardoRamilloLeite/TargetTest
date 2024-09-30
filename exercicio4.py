sales = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_sales = sum(sales.values())

percentages = {state: (value / total_sales) * 100 for state, value in sales.items()}

print("Percentual de representação por estado:")
for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")