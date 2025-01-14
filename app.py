import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Connexion à PostgreSQL
engine = create_engine("postgresql://user:password@postgres_db:5432/testdb")

# Charger les données
clients = pd.read_sql("SELECT * FROM clients", engine)
produits = pd.read_sql("SELECT * FROM produits", engine)
ventes = pd.read_sql("SELECT * FROM ventes", engine)

# Afficher les données dans Streamlit
st.title("Visualisation des données")
st.write("Clients")
st.dataframe(clients)
st.write("Produits")
st.dataframe(produits)
st.write("Ventes")
st.dataframe(ventes)
