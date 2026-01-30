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
elif menu == "Notes":
    st.header("Biology Notes Generator")
chapter = st.selectbox(
    "Select Chapter",
    ["The living world", "Biological classification", "Plant kingdom"]
)

if st.button("Generate Notes"):
    st.subheader(f"Notes: {chapter}")

    if chapter == "The living world":
        st.markdown("""
### 📘 The Living World – NEET Biology Notes

**Definition**
Living organisms show metabolism, growth, reproduction and response to stimuli.

**Characteristics**
- Growth
- Reproduction
- Metabolism (most important)
- Cellular organisation
- Consciousness

**NCERT Key Points**
- Metabolism is defining property
- Viruses are borderline between living & non-living
- Binomial nomenclature by Carolus Linnaeus

**NEET Focus**
- Direct definition based MCQs
- Virus & taxonomy questions
""")

    else:
        st.info("Notes for this chapter will be added soon.")
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
 
