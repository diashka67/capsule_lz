import pandas as pd
import matplotlib.pyplot as plt
from log import log


class AAPL:
    def __init__(self, file_path, start_date='2016-12-12', end_date='2022-01-09'):
        self.df = pd.read_csv(file_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
        self.df = self.df.reset_index(drop=True)
    
    
    
    #https://www.tutorialspoint.com/article/how-to-create-a-candlestick-chart-in-matplotlib
    @log
    def plot_stock_prices(self):
        plt.figure(figsize=(10,5), dpi = 80,  facecolor="#2d3bd6")
        ax = plt.gca()
        ax.set_facecolor("#0b3675")


        up = self.df[self.df.Close >= self.df.Open]
        down = self.df[self.df.Close < self.df.Open]
        
        # Тела свечей
        plt.bar(up.index, up.Close - up.Open, 0.5, bottom=up.Open, color="#2ae78b")
        plt.bar(down.index, down.Close - down.Open, 0.5, bottom=down.Open, color="#b81334")
        
        # Тени (фитили)
        plt.bar(up.index, up.High - up.Close, 0.08, bottom=up.Close, color='white')
        plt.bar(up.index, up.Low - up.Open, 0.08, bottom=up.Open, color='white')
        plt.bar(down.index, down.High - down.Open, 0.08, bottom=down.Open, color='white')
        plt.bar(down.index, down.Low - down.Close, 0.08, bottom=down.Close, color='white')
        
        plt.title('СТОИМОСТЬ АКЦИЙ APPLE', fontsize = 12, fontweight = 'bold', color='white')
        plt.xlabel('Дата', color='white')
        plt.ylabel('Цена', color='white')
        plt.grid(True, alpha = 0.3, color='white')

        

        max_index = len(self.df) - 1
        plt.xlim(-0.5, max_index + 0.5)

        step = max(1, len(self.df) // 5)
        plt.xticks(
                ticks = range(0, len(self.df), step), 
                labels = self.df['Date'].iloc[::step].dt.strftime('%d.%m.%Y'),
                rotation=45,
                color='white'
        )
        plt.tick_params(colors='white')
        plt.tight_layout()
        plt.show()



if __name__ == '__main__':
    main()
