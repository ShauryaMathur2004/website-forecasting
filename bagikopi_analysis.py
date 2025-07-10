import pandas as pd
import matplotlib.pyplot as plt

#Load the website data into a pandas DataFrame:
df = pd.read_csv('bagikopi_website_data.csv')


#Calculate the number of unique users who visited each page:
unique_users = df.groupby('page')['user_id'].nunique()


#Calculate the retention rate for each page:
retention_rate = df.groupby('page')['user_id'].apply(lambda x: x.nunique() / x.count())


#Visualize the results using a bar chart and line plot:
fig, ax1 = plt.subplots()
ax1.bar(unique_users.index, unique_users.values)
ax1.set_ylabel('Unique Users')
ax2 = ax1.twinx()
ax2.plot(retention_rate.index, retention_rate.values, color='r')
ax2.set_ylabel('Retention Rate')
plt.title('User Views and Retention on ladlifoundationtrust.org')
plt.show()


#Save the figure to a file:
fig.savefig('user_views_and_retention.png')




