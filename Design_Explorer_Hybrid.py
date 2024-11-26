import streamlit as st
from Lattice.src.Lattice import Lattice


def Design_Explorer_Hybrid():
    st.title("Design Explorer Lattice Hybrid")

    rad1 = st.slider("hybrid radius 1", min_value=0.0, max_value=0.1, value=0.05, step=0.001)
    rad2 = st.slider("hybrid radius 2", min_value=0.0, max_value=0.1, value=0.05, step=0.001)
    rad3 = st.slider("hybrid radius 3", min_value=0.0, max_value=0.1, value=0.05, step=0.001)

    hybridLatticeData = [rad1, rad2, rad3]

    if rad1 + rad2 + rad3 == 0.0:
        st.error("Please select at least one radius")
        return
    else:
        lattice = Lattice.hybridgeometry(1, 1, 1, 0, 0, hybridLatticeData)

        fig = lattice.visualizeLattice3D_interactive(beamColor="Material", voxelViz=False,
                                                     plotCellIndex=False)

        st.plotly_chart(fig, use_container_width=True)