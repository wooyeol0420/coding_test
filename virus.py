import random

def virus_spread_model(infection_probability, infected_people_per_day, fatality_rate, total_population):
    days = 0
    infected_people = 1
    total_infected_people = 1
    deaths = 0

    while total_infected_people < total_population:
        new_infections = 0
        for _ in range(infected_people):
            if random.random() < infection_probability:
                new_infections += infected_people_per_day

        total_infected_people += new_infections
        deaths += int(new_infections * fatality_rate)
        infected_people = new_infections
        days += 1

    return days, deaths

try:
    infection_probability = float(input("1人が他の人を感染させる確率（0から1までの値）："))
    infected_people_per_day = int(input("1人が感染させる人数："))
    fatality_rate = float(input("致死率（0から1までの値）："))
    total_population = int(input("総人口："))

    days, deaths = virus_spread_model(infection_probability, infected_people_per_day, fatality_rate, total_population)
    print(f"{days}日で全人口が感染し、その時の死亡者数は{deaths}人です。")

except ValueError:
    print("入力エラー：有効な数字を入力してください。")
