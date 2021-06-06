class RM:
    @staticmethod
    def sort_tasks(queue):
        queue.sort(key=lambda el: el.wcet)
        return queue

