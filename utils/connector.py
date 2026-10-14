import pandas as pd
import numpy as np
from datetime import datetime

def fetch_live_ecommerce_data():
    """
    Simulates a live connection to an E-commerce API (e.g., Shopify or Stripe)
    and returns a DataFrame containing recent sales transaction data.
    """
    np.random.seed(42)
    dates = pd.date_range(end=datetime.today(), periods=90, freq='D')
    
    categories = ['Smart Home', 'Audio', 'Gaming', 'Accessories']
    
    data = []
    for date in dates:
        for cat in categories:
            transactions = np.random.randint(5, 20)
            base_price = 50 if cat == 'Accessories' else (120 if cat == 'Audio' else 250)
            revenue = transactions * np.random.normal(base_price, 15)
            
            data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Category': cat,
                'Transactions': int(transactions),
                'Revenue': round(float(revenue), 2)
            })
            
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

if __name__ == "__main__":
    df = fetch_live_ecommerce_data()
    print(df.head())