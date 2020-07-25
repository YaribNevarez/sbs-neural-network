import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1)

fig.suptitle('Performance')

begin   = np.array([0.000, 0.001, 0.054, 0.059, 0.870, 0.874, 1.266, 1.270, 1.595, 1.598, 1.926, 1.929, 2.144, 2.149, 2.924, 3.038, 3.042])
latency = np.array([3.085, 0.056, 1.653, 0.813, 2.176, 0.395, 1.666, 0.327, 2.146, 0.330, 2.145, 0.218, 1.431, 0.774, 0.116, 0.820, 0.042])
event   = ["SbS_Network", "HX_IN_Software", "HX_IN_Hardware", "H1_CONV_Software", "H1_CONV_Hardware", "H2_POOL_Software", "H2_POOL_Hardware", "H3_CONV_Software", "H3_CONV_Hardware", "H3_CONV_Software", "H3_CONV_Hardware", "H3_CONV_Software", "H3_CONV_Hardware", "H4_POOL_Software", "H5_DENSE_Software", "H5_DENSE_Hardware", "HY_OUT_Software"]

ax1.barh(range(len(begin)),  latency, left=begin)
ax1.grid(linestyle = ':')


plt.sca(ax1)
plt.yticks(range(len(begin)), event)
ax1.tick_params(axis='both', which='major', labelsize=5)
ax1.tick_params(axis='both', which='minor', labelsize=1)

plt.xlabel("Schedule (mS)")
plt.ylabel("Task")

data = [[ 0.001, 0.059, 0.874, 1.270, 1.598, 1.929, 2.149, 2.924, 3.042],
        [ 0.056, 0.813, 0.395, 0.327, 0.330, 0.218, 0.774, 0.116, 0.042],
        [ 1.653, 2.176, 1.666, 2.146, 2.145, 1.431, 0.000, 0.820, 0.000]]

columns = ("HX_IN", "H1_CONV", "H2_POOL", "H3_CONV", "H3_CONV", "H3_CONV", "H4_POOL", "H5_DENSE", "HY_OUT")
rows = ["Hardware", "Software", "II OFFSET"]

# Get some pastel shades for the colors
colors = plt.cm.Blues(np.linspace(0.5, .75, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    ax2.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(data[row])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

plt.sca(ax2)
# Add a table at the bottom of the axes
the_table = ax2.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom',
                      fontsize='xx-small')

the_table.auto_set_font_size(False)
the_table.set_fontsize(7)


# Adjust layout to make room for the table:

plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Latency (mS)")

plt.xticks([])
ax2.grid(linestyle = ':')


plt.show()