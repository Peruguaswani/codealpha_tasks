#Step 1: Create a dictionary with stock prices
stock_prices = {
    "AAPL":120,
    "TSLP":130,
    "GOOG":180,
    "MISFT":185,
    "AMAZON":190,
    "RELIANCE":175
}

print("\n" + "=" * 60)
print("        📈 SMART STOCK PORTFOLIO TRACKER 📈")
print("=" * 60)

# Step 2: Show available stocks
print("--Available Stocks--")

for stock , price in stock_prices.items():
    print(stock,"=",price)

print("\n ----enter your Stocks----")

# Step 3: Take user input
stock1 = input("Enter the stock name:").upper()
qty1 = int(input("Enter the quantity:"))

choice = input("\nDo you want to add another stock? (yes/no): ").lower()

# Default values
stock2 = ""
qty2 = 0

# If user wants second stock
if choice == "yes":

    stock2 = input("Enter the stock name:").upper()
    qty2 = int(input("Enter the quantity:"))

# Step 4: Calculate investment
total = 0

if stock1 in stock_prices:
    total += stock_prices[stock1] * qty1
else:
    print(stock1,"is not available")

if stock2 in stock_prices:
    total += stock_prices[stock2] * qty2
elif stock2 != "":
    print(stock2,"is not available")

# Step 5: Display total investment
print("Total Investment value:", total)

# File handling
file = open("portfolio.txt","w")

file.write("Stock portfolio Summary\n")
file.write("---------------\n")

file.write(f"Stock 1 Name: {stock1}\n")
file.write(f"Quantity: {qty1}\n")

if stock2 != "":
    file.write(f"Stock 2 Name: {stock2}\n")
    file.write(f"Quantity: {qty2}\n")

file.write(f"Total Investment Value: {total}\n")

file.close()

print("Data saved successfully!")