
                                        # Dictionary Comphrehension
                                # dictionary = {key:expression for (key,value) in iterable}


                                                # Qn - 1
# card = {"phone" : 25000.00,'lamp':2560.00,'table':5499.00,'pen':20.50,'bag':650.20,'kettle':1500.00}
# card_round = {key : round(val) for (key,val) in card.items()}
# print(card_round)

                                                # Qn - 2
                                # dictionary = {key:exp for (key,val) in iterable if condition }

# card = {"phone" : 25000.00,'lamp':2560.00,'table':5499.00,'pen':20.50,'bag':650.20,'kettle':1500.00}
# card_rate = {key : round(val) for (key,val) in card.items() if val > 1000}
# print(card_rate)

                                               # Qn - 3
                                # dictionary = {key:expression if - else for (key,val) in iterable}

card = {"phone" : 25000.00,'lamp':2560.00,'table':5499.00,'pen':20.50,'bag':650.20,'kettle':1500.00}
card_disc ={key : round(val*.9) if val > 5000 else val for (key,val) in card.items()}
print(card_disc)

                                                # Qn - 4
                                # dictinary = {key : exp function for (key,val) in iterable}

card = {"phone" : 25000.00,'lamp':2560.00,'table':5499.00,'pen':20.50,'bag':650.20,'kettle':1500.00}
def card_disc(key,val):
    if(key=="lamp" or key == "table"):
        val = round(val * .95)
    return val
card__disc = {key : card_disc(key,val) for (key,val) in card.items() }
print(card__disc)