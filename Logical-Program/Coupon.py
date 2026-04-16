import random

def generate_random(n):
    return random.randint(1, n)

def collect_coupons(n):
    collected = set()
    count = 0

    while len(collected) < n:
        num = generate_random(n)
        count += 1

        if num not in collected:
            collected.add(num)
            print(f"Collected new coupon: {num}")

    return count

n = int(input("Enter number of distinct coupons: "))
total= collect_coupons(n)
print(f"Total random numbers needed to collect all {n} coupons: {total}")