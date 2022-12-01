import random
import math

for i in range(100):
    boats = 2
    pots = 5
    money = 0
    for j in range(15):
        in_pots = random.randint(0, pots)
        out_pots = pots - in_pots
        weather = random.choice([
            "good",
            "bad"
        ])
        if weather == "good":
            money += in_pots*2+out_pots*6
        elif weather == "bad":
            money += in_pots*4
            pots -= out_pots
        num_boats = math.floor(money/100)
        boats += num_boats
        money -= num_boats*100
        if pots*10 <= boats:
            num_pots = math.floor(money/5)
            pots += num_pots
            money -= num_pots * 5
        print(f"""t
        Boats: {boats}
        New Boats: {num_boats}

        """)
            
