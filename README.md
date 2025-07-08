# 🌍 Global Price Comparison Tool

This tool helps users find the **lowest prices** for any product from multiple websites based on the **country** they are shopping from.

It supports **any country** and **any product** (like phones, earphones, laptops, etc.), and uses **AI (Groq LLM)** to make sure the product matched is accurate.

---

##  Features

- Search products from websites like Amazon, Flipkart, Reliance Digital, Apple, etc.
- Works for all countries and categories
- Results sorted by **lowest price**
- Uses **Groq LLM** to filter correct product match
- Works with **Streamlit frontend** or with **curl (API only)**

---

##  Sample Input

```json
{
  "country": "US",
  "query": "iPhone 16 Pro, 128GB"
}

## Output

[
  {
    "link": "https://www.apple.com/us/iphone-16-pro",
    "price": "999",
    "currency": "USD",
    "productName": "Apple iPhone 16 Pro (128GB)",
    "site": "Apple US"
  },
  {
    "link": "https://www.amazon.com/iphone-16-pro-128gb-black",
    "price": "1029",
    "currency": "USD",
    "productName": "iPhone 16 Pro - 128GB - Black",
    "site": "Amazon"
  }
]
