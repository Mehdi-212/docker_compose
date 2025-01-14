import pandas as pd
from sqlalchemy import create_engine

# Connexion à la base PostgreSQL
engine = create_engine("postgresql://user:password@postgres_db:5432/testdb")

# Charger les données CSV
clients = pd.read_csv("data/clients.csv", delimiter=";")
produits = pd.read_csv("data/produits_sous_categorie.csv", delimiter=";")
ventes = pd.read_csv("data/ventes.csv", delimiter=";")

# Insérer les données dans PostgreSQL
clients.to_sql("clients", engine, if_exists="replace", index=False)
produits.to_sql("produits", engine, if_exists="replace", index=False)
ventes.to_sql("ventes", engine, if_exists="replace", index=False)

print("ETL terminé : données insérées dans PostgreSQL.")
