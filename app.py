import streamlit as st
from Lattice.src.Lattice import Lattice


st.set_page_config(layout="wide")

# Titre de l'application
st.title("Lattice Generator")

# Créer deux colonnes
col1, col2 = st.columns(2)

# Dans la première colonne, placez les contrôles de saisie
with (col1):
    st.header("Parameters")
    # Bouton pour générer la lattice
    col1Option, col2Option = st.columns(2)
    with col1Option:
        generate = st.button("Generate lattice")
    with col2Option:
        generateAutomatic = st.checkbox("Generate lattice automatically")
    # Création des widgets pour les paramètres
    Radius = st.number_input("Radius", value=0.01)
    col1CellSize, col2CellSize, col3CellSize = st.columns(3)
    with col1CellSize:
        cell_size_X = st.number_input("Cell size on the X-axis", min_value=0.01, value=1.0)
    with col2CellSize:
        cell_size_Y = st.number_input("Cell size on the Y-axis", min_value=0.01, value=1.0)
    with col3CellSize:
        cell_size_Z = st.number_input("Cell size on the Z-axis", min_value=0.01, value=1.0)

    col1numberCell, col2numberCell, col3numberCell = st.columns(3)
    with col1numberCell:
        number_cell_X = int(st.number_input("Cell number on the X-axis", min_value=1, value=3, step=1))
    with col2numberCell:
        number_cell_Y = int(st.number_input("Cell number on the Y-axis", min_value=1, value=3, step=1))
    with col3numberCell:
        number_cell_Z = int(st.number_input("Cell number on the Z-axis", min_value=1, value=3, step=1))

    lattice_options = [
        "BCC",
        "Octet",
        "OctetExt",
        "OctetInt",
        "BCCZ",
        "Cubic",
        "OctahedronZ",
        "OctahedronZcross",
        "Kelvin",
        "Cubic center",
        "Cubic V3",
        "Cubic V4",
        "No named lattice",
        "Diamond",
        "Auxetic",
        "Méthode cellule aléatoire",
        "Hybrid"
    ]
    Lattice_Type = st.selectbox("Type de Lattice", options=lattice_options, index=0)
    Lattice_Type = lattice_options.index(Lattice_Type)
    if Lattice_Type == 15:
        Lattice_Type = -2
    elif Lattice_Type == 16:
        Lattice_Type = 1000
        with st.container(border=True):
            hybridLatticeData = [0,0,0]
            latticeGeom = [0, 16, 17]
            col = st.columns(3)
            for idx, colI in enumerate(col):
                with colI:
                    hybridLatticeData[idx] = st.number_input(f"Hybrid lattice data {idx}", value=0.0)
    else:
        hybridLatticeData = [0, 0, 0]


    col1Grad, col2Grad, col3Grad = st.columns(3)
    with col1Grad:
        GradDimRuleActivated = st.checkbox("Graded dimensions", value=False)
        if GradDimRuleActivated:
            with st.container(border=True):
                GradDimRule = st.selectbox("Rule", options=["constant", "linear", "parabolic", "sinusoide", "exponential"], index=0)
                optionX = st.checkbox("X-axis", value=False)
                if optionX:
                    GradDimParametersX = st.number_input("Parameters X", value=0.0)
                else:
                    GradDimParametersX = 0.0
                optionY = st.checkbox("Y-axis", value=False)
                if optionY:
                    GradDimParametersY = st.number_input("Parameters Y", value=0.0)
                else:
                    GradDimParametersY = 0.0
                optionZ = st.checkbox("Z-axis", value=False)
                if optionZ:
                    GradDimParametersZ = st.number_input("Parameters Z", value=0.0)
                else:
                    GradDimParametersZ = 0.0
                GradDimDirection = [int(optionX), int(optionY), int(optionZ)]
        else:
            GradDimRule = "constant"
            GradDimDirection = "[0, 0, 0]"
            GradDimParameters = "[0.0, 0.0, 0.0]"
    with col2Grad:
        GradRadRuleActivated = st.checkbox("Graded radius", value=False)
        if GradRadRuleActivated:
            with st.container(border=True):
                GradRadRule = st.selectbox("Rule", options=["constant", "linear", "parabolic", "sinusoide", "exponential"], index=0)
                optionX = st.checkbox("X-axis", value=False)
                if optionX:
                    GradRadParametersX = st.number_input("Parameters X", value=0.0)
                else:
                    GradRadParametersX = 0.0
                optionY = st.checkbox("Y-axis", value=False)
                if optionY:
                    GradRadParametersY = st.number_input("Parameters Y", value=0.0)
                else:
                    GradRadParametersY = 0.0
                optionZ = st.checkbox("Z-axis", value=False)
                if optionZ:
                    GradRadParametersZ = st.number_input("Parameters Z", value=0.0)
                else:
                    GradRadParametersZ = 0.0
                GradRadDirection = [int(optionX), int(optionY), int(optionZ)]
        else:
            GradRadRule = "constant"
            GradRadDirection = "[0, 0, 0]"
            GradRadParameters = "[0.0, 0.0, 0.0]"
    with col3Grad:
        Multimat = st.checkbox("Material Gradient", value=False)
        if Multimat:
            with st.container(border=True):
                matGradOption = ["Full random", "Layer by layer"]
                Multimat = st.selectbox("Rule", options=matGradOption, index=1)
                Multimat = matGradOption.index(Multimat)
                if Multimat == 0:
                    Multimat = -1
                matGradOptionDirection = ["X", "Y", "Z"]
                GradMaterialDirection = st.selectbox("Axis", options=matGradOptionDirection, index=0)
                GradMaterialDirection = matGradOptionDirection.index(GradMaterialDirection) + 1
        else:
            Multimat = 0
            GradMaterialDirection = 1

    MethodSim = st.checkbox("Simulation method (Node penalization)", value=0)
    st.write("More information on article : An optimal penalty method for the joint stiffening in beam models of "
             "additively manufactured lattice structures")

    uncertaintyNode = st.checkbox("Node incertainty", value=0)

    gradDimProperty = [GradDimRule, GradDimDirection, GradDimParameters]
    gradRadiusProperty = [GradRadRule, GradRadDirection, GradRadParameters]
    gradMatProperty = [Multimat, GradMaterialDirection]

with col2:
    st.header("Vizualisation")

    # Initialiser les variables avant leur utilisation
    st.subheader("Parameters for vizualisation")
    col1Viz, col2Viz, col3Viz = st.columns(3)
    with col1Viz:
        beamColor = st.selectbox("Color type", options=["Material", "Type"], index=0)
    with col2Viz:
        plotCellIndexOption = st.checkbox("Plot cell index", value=False)
    with col3Viz:
        voxelVizOption = st.checkbox("Voxel view", value=False)

    if generate or generateAutomatic:
        # Création de l'instance de Lattice avec les paramètres
        lattice = Lattice(cell_size_X, cell_size_Y, cell_size_Z, number_cell_X, number_cell_Y, number_cell_Z,
                          Lattice_Type,
                          Radius, gradRadiusProperty, gradDimProperty, gradMatProperty, MethodSim, uncertaintyNode,
                          hybridLatticeData=hybridLatticeData, hybridGeomType=[0, 16, 17])

        # Génération de la visualisation
        fig = lattice.visualizeLattice3D_interactive(beamColor=beamColor, voxelViz=voxelVizOption,
                                                     plotCellIndex=plotCellIndexOption)

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Click on the button to generate the lattice")


