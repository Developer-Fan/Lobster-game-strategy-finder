import random
import math

stuff = {}

for i in range(1000):
    boats = 2
    pots = 5
    money = 0
    for j in range(15):
        num_pots = 0
        num_boats = 0
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
        if pots <= boats*10:
            num_pots = math.floor(money/5)
            pots += num_pots
            money -= num_pots * 5
        #print(f"""
        #Boats: {boats}
        #New Boats: {num_boats}
        #Pots: {pots}
        #New Pots: {num_pots}
        #Money: {money}
        #""")
    journey = {
        "boats": boats,
        "pots": pots,
        "money": money
    }
    stuff[str(i)] = journey

money_journey = []

for i in stuff:
    money_journey.append(
        stuff[i]["boats"]*100+
        stuff[i]["pots"]*5+
        stuff[i]["money"]
    )

money_journey.sort()
print(money_journey[999])
            
