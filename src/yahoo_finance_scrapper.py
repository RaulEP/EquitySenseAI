import yfinance as yf
import os

ROOT_DIR = 'C:\Development\EquitySenseAI'
os.chdir(ROOT_DIR)
os.makedirs("financials", exist_ok=True)

def get_financials(ticker, doc_name='income_statement'):

    if isinstance(doc_name, str):
        # If a single string is passed, convert it to a list
        doc_name = [doc_name]

    # Get stock data
    stock = yf.Ticker(ticker)

    for doc in doc_name:
        if doc == 'income_statement':
            # Download and save income statement
            income = stock.financials
            income.to_csv("financials/" + f'{ticker}_income_statement.csv')
            print(f"{doc} for {ticker} have been saved as CSV files")

        if doc == 'balance_sheet':
            # Download and save balance sheet
            balance = stock.balance_sheet
            balance.to_csv("financials/" + f'{ticker}_balance_sheet.csv')
            print(f"{doc} for {ticker} have been saved as CSV files")

        if doc == 'cash_flow':
            # Download and save cash flow
            cashflow = stock.cashflow
            cashflow.to_csv("financials/" + f'{ticker}_cash_flow.csv')
            print(f"{doc} for {ticker} have been saved as CSV files")

# Use it for any ticker
ticker = "SBUX"  # Change this to any stock ticker
get_financials(ticker, 'income_statement')