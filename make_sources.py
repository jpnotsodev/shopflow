import csv
import json
import random
from pathlib import Path

CWD = Path(__file__).parent
SOURCES_DIR = Path(CWD / "sources")
# print(f"current_working_dir: {CWD}\nsources_dir: {SOURCES_DIR}")

cities = ["Karachi", "Lahore", " lahore ", "Dubai", "LONDON", "Toronto", "Austin"]
product_categories = ["Phone", "Audio", "Gaming", "Accessories", "Laptops"]

# creates the 'sources' folder if it doesn't exists
SOURCES_DIR.mkdir(exist_ok=True)

def generate_mock_customers():
    filename = "customers.csv"
    with open(SOURCES_DIR / filename, "w", encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["customer_id", "name", "email", "city", "date_added"])
        for i in range(1, 2001):
            # email is empty for every 98th customer
            email = "" if i % 98 == 0 else f"customer{i}@_email@sample.com"
            custrow = [
                i, 
                f"Customer {i}", 
                email, 
                random.choice(cities), 
                f"2026-{random.randint(1, 12)}-{random.randint(1, 28)}"
            ]
            csvwriter.writerow(custrow)
            # create a duplicate for every 200th customer
            if i % 200 == 0:
                csvwriter.writerow(custrow) 

def generate_mock_products():
    filename = "products.json"
    products = []
    
    for i in range(1, 41):
        random_category = random.choice(product_categories)
        product_json = {"id": i,
                        "name": f"{random_category} {i}",
                        "sku": f"SKU-00{i:02}",
                        "category": random_category,
                        "price": round(random.uniform(420, 5000), 2)}
        products.append(product_json)
    (SOURCES_DIR / filename).write_text(json.dumps(products, indent=4))


if __name__ == "__main__":
    generate_mock_customers()
    generate_mock_products()