
import streamlit as st

st.set_page_config(
    page_title="BananaLoop Design Studio",
    page_icon="🍌",
    layout="wide"
)

# Colour palette and styling
st.markdown("""
<style>
.stApp {
    background-color: #f4f5ed;
}
h1, h2, h3 {
    color: #254b35;
}
[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 12px;
}
.preview {
    background: #e6eddf;
    border-radius: 18px;
    padding: 35px;
    text-align: center;
    min-height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.package {
    background: #d9c795;
    border: 2px solid #a89564;
    color: #465139;
    width: 190px;
    height: 200px;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    box-shadow: 5px 8px 15px #00000022;
    margin: auto;
}
.small-note {
    color: #687568;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🍌 BananaLoop")
st.write("**BIOCOMPOSITE DESIGN STUDIO**")
st.caption("Exploring plantain pseudostem fibre in starch-based packaging.")

st.divider()

# Main layout
controls, preview = st.columns([1, 1.5], gap="large")

with controls:
    st.subheader("01 / Formulation")

    fibre = st.slider(
        "Fibre loading (%)",
        0, 40, 20, 5
    )

    glycerol = st.slider(
        "Glycerol setting (mL)",
        1.5, 2.5, 2.0, 0.1
    )

    package_type = st.selectbox(
        "Packaging format",
        ["Film", "Pouch", "Wrapper"]
    )

    st.write("### Selected formulation")

    st.metric("Fibre loading", f"{fibre}%")
    st.metric("Glycerol setting", f"{glycerol:.1f} mL")

with preview:
    st.subheader("02 / Design preview")

    # Change the shape depending on packaging type
    if package_type == "Pouch":
        width, height, radius = 150, 210, 15
    elif package_type == "Wrapper":
        width, height, radius = 260, 110, 5
    else:
        width, height, radius = 190, 190, 8

    st.markdown(f"""
    <div class="preview">
        <div class="package"
        style="width:{width}px;
        height:{height}px;
        border-radius:{radius}px;">
            <div>
                <div style="font-size:32px;">🍌</div>
                BANANALOOP<br>
                <small>{package_type}</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write(
        f"Current design: **{package_type}** "
        f"with **{fibre}% fibre loading**."
    )

st.divider()

# Research section
st.subheader("03 / Research context")

left, right = st.columns(2)

with left:
    st.info(
        "**Fibre reinforcement**\n\n"
        "Plantain pseudostem contains lignocellulosic "
        "fibres that can be investigated as reinforcement "
        "in starch-based materials."
    )

with right:
    st.info(
        "**Plasticiser selection**\n\n"
        "Glycerol is used to modify the flexibility "
        "of starch-based films."
    )

st.warning(
    "The packaging preview is illustrative, not a physical "
    "simulation. Slider values do not predict measured "
    "strength, flexibility or water resistance."
)

st.caption("BananaLoop | Computational research project")
