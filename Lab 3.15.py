#This lab is inteded to print musical note frequencies
#Each hey has a frequency of f0*r^n where n is the number of keys (distance) from that key, and r is 2^(1/12)
#Given the inital key frequency, output that frequency and the next 3 higher key frequencies.
#Output the floating point value with two digits ager the decimal

import math

init_note_input = float(440)

output_frq = math.sqrt(init_note_input, (1/12)) 
first_from_output = init_note_input
second_from_output = init_note_input
thrid_from_output = init_note_input

print(f'{output_frq:.2f} Hz')
print(f'{first_from_output:.2f} Hz')
print(f'{second_from_output:.2f} Hz')
print(f'{thrid_from_output:.2f} Hz')