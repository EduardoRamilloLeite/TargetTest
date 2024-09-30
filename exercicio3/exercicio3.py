import json

def load_data(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

def faturamento_estatisticas(data):
    sales = list(filter(lambda x: x is not None and x > 0, (day['valor'] for day in data)))

    min_sales = min(sales)
    max_sales = max(sales)

    average_monthly = sum(sales) / len(sales)

    days_above_average = sum(1 for day in sales if day > average_monthly)

    return min_sales, max_sales, days_above_average

filename = 'C:/Users/eduar/OneDrive/Desktop/Codigos/codigo_estagio/exercicio3/faturamento.json'
data = load_data(filename)
min_sales, max_sales, days_above_average = faturamento_estatisticas(data)

print(f"Menor faturamento: {min_sales}")
print(f"Maior faturamento: {max_sales}")
print(f"Número de dias acima da média: {days_above_average}")