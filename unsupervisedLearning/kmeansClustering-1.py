import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

stores = ["Avenue Jewelers", "Avenue Restaurant", "Barney's Castle", \
          "City Appliances", "Clancy's Clothiers","Friendly Fast Food", \
          "Hardware Corner", "Musical Planet", "Randolph's","Sports and More"]
categories = ["Jewelry Store", "Family Restaurant", "Arcade Games", \
              "Home Appliances", "Clothing", "Fast Food Restaurant", \
              "Hardware and Tools", "Music and Movies", "Books, Games and Gifts", "Sports Equipment"]
traffic = [101, 273, 108, 97, 76, 203, 306, 121, 83, 192]
sales = [60.2, 73.4, 12.7, 98.1, 18.7, 16.1, 30.9, 17.3, 19.4, 22.0]
proximity = [3, 2, 4, 1, 1, 2, 1, 8, 10, 6]
chain = ["No", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes"]
anchor = ["No", "No", "No", "Yes", "Yes", "No", "Yes", "No", "No", "No"]
zones = [7, 6, 8, 4, 5, 9, 3, 10, 2, 1]
places = []
scores = [0] * 10


# create a dataframe to include all factors that may have impact on the decision of store locations
data = {'Store Name': stores, 'Category': categories, \
        'Daily Traffic': traffic, 'Monthly Sales': sales, \
        'Proximity to Anchor Store': proximity, 'Chain Store': chain, 'Anchor Store': anchor}
df = pd.DataFrame(data)
print(df)
print("")

# apply K-means clustering to divide stores into 3 differenct groups: high-traffic-sale, medium-traffic-sale, low-traffic-sale
X = np.array(list(zip(df['Monthly Sales'], df["Daily Traffic"])))
k = 3
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)

# score calculator that consider the impact of traffic-sale, chain store and proximity to anchor store:
def overall_score(store_index, store_clusters) :
  score = 0
  proximity_anchor = proximity[store_index]
  if_chain = chain[store_index]
  weights = {
        "traffic_and_sales": 0.5,
        "proximity_anchor": 0.3,
        "if_chain": 0.2
  }
  # higher score if the store near anchor stores
  score += weights["proximity_anchor"] * (1 / proximity_anchor)
  # higher score if it is a chain store
  if (if_chain == 'Yes') :
    score += weights['if_chain']
  # score based on the traffic and sales
  score += store_clusters[store_index] * weights['traffic_and_sales']
  return score

scores = [overall_score(i, labels) for i in range(len(stores))]

count = 10
while (count > 0) :
  max_index = scores.index(max(scores))
  places += [stores[max_index], zones[10 - count]]
  stores.remove(stores[max_index])
  scores.remove(scores[max_index])
  count -= 1

print(places)

