import streamlit as st
from src.Lattice import Lattice
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Générateur de Lattice")

# Création des widgets pour les paramètres
Radius = st.number_input("Radius", value=0.08)
cell_size = st.number_input("Taille de la cellule", value=1.0)
number_cell_X = st.number_input("Nombre de cellules en X", min_value=1, value=3, step=1)
number_cell_Y = st.number_input("Nombre de cellules en Y", min_value=1, value=3, step=1)
number_cell_Z = st.number_input("Nombre de cellules en Z", min_value=1, value=3, step=1)
Lattice_Type = st.selectbox("Type de Lattice", options=[
    "-2: Méthode cellule aléatoire",
    "-1: Complètement aléatoire",
    "0: BCC",
    "1: Octet",
    "2: OctetExt",
    "3: OctetInt",
    "4: BCCZ",
    "5: Cubic",
    "6: OctahedronZ",
    "7: OctahedronZcross",
    "8: Kelvin",
    "9: Cubic formulation 2 (centrée)",
    "10: Cubic V3",
    "11: Cubic V4",
    "12: Nouvelle lattice (inconnue) générée par GPT",
    "13: Diamond",
    "14: Auxetic"
], index=2)

# Conversion du type de lattice en entier
Lattice_Type_value = int(Lattice_Type.split(":")[0])

# Bouton pour générer la lattice
if st.button("Générer la Lattice"):
    # Création de l'instance de Lattice avec les paramètres
    lattice = Lattice(
        cell_size, cell_size, cell_size,
        int(number_cell_X), int(number_cell_Y), int(number_cell_Z),
        Lattice_Type_value, Radius,
        # Ajoutez ici les autres paramètres nécessaires ou utilisez des valeurs par défaut
        gradRadiusProperty=['constant', [0, 0, 0], [1.0, 0.0, 1.0]],
        gradDimProperty=['constant', [0, 0, 0], [1.0, 0.0, 1.0]],
        gradMatProperty=[0, 1],
        MethodSim=1,
        uncertaintyNode=0,
        hybridLatticeData=[Radius, 0, 0],
        hybridGeomType=[0, 16, 17],
        periodicity=True,
        randomHybrid=True
    )

    # Génération de la visualisation
    lattice.visualizeLattice3D("Type", deformedForm=True, plotCellIndex=False)

    # Récupération de la figure actuelle
    fig = plt.gcf()

    # Affichage de la figure dans Streamlit
    st.pyplot(fig)
