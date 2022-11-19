# import main
#
# attempt_round = 1
# number_of_attempts = 3
#
# while attempt_round <= number_of_attempts:
#     secret_number = 42
#     user_guess_input = input("Digite o número: ")
#     guess_number = int(user_guess_input)
#
#     attempts_left = number_of_attempts - attempt_round
#
#     if guess_number == secret_number:
#         print("Você adivinhou o número secreto. Parabéns!")
#     else:
#         if guess_number > secret_number:
#             print("O número digitado é maior que o número secreto. " + str(attempts_left) + " restantes!")
#         elif guess_number < secret_number:
#             print("O número digitato é menor que o número secreto. " + str(attempts_left) + " restantes!")
#         attempt_round = attempt_round + 1
#
# main.print_number_of_attempts_remaining(attempt_round, number_of_attempts)

values = [0, 1, 2, 3, 4]

values.__add__()

print(8 in values)
