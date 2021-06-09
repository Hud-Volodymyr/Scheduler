import numpy as np
from PoissonGenerator import Generator
from SMO import Scheduler
import matplotlib.pyplot as plt
from EarliestDeadlineFirst import EDF
from RateMonotonic import RM


AVG_SOLUTION_1 = 0.045
AVG_SOLUTION_2 = 0.09
AVG_SOLUTION_3 = 0.2
QUEUE_SIZE = 100
intensities = np.linspace(0.1, 30)
tact_size = 1


def plot_stats(algorithm):
    stats_wait_time = []
    stats_free_time = []
    stats_avg_queue_length = []
    for i in intensities:
        generator = Generator(i, QUEUE_SIZE, 0.5, 0.3, 0.2)
        queue = generator.generate_queue(AVG_SOLUTION_1, AVG_SOLUTION_2, AVG_SOLUTION_3)
        scheduler = Scheduler(
            queue, QUEUE_SIZE, algorithm, tact_size
        )
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


def plot_wait_time():
    stats_wait_time_1 = []
    stats_wait_time_2 = []
    stats_wait_time_3 = []

    for i in intensities:
        generator = Generator(i, QUEUE_SIZE, 0.5, 0.3, 0.2)
        queue_1 = generator.generate_queue(AVG_SOLUTION_1, AVG_SOLUTION_2, AVG_SOLUTION_3)
        queue_2 = queue_1.copy()
        queue_3 = queue_1.copy()
        scheduler_1 = Scheduler(
            queue_1, QUEUE_SIZE, 'FIFO', tact_size
        )
        scheduler_2 = Scheduler(
            queue_2, QUEUE_SIZE, EDF, tact_size
        )
        scheduler_3 = Scheduler(
            queue_3, QUEUE_SIZE, RM, tact_size
        )
        stats_1 = scheduler_1.schedule
        stats_2 = scheduler_2.schedule
        stats_3 = scheduler_3.schedule
        stats_wait_time_1.append(stats_1['avg_wait_time'])
        stats_wait_time_2.append(stats_2['avg_wait_time'])
        stats_wait_time_3.append(stats_3['avg_wait_time'])

    fig = plt.figure(figsize=(11, 7))
    fig.suptitle('Час очікування від інтенсивності')
    plot = fig.add_subplot(311)
    plot.set_title('FIFO')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час очікування')
    plot.plot(intensities, stats_wait_time_1)
    plot = fig.add_subplot(312)
    plot.set_title('EDF')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час очікування')
    plot.plot(intensities, stats_wait_time_2)
    plot = fig.add_subplot(313)
    plot.set_title('RM')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час очікування')
    plot.plot(intensities, stats_wait_time_3)
    plt.subplots_adjust(wspace=0.1, hspace=1, bottom=0.1, top=0.9)
    plt.tight_layout()
    plt.show()


def plot_free_time():
    stats_free_time_1 = []
    stats_free_time_2 = []
    stats_free_time_3 = []

    for i in intensities:
        generator = Generator(i, QUEUE_SIZE, 0.5, 0.3, 0.2)
        queue_1 = generator.generate_queue(AVG_SOLUTION_1, AVG_SOLUTION_2, AVG_SOLUTION_3)
        queue_2 = queue_1.copy()
        queue_3 = queue_1.copy()
        scheduler_1 = Scheduler(
            queue_1, QUEUE_SIZE, 'FIFO', tact_size
        )
        scheduler_2 = Scheduler(
            queue_2, QUEUE_SIZE, EDF, tact_size
        )
        scheduler_3 = Scheduler(
            queue_3, QUEUE_SIZE, RM, tact_size
        )
        stats_1 = scheduler_1.schedule
        stats_2 = scheduler_2.schedule
        stats_3 = scheduler_3.schedule
        stats_free_time_1.append(stats_1['free_time'])
        stats_free_time_2.append(stats_2['free_time'])
        stats_free_time_3.append(stats_3['free_time'])

    fig = plt.figure(figsize=(11, 7))
    fig.suptitle('Час простою від інтенсивності')
    plot = fig.add_subplot(311)
    plot.set_title('FIFO')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час простою')
    plot.plot(intensities, stats_free_time_1)
    plot = fig.add_subplot(312)
    plot.set_title('EDF')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час простою')
    plot.plot(intensities, stats_free_time_2)
    plot = fig.add_subplot(313)
    plot.set_title('RM')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середній час простою')
    plot.plot(intensities, stats_free_time_3)
    plt.subplots_adjust(wspace=0.1, hspace=1, bottom=0.1, top=0.9)
    plt.tight_layout()
    plt.show()


def plot_avg_queue_len():
    stats_avg_queue_length_1 = []
    stats_avg_queue_length_2 = []
    stats_avg_queue_length_3 = []

    for i in intensities:
        generator = Generator(i, QUEUE_SIZE, 0.5, 0.3, 0.2)
        queue_1 = generator.generate_queue(AVG_SOLUTION_1, AVG_SOLUTION_2, AVG_SOLUTION_3)
        queue_2 = queue_1.copy()
        queue_3 = queue_1.copy()
        scheduler_1 = Scheduler(
            queue_1, QUEUE_SIZE, 'FIFO', tact_size
        )
        scheduler_2 = Scheduler(
            queue_2, QUEUE_SIZE, EDF, tact_size
        )
        scheduler_3 = Scheduler(
            queue_3, QUEUE_SIZE, RM, tact_size
        )
        stats_1 = scheduler_1.schedule
        stats_2 = scheduler_2.schedule
        stats_3 = scheduler_3.schedule
        stats_avg_queue_length_1.append(stats_1['avg_queue_length'])
        stats_avg_queue_length_2.append(stats_2['avg_queue_length'])
        stats_avg_queue_length_3.append(stats_3['avg_queue_length'])

    fig = plt.figure(figsize=(11, 7))
    fig.suptitle('Довжина черги від інтенсивності')
    plot = fig.add_subplot(311)
    plot.set_title('FIFO')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середня довжин черги')
    plot.plot(intensities, stats_avg_queue_length_1)
    plot = fig.add_subplot(312)
    plot.set_title('EDF')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середня довжин черги')
    plot.plot(intensities, stats_avg_queue_length_2)
    plot = fig.add_subplot(313)
    plot.set_title('RM')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Середня довжин черги')
    plot.plot(intensities, stats_avg_queue_length_3)
    plt.subplots_adjust(wspace=0.1, hspace=1, bottom=0.1, top=0.9)
    plt.tight_layout()
    plt.show()


def plot_discarded():
    stats_discarded_1 = []
    stats_discarded_2 = []
    stats_discarded_3 = []

    for i in intensities:
        generator = Generator(i, QUEUE_SIZE, 0.5, 0.3, 0.2)
        queue_1 = generator.generate_queue(AVG_SOLUTION_1, AVG_SOLUTION_2, AVG_SOLUTION_3)
        queue_2 = queue_1.copy()
        queue_3 = queue_1.copy()
        scheduler_1 = Scheduler(
            queue_1, QUEUE_SIZE, 'FIFO', tact_size
        )
        scheduler_2 = Scheduler(
            queue_2, QUEUE_SIZE, EDF, tact_size
        )
        scheduler_3 = Scheduler(
            queue_3, QUEUE_SIZE, RM, tact_size
        )
        stats_1 = scheduler_1.schedule
        stats_2 = scheduler_2.schedule
        stats_3 = scheduler_3.schedule
        stats_discarded_1.append(100 * stats_1['discarded'] / (stats_1['complete'] + stats_1['discarded']))
        stats_discarded_2.append(100 * stats_2['discarded'] / (stats_2['complete'] + stats_2['discarded']))
        stats_discarded_3.append(100 * stats_3['discarded'] / (stats_3['complete'] + stats_3['discarded']))

    fig = plt.figure(figsize=(11, 7))
    fig.suptitle('Кількість відкинутих задач від інтенсивності(у відсотках)')
    plot = fig.add_subplot(311)
    plot.set_title('FIFO')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Кількість відкинутих задач')
    plot.plot(intensities, stats_discarded_1)
    plot = fig.add_subplot(312)
    plot.set_title('EDF')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Кількість відкинутих задач')
    plot.plot(intensities, stats_discarded_2)
    plot = fig.add_subplot(313)
    plot.set_title('RM')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Кількість відкинутих задач')
    plot.plot(intensities, stats_discarded_3)
    plt.subplots_adjust(wspace=0.1, hspace=1, bottom=0.1, top=0.9)
    plt.tight_layout()
    plt.show()


def plot_rm_reverse_intensity():
    stats_discarded_1 = []
    stats_discarded_2 = []

    for i in intensities:
        generator_1 = Generator(i, QUEUE_SIZE, 0.5, 0.3, 0.2)
        generator_2 = Generator(i, QUEUE_SIZE, 0.2, 0.3, 0.5)
        queue_1 = generator_1.generate_queue(AVG_SOLUTION_1, AVG_SOLUTION_2, AVG_SOLUTION_3)
        queue_2 = generator_2.generate_queue(AVG_SOLUTION_1, AVG_SOLUTION_2, AVG_SOLUTION_3)
        scheduler_1 = Scheduler(
            queue_1, QUEUE_SIZE, RM, tact_size
        )
        scheduler_2 = Scheduler(
            queue_2, QUEUE_SIZE, RM, tact_size
        )
        stats_1 = scheduler_1.schedule
        stats_2 = scheduler_2.schedule
        stats_discarded_1.append(100 * stats_1['discarded'] / (stats_1['complete'] + stats_1['discarded']))
        stats_discarded_2.append(100 * stats_2['discarded'] / (stats_2['complete'] + stats_2['discarded']))

    fig = plt.figure(figsize=(10, 7))
    fig.suptitle('Кількість відкинутих задач від інтенсивності(у відсотках)')
    plot = fig.add_subplot(211)
    plot.set_title('0.5, 0.3, 0.2')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Кількість відкинутих задач')
    plot.plot(intensities, stats_discarded_1)
    plot = fig.add_subplot(212)
    plot.set_title('0.2, 0.3, 0.5')
    plot.set_xlabel('Інтенсивність')
    plot.set_ylabel('Кількість відкинутих задач')
    plot.plot(intensities, stats_discarded_2)
    plt.subplots_adjust(wspace=0.1, hspace=1, bottom=0.1, top=0.9)
    plt.tight_layout()
    plt.show()
