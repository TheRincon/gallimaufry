import ding_an_sich_plot as das
import pandas as pd

if __name__ == '__main__':
    x = pd.read_csv('/home/rincon/Desktop/bird_diets.csv', sep=',')
    plotted = das.ding_an_sich_plot(
        x,
        color=['#F9E4B7', '#603101', '#603101', '#232B2B'],
        ylabel='Grams / Day',
        title='Large Birds'
    )
    das.save_figure(plotted, '/home/rincon/Desktop/Workspace/gallimaufry/output/', 'Bird_Diets.png')
