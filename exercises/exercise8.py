# Input system to ask for heads or tails
# match user action for "heads" or "tails" response
# store the two words into variables and assign them
# stores the heads or tails in a .txt file

# the test is calculated based on the amount of times head is counted

while True:
    with open("sides.txt", "r") as file:
        head_or_tail = file.readlines()

    coin_input = input("Throw the coin and enter heads or tails here: ") + "\n"

    head_or_tail.append(coin_input)

    with open("sides.txt", "w") as file:
        file.writelines(head_or_tail)

    nr_flips = head_or_tail.count(coin_input) #number of times head is counted
    percentage = nr_flips / len(head_or_tail) * 100

    print(f"{coin_input}: {percentage}%")





