import streamlit as st
import subprocess

# Function to execute the command and generate the output file


def generate_qr_gram(message):
    command = [
        'python', './src/NonogramQR.py',
        message,
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        st.error(f"Error: {result.stderr}")
        return None
    else:
        st.success("NonogramQR generated successfully!")
        # Read the generated PDF file in binary mode
        try:
            with open("NonogramQR.pdf", "rb") as file:
                pdf_content = file.read()
            return pdf_content
        except FileNotFoundError:
            st.error("The generated PDF file was not found.")
            return None


st.set_page_config(page_title="NonogramQR", page_icon=":gear:")
st.title("NonogramQR")
# st.image("banner.png")
st.subheader("Solve, Scan, Discover: Turn Text into a Puzzle!")
st.markdown("""**Transform your messages into puzzles!**
            Encode your text or URL into a QR code, hide it within a nonogram puzzle, and challenge yourself or others to reveal and scan the hidden message. Dive into a unique blend of puzzle-solving and QR code functionality.
            """)

pdf_content = None

with st.form("message_form"):
    st.write("**Enter the message to encode in a nonogram**")
    file_message = st.text_input("Message", "Love is love!")

    if st.form_submit_button("Generate"):
        pdf_content = generate_qr_gram(file_message)

if pdf_content:
    st.download_button(
        label="Download PDF",
        data=pdf_content,
        file_name="NonogramQR.pdf",
        mime="application/pdf"
    )
    st.balloons()
