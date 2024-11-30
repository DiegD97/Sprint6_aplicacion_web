# %%
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de tener el archivo en tu directorio
car_data.head()  # Mostrar las primeras filas para confirmar la carga


# Crear un histograma de la columna "odometer"
fig_histogram = px.histogram(car_data, x="odometer", title="Histograma del Odómetro")
fig_histogram.show()

# Crear un gráfico de dispersión entre el odómetro y el precio
fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odómetro vs Precio")
fig_scatter.show()

# %%



