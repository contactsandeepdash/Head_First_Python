def total_amount(price1, price2, price3):
    """
        This function takes the price of 3 items and returns the total order amount
    """
    # Compute the total order amount
    total = price1 + price2 + price3

    # return the total amount
    return total

# * represent multiple arguments
def total_amount_dynamic(*prices):
    # This function takes the price of 3 items and returns the total order amount

    total = 0
    # Compute the total order amount
    for price in prices:
        total += price

    # return the total amount
    return total


def total_amount_dynamic_with_discount(*prices, discount=0.0):
    # This function takes the price of 3 items and returns the total order amount

    total = 0
    # Compute the total order amount
    for price in prices:
        total += price

    total_discounted_price = total - (discount * total)
    # return the total_discounted_price
    return total_discounted_price

# **kwargs = flexibility with key word arguments
def total_amount_dynamic_with_discount_and_kwargs(*prices, discount=0.0, **kwargs):
    # This function takes the price of 3 items and returns the total order amount

    total = 0
    # Compute the total order amount
    for price in prices:
        total += price

    total_discounted_price = total - (discount * total)

    net_spend = total_discounted_price - kwargs['cashback']

    # return the net_spend
    return net_spend



def order_summary(*prices, **additionals):
    # This function takes the price of 3 items and returns the total order amount

    total = 0
    # Compute the total order amount
    for price in prices:
        total += price

    net_spend = total - additionals['discount']*total - additionals['cashback']

    if total >= 10000:
        reward_point = 300
    elif total >= 5000:
        reward_point = 200
    elif total >= 2000:
        reward_point = 100
    else:
        reward_point = 0

    # return the total_amount
    return total, net_spend, reward_point

print('Total order amount: {}'.format(total_amount(700, 800, 900)))
print('Total order amount dynamic: {}'.format(total_amount_dynamic(1000, 2000)))
print('total_discounted_price dynamic: {}'.format(total_amount_dynamic_with_discount(1000, 2000, discount=0.05)))

additionals = {'cashback': 5}
print('total_amount_dynamic_with_discount_and_kwargs: {}'.format(total_amount_dynamic_with_discount_and_kwargs(1000, 2000, **additionals)))


additionals = {'discount': 0.05, 'cashback': 5}
ta, ns, rp = order_summary(700, 599, 750, **additionals)
print('Customer order summary:\n', '\nTotal Amount:', ta, '\nNet Spend:', ns, '\nRewards point earned:', rp)

for i in (x*3 for x in [1, 2, 3, 4, 5]):
    print(i)