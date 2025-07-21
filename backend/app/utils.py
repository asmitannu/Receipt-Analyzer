import re
import statistics
import os
import pandas as pd
from collections import defaultdict
from datetime import datetime

"""Sample data expected format (list of dictionaries):
 data = [
     {"vendor": "Airtel", "date": "2024-03-15", "amount": 599.0},
     {"vendor": "Reliance", "date": "2024-04-10", "amount": 1200.0}, 
    ]
"""
#--------------SEARCHING------------
# Keyword Search
def keyword_based_search(vendor, data):
    return [d for d in data if vendor.lower() in d['vendor'].lower()]  #case-sensitivity

# Amount Search
def amount_based_search(min_amt, max_amt, data):
    return [d for d in data if (d['amount'] <= max_amt and d['amount'] >= min_amt)]

# Pattern Search
def pattern_based_search(pattern,data):
    return [d for d in data if re.search(pattern, d['vendor'], re.IGNORECASE)]

#---------------SORTING--------------
# SORT BASED ON KEY        O(n LOG n)
def sort_data(data, key = "amount", reverse = False):
    return sorted(data, key = lambda x: x[key], reverse = reverse)  #ascending order

#--------------AGGREGATE-------------
# SUM, MEAN, MEDIAN, MODE
def calculate_stats(data, currency_filter="INR"):
    filtered = [d for d in data if d.get("currency") == currency_filter]
    amounts = [d['amount'] for d in data]
    
    stats = {
        "total_spend": sum(amounts),
        "mean": round(statistics.mean(amounts) , 2) if amounts else 0,
        "median" : round(statistics.median(amounts),2) if amounts else 0,
        "mode": statistics.mode(amounts) if len(amounts) < len(set(amounts)) else "no mode"
    }
    # Create a DataFrame and export to CSV
    df = pd.DataFrame([stats])
    os.makedirs("output/exported_reports", exist_ok=True)
    df.to_csv("output/exported_reports/summary_{currency_filter}.csv", index=False)

    return stats

# FREQUENCY DISTRIBUTIONS
def vendor_freq(data):
    freq = defaultdict(int)   
    for d in data:
        freq[d["vendor"]] += 1
    return dict(freq)

# MONTHLY EXPENDITURE
def monthly_expense(data):
    monthly_totals = defaultdict(float)
    for d in data:
        try:
            dt = datetime.strptime(d["date"], "%Y-%m-%d")
            month_key = dt.strftime("%Y-%m")
            monthly_totals[month_key] += d["amount"]
        except:
            pass
    return dict(monthly_totals)
