
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
from pathlib import Path
import matplotlib as mpl

st.set_page_config(
    page_title="Planeta Formation - Enquête Diplômés",
    page_icon="🎓",
    layout="wide",
)

def load_css():
    css = """
    body {
        background-color: #f8f9fa;
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3 {
        color: #1a73e8;
        font-weight: 600;
    }

    [data-testid="metric-container"] {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        text-align: center;
        margin: 10px 0;
    }

    hr {
        border-top: 1px solid #ccc;
        margin: 30px 0;
    }

    div.element-container svg {
        border-radius: 8px;
    }

    .stMultiSelect, .stSelectbox, .stSlider {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }

    button {
        background-color: #1a73e8 !important;
        color: #fff !important;
        border-radius: 8px !important;
    }

    footer {
        visibility: hidden;
    }

    .planeta-logo {
        max-width: 200px;
        display: block;
        margin: auto;
        padding-bottom: 1rem;
    }

    .planeta-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        border-bottom: 1px solid #e1e4e8;
    }
    """
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_matplotlib_styles():
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'sans-serif']
    mpl.rcParams['axes.facecolor'] = '#F8FBFD'
    mpl.rcParams['axes.edgecolor'] = '#DDE6ED'
    mpl.rcParams['axes.labelcolor'] = '#2C3E50'
    mpl.rcParams['axes.grid'] = True
    mpl.rcParams['grid.color'] = '#E5E9F0'
    mpl.rcParams['grid.linestyle'] = '--'
    mpl.rcParams['grid.alpha'] = 0.6
    mpl.rcParams['xtick.color'] = '#2C3E50'
    mpl.rcParams['ytick.color'] = '#2C3E50'
    mpl.rcParams['figure.figsize'] = [10, 6]
    mpl.rcParams['figure.facecolor'] = '#FFFFFF'

load_css()
set_matplotlib_styles()
df = pd.read_csv("enquete_diplomes_planeta.csv")

logo_path = "Diseño sin título (32).png"
logo_html = f'<img src="data:image/png;base64,{img_to_base64(logo_path)}>" class="planeta-logo">'


st.markdown(f"""
<div class="planeta-header">
    {{logo_html}}
    <h1>🎓 Analyse Enquête Diplômés – Planeta Formation</h1>
    <p>Un aperçu interactif des données d'insertion professionnelle et de satisfaction des diplômés.</p>
</div>
""", unsafe_allow_html=True)

