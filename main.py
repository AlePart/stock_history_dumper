

import csv
import sys
import price_manager as pm


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python main.py <stock> <start_date> <end_date> <filename>")
        sys.exit(1)

    stock = sys.argv[1]
    date_start = sys.argv[2]
    date_end = sys.argv[3]
    filename = sys.argv[4]

    price = pm.get_edo_stock_price(stock, date_start, date_end)

    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Price"])
        for i in range(len(price)):
            writer.writerow([price.index[i], price.iloc[i]])

    print("Data dumped successfully.")