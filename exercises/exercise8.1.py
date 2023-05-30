# created a while statement
# opened the .txt in a read format
# created a var that contains listed items
# created an input statement
# inputted response is appended into the list
# got the count (nr of times) of all items in list
# got percentage of the count ( count / specific input) * 100

while True:
    with open('coin.txt', 'r') as file:
        coin_flip = file.readlines()  # this repr list & returns list contained in .txt

    coin_toss = input("Heads or Tails? ") + "\n"  # input function

    coin_flip.append(coin_toss)  # append the written input into the list

    with open('coin.txt', 'w') as file:
        file.writelines(coin_flip) # write into the list (coin_flip)

    total = coin_flip.count(coin_toss) # nr of times input is counted in list
    percentage = total / len(coin_flip) * 100
    print(f"{coin_toss} represents {percentage}% of the flips")

