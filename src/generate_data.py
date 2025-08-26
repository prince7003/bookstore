import pandas as pd
import random

def create_bookstore_a():
    genres = ["Sci-Fi", "Romance", "Historical", "Psychology", "Fantasy", "Mystery"]
    authors = ["A. Clarke", "M. Atwood", "B. Cornwell", "D. Ariely", "S. Hawke", "R. Martin"]

    rows = []
    for i in range(1, 31):
        rows.append({
            "book_id": i,
            "title": f"Book_A_{i}",
            "author": random.choice(authors),
            "genre": random.choice(genres),
            "price_usd": round(random.uniform(5, 30), 2),
            "rating": round(random.uniform(3.0, 5.0), 1),
            "sales_count": random.randint(100, 2000),
            "bookstore_name": random.choice(["CityBooks", "Read&Co"])
        })

    df = pd.DataFrame(rows)
    df.to_csv("data/bookstore_a.csv", index=False)

def create_bookstore_b():
    categories = ["Science Fiction", "Romantic", "Historical", "Psychology", "Fantasy", "Mystery"]
    writers = ["A. Clarke", "M. Atwood", "B. Cornwell", "D. Ariely", "S. Hawke", "R. Martin"]

    rows = []
    for i in range(1, 31):
        rows.append({
            "isbn": f"978-{10000+i}",
            "name": f"Book_B_{i}",
            "writer": random.choice(writers),
            "category": random.choice(categories),
            "cost": round(random.uniform(5, 30), 2),
            "avg_score": round(random.uniform(3.0, 5.0), 1),
            "total_reviews": random.randint(10, 500),
            "units_sold": random.randint(100, 2000),
            "store_name": random.choice(["BookHive", "LitWorld"])
        })

    df = pd.DataFrame(rows)
    df.to_csv("data/bookstore_b.csv", index=False)

if __name__ == "__main__":
    create_bookstore_a()
    create_bookstore_b()
    print("Synthetic datasets created in data/")
