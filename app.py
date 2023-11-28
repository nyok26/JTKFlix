import streamlit as st
import pandas as pd

# Data loading
st.set_page_config(page_title="JTKFlix", page_icon="🎥") 
data = pd.read_csv("all_streaming.csv") 

st.title("Welcome To JTKFlix!🎬")
st.header("JTKFlix Adalah Website Untuk Mencari Ribuan Rekomendasi Film Bedasarkan Genre")
st.subheader("Bingung Mau Nonton Apa?? Cari Rekomendasi Filmnya Di JTKFlix Aja")
genre = st.selectbox("Pilih Genre🎞:", data['gender_type'].unique())  
data_filtered = data[data["gender_type"].str.contains(genre)]

# Kolom default
columns = ["title", "gender_type", "channel_streaming"]  

# Checkbox kolom
if st.checkbox('Tampilkan Kolom Director'):
    columns.append("director")
    
if st.checkbox('Tampilkan Kolom Negara'):
    columns.append("country")

if st.checkbox("Tampilkan Kolom Tahun Rilis"):
    columns.append("release_year")

if st.checkbox("Tampilkan Kolom Durasi Film"):
    columns.append("duration_seconds")
    
if st.checkbox("Tampilkan Kolom Deskripsi"):
    columns.append("description")

# Dan seterusnya untuk checkbox kolom lainnya
    
# Tampilkan tabel
st.dataframe(data_filtered[columns].style.set_properties(**{'maxHeight': '150px', 'overflowY': 'scroll'}))
# Footer
st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
footer="""<style>
a:link , a:visited{
color: #F63366;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #393a3d;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# Custom CSS
hide_menu="""
        <style>
        MainMenu {visibility: hidden}
        footer {visibility: hidden}
        </style>
        """
st.markdown(hide_menu, unsafe_allow_html=True)