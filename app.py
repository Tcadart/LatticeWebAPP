import streamlit as st
from Lattice.src.Lattice import Lattice
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

# Titre de l'application
st.title("Générateur de Lattice")

# Créer deux colonnes
col1, col2 = st.columns(2)

# Dans la première colonne, placez les contrôles de saisie
with col1:
    st.header("Paramètres")

    # Création des widgets pour les paramètres
    Radius = st.number_input("Radius", value=0.08)
    cell_size = st.number_input("Taille de la cellule", min_value=0.01, value=1.0)
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
    GradDimRule = st.selectbox("Règle de gradient sur les dimensions de la cellule", options=["constant", "linear", "parabolic", "sinusoide", "exponential"], index=0)
    GradDimDirection = st.text_input("Direction du gradient sur les dimensions de la cellule", value="[1, 0, 1]")
    GradDimParameters = st.text_input("Paramètres du gradient sur les dimensions de la cellule", value="[1.5, 0.0, 1.5]")
    GradRadRule = st.selectbox("Règle de gradient sur le rayon des poutres", options=["constant", "linear", "parabolic", "sinusoide", "exponential"], index=0)
    GradRadDirection = st.text_input("Direction du gradient sur le rayon des poutres", value="[0, 0, 1]")
    GradRadParameters = st.text_input("Paramètres du gradient sur le rayon des poutres", value="[1.0, 0.0, 2.0]")
    Multimat = st.selectbox("Multimat", options=["-1: Complètement aléatoire", "0: Matériaux", "1: Multimat par couche"], index=0)
    GradMaterialDirection = st.selectbox("Direction du gradient sur les matériaux", options=["1:X", "2:Y", "3:Z"], index=2)
    MethodSim = st.selectbox("Méthode de simulation", options=["0: Pas de modification", "1: Modification des noeuds"], index=1)
    uncertaintyNode = st.number_input("Noeud d'incertitude", value=0)

    gradDimProperty = [GradDimRule, GradDimDirection, GradDimParameters]
    gradRadiusProperty = [GradRadRule, GradRadDirection, GradRadParameters]
    gradMatProperty = [int(Multimat.split(":")[0]), int(GradMaterialDirection.split(":")[0])]

    # Conversion du type de lattice en entier
    Lattice_Type = int(Lattice_Type.split(":")[0])
    MethodSim = int(MethodSim.split(":")[0])

    # Bouton pour générer la lattice
    generate = st.button("Générer la Lattice")

# Dans la deuxième colonne, affichez le graphique
with col2:
    st.header("Visualisation")

    if generate:
        # Création de l'instance de Lattice avec les paramètres
        lattice = Lattice(cell_size, cell_size, cell_size, number_cell_X, number_cell_Y, number_cell_Z,
                          Lattice_Type,
                          Radius, gradRadiusProperty, gradDimProperty, gradMatProperty, MethodSim, uncertaintyNode,
                          hybridGeomType=[0, 16, 17], periodicity=True,
                          randomHybrid=True)

        # Génération de la visualisation
        fig = lattice.visualizeLattice3D_interactive("Type", deformedForm=True, plotCellIndex=False)

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Veuillez cliquer sur le bouton pour générer la lattice.")
