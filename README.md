# 🌍 Global Price Comparison Tool

A smart tool that fetches the **lowest prices** for any product from **multiple websites** across the world based on the **country** and **product query** you provide.

Powered by **Groq LLM (Mixtral)** to ensure **accurate product matching**, even when websites list similar or unrelated products.

---

##  Features

-  Works for **any country** and **any product**
-  Searches websites like Amazon, Flipkart, Croma, Reliance Digital, Apple, etc.
-  Uses **LLM (Groq)** to filter only exact product matches
-  Results are **ranked by lowest price**
-  Google Search + custom scraping for coverage
- ⚙ Fully **Dockerized**
-  Optional: Use with **Streamlit frontend** or **curl**

---

## 
Input Format

Provide a JSON input like:

```json
{
  "country": "US",
  "query": "iPhone 16 Pro, 128GB"
}
