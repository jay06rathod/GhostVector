import streamlit as st
import cairosvg
import re
import io
import zipfile

st.title("GhostVector 👻")

# User Options
target_color = st.color_picker("Pick a color to replace black outlines:", "#FFFFFF")
output_format = st.radio("Choose Output Format:", ["PNG", "SVG"])

# File uploader
uploaded_files = st.file_uploader("Upload SVG files", type=["svg"], accept_multiple_files=True)

if uploaded_files and st.button("Convert Files"):
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for uploaded_file in uploaded_files:
            svg_data = uploaded_file.getvalue().decode('utf-8')
            
            # Replace black with the chosen color
            modified_svg = re.sub(r'#000000|black|rgb\(0,0,0\)', target_color, svg_data, flags=re.IGNORECASE)
            
            # Handle output format
            if output_format == "PNG":
                file_bytes = cairosvg.svg2png(bytestring=modified_svg.encode('utf-8'))
                ext = ".png"
            else:
                file_bytes = modified_svg.encode('utf-8')
                ext = ".svg"
                
            # Write to ZIP
            filename = uploaded_file.name.replace('.svg', ext)
            zip_file.writestr(filename, file_bytes)

    st.success(f"Successfully converted {len(uploaded_files)} files!")
    st.download_button(
        label=f"Download {output_format}s (ZIP)",
        data=zip_buffer.getvalue(),
        file_name=f"GhostVector_{output_format.lower()}s.zip",
        mime="application/zip"
    )