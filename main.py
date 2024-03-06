

import csv
import sys
import price_manager as pm


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <stock> <start_date> <end_date>")
        
        sys.exit(1)

    stock = sys.argv[1]
    date_start = sys.argv[2]
    date_end = sys.argv[3]


    price = pm.get_edo_stock_price(stock, date_start, date_end)
    filename = sys.argv[1] + "_from_{date_start}_to_{date_end}.csv".format(date_start=date_start, date_end=date_end)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Price"])
        for i in range(len(price)):
            writer.writerow([price.index[i], price.iloc[i]])

    print("Data dumped successfully.")