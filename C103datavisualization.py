import pandas as pd
import plotly.express as px

df1 = pd.read_csv("CovidData.csv")
fig1 = px.scatter(df1, x = "date", y = "cases", color = "country", title = 'Covid cases')
fig1.show()


