waehrung = {"EURO": 1,"DOLLAR": 1.13,"GBP": 0.88}

# 1
def eu_in_dollar(eu):
    return eu*1.13
def eu_in_pound(eu):
    return eu*0.88

print(eu_in_dollar(1))
print(eu_in_pound(1))


# 2
def eu_in_all(eu, curr):
    return eu*waehrung[curr]

print(eu_in_all(1, "DOLLAR"))
print(eu_in_all(1, "GBP"))


# 3
def umrechnen(amount, curr_from, curr_to):
    return amount * waehrung[curr_to] / waehrung[curr_from]

print(umrechnen(100,"EURO","GBP"))
print(umrechnen(10,"EURO","DOLLAR"))
print(umrechnen(1, "DOLLAR", "GBP"))
