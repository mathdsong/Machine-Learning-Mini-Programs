import pandas as pd
import numpy as np
from timeit import default_timer as timer

pd.set_option('display.max_colwidth', None)

mydata = {
  'INTERVIEW QUESTIONS': ["What is Overfitting?",
                          "How Do You Handle Missing or Corrupted Data in a Dataset?",
                          "How Can You Choose a Classifier Based on a Training Set Data Size?",
                          "Explain the Confusion Matrix with Respect to Machine Learning Algorithms.",
                          "What Is a False Positive and False Negative and How Are They Significant?",
                          "What Are the Three Stages of Building a Model in Machine Learning?",
                          "What Are the Differences Between Machine Learning and Deep Learning?",
                          "What is the Difference Between Supervised and Unsupervised Machine Learning?",
                          "Compare K-means and KNN Algorithms.",
                          "What is a Random Forest?"],
  'RESPONSE DURATION': [0.0] * 10
}

df = pd.DataFrame(mydata)
df.index = np.arange(1, len(df) + 1)
print('******************************** ORIGINAL DATAFRAME ********************************')
print(df)

avg_response_duration = 0

for i in range(len(mydata['INTERVIEW QUESTIONS'])):
  start = timer()
  print(mydata['INTERVIEW QUESTIONS'][i])
  yourInput = input()
  end = timer()
  duration = end - start
  avg_response_duration += duration
  print ("response time for question #{} is: {} seconds".format(i+1, duration))
  df.loc[i + 1, ['RESPONSE DURATION']] = duration


print('******************************** UPDATED DATAFRAME ********************************')
print(df)

print('******************************** STATISTICS ********************************')
# Generate Statistics:
avg_response_duration /= len(mydata['INTERVIEW QUESTIONS'])
duration_series = df['RESPONSE DURATION']
std = duration_series.std()
print('average response duration: ', avg_response_duration)
print('standard deviation of the responsing duration is: ', std)


"""
1. https://www.guru99.com/timeit-python-examples.html
2. https://www.geeksforgeeks.org/timeit-python-examples/
3. https://stackoverflow.com/questions/63757763/timeit-and-its-default-timer-completely-disagree
4. https://www.simplilearn.com/tutorials/machine-learning-tutorial/machine-learning-interview-questions
5. https://stackoverflow.com/questions/32249960/start-row-index-from-1-instead-of-zero-without-creating-additional-column-in-pan
6. https://stackoverflow.com/questions/68490745/how-to-display-the-full-text-of-a-column-in-pandas
7. https://stackoverflow.com/questions/37725195/pandas-replace-values-based-on-index
"""