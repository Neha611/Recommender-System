# Hybrid Recommendation System for Restaurant Orders

## Overview

This project implements a hybrid recommendation system that utilizes both market basket analysis (association rules) and collaborative filtering (cosine similarity) to suggest related products based on 
restaurant orders.

## Features

**Data Preprocessing**: Cleans and normalizes product names from restaurant order data.

**Market Basket Analysis**: Uses the Apriori algorithm to find frequent itemsets and generate association rules.

**Collaborative Filtering**: Computes cosine similarity between products for recommendations.

**Hybrid Recommendation**: Combines both techniques to generate product suggestions.

## Installation

**Prerequisites**

Ensure you have Python installed along with the required libraries:
```
pip install pandas mlxtend scikit-learn openpyxl
```

## Dataset

The system processes restaurant order data from multiple sources.

The data is read from Excel files and converted to CSV for easier manipulation.

Product names are cleaned by removing unnecessary descriptions and formatting inconsistencies.

Data is grouped by order numbers to create a transaction dataset.

## Methodology

1. **Preprocessing**

Reads order data from multiple Excel files and merges them.

Normalizes product names by removing extra descriptions and spaces.

Groups data by order numbers to create transaction baskets.

2. **Market Basket Analysis**

Converts transactions into a one-hot encoded format using TransactionEncoder.

Applies the Apriori algorithm to find frequent itemsets with a minimum support threshold.

Extracts association rules based on confidence scores.

3. **Collaborative Filtering**

Computes item-item similarity using cosine similarity on the one-hot encoded data.

Generates recommendations based on similarity scores.

4. **Hybrid Recommendation**

Uses association rules to suggest items frequently bought together.

Uses collaborative filtering to recommend similar products based on past orders.

Merges both approaches to provide comprehensive recommendations.

## Usage

Run the script and provide a selected item to get recommendations:
```
selected_item = "paneer butter masala"
recommendations = recommend_items(selected_item)
print("Market Basket Recommendations:", recommendations["Market Basket Recommendations"])
print("Collaborative Filtering Recommendations:", recommendations["Collaborative Filtering Recommendations"])
```

## Example Output
```
Selected Item: paneer butter masala
Market Basket Recommendations: ["Customers who order paneer butter masala also tend to order naan with a confidence of 75%."]
Collaborative Filtering Recommendations: ['butter naan', 'dal makhani', 'jeera rice', 'shahi paneer', 'tandoori roti']
```

## Future Improvements

Enhance data preprocessing to include additional text normalization techniques.

Optimize hyperparameters for better association rule mining.

Experiment with other similarity metrics for collaborative filtering.

Integrate with a real-time recommendation system for a restaurant POS.

## Author

Developed by Neha
