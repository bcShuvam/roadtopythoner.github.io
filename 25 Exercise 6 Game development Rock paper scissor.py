import random

lst = ["Rock","Paper","Scissor"]
rand = random.choice(lst)
player_name = input("Enter Player_Name.\n")
print(f"Press 0 for {lst[0]} , Press 1 for {lst[1]} and Press 2 for {lst[2]}")
user_choice = int(input("Enter your choice : "))
while True:
    if rand == lst[user_choice]:
        print("\t\t\"D_R_A_W\"\t")
        print(f"\"Bot\" {rand}  and \"{player_name}\" {lst[user_choice]}")
        break

    elif rand == lst[0] and lst[user_choice] == lst[1]:
        print(f"\"{player_name}\" {lst[user_choice]} Wins ! and \"Bot\" {rand} Loos !")
        break

    elif rand == lst[0] and lst[user_choice] == lst[2]:
        print(f"\"Bot\" {rand} Wins ! and \"{player_name}\" {lst[user_choice]} Loose !")

    elif rand == lst[1] and lst[user_choice] == lst[0]:
        print(f"\"{player_name}\" {lst[user_choice]} Wins ! and \"Bot\" {rand} Loos !")
        break

    elif rand == lst[1] and lst[user_choice] == lst[2]:
        print(f"\"{player_name}\" {lst[user_choice]} Wins ! and \"Bot\" {rand} Loos !")
        break

    elif rand == lst[2] and lst[user_choice] == lst[0]:
        print(f"\"{player_name}\" {lst[user_choice]} Wins ! and \"Bot\" {rand} Loos !")
        break

    elif rand == lst[2] and lst[user_choice] == lst[1]:
        print(f"\"Bot\" {rand} Wins ! and \"{player_name}\" {lst[user_choice]} Loos !")

print("\t\t\"G_A_M_E O_E_V_E_R\"\t\t")