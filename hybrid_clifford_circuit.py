from matplotlib import pyplot as plt
import graphsim
import numpy as np
from pdb import set_trace

# Parameters

N = 40
num_steps = 20*N
num_samples = 100
prob = 0.1

sample_times = np.rint(np.linspace(0, num_steps, num_samples)).astype(int)
sample_time_check_list = np.isin(np.arange(num_steps+1), sample_times)

unaveraged_entropies_vs_time = np.zeros(num_samples)
A = int(N/2)
ent_subsystem = np.arange(A).tolist()

# Main

gr = graphsim.GraphRegister(N)

for n in range(num_steps):

    parity = n % 2
    for v in range(parity, parity+N, 2):
        gr.randomTwoQubitClifford(v,(v+1)%N)

    measurement_list = np.random.choice([0,1], size=N, p=[1-prob, prob])
    measured_indices = np.argwhere(measurement_list > 0)[:,0].tolist()

    for v in measured_indices:
        gr.measure(v)

    if sample_time_check_list[n]:
        index = np.argwhere(sample_times == n)
        unaveraged_entropies_vs_time[index] = gr.entEntropy(ent_subsystem)

print("d/N^2 = {}".format(gr.degreeSum() / N**2))
set_trace()
#
#plt.plot(sample_times, unaveraged_entropies_vs_time, marker='o')
#plt.xlabel("Time")
#plt.ylabel("Half-chain entropy")
#plt.show()
