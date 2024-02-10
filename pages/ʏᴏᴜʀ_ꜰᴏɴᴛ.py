import streamlit as st


# Streamlit app
def main():
    st.set_page_config(
        page_title="About​",
        page_icon="🔮",
        layout="centered"
    )

    st.error("##### 🚨ᴛʀᴀɴꜱꜰᴏʀᴍ ʏᴏᴜʀ ʜᴀɴᴅᴡʀɪᴛɪɴɢ ᴏʀ ᴄᴀʟʟɪɢʀᴀᴘʜʏ ɪɴᴛᴏ ᴀ ꜰᴏɴᴛ!​ ")
    st.image("pages//1.jpg", caption="", use_column_width=True)
    st.info("###### 👉🏻 ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ᴏᴡɴ ꜰᴏɴᴛ.")
    st.markdown("#### ᴄʀᴇᴀᴛᴇ ᴛᴇᴍᴘʟᴀᴛᴇ ⏬")

        

    st.image("pages//2.jpg", caption="", use_column_width=True)
    st.markdown("#### ᴄʟɪᴄᴋ ᴀʀʙɪᴛʀᴀʀʏ ᴄʜᴀʀᴀᴄᴛᴇʀꜱ ᴀɴᴅ ᴀᴅᴅ ᴛʜᴇ ᴄʜᴀʀᴀᴄᴛᴇʀꜱ ⏬")

    st.image("pages//3.jpg", caption="", use_column_width=True)
    st.markdown("#### ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ᴘᴅꜰ ᴀɴᴅ ᴡʀɪᴛᴇ ᴀɴᴅ ꜱᴄᴀɴ ᴛʜᴇ ᴘᴀɢᴇ ᴀɴᴅ ᴜᴘʟᴏᴀᴅ ⏬")
    st.info("###### ⏬ ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ᴏᴡɴ ꜰᴏɴᴛ ⏬")
    st.image("pages//5.jpg", caption="", use_column_width=True) 
    st.markdown("##### ᴜᴘʟᴏᴀᴅ ᴛʜᴇ ꜱᴄᴀɴɴᴇᴅ ᴘᴀɢᴇ ⏬")
    st.image("pages//4.jpg", caption="", use_column_width=True)
    st.markdown("##### ᴘʀᴇᴠɪᴇᴡ ᴛʜᴇ ᴘᴀɢᴇ ᴀɴᴅ ᴍᴏᴅɪꜰʏ ꜰᴏɴᴛ ʙᴀꜱᴇᴅ ᴏɴ ʏᴏᴜʀ ɴᴇᴇᴅꜱ ⏬")
    st.image("pages//6.jpg", caption="", use_column_width=True)
    st.markdown("##### ʙᴜɪʟᴅ ʏᴏᴜʀ ꜰᴏɴᴛ ⏬")
    st.image("pages//7.jpg", caption="", use_column_width=True)
    st.markdown("##### ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ɪɴꜱᴛᴀʟʟ ᴛʜᴇ ꜰᴏɴᴛ ɪɴ ʏᴏᴜʀ ᴘᴄ ⏬")
    st.image("pages//8.jpg", caption="", use_column_width=True)
    
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