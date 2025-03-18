age = int(input('Insira sua idade: '))

right_to_vote = age >= 16
obligation_vote = 18 <= age <= 69
optional_vote = (16 <= age <= 17) or (age >= 70)

print(f'Você tem direito ao voto? {right_to_vote}')
print(f'O seu voto é obrigatório? {obligation_vote}')
print(f'O seu voto é opcional? {optional_vote}')
