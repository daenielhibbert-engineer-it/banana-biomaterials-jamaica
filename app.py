
import streamlit as st

# Set up the page
st.set_page_config(
    page_title="BananaLoop",
    page_icon="🍌",
    layout="wide"
)

# Main heading
st.title("🍌 BananaLoop")
st.subheader("Plant-Based Packaging Design Studio")

st.write(
    "Explore formulation choices for starch-based "
    "biocomposite packaging reinforced with plant fibres."
)

st.divider()

# Formulation section
st.header("1. Formulation Explorer")

st.write("Adjust the variables below to explore different designs.")

fibre_content = st.slider(
    "Fibre loading (%)",
    min_value=0,
    max_value=40,
    value=20,
    step=5
)

glycerol = st.slider(
    "Glycerol setting (mL)",
    min_value=1.5,
    max_value=2.5,
    value=2.0,
    step=0.1
)

package_type = st.selectbox(
    "Packaging format",
    ["Film", "Pouch", "Wrapper"]
)

st.divider()

# Display the selected formulation
st.header("2. Your Formulation")

col1, col2, col3 = st.columns(3)

col1.metric("Fibre loading", f"{fibre_content}%")
col2.metric("Glycerol setting", f"{glycerol:.1f} mL")
col3.metric("Packaging format", package_type)

st.info(
    f"You selected a {package_type.lower()} with "
    f"{fibre_content}% fibre loading and "
    f"{glycerol:.1f} mL glycerol."
)

st.caption(
    "BananaLoop | Student Computational Research Project"
)

st.warning(
    "This is an illustrative formulation explorer. "
    "The selected values do not predict actual material "
    "properties or represent a validated manufacturing recipe."
)

