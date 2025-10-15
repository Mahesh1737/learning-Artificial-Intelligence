import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

dataset = [
    ['milk', 'bread', 'butter'],
    ['beer', 'bread'],
    ['milk', 'bread', 'butter', 'beer'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'bread', 'butter'],
]

# step 1 convert dataset into a one-hot encoded daataframe

from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_array = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)

print("One hot encoded Dataframe : \n")
print(df)

# step 2 apply the apriori algorithm
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
print("\nFrequent Intemsets: ")
print(frequent_itemsets)

# Step 3 generate the association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print("\nAssociation rules : ")
print(rules[['antecedents', 'consequents', 'support', 'confidense', 'lift']])


import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt

lam = 0.2
x = 3

prob = expon.cdf(x, scale=1/lam)
print("Probability waiting <= 3 minutes : ", prob)

data = np.random.exponential(scale=1/lam, size=1000)

plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', label="Simulate Data")

x_vals = np.linspace(0, 20, 100)
pdf_vals = lam * np.exp(-lam * x_vals)
plt.plot(x_vals, pdf_vals, 'r-', lw=2, label="Theoratical pdf")

plt.xlabel("Waiting time (minutes)")
plt.ylabel("Density")
plt.title("Exponential distribution (0.2)")
plt.legend()
plt.show()



from scipy.stats import bernoulli

p = 0.7

print("(X=1) : ", bernoulli.pmf(1,p))
print("(X=0) : ", bernoulli.pmf(0,p))

data = bernoulli.rvs(p, size=1000)

# plot histogram

plt.bar([0,1], [sum(data==0)/1000, sum(data==1)/1000],
        color=['lightcoral', 'lightgreen'],
        tick_label = ["0 (tails)", "1 (Heads)"]
    )

plt.title("Bernoulli Distribution (p = 0.7)")

plt.ylabel("probability")

plt.show()