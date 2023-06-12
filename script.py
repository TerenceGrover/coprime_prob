# This script will generate a certain amount of numbers, check if they are coprime
# Check the frequency of coprime vs cofactor
# Establish whether or not it is close to 6/pi^2

import random
import pandas
import math

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1

def generate_numbers(amount, limit):
    df = pandas.DataFrame(columns=['num1', 'num2', 'coprime'])
    for i in range(amount):
        obj = dict(
            num1 = 0,
            num2 = 0,
            coprime = False
        )
        obj['num1'] = random.randint(0,limit)
        obj['num2'] = random.randint(0,limit)
        if is_coprime(obj['num1'], obj['num2']):
          obj['coprime'] = True
        df.loc[len(df)] = obj
    return df

def count_coprime(amount, limit):
    df = generate_numbers(amount, limit)
    true_count = (df['coprime'] == True).sum()
    prob = true_count / amount
    return (math.sqrt(6/prob))

print(count_coprime(100000,10000))

# It is.