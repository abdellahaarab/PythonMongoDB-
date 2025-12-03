# 🚀 Connect Python and MongoDB — Professional Guide

## 📌 Introduction

This documentation provides a clean and professional overview of how to connect **Python** and **MongoDB**, including:

* PyMongo (direct driver)
* MongoEngine (ORM for MongoDB)
* Example code
* GeoJSON sample

---

## 🐍 About Python

Python, one of the most popular languages for **data science**, AI, automation, and backend development, integrates naturally with MongoDB to build powerful and scalable applications.

<div align="center">
  <img src="asset/python.png" alt="Python MongoDB" width="220">
</div>

---

## 🍃 About MongoDB

MongoDB is a **NoSQL**, document-oriented, schema-less database using a flexible **JSON-like format**.

Here is a visual comparison between inserting a medicine record in SQL vs MongoDB:

<div align="center">
  <img src="asset/img.jpg" alt="SQL vs MongoDB" width="450">
</div>

---

## 🔌 Connect Python and MongoDB Using PyMongo

### 📦 Installation

```bash
pip install pymongo
```

### 🧩 Why PyMongo?

* Simple and powerful driver to communicate with MongoDB
* Supports JSON-like documents
* Allows dictionary-style data access
* Fast and flexible

### ✔ Example Connection

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["db_name"]

# Example insert
db.users.insert_one({"name": "John", "age": 30})
```

---

## 🏗 Connect Django and MongoDB Using MongoEngine

`MongoEngine` is an ORM layer on top of PyMongo.

### 📦 Installation

```bash
pip install mongoengine
```

### 🛠 Django Integration

In `settings.py`, remove or comment the default `DATABASES` section, then:

```python
import mongoengine

mongoengine.connect(
    db="db_name",
    host="hostname",
    username="username",
    password="mypassword"
)
```

### 🎯 Why Use MongoEngine?

* Provides familiar ORM-style models
* Supports fields like `ListField`, `DictField`
* Schema is enforced at application level (MongoDB stays schemaless)
* Very useful for working with unstructured or large JSON data

---

## 🌍 GeoJSON Example

MongoDB natively supports **GeoJSON** objects for geospatial queries.

```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": { "ID": 0 },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-90, 35],
            [-90, 30],
            [-85, 30],
            [-85, 35],
            [-90, 35]
          ]
        ]
      }
    }
  ]
}
```

---

## ✅ Conclusion

You now have:

✔ A clean explanation of Python and MongoDB
✔ PyMongo connection example
✔ Django + MongoEngine integration
✔ GeoJSON sample for geospatial operations

---