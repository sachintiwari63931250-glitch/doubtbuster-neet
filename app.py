 import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="BioMaster AI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 BioMaster AI – Class 9 to 12 Biology")
st.success("All-in-one Biology Prep: Notes • MCQs • Tests • Doubt Solver")

# ---------------- DATA ----------------
chapters = {
    "Class 9": [
        "Cell – Structure & Function",
        "Tissues",
        "Diversity in Living Organisms",
        "Why Do We Fall Ill",
        "Natural Resources"
    ],
    "Class 10": [
        "Life Processes",
        "Control and Coordination",
        "How do Organisms Reproduce",
        "Heredity and Evolution",
        "Environment"
    ],
    "Class 11": [
        "The Living World",
        "Biological Classification",
        "Plant Kingdom",
        "Animal Kingdom",
        "Cell Structure",
        "Biomolecules",
        "Photosynthesis",
        "Respiration"
    ],
    "Class 12": [
        "Reproduction in Organisms",
        "Sexual Reproduction in Flowering Plants",
        "Human Reproduction",
        "Molecular Basis of Inheritance",
        "Evolution",
        "Human Health and Disease",
        "Biotechnology",
        "Ecology"
    ]
}

notes_db = {
    "Plant Kingdom": """
• Classification based on body organisation  
• Algae – chlorophyll bearing simple plants  
• Bryophytes – amphibians of plant kingdom  
• Pteridophytes – first vascular plants  
• Gymnosperms – naked seeds  
• Angiosperms – flowering plants
""",
    "The Living World": """
• Metabolism is defining property  
• Growth, reproduction, response to stimuli  
• Viruses are borderline  
• Binomial nomenclature – Carolus Linnaeus
"""
}

mcq_db = {
    "Plant Kingdom": [
        ("Amphibians of plant kingdom?", "Bryophytes"),
        ("Naked seeded plants?", "Gymnosperms")
    ],
    "The Living World": [
        ("Defining property of life?", "Metabolism"),
        ("Binomial nomenclature given by?", "Linnaeus")
    ]
}

# ---------------- SIDEBAR ----------------
st.sidebar.header("📘 Select Options")

selected_class = st.sidebar.selectbox("Select Class", list(chapters.keys()))
selected_chapter = st.sidebar.selectbox(
    "Select Chapter", chapters[selected_class]
)

feature = st.sidebar.radio(
    "Choose Feature",
    ["Notes", "MCQs", "Daily Plan", "Mistake Points", "Photo Doubt Solver"]
)

# ---------------- NOTES ----------------
if feature == "Notes":
    st.header(f"📖 Notes: {selected_chapter}")
    notes = notes_db.get(
        selected_chapter,
        "Notes will be added soon for this chapter."
    )
    st.markdown(notes)

# ---------------- MCQs ----------------
elif feature == "MCQs":
    st.header(f"❓ MCQs: {selected_chapter}")
    questions = mcq_db.get(selected_chapter)

    if questions:
        for i, (q, ans) in enumerate(questions, 1):
            st.write(f"{i}. {q}")
            if st.button(f"Show Answer {i}"):
                st.success(ans)
    else:
        st.info("MCQs coming soon for this chapter.")

# ---------------- DAILY PLAN ----------------
elif feature == "Daily Plan":
    st.header("📅 Daily Biology Study Plan")
    st.markdown("""
**Day Plan**
• 1 hr – NCERT reading  
• 30 min – Notes revision  
• 20 MCQs practice  
• 10 min – Mistake analysis  
• 1 image doubt (if any)
""")

# ---------------- MISTAKE POINTS ----------------
elif feature == "Mistake Points":
    st.header("⚠️ Common Mistake Points")
    st.markdown("""
• Confusing examples  
• Not reading NCERT lines  
• Ignoring diagrams  
• Not revising previous chapters
""")

# ---------------- DOUBT SOLVER ----------------
elif feature == "Photo Doubt Solver":
    st.header("📸 Photo Doubt Solver")
    image = st.file_uploader(
        "Upload Biology Question Image",
        type=["jpg", "png", "jpeg"]
    )
    if image:
        st.image(image, caption="Uploaded Doubt Image")
        st.info("AI analysis feature will be added soon.")
