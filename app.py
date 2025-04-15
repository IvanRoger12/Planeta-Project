
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv("enquete_diplomes_planeta.csv")

st.title("🎓 Analyse Enquête Diplômés – Planeta Formation")
st.markdown("Un aperçu interactif des données d'insertion professionnelle et de satisfaction des diplômés.")

# Filtres
ecoles = st.multiselect("Choisissez une ou plusieurs écoles :", options=df["École"].unique(), default=df["École"].unique())
promos = st.multiselect("Choisissez une ou plusieurs promotions :", options=df["Promo"].unique(), default=df["Promo"].unique())

df_filtered = df[(df["École"].isin(ecoles)) & (df["Promo"].isin(promos))]

# KPIs
col1, col2, col3 = st.columns(3)
with col1:
    taux_insertion = df_filtered["Emploi trouvé"].value_counts(normalize=True).get("Oui", 0) * 100
    st.metric("💼 Taux d'insertion", f"{taux_insertion:.1f}%")
with col2:
    satisfaction_moy = df_filtered["Satisfaction (/5)"].mean()
    st.metric("😊 Satisfaction moyenne", f"{satisfaction_moy:.2f} / 5")
with col3:
    salaire_moy = df_filtered["Salaire (€)"].mean()
    st.metric("💶 Salaire moyen", f"{salaire_moy:,.0f} €")

st.divider()

# Graphiques
st.subheader("📊 Répartition des diplômés par école")
fig1, ax1 = plt.subplots()
df_filtered["École"].value_counts().plot(kind='bar', ax=ax1)
st.pyplot(fig1)

st.subheader("📈 Délai moyen d'insertion par école")
fig2, ax2 = plt.subplots()
df_filtered.groupby("École")["Délai (mois)"].mean().plot(kind='bar', ax=ax2)
st.pyplot(fig2)

st.subheader("📍 Satisfaction par promo")
fig3, ax3 = plt.subplots()
df_filtered.groupby("Promo")["Satisfaction (/5)"].mean().plot(kind='line', marker='o', ax=ax3)
st.pyplot(fig3)

st.markdown("""
> 📝 *Ce tableau de bord pourrait être utilisé pour accompagner les rapports à France Compétences et permettre une prise de décision éclairée sur les cursus proposés.*
""")
