# Give appropriate code to plot the following categorial data using Seaborn:
# blood type (A, B, AB, O) and frequency of occurrence per blood category (14, 16, 20, 50)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {'Blood Type': ['A', 'B', 'AB', 'O'], 'Frequency': [14, 16, 20, 50]}
df = pd.DataFrame(data)

sns.barplot(x='Blood Type', y='Frequency', data=df)

plt.title('Blood Type Frequency')
plt.show()
