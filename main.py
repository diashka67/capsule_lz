
import log as log
from graf_stat import plot_stock_prices
from  graf_stat import AAPL


def main():
    
    plotter = AAPL(file_path ='AAPL.csv', start_date = '2016-12-12', end_date = '2022-01-09')
    plotter.plot_stock_prices()
if __name__ == '__main__':
    main()
