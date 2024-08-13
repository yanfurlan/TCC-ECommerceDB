import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data(query):
    conn = sqlite3.connect('ECommerceDB.db')
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def plot_stock_levels():
    query = '''
    SELECT ProductName, Stock FROM Products
    '''
    data = fetch_data(query)
    product_names = [row[0] for row in data]
    stock_levels = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=product_names, y=stock_levels)
    plt.title('Stock Levels by Product')
    plt.xlabel('Product')
    plt.ylabel('Stock Level')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_stock_levels()
    plot_sales_by_product()
