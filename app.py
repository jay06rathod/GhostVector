import streamlit as st
import cairosvg
import re
import io
import zipfile

st.title("GhostVector 👻")

target_color = st.color_picker("Pick a color to replace black outlines:", "#FFFFFF")
output_format = st.radio("Choose Output Format:", ["PNG", "SVG"])

uploaded_files = st.file_uploader("Upload SVG files", type=["svg"], accept_multiple_files=True)

if uploaded_files:
    zip_buffer = io.BytesIO()
    
    st.subheader("Preview & Download")
    cols = st.columns(3)
    
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for idx, uploaded_file in enumerate(uploaded_files):
            svg_data = uploaded_file.getvalue().decode('utf-8')
            modified_svg = re.sub(r'#000000|black|rgb\(0,0,0\)', target_color, svg_data, flags=re.IGNORECASE)
            
            # ALWAYS create a PNG version just for the on-screen preview
            preview_bytes = cairosvg.svg2png(bytestring=modified_svg.encode('utf-8'))
            
            # Handle the actual download format
            if output_format == "PNG":
                file_bytes = preview_bytes
                ext = ".png"
                mime = "image/png"
            else:
                file_bytes = modified_svg.encode('utf-8')
                ext = ".svg"
                mime = "image/svg+xml"
                
            filename = uploaded_file.name.replace('.svg', ext)
            zip_file.writestr(filename, file_bytes)
            
            with cols[idx % 3]:
                # Use the PNG bytes for the preview to avoid the PIL error
                st.image(preview_bytes, caption=filename, use_container_width=True)
                
                # The download button uses the requested format bytes
                st.download_button(
                    label=f"⬇️ {filename}", 
                    data=file_bytes, 
                    file_name=filename, 
                    mime=mime, 
                    key=f"dl_{idx}"
                )

    st.divider()
    st.download_button(
        label=f"📦 Download All {output_format}s (ZIP)",
        data=zip_buffer.getvalue(),
        file_name=f"GhostVector_files.zip",
        mime="application/zip"
    )