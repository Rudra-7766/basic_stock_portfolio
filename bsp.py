import requests
import pandas as pd
import numpy as np
import yfinance as yf
class portfolio:
    def __init__(self):
        self.stocks ={}
    def add_stock(self,ticker,shares,purchase_price):
        self.stocks[ticker]={'shares':shares,'purchase_price':purchase_price}
    def remove_stock(self,ticker):
        if ticker in self.stocks:
            del self.stocks[ticker]
    def calculate_value(self):
        total_value=0
        for ticker,data in self.stocks.items():
            current_price=yf.Ticker(ticker).info['regularMarketPrice']
            total_value+=current_price*data['shares']
            return total_value
    def calculate_profit_loss(self):
        total_profit_loss=0
        for ticker,data in self.stocks.items():
                current_price = yf.Ticker(ticker).info['regularMarketPrice']
                profit_loss = (current_price - data['purchase_price'])*data['shares']
                total_profit_loss +=profit_loss
                return total_profit_loss
Portfolio=portfolio()
Portfolio.add_stock('AAPL',10,150)
Portfolio.add_stock('GOOGL',5,2500)
print(Portfolio.calculate_value())
print(Portfolio.calculate_profit_loss())
                    
