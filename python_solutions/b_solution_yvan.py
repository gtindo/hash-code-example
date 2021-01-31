import os


def solution(n, t, p):
    deliveries = ""
    current_pizza = 1
    nb_deliveries = 0

    p.sort(key=lambda x: int(x[0]), reverse=True)

    for i in range(0, t[0]):
        pizza_1 = current_pizza
        pizza_2 = current_pizza + 1

        if n - current_pizza > 2:
            deliveries += "{} {} {}\n".format(2, pizza_1, pizza_2)
            current_pizza = current_pizza + 2
            nb_deliveries += 1

    for i in range(0, t[1]):
        pizza_1 = current_pizza
        pizza_2 = current_pizza + 1
        pizza_3 = current_pizza + 2

        if n - current_pizza > 3:
            deliveries += "{} {} {} {}\n".format(3, pizza_1, pizza_2, pizza_3)
            current_pizza = current_pizza + 3
            nb_deliveries += 1

    for i in range(0, t[2]):
        pizza_1 = current_pizza
        pizza_2 = current_pizza + 1
        pizza_3 = current_pizza + 2
        pizza_4 = current_pizza + 3

        if n - current_pizza > 4:
            deliveries += "{} {} {} {} {}\n".format(4, pizza_1, pizza_2, pizza_3, pizza_4)
            current_pizza = current_pizza + 4
            nb_deliveries += 1

    deliveries = "{}\n{}".format(nb_deliveries, deliveries)

    return deliveries


if __name__ == "__main__":
    input_name = "inputs/b_little_bit_of_everything.in"
    output_name = "outputs/b_little_bit_of_everything.out"

    input_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), input_name)
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), output_name)

    with open(input_path, "r") as f:
        line = f.readline()
        line = line.split(" ")

        nb_pizzas = int(line[0])
        two_teams = int(line[1])
        three_teams = int(line[2])
        four_teams = int(line[3])

        pizzas_data = f.readlines()
        pizzas = []

        for data in pizzas_data:
            pizza = data.split(" ")
            pizza[-1] = pizza[-1].split("\n")[0]
            pizzas.append(pizza)

    output = solution(nb_pizzas, [two_teams, three_teams, four_teams], pizzas)

    with open(output_path, "w") as f:
        f.write(output)
