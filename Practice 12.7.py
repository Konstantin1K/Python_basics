per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Cумма_вклада"))
days_in_year = 365
deposit_term = 365
TKB = int((per_cent['ТКБ'] * money * deposit_term) / (100 * days_in_year))
SKB = int((per_cent['СКБ'] * money * deposit_term) / (100 * days_in_year))
VTB = int((per_cent['ВТБ'] * money * deposit_term) / (100 * days_in_year))
SBER = int((per_cent['СБЕР'] * money * deposit_term) / (100 * days_in_year))
deposit = [TKB, SKB, VTB, SBER]
print("Накопления_в_каждом_банке =", deposit)
print("Максимальное_значение_в_списке:", max(deposit))












