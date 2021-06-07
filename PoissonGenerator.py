import numpy as np
import random as r
from Task import Task


class Generator:
    def __init__(self, intensity, tact_number):
        self.poisson_1 = np.random.poisson(intensity / 2, tact_number)
        self.poisson_2 = np.random.poisson(intensity / 4, tact_number)
        self.poisson_3 = np.random.poisson(intensity / 6, tact_number)
        self.intensity = intensity
        self.queue_size = tact_number

    def generate_queue(self, solution_time_1, solution_time_2, solution_time_3):
        queue = []
        queue_1 = self.iterate([], solution_time_1, self.poisson_1)
        queue_2 = self.iterate([], solution_time_2, self.poisson_2)
        queue_3 = self.iterate([], solution_time_3, self.poisson_3)
        for i in range(len(queue_1)):
            queue.append(queue_1[i] + queue_2[i] + queue_3[i])
            r.shuffle(queue[i])
        return queue

    def iterate(self, queue, solution_time, poisson):
        for i in range(len(poisson)):
            tact = []
            for j in range(poisson[i]):
                margin = r.uniform(solution_time * 0.2, solution_time * 0.4) / 2
                if r.random() < 0.5:
                    tact.append(Task(i, solution_time + margin, i + (solution_time + margin) + r.randint(4, 10)))
                else:
                    tact.append(Task(i, solution_time - margin, i + (solution_time - margin) + r.randint(4, 10)))
            queue.append(tact)
        return queue
