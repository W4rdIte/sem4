import threading
import time
import random


class Philosopher(threading.Thread):
    def __init__(self, id, left_fork, right_fork, meals_to_eat, log_lock):
        threading.Thread.__init__(self)
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.meals_to_eat = meals_to_eat
        self.log_lock = log_lock
        self.meals_eaten = 0

    def run(self):
        while self.meals_eaten < self.meals_to_eat:
            self.think()
            self.eat()

    def think(self):
        with self.log_lock:
            print(f"Filozof {self.id + 1} myśli.")
        time.sleep(random.uniform(1, 3))

    def eat(self):
        left, right = self.left_fork, self.right_fork

        if self.id % 2 == 0:
            first, second = left, right
        else:
            first, second = right, left

        with first:
            with self.log_lock:
                print(f"Filozof {self.id + 1} podniósł pierwszy widelec.")
            with second:
                with self.log_lock:
                    print(f"Filozof {self.id +1 } podniósł drugi widelec.")
                self.meals_eaten += 1
                with self.log_lock:
                    print(f"Filozof {self.id + 1} je posiłek {self.meals_eaten}.")
                time.sleep(random.uniform(1, 2))

        with self.log_lock:
            print(f"Filozof {self.id + 1} odkłada widelce.")


def main():
    num_philosophers = 5
    meals_to_eat = 3
    forks = [threading.Lock() for _ in range(num_philosophers)]
    log_lock = threading.Lock()

    philosophers = [
        Philosopher(
            i, forks[i], forks[(i + 1) % num_philosophers], meals_to_eat, log_lock
        )
        for i in range(num_philosophers)
    ]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

    print("Wszyscy filozofowie zakończyli jedzenie.")


if __name__ == "__main__":
    main()
