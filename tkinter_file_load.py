import tkinter as tk
from tkinter import filedialog
import streamlit as st
import glob

# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title('Folder Picker')
st.write('Please select a folder:')
clicked = st.button('Folder Picker')
if clicked:
    path = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
    files = glob.glob(str(path) + '\*.csv')
    st.text(files)