 if important streamlit as st
# All NEET Biology chapters
chapters = [
    "The Living World",
    "Biological Classification",
    "Plant Kingdom",
    "Animal Kingdom",
    "Morphology of Flowering Plants",
    "Anatomy of Flowering Plants",
    "Cell: The Unit of Life",
    "Biomolecules",
    "Cell Cycle and Cell Division"
]
def generate_notes(chapter):
    return f"""
## {chapter} – NEET Biology Notes

### Introduction
This chapter is important for NEET Biology and is strictly based on NCERT.

### Key Concepts
- Definitions and explanations
- Important terminology
- NCERT-based facts

### NEET Focus
- Direct NCERT lines
- Frequently asked concepts
- Diagram-based questions

### Exam Tip
Revise NCERT multiple times and practice MCQs.
"chapter = st.selectbox("Select Chapter", chapters)""

    }

    return notes.get(chapter, "Notes not available")
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
st.subheader("Prepare NEET Biology with AI-powered tools")

chapter = st.selectbox(
    "Select Chapter",
    ["The Living World", "Plant Kingdom"]
)

if st.button("Generate Notes"):
    st.markdown(generate_notes(chapter))
    if chapter == "The Living World":
        st.subheader("The Living World – NEET Biology Notes")
        st.write("Living organisms show metabolism, growth, reproduction...")

    elif chapter == "Plant Kingdom":
        st.subheader("Plant Kingdom – NEET Biology Notes")
        st.write("Plant Kingdom includes algae, bryophytes, pteridophytes...")
        st.write("Classification based on body organization and reproduction.")

    elif chapter == "Biological Classification":
        st.subheader("Biological Classification – NEET Biology Notes")
        st.write("Five kingdom classification by R.H. Whittaker...")
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
st.markdown("**NCERT Key Points**")
st.markdown("- Metabolism is defining property")
st.markdown("- Viruses are borderline between living & non-living")
st.markdown("- Binomial nomenclature by Carolus Linnaeus")

st.markdown("**NEET Focus**")
st.markdown("- Direct definition based MCQs")
st.markdown("- Virus & taxonomy questions")
if menu == "Notes":
    st.header("Notes Section")
    st.markdown("**NCERT Key Points**")
    st.markdown("- Line 1")
    st.markdown("- Line 2")

elif menu == "MCQ Practice":
    st.header("MCQ Practice")
    st.write("MCQs will appear here")

elif menu == "Doubt Solver":
    st.header("Ask Your Doubt")

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

