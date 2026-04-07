import streamlit as st
import sys
import os
from io import BytesIO

# FIX IMPORT PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.coordinator import run_research

# PDF LIB
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# FUNCTION TO CREATE PDF
def generate_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)
    buffer.seek(0)

    return buffer


# UI
st.title("🧠 AI Research Assistant")

topic = st.text_input("Enter Research Topic")

if st.button("Generate Report"):
    if topic:
        with st.spinner("Researching..."):
            result = run_research(topic)

            st.markdown(result)

            # 🔥 PDF BUTTON
            pdf_file = generate_pdf(result)

            st.download_button(
                label="📄 Download Report as PDF",
                data=pdf_file,
                file_name="research_report.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Enter a topic")