# import datetime
#
# age = 21
# date = datetime.datetime(2022, 11, 20).strftime("%d/%m/%Y")
#
# print("Pedro faz {} em {}".format(age, date))
import random

eduardo = True
secret_number = round(int(random.randrange(0, 42)))
number_of_attempts = 4


def print_number_of_attempts_remaining(round_number, total_attempts):
    attempts = total_attempts - 1
    if round_number < attempts:
        rounds_left = attempts - round_number
        return "Tente novamente. Você possui {} tentativa(s)!\n".format(rounds_left)
    elif round_number >= attempts:
        return "Você errou em todas as tentativas. Perdeu a bola de cristal foi?\n"


for user_round in range(1, number_of_attempts):
    user_attempt = int(input("Digite sua tentativa de adivinhar o número: \n"))
    if user_attempt.__eq__(secret_number):
        print("Você adivinhou o número corretamente. Parabéns!")
        break
    else:
        if user_attempt > secret_number:
            print("O número que você digitou é maior que o número a ser adivinhado.")
            print_number_of_attempts_remaining(user_round, number_of_attempts)
        elif user_attempt < secret_number:
            print("O número que você digitou é menor que o número a ser adivinhado.")
            print_number_of_attempts_remaining(user_round, number_of_attempts)
