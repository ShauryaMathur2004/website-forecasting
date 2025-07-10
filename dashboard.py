import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load data from CSV file
df = pd.read_csv("bagikopi_website_data.csv")

# Convert timestamp column to datetime type
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create a figure with multiple subplots
fig = make_subplots(rows=2, cols=2, subplot_titles=("User Visits by Page", "Daily User Visits", "User Retention by Page", "Hourly User Visits"))

# Add trace for user visits by page
page_visits = df.groupby('page').count()['user_id']
fig1 = go.Bar(x=page_visits.index, y=page_visits.values)
fig.add_trace(fig1, row=1, col=1)

# Add trace for daily user visits
daily_visits = df.groupby(df.timestamp.dt.date).count()['user_id']
fig2 = go.Scatter(x=daily_visits.index, y=daily_visits.values, mode='lines+markers')
fig.add_trace(fig2, row=1, col=2)

# Add trace for user retention by page
page_retention = df.groupby(['page', df.timestamp.dt.date]).nunique()['user_id'].reset_index()
fig3 = go.Scatter(x=page_retention[page_retention['page'] == 'Menu']['timestamp'], y=page_retention[page_retention['page'] == 'Menu']['user_id'], mode='lines+markers', name='Menu')
fig.add_trace(fig3, row=2, col=1)
fig4 = go.Scatter(x=page_retention[page_retention['page'] == 'Outlets']['timestamp'], y=page_retention[page_retention['page'] == 'Outlets']['user_id'], mode='lines+markers', name='Outlets')
fig.add_trace(fig4, row=2, col=1)

# Add trace for hourly user visits
hourly_visits = df.groupby([df.timestamp.dt.hour]).count()['user_id']
fig5 = go.Scatter(x=hourly_visits.index, y=hourly_visits.values, mode='lines+markers')
fig.add_trace(fig5, row=2, col=2)

# Update figure layout
fig.update_layout(title="LADLI FOUNDATION Website User Analysis Dashboard",
                  xaxis_title="Page/Dates/Hour of Day",
                  yaxis_title="Number of User Visits",
                  height=700,
                  width=1000)

# Display the dashboard
fig.show()


