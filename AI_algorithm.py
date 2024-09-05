import pandas as pd
from surprise import Reader, Dataset, SVD

# Load data
ratings = pd.read_csv("ratings.csv")

# Create a Surprise Dataset
reader = Reader()
data = Dataset.load_from_df(ratings[['user_id', 'item_id', 'rating']], reader)

# Train a SVD model
algo = SVD()
trainset = data.build_full_trainset()
algo.fit(trainset)

# Get recommendations for a specific user
user_id = 123  # Replace with the actual user ID
recommendations = algo.get_recommendations(user_id)

# Provide personalized information based on the recommendations
for item_id, rating in recommendations:
    product_info = get_product_info(item_id)  # Function to retrieve product details
    print(f"Recommended product: {product_info['name']}")
    print(f"Description: {product_info['description']}")
    # ... provide more personalized information