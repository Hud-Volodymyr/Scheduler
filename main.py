from EarliestDeadlineFirst import EDF
from RateMonotonic import RM
from Plotter import plot_stats,\
    plot_wait_time,\
    plot_free_time,\
    plot_avg_queue_len,\
    plot_discarded,\
    plot_rm_reverse_intensity

# plot_stats('FIFO')

# plot_stats(EDF)
# plot_stats(RM)

# plot_wait_time()
# plot_free_time()
# plot_avg_queue_len()
# plot_discarded()

plot_rm_reverse_intensity()
