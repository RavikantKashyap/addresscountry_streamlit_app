import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='test_project')


file = st.file_uploader('Upload a csv file')

def load_overall_analysis():
    st.title("Null values records from all fields")
    null_giv_name = df[df['giv_name'].isna()].shape[0]
    null_last_name = df[df['last_name'].isna()].shape[0]
    
    
    col1,col2 = st.columns(2)
    with col1:
        st.metric('Null in given name',str(null_giv_name))
        st.dataframe(df[df['giv_name'].isna()])
    with col2:
        st.metric('Null in last name',str(null_last_name))
        st.dataframe(df[df['last_name'].isna()])

    if null_last_name or null_giv_name >0:
        st.title("After handling Null Values")
        df.fillna('',inplace=True)
        st.dataframe(df)
        total_records_after_rem_null= df.shape[0]
        st.metric('Total Records after handling null values',str(total_records_after_rem_null))
    df.drop_duplicates(subset=['concat_id'],inplace=True)
    st.title("After removing duplicates on basis of concat id")
    st.dataframe(df)
    total_records_after_rem_dup= df.shape[0]
    st.metric('Total Records after removing duplicates values',str(total_records_after_rem_dup))

    null_prep_but_lp_Present=df[(df['giv_name']!='') & (df['last_name']=='')].shape[0]
    null_lp_but_prep_Present=df[(df['giv_name']=='') & (df['last_name']!='')].shape[0]
    null_both_lp_prep=df[(df['giv_name']=='') & (df['last_name']=='')].shape[0]
    st.title("Checks Performed")
    st.text("records where LP having values but not present in Prep")
    st.metric('Len of Null Prep',str(null_prep_but_lp_Present))
    st.dataframe(df[(df['giv_name']!='') & (df['last_name']=='')])
    st.text("records where Prep having values but not present in LP")
    st.metric('Len of Null LP',str(null_lp_but_prep_Present))
    st.dataframe(df[(df['giv_name']=='') & (df['last_name']!='')])
    st.text("records where both LP and Prep values missing")
    st.metric('Len of both LP and Prep missing',str(null_both_lp_prep))
    st.dataframe(df[(df['giv_name']=='') & (df['last_name']=='')])
    # col3,col4,col5 = st.columns(3)
    # with col3:
    #     st.text("records where LP having values but not present in Prep")
    #     st.metric('Len of Null Prep',str(null_prep_but_lp_Present))
    #     st.dataframe(df[(df['giv_name']!='') & (df['last_name']=='')])

    # with col4:
    #     st.text("records where Prep having values but not present in LP")
    #     st.metric('Len of Null LP',str(null_lp_but_prep_Present))
    #     st.dataframe(df[(df['giv_name']=='') & (df['last_name']!='')])

    # with col5:
    #     st.text("records where both LP and Prep values missing")
    #     st.metric('Len of both LP and Prep missing',str(null_both_lp_prep))
    #     st.dataframe(df[(df['giv_name']=='') & (df['last_name']=='')])
def load_lp_analysis():
    df.fillna('',inplace=True)
    st.sidebar.selectbox('Select lp field',sorted(df['giv_name'].unique().tolist()))

def load_PDE_details(selected_PDE):
    st.title(selected_PDE)
    st.title("Null values records from all fields")
    null_giv_name = df[df['giv_name'].isna()].shape[0]
    null_last_name = df[df['last_name'].isna()].shape[0]
    
    
    col1,col2 = st.columns(2)
    with col1:
        st.metric('Null in given name',str(null_giv_name))
        st.dataframe(df[df['giv_name'].isna()])
    with col2:
        st.metric('Null in last name',str(null_last_name))
        st.dataframe(df[df['last_name'].isna()])

    if null_last_name or null_giv_name >0:
        st.title("After handling Null Values")
        df.fillna('',inplace=True)
        st.dataframe(df)
        total_records_after_rem_null= df.shape[0]
        st.metric('Total Records after handling null values',str(total_records_after_rem_null))
    df.drop_duplicates(subset=['concat_id'],inplace=True)
    st.title("After removing duplicates on basis of concat id")
    st.dataframe(df)
    total_records_after_rem_dup= df.shape[0]
    st.metric('Total Records after removing duplicates values',str(total_records_after_rem_dup))

    null_prep_but_lp_Present=df[(df['giv_name']!='') & (df['last_name']=='')].shape[0]
    null_lp_but_prep_Present=df[(df['giv_name']=='') & (df['last_name']!='')].shape[0]
    null_both_lp_prep=df[(df['giv_name']=='') & (df['last_name']=='')].shape[0]
    st.title("Checks Performed")
    st.text("records where LP having values but not present in Prep")
    st.metric('Len of Null Prep',str(null_prep_but_lp_Present))
    st.dataframe(df[(df['giv_name']!='') & (df['last_name']=='')])
    st.text("records where Prep having values but not present in LP")
    st.metric('Len of Null LP',str(null_lp_but_prep_Present))
    st.dataframe(df[(df['giv_name']=='') & (df['last_name']!='')])
    st.text("records where both LP and Prep values missing")
    st.metric('Len of both LP and Prep missing',str(null_both_lp_prep))
    st.dataframe(df[(df['giv_name']=='') & (df['last_name']=='')])


if file is not None:
    df = pd.read_csv(file)
    st.title("adrresscountry analysis ")
    st.sidebar.title("adrresscountry analysis")
    st.dataframe(df)
    total_records= df.shape[0]
    st.metric('Total Records',str(total_records))
    option = st.sidebar.selectbox('Select One',['Overall Analysis','landing_pad','Prep','PDE'])
    if option=='Overall Analysis':
        btn0 = st.sidebar.button("Show Overall Analysis")
        if btn0:
            load_overall_analysis()

    elif option=='landing_pad':
        btn1 = st.sidebar.button("Find lp field Details")
        if btn1:
            load_lp_analysis()
    
    elif option=='PDE':
        selected_PDE = st.sidebar.selectbox('Select PDE',['Select PDE','addresscountrycode','DateOfBirth'])
        btn2 = st.sidebar.button("Find PDE Details")
        st.title('PDE Analysis')
        if btn2:
            load_PDE_details(selected_PDE)
        
        
        
        