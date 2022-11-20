# MusicMixer
This was a class project for CS 4701 (AI practicum) in the spring of 2019. My partners were [Katherine Pioro](https://www.linkedin.com/in/katherine-pioro-8a1183127?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAB8r3TkBrMNH5rIE6P-S_Ajfkc6yl5fLYps&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3B3fQz1EupT320gZPojtu8Sg%3D%3D&original_referer=) and [David Huang](https://www.linkedin.com/in/david-huang-86676a129/). The original github was hosted on our Cornell enterprise accounts. I have transferred over to my personal github for public view. 

## Instructions to Run
In order to run this project, you must first have the libraries
numpy, scipy, os, and random available for python. You should also have
the submodules scipy.io and scipy.fftpack available. Most importantly,
python should be installed on your machine.

You can adjust a few hyperparameters which are listed on lines 10-17 of
main.py

**input_dir** is the source of sound samples you would like to extract a random
population from.

**output_dir** is the output location of sound samples resulting from the
genetic algorithm. The 2 initial parents will be labeled parent1.wav and
parent2.wav while the offspring will be titled result_x where x is an integer.

**desired_chord** is the chord you deem as a desirable fitness characteristic
in the music samples. The string values can range from A_FLAT_MAJOR
to G_SHARP_MAJOR

**desired_scale** is the scale you deem as a desirable fitness characteristic
in the music samples. The string values can range from A_FLAT_MAJOR
to G_SHARP_MAJOR

**desired_generations** is the number of iterations you would like the
genetic algorithm to run for. A value of 1 would select two parents from the
initial population and return the recombined offspring.

**desired_crossover_points** is the number of crossover points for a
sound sample in frequency space.

**desired_mutations** is the number of potential mutations you would like
to occur for each offspring.

**desired_prob** is the percent probability for a single mutation to occur.

Entering the same directory as the main.py file through terminal and typing:
*python main.py*
will run the program and send outputs to the **output_dir** folder.
The program may take some while to run depending on the number of
generations. Higher iterations likely result in longer runtimes.

The *inputs* folder contains a few samples that you can use.
