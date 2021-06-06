class EDF:
    @staticmethod
    def sort_tasks(queue):
        queue.sort(key=lambda el: el.deadline)
        return queue
