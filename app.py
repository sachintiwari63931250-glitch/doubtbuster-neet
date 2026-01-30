
import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="DoubtBuster NEET", layout="centered")

st.title("🧠 DoubtBuster NEET")
st.caption("NEET Biology | Notes • MCQs • PDF • Photo Doubt Solver")

menu = st.radio(
    "Select Feature",
    ["📘 Notes", "📝 MCQs", "📄 PDF Viewer", "📷 Photo Doubt Solver"]
)

if menu == "📘 Notes":
    st.header("Biology Notes")
    st.write("• Cell Biology")
    st.write("• Plant Physiology")
    st.write("• Human Physiology")
    st.write("• Genetics & Evolution")
    st.write("• Ecology")

elif menu == "📝 MCQs":
    st.header("Practice MCQs")

    q = "Which organelle is known as the powerhouse of the cell?"
    st.write(q)

    option = st.radio(
        "Choose your answer",
        ["Nucleus", "Mitochondria", "Ribosome", "Golgi Apparatus"]
    )

    if st.button("Check Answer"):
        if option == "Mitochondria":
            st.success("Correct ✅")
        else:
            st.error("Wrong ❌ Correct answer is Mitochondria")

elif menu == "📄 PDF Viewer":
    st.header("Upload Biology PDF")
    pdf = st.file_uploader("Upload PDF", type=["pdf"])

    if pdf is not None:
        st.success("PDF uploaded successfully!")

elif menu == "📷 Photo Doubt Solver":
    st.header("Upload Image of Question / Diagram")
    img = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if img is not None:
        image = Image.open(img)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.info("AI solver feature coming soon 🚀")
