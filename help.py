import matplotlib.pyplot as plt
fig, ax = plt.subplots()
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
bars = ax.bar(langs, students)
fig.canvas.draw()
r = fig.canvas.get_renderer()
heights = [bar.get_window_extent(r).height for bar in bars]
widths = [bar.get_window_extent(r).width for bar in bars]
print(heights)
print(widths)
