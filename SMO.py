
class Scheduler:
    def __init__(self, queue, queue_size, algorithm, tact_size):
        self.queue = queue
        self.queue_size = queue_size
        if algorithm != 'FIFO':
            self.algorithm = algorithm
        else:
            self.algorithm = 'FIFO'
        self.tact_size = tact_size
        self.stats = {
            'avg_wait_time': 0,
            'complete': 0,
            'free_time': 0,
            'avg_queue_length': 0,
            'queue_length': [],
            'discarded': 0
        }
        self.rt_queue = []
        self.sys_clock = 0
        self.remainder_tact_time = 0
        self.processing = 0

    @property
    def schedule(self):
        while True:
            if self.processing == 0:
                all_tasks = len(self.rt_queue)
                # discard tasks with expired deadline
                self.rt_queue = [task for task in self.rt_queue if task.deadline > self.sys_clock]
                filtered = len(self.rt_queue)
                self.stats['discarded'] += all_tasks - filtered
            if len(self.rt_queue) == 0 and len(self.queue) == 0:
                # if all tasks complete break the loop
                break
            if len(self.queue) != 0 and self.remainder_tact_time == 0:
                # a new task comes if there are any in the queue and its a start of the tact!
                self.rt_queue += self.queue.pop(0)
                # recording queue length
                self.stats['queue_length'].append(len(self.rt_queue))
            if self.processing == 0:
                # if no task is processed sort tasks in queue according to algorithm
                if self.algorithm != 'FIFO':
                    self.rt_queue = self.algorithm.sort_tasks(self.rt_queue)
            if len(self.rt_queue) != 0:
                if self.remainder_tact_time != 0:
                    if self.rt_queue[0].wcet > self.remainder_tact_time:
                        # if we can't do a task in one tact
                        self.sys_clock += self.remainder_tact_time
                        self.rt_queue[0].wcet -= self.remainder_tact_time
                        self.processing = 1
                        self.remainder_tact_time = 0
                    else:
                        # if we can do a task in one tact
                        self.remainder_tact_time -= self.rt_queue[0].wcet
                        self.sys_clock += self.rt_queue[0].wcet
                        self.stats['avg_wait_time'] += self.sys_clock - self.rt_queue[0].start - self.rt_queue[0].wcet
                        # print('SysClock {} Task start time {} Task solution time {}'.format(self.sys_clock,
                        #                                                                    self.rt_queue[0].start,
                        #                                                                    self.rt_queue[0].wcet))
                        self.stats['complete'] += 1
                        self.processing = 0
                        del self.rt_queue[0]
                else:
                    # if we have no time in this tact left, proceed to the next tact
                    if self.rt_queue[0].wcet > self.tact_size:
                        # if solution time is too long for next tact
                        self.rt_queue[0].wcet -= self.tact_size
                        self.processing = 1
                        self.remainder_tact_time = 0
                        self.sys_clock += self.tact_size
                    else:
                        # if task can be complete
                        self.sys_clock += self.rt_queue[0].wcet
                        self.stats['avg_wait_time'] += self.sys_clock - self.rt_queue[0].start - self.rt_queue[0].wcet
                        self.stats['complete'] += 1
                        self.remainder_tact_time = self.tact_size - self.rt_queue[0].wcet
                        self.processing = 0
                        del self.rt_queue[0]
            else:
                if self.remainder_tact_time != 0:
                    self.stats['free_time'] += self.remainder_tact_time
                    self.sys_clock += self.remainder_tact_time
                    self.remainder_tact_time = 0
                else:
                    self.sys_clock += self.tact_size
                    self.stats['free_time'] += self.tact_size

        print(self.stats)


        self.stats['avg_wait_time'] = (self.stats['avg_wait_time'] / self.stats['complete'])
        self.stats['avg_queue_length'] = sum(self.stats['queue_length']) / self.queue_size

        return self.stats
