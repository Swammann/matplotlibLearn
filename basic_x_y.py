#
# Plotting median wages for age
#

from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  # The x values, represents ages

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]  # The y axis, median salary


plt.plot(ages_x, dev_y, color='#00635f', linestyle='--', label='All Developers')

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, marker='o', label='Python Developers')

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# plt.legend(['All Developers', 'Python Developers']),
# Using this method for legend requires knowing the order plt.plot was used
plt.legend()
# When you add 'label=' in the 'plt.plot' function
# it adds to the legend at the right plot

plt.show()





