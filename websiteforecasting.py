import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
data = pd.read_csv("Website.csv")
print(data.head())


data["Date"] = pd.to_datetime(data["Date"], 
                              format="%m/%d/%Y")
print(data.info())


plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
plt.plot(data["Date"], data["Views"])
plt.title("Daily Traffic of WebSite.com")
plt.show()


from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(data["Views"], model='multiplicative',extrapolate_trend='freq', period=30)
fig = plt.figure()  
fig = result.plot()  
fig.set_size_inches(15, 10)


pd.plotting.autocorrelation_plot(data["Views"])


plot_pacf(data["Views"], lags = 100)



p, d, q = 5, 1, 2
model=sm.tsa.statespace.SARIMAX(data['Views'],
                                order=(p, d, q),
                                seasonal_order=(p, d, q, 12))
model=model.fit()
print(model.summary())


predictions=model.predict(len(data),len(data)+50)
print(predictions)


data["Views"].plot(legend=True, label="Training Data", 
                   figsize=(15, 10))
predictions.plot(legend=True, label="Predictions")


