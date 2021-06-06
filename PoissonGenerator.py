import numpy as np
import random as r
from Task import Task


class Generator:
    def __init__(self, intensity, tact_number):
        self.poisson = np.random.poisson(intensity, tact_number)
        self.intensity = intensity
        self.queue_size = tact_number

    def generate_queue(self, solution_time):
        queue = []
        for i in range(len(self.poisson)):
            tact = []
            for j in range(self.poisson[i]):
                margin = r.uniform(solution_time * 0.2, solution_time * 0.4) / 2
                if r.random() < 0.5:  # Erlang flow takes every second task
                    tact.append(Task(i, solution_time + margin, i + (solution_time + margin) + r.randint(4, 10)))
                else:
                    tact.append(Task(i, solution_time - margin, i + (solution_time - margin) + r.randint(4, 10)))
            queue.append(tact)
        return queue



