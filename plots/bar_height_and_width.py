import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.figure(figsize=(5,5), dpi=80)
myplot = plt.barh(y_pos, performance, height=0.8, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

for obj in myplot:
    # Let's say we want to set height of bars to always 5px..
    desired_h = 5
    current_h = obj.get_height()
    current_y = obj.get_y()
    pixel_h = obj.get_verts()[2][1] - obj.get_verts()[0][1]
    print("current position = ", current_y)
    print("current pixel height = ", pixel_h)

    # (A) Use ratio of pixels to height-units to calculate desired height
    h = desired_h / (pixel_h/current_h)
    obj.set_height(h)
    pixel_h = obj.get_verts()[2][1] - obj.get_verts()[0][1]
    print("now pixel height = ", pixel_h)

    # (B) Move the rectangle so it still aligns with labels and error bars
    y_diff = current_h - h # height is same units as y
    new_y = current_y + y_diff/2
    obj.set_y(new_y)
    print("now position = ", obj.get_y())
plt.show()
