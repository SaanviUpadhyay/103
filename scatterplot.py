import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Date", y="cases",
	          size="Percentage",color="country",
                   size_max=70)
fig.show()
