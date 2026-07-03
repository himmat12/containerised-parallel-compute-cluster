import time
from collections import defaultdict
from celery import Celery 

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

@app.task
def generate_k_square_numbers(k:int) -> list[int]:
    print(f"[Worker] Starting heavy {k} square numbers computation...")
    k_squares = []
    n = 1
    while n <= k:
        time.sleep(0.5)
        k_squares.append(n * n)
        n += 1          
    print(f"[Worker] Finished computation!\nResult: {k_squares}")
    return k_squares

# def main():
#     print('Heavy computation task')

# if __name__ == "__main__":
#     main()