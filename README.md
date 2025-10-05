A basic Python script I made in Grade 11 using youtube, coursera and AI to analyze stock prices. It pulls real data from Yahoo Finance, calculates simple stuff like average price and total return, and plots a chart with a moving average. Great for learning data analysis!

Features
Fetches 1 year of closing prices for any stock (e.g., AAPL).
Computes: Average close, total return (%), latest price, 20-day moving average.
Gives a quick insight (upward or downward trend).
Shows results in the console and saves a PNG chart.
Setup
Install Python from python.org (version 3.8+). Add to PATH on Windows.
Open terminal (Command Prompt on Windows, Terminal on Mac) and run: pip install yfinance pandas numpy matplotlib.
Save the code as simple_stock_analyzer.py in a folder.
How to Run
In terminal, go to the folder: cd your-folder-path.
Run: python simple_stock_analyzer.py.
Enter a stock symbol (e.g., AAPL) when prompted. Defaults to AAPL if blank.
Check the console for metrics and a chart window/PNG file.
Example output:
Average Closing Price: $145.23
Total Return over 1 Year: 15.20%
Insight: Stock is above its 20-day average (possible upward trend)!
Chart saved as AAPL_chart.png.

Try These Symbols
AAPL (Apple)
MSFT (Microsoft)
TSLA (Tesla)
Troubleshooting
"No module named...": Re-run pip install.
"No data": Check symbol spelling, ensure internet.
Chart not showing: Look for the PNG file.
Errors? Google "Python [error message]".

Made by Divij Jain 
This is for education—stocks are risky! Built with help from YouTube tutorials and Python docs. Questions? Comment below.
