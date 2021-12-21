import tkinter as tk
From Tkinter import *
from tkinter import filedialog
import streamlit as st
import glob


st.title('Folder Picker')
st.write('Please select a folder:')
clicked = st.button('Folder Picker')
if clicked:
    path = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
    files = glob.glob(str(path) + '\*.csv')
    st.text(files)