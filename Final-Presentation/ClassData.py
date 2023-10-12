import numpy as np 
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import streamlit as st

plt.rcParams['text.color'] = 'w'
plt.rcParams['axes.labelcolor'] = 'w'
plt.rcParams['xtick.color'] = 'w'
plt.rcParams['ytick.color'] = 'w'

def main():
    st.markdown("<h1 align='center'>MSDS Cohort height testing</h1>",unsafe_allow_html=True)
    st.divider()
    # Heights with glasses
    col1, col2, col3 = st.columns(3)
    # Heights without glasses
    with col1:
        st.markdown('##### Heights of those without glasses')
        no_glasses = pd.DataFrame([60,62,64,65,66], columns=['Height'])
        no_glasses = st.data_editor(no_glasses, hide_index=True)
    with col2:
        st.markdown('##### Heights of those with glasses')
        glasses = pd.DataFrame([52,54,53,49,60], columns=['Height'])
        glasses = st.data_editor(glasses, hide_index=True)
    with col3:
        st.markdown('##### Conducting a 2 sample t-test')
        t_statistic, p_value = stats.ttest_ind(glasses['Height'], no_glasses['Height'])
        st.metric('T statistic',round(t_statistic,2))
        st.metric('P Value',round(p_value,4))

    glasses['Glasses'] = 1
    no_glasses['Glasses'] = 0
    # Combine the data
    data = pd.concat([glasses, no_glasses])

    # Add a constant for the intercept term
    data['Intercept'] = 1
    st.divider()
    st.markdown("<h2 align='center'>Relating Hypothesis Testing to Linear Regression</h2>",unsafe_allow_html=True)
    # 
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(5,4))
    
    ax.scatter(data['Glasses'], data['Height'],color='r')
    ax.set_facecolor('#0f1116')
    ax.spines[:].set_color('w')

    # Label x and y axes
    ax.set_xlabel('Glasses')
    ax.set_ylabel('Height')
    # Show the plot
    fig.set_facecolor('#0f1116')
    fig.tight_layout()

    col1, col2 = st.columns(2)
    with col1:
        if st.toggle('Line of Best Fit'):
            slope, intercept = np.polyfit(data['Glasses'], data['Height'], 1)
            # Add line of best fit
            plt.plot(data['Glasses'], slope*data['Glasses'] + intercept, color='c')

        st.pyplot(fig,use_container_width=True)
    
    # Define the model
    model = sm.OLS(data['Height'], data[['Intercept', 'Glasses']])
    # Fit the model
    results = model.fit()
    summary = results.summary().tables
    # Return Summary Table

    with col2:
        if st.toggle('Model Summary'):
            st.markdown(summary[0].as_html(),unsafe_allow_html=True)
            st.markdown(summary[1].as_html(),unsafe_allow_html=True)
            st.markdown(summary[2].as_html(),unsafe_allow_html=True)
        
    st.divider()
    if st.button('CONCLUSION',use_container_width=True):
        st.markdown('# THIS IS THE SAME RESULT WE GOT USING STATS.TTEST_IND() !')

if __name__ == '__main__':
    st.set_page_config(page_title='Hypothesis Testing',page_icon='🧑‍🎓', layout='wide')
    main()