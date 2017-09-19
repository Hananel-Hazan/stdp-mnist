from __future__ import division

import matplotlib.pyplot as plt
import cPickle as p
import numpy as np
import os

model_name = 'csnn_pc_inhibit_far'

top_level_path = os.path.join('..', '..')
delta_dir = os.path.join(top_level_path, 'deltas', model_name)

if not os.path.isdir(os.path.join(delta_dir, 'delta_plots')):
    os.makedirs(os.path.join(delta_dir, 'delta_plots'))

print '\n'
print '\n'.join(
    [str(idx + 1) + ' | ' + file_name for idx, file_name in enumerate(sorted(os.listdir(delta_dir))) if
     '.p' in file_name]), '\n'

to_plot = raw_input('Enter the index of the file from above which you\'d like to plot: ')
file_name = sorted([file_name for file_name in os.listdir(delta_dir) if '.p' in file_name])[int(to_plot) - 2]

# get pickled deltas dictionary (voting mechanism, performance recordings over training)
_, deltas = p.load(open(os.path.join(delta_dir, file_name), 'rb'))

print deltas
print type(deltas)
print '\n'

delta_plots = []
delta_plots.append(plt.plot(deltas, label='deltas')[0])

plt.legend(handles=delta_plots)

fig = plt.gcf()
fig.set_size_inches(16, 12)

plt.xlabel('Iteration number (1 through ' + str(len(deltas) * 10) + ')')
plt.xticks([x for x in xrange(0, len(deltas) + 25, 50)],
           [x * 10 for x in xrange(0, len(deltas) + 25, 50)])
plt.ylabel('Delta changes')
plt.ylim(0, np.amax(deltas) )

plt.title(' '.join(file_name.split('_')))
plt.tight_layout()

plt.savefig(os.path.join(delta_dir, 'delta_plots', file_name[:-2].replace('.', '_')))
plt.show()

print '\n'
