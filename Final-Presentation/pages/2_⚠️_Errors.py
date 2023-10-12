import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import streamlit as st

def main():
    url = 'https://raw.githubusercontent.com/bhumikasrc/Hypothesis-Testing/master/Final-Presentation/pages/errors.jpg'
    st.image(url,use_column_width=True)
if __name__ == '__main__':
    st.set_page_config(page_title="Errors", page_icon="⚠️",layout='wide')
    main()