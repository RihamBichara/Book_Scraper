import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. الاتصال بالموقع
url = "http://books.toscrape.com/"
response = requests.get(url)

# 2. تجهيز الشوربة (Parsing)
soup = BeautifulSoup(response.content, "html.parser")
# 3. العثور على جميع حاويات الكتب
books = soup.find_all("article", class_="product_pod")

data_list = []
print(f"جاري سحب بيانات {len(books)} كتاب...")

# 4. الدوران على كل كتاب لاستخراج بياناته
for book in books:
    # استخراج العنوان
    h3_tag = book.find("h3")
    title = h3_tag.find("a")["title"]

    # استخراج السعر
    price_tag = book.find("p", class_="price_color")
    price = price_tag.text

    data_list.append({"Book Title": title, "Price": price})

    df = pd.DataFrame(data_list)
    df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")
print("✅ تم حفظ البيانات في ملف 'books_data.csv' بنجاح!")
print("To try a new git command")