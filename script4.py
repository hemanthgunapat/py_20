
def cal_bill(price,quantity):
    total_cost = price * quantity
    delivary_fee=40
    if (total_cost<200):
        total_cost+=delivary_fee
        return total_cost
print(cal_bill(50,2))


