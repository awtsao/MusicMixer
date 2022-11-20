from scipy.io import wavfile
from os import listdir
import numpy as np
import random
import recombination
import genetic_algorithm
import objective_function

# Parameters that can be tuned to your liking
input_dir = 'inputs'
output_dir = 'outputs'
desired_chord = 'C_MAJOR'
desired_scale = 'C_MAJOR'
desired_generations = 1
desired_crossover_points = 5
desired_mutations = 10
desired_prob = 50

if __name__ == '__main__':
    file_list = listdir(input_dir)
    init_pop = []
    rand_idxs = random.sample(range(len(file_list)), int(len(file_list) / 2))
    for i in rand_idxs:
        dat = (wavfile.read(input_dir + '/' +file_list[i]))[1]
        if(dat.ndim == 1):
            dat_mono = dat
        else:
            dat_mono = dat.T[0]
        loudest = np.amax(np.abs(dat_mono))
        init_pop.append(np.float32(dat_mono / loudest))
    pop = genetic_algorithm.evolve(init_pop, desired_generations, desired_chord, desired_scale)
    for i in range(len(pop)):
        wavfile.write(output_dir + '/result_' + str(i) + '.wav', 44100, pop[i])
