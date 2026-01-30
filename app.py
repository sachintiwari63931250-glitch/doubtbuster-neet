import streamlit as st

st.set_page_config(
    page_title="DoubtBuster NEET",
    layout="centered"
)

st.title("🧠 DoubtBuster NEET")
st.subheader("NEET Biology AI Helper")

menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "Home",
        "Notes",
        "MCQ Practice",
        "PDF Upload",
        "Photo Doubt Solver"
    ]
)

if menu == "Home":
    st.success("App is running successfully 🚀")
st.write("Prepare NEET Biology with AI-powered tools.")
chapters = [
    "The Living World",
    "Biological Classification",
    "Plant Kingdom",
    "Animal Kingdom",
    "Morphology of Flowering Plants",
    "Anatomy of Flowering Plants",
    "Structural Organisation in Animals",
    "Cell: The Unit of Life",
    "Biomolecules",
    "Cell Cycle and Cell Division",

    "Transport in Plants",
    "Mineral Nutrition",
    "Photosynthesis in Higher Plants",
    "Respiration in Plants",
    "Plant Growth and Development",

    "Digestion and Absorption",
    "Breathing and Exchange of Gases",
    "Body Fluids and Circulation",
    "Excretory Products and their Elimination",
    "Locomotion and Movement",
    "Neural Control and Coordination",
    "Chemical Coordination and Integration",

    "Reproduction in Organisms",
    "Sexual Reproduction in Flowering Plants",
    "Human Reproduction",
    "Reproductive Health",

    "Principles of Inheritance and Variation",
    "Molecular Basis of Inheritance",
    "Evolution",

    "Human Health and Disease",
    "Strategies for Enhancement in Food Production",
    "Microbes in Human Welfare",

    "Biotechnology: Principles and Processes",
    "Biotechnology and its Applications",

    "Organisms and Populations",
    "Ecosystem",
    "Biodiversity and Conservation",
    "Environmental Issues"
]
menu = st.sidebar.selectbox("Menu", ["Home", "Notes"])

if menu == "Home":
    st.success("App is running successfully ✅")
    st.write("Prepare NEET Biology with AI-powered tools.")
elif menu == "Notes" :
    st.header("Biology Notes Generator")
chapter = st.selectbox("Select Chapter", chapters)
if st.button("Generate Notes"):
    st.subheader(f"Notes: {chapter}")
st.markdown("""    
### 📘 The Living World – NEET Biology Notes

**Definition**
Living organisms show metabolism, growth, reproduction and response to stimuli.

**Characteristics**
- Growth
- Reproduction
- Metabolism (most important)
- Cellular organisation
- Consciousness""")

**NCERT Key Points**
- Metabolism is defining property
- Viruses are borderline between living & non-living
- Binomial nomenclature by Carolus Linnaeus

**NEET Focus**
- Direct definition based MCQs
- Virus & taxonomy questions
""")
elif menu == "MCQ Practice":
    st.header("Sample MCQ")
    q = "Which organelle is the powerhouse of the cell?"
    st.write(q)

    ans = st.radio(
        "Choose answer:",
        ["Nucleus", "Ribosome", "Mitochondria", "Golgi body"]
    )

    if st.button("Submit"):
        if ans == "Mitochondria":
            st.success("Correct answer ✅")
        else:
            st.error("Wrong answer ❌")

elif menu == "PDF Upload":
    st.header("Upload Biology PDF")
    pdf = st.file_uploader("Upload PDF", type=["pdf"])
    if pdf:
        st.success("PDF uploaded successfully")

elif menu == "Photo Doubt Solver":
    st.header("Upload Question Image")
    img = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if img:
        st.image(img, caption="Uploaded Image")
        st.info("AI solver feature coming soon")
 
