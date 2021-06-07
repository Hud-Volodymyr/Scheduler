import numpy as np
from PoissonGenerator import Generator
from SMO import Scheduler
import matplotlib.pyplot as plt


AVG_SOLUTION = 0.045
QUEUE_SIZE = 100
intensities = np.linspace(0.1, 30)
tact_size = 1


def plot_stats(algorithm):
    stats_wait_time = []
    stats_free_time = []
    stats_avg_queue_length = []
    for i in intensities:
        generator = Generator(i, QUEUE_SIZE)
        scheduler = Scheduler(generator.generate_queue(AVG_SOLUTION), QUEUE_SIZE, algorithm, tact_size)
        stats = scheduler.schedule
        stats_wait_time.append(stats['avg_wait_time'])
        stats_free_time.append(stats['free_time'])
        stats_avg_queue_length.append(stats['avg_queue_length'])

    fig = plt.figure(figsize=(11, 7))
    if algorithm != 'FIFO':
        fig.suptitle(algorithm.__name__)
    else:
        fig.suptitle('FIFO')
    plot = fig.add_subplot(311)
    plot.set_title('Час очікування від інтенсивності')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час очікування')
    plot.plot(intensities, stats_wait_time)
    plot = fig.add_subplot(312)
    plot.set_title('Довжина черги від інтенсивності')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середня довжин черги')
    plot.plot(intensities, stats_avg_queue_length)
    plot = fig.add_subplot(313)
    plot.set_title("Час простою від інтенсивності")
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час простою')
    plot.plot(intensities, stats_free_time)
    plt.subplots_adjust(wspace=0.1, hspace=1, bottom=0.1, top=0.9)
    plt.tight_layout()
    plt.show()




