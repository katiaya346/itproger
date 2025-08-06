import random

def get_bot_choice():
    return random.choice( ['камінь', 'ножниці', 'папір'])

def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "Нічия"
    if (user_choice == 'камінь' and bot_choice == 'ножниці') or \
       (user_choice == 'ножниці' and bot_choice == 'папір') or \
       (user_choice == 'папір' and bot_choice == 'камінь'):
        return "Ви виграли!"
    return "Ви виграли"


while True:
    user_choice = input("Ваш вибір (камінь, ножниці, папір або 'вихід' для завершення): ").lower()
    if user_choice == 'вихід':
        print("Дякую за гру!")
        break
    if user_choice not in ['камінь', 'ножниці', 'папір']:
        print("Неправильне введення! Попробуйте ще раз.")
        continue
    bot_choice = get_bot_choice()
    print(f"Бот вибрав: {bot_choice}")
    print(determine_winner(user_choice, bot_choice))