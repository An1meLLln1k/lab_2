import pandas as pd
import json
import msgpack
import pickle
import os

books_df = pd.read_csv("data/Books.csv", low_memory=False)

print("Колонки в наборе данных:", books_df.columns)

selected_fields = ["Book-Title", "Book-Author", "Year-Of-Publication", "Publisher"]
filtered_books_df = books_df[selected_fields].copy()

filtered_books_df["Year-Of-Publication"] = pd.to_numeric(filtered_books_df["Year-Of-Publication"], errors='coerce')

filtered_books_df.to_csv("filtered_books.csv", index=False)

stats = {}
numeric_fields = ["Year-Of-Publication"]

for field in numeric_fields:
    stats[field] = {
        "max": filtered_books_df[field].max(),
        "min": filtered_books_df[field].min(),
        "mean": filtered_books_df[field].mean(),
        "sum": filtered_books_df[field].sum(),
        "std": filtered_books_df[field].std(),
    }

categorical_fields = ["Book-Title", "Book-Author", "Publisher"]
for field in categorical_fields:
    stats[field] = filtered_books_df[field].value_counts().to_dict()

with open("books_statistics.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=4)

filtered_books_df.to_csv("fifth_task.csv", index=False)

with open("fifth_task.json", "w", encoding="utf-8") as f:
    json.dump(filtered_books_df.to_dict(orient='records'), f, ensure_ascii=False, indent=4)

with open("fifth_task.msgpack", "wb") as f:
    msgpack.dump(filtered_books_df.to_dict(orient='records'), f)

with open("fifth_task.pkl", "wb") as f:
    pickle.dump(filtered_books_df, f)

csv_size = os.path.getsize("fifth_task.csv")
json_size = os.path.getsize("fifth_task.json")
msgpack_size = os.path.getsize("fifth_task.msgpack")
pickle_size = os.path.getsize("fifth_task.pkl")

print(f"Размер CSV файла: {csv_size} байт")
print(f"Размер JSON файла: {json_size} байт")
print(f"Размер MsgPack файла: {msgpack_size} байт")
print(f"Размер Pickle файла: {pickle_size} байт")
