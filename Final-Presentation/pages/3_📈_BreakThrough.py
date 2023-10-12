import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import streamlit as st

sns.set_style('white',rc = {'axes.facecolor': '#0f1116',
                            'xtick.color':'w',
                            'ytick.color':'w',
                            'axes.labelcolor':'w',
                            'text.color':'w'})


def main():

    st.markdown('<h2 align="center"> Glasses Make you Taller*</h2>',unsafe_allow_html=True)
    st.divider()

    np.random.seed(10)
    control = np.random.normal(165,30,100).astype(int)
    glasses = np.random.normal(160,30,100).astype(int)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h5 align="center">Control Hacking</h5>',unsafe_allow_html=True)
        control_cutoff = st.slider('Control Slider',
                                   control.min(),
                                   control.max(),
                                   value= control.max(),
                                   label_visibility='collapsed')
    
    with col2:
        st.markdown('<h5 align="center">Glasses Hacking</h5>',unsafe_allow_html=True)
        glasses_cutoff = st.slider('Glasses Slider',
                                   glasses.min(),
                                   glasses.max(),
                                   label_visibility='collapsed')
    
    control_edit = control[control <= control_cutoff]
    glasses_edit = glasses[glasses >= glasses_cutoff]

    fig = plt.figure(figsize=(6,4))
    fig.set_facecolor('#0f1116')
    sns.kdeplot(control_edit,fill=True, label='control')
    sns.kdeplot(glasses_edit,fill=True, label='glasses')
    plt.title('Distribution of Heights',weight='bold')
    plt.xlabel('Height (cm)')
    c_m = round(control_edit.mean(),2)
    g_m = round(glasses_edit.mean(),2)
    plt.axvline(c_m,c='c',linestyle='--')
    plt.axvline(g_m,c='r',linestyle='-')
    
    if st.toggle('6 FOOT',label_visibility='collapsed'):
        plt.axvline(182.88,linewidth=3,color='lightgreen')
        plt.text(185.88, 0.01,'6 Foot line',weight='bold',fontsize=20,color='lightgreen')
    
    plt.legend()
    plt.tight_layout()
    st.pyplot(fig)


    col1, col2, col3 = st.columns(3)
    
    c = round(control.mean(),2)
    g = round(glasses.mean(),2)
    
    col1.metric("Control Mean", c_m, round(c_m-c,2))
    col2.metric("Glasses Mean", g_m, round(g_m-g,2))
    col3.metric("P-Value", round(stats.mannwhitneyu(control_edit,glasses_edit,alternative='less')[1],4))
    
    st.divider()
    st.markdown("""               
                \* Big Glasses is not resposible for inability to grow taller after purchase of our glasses.
                Purchase at your own discretion. Terms and conditions apply.
                """)

if __name__ == '__main__':
    st.set_page_config(page_title='Breakthrough in growth', layout='centered')
    main()