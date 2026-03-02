# DataCompression.py
"""Dynamically graphing compressed data length."""
from matplotlib import animation
import matplotlib.pyplot as plt
import random 
import seaborn as sns
import sys

def update(frame_number, prob, faces, lengths):
    """Configures bar plot contents for each animation frame."""
    # Generate two bits according to prob(0)
    length = 1
    if (random.random() > prob): length += 2 # bit 1
    if (random.random() > prob): length += 1 # bit 2
    lengths[0] += 2
    lengths[1] += length

    # reconfigure plot for compressed data length
    plt.cla()  # clear old contents contents of current Figure
    axes = sns.barplot(faces, lengths, palette='bright')  # new bars
#    axes.set_title(f'Compressed Data Length')
    axes.set(xlabel='', ylabel='Number of Bits')  
    axes.set_ylim(top=max(lengths) * 1.10)  # scale y-axis by 10%

    # display length above each patch (bar)
    for bar, length in zip(axes.patches, lengths):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        text = f'{length / lengths[0] * 2:,}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

# read command-line arguments for number of frames and rolls per frame
number_of_frames = int(sys.argv[1])  
probability_zero = float(sys.argv[2]) 

sns.set_style('whitegrid')  # white backround with gray grid lines
figure = plt.figure('Data Compression')  # Figure for animation
values = list(('Original', 'Compressed'))  # data type
lengths = [0] * 2  # original vs compressed

# configure and start animation that calls function update
compression_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(probability_zero, values, lengths))

plt.show()  # display window