#importing libraries
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.metrics.pairwise import cosine_similarity
#converting excel files to csv
df1=pd.read_excel('./Restaurant1_Jan_2025.xlsx')
df2=pd.read_excel('./Restaurant2_Jan_2025.xlsx')
df=pd.concat([df1,df2])
df.to_csv('Restaurant_Jan_2025.csv',index=False)
# print(df['Product'].unique())

#normalizing product names (remove extra descriptions, quantities, etc.)
df['Product'] = df['Product'].str.lower().str.strip().str.replace(r"\(.*?\)", "", regex=True)


#removing all the unnecessary columns
new_df=df[['Order No','Product']]

#grouping the data
basket_data = new_df.groupby("Order No")["Product"].apply(list).reset_index()
# print(basket_data.head())

#one hot encoding
te = TransactionEncoder()
te_ary = te.fit(basket_data["Product"]).transform(basket_data["Product"])
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

#apply Apriori to find frequent itemsets with minimum support threshold
frequent_itemsets = apriori(df_encoded, min_support=0.005, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
filtered_rules = rules[rules['antecedents'].apply(lambda x: len(x) == 1)]

#cosine similarity
item_similarity = cosine_similarity(df_encoded.T)
item_sim_df = pd.DataFrame(item_similarity, index=df_encoded.columns, columns=df_encoded.columns)

#hybrid model
def recommend_items(selected_item):
    selected_item = selected_item.lower().strip()

    # Association Rules Suggestion (Proper Formatting)
    matching_rules = filtered_rules[filtered_rules['antecedents'].apply(lambda x: selected_item in list(x))]

    if not matching_rules.empty:
        assoc_recommendations = [
            f"Customers who order {', '.join(list(row['antecedents']))} also tend to order {', '.join(list(row['consequents']))} with a confidence of {row['confidence']:.0%}."
            for _, row in matching_rules.iterrows()
        ]
    else:
        assoc_recommendations = ["No strong association found."]

    # Collaborative Filtering Suggestion
    if selected_item in item_sim_df.index:
        collab_recommendations = item_sim_df[selected_item].sort_values(ascending=False).iloc[1:6].index.tolist()
    else:
        collab_recommendations = []

    return {
        "Market Basket Recommendations": assoc_recommendations,
        "Collaborative Filtering Recommendations": collab_recommendations
    }

# Testing the model
selected_item = "paneer butter masala"
recommendations = recommend_items(selected_item)

print("Selected Item:", selected_item)
print("Market Basket Recommendations:", recommendations["Market Basket Recommendations"])
print("Collaborative Filtering Recommendations:", recommendations["Collaborative Filtering Recommendations"])

