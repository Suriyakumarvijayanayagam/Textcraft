import streamlit as st
from llm import palmllm
from docgen import analyze_and_add
import io
from pages import  ʏᴏᴜʀ_ꜰᴏɴᴛ
st.set_page_config(
        page_title="ᴛᴇxᴛᴄʀᴀꜰᴛ​",
        page_icon="📕",
        layout="centered"
    )




def main():
   
    st.markdown("<h1 style='text-align: center;'> ᴛᴇxᴛᴄʀᴀꜰᴛ</h1>", unsafe_allow_html=True)

    #st.sidebar.write("")
    user_prompt = st.text_area("ɢᴇɴʀᴀᴛᴇ ʏᴏᴜʀ ᴄᴏɴᴛᴇɴᴛ ʜᴇʀᴇ ✍🏼", value="", height=150, key="user_input", placeholder="​​🇳​​🇪​​🇪​​🇩​​ ​🇸​​🇴​​🇲​​🇪​​🇹​​🇭​​🇮​​🇳​​🇬​...🧐")

    button = st.button("​🇸​​🇺​​🇧​​🇲​​🇮​​🇹​🙋🏻‍♂")

    if button:
        contents = palmllm(user_prompt)

        st.write(contents)

        docx = analyze_and_add(contents)
        buffer = io.BytesIO()
        docx.save(buffer)
        docx_binary = buffer.getvalue()

        st.download_button(
            label="Download data as Word Document",  # Updated comment to reflect the correct file format
            data=docx_binary,
            file_name='document.docx',
            mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        )

   

if __name__ == "__main__":
    main()
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.caption("ᴄʀᴇᴀᴛᴇᴅ  😉 ʙʏ ꜱᴜʀɪʏᴀ 😎 ꜱᴜᴅʜᴀʀꜱᴏɴ")