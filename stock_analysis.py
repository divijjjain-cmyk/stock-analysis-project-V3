# Simple Stock Analyzer 
# This script fetches stock data, calculates basic metrics, and plots a chart.
# Made by Divij Jain 
# Requirements: pip install yfinance pandas numpy matplotlib

    plt.ylabel('Price ($)')
    plt.legend()  # Show labels
    plt.grid(True)  # Add grid for easier reading
    plt.xticks(rotation=45)  # Rotate dates so they don't overlap
    plt.tight_layout()  # Make it look neat
    plt.savefig(f'{symbol}_chart.png')  # Save as an image file
    print(f"\nChart saved as {symbol}_chart.png. Opening it...")
    plt.show()  # Display the chart
def main():
    """
    Main function: Asks for input and runs the analysis.
    """
    print("=== Simple Stock Analyzer ===")
    print("This tool fetches real stock data and shows basic analysis.")
    print("Generated on:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    symbol = input("\nEnter a stock symbol (e.g., AAPL for Apple): ").upper().strip()
    if not symbol:
        symbol = 'AAPL'  # Default to Apple if nothing entered
        print("Using default: AAPL")
    
    data = get_stock_data(symbol)
    if data is None:
        return  # Stop if no data
    
    sma_20 = calculate_basics(data)
    plot_chart(data, sma_20, symbol)
    
    print("\nAnalysis complete! Check the chart and metrics above.")
    print("Note: This is for learning—stocks can be risky!")
if __namze__ == "__main__":
    main()
vol = data['Close'].pct_change().std() * 100; print(f"Volatility: {vol:.2f}%")
