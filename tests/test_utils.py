
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.utils import calculate_stats, vendor_freq, monthly_expense

def test_calculate_stats_basic():
    data = [{"amount": 100}, {"amount": 300}]
    stats = calculate_stats(data)
    assert stats["total_spend"] == 400
    assert stats["mean"] == 200

def test_vendor_freq():
    data = [{"vendor": "A"}, {"vendor": "A"}, {"vendor": "B"}]
    freq = vendor_freq(data)
    assert freq == {"A": 2, "B": 1}

def test_monthly_expense():
    data = [{"date": "2025-07-01", "amount": 100}, {"date": "2025-07-25", "amount": 200}]
    trend = monthly_expense(data)
    assert trend == {"2025-07": 300.0}
