import time
from collections import defaultdict
from celery import Celery

app = Celery("tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0")

def get_prime_factors(num: int) -> int:
    divisor: int = 2
    if num <= 1:
        return []

    prime_factors = []
    current_factor = num
    while True:
        if current_factor == 1:
            break
        if current_factor % divisor != 0:
            divisor += 1
            continue
        current_factor = current_factor // divisor
        prime_factors.append(divisor)
    return prime_factors


def is_square_num(num: int) -> bool:
    prime_factors = get_prime_factors(num)
    factor_freq = defaultdict(int)

    for factor in prime_factors:
        factor_freq[factor] += 1

    for freq in factor_freq.values():
        if freq % 2 != 0:
            return False
        continue
    return True


@app.task
def get_prime_factors_chunk(nums: list[int]) -> list[dict]:
    return [{"n": n, "factors": get_prime_factors(n)} for n in nums]
