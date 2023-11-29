import snowflake.snowpark.session as session
import streamlit as st 
import streamlit.components.v1 as components
import os


def jstag(jsfile:str,diraname:str):
    jstexto = openfiles(jsfile,diraname)
    jstag = '<script>' + jstexto + '</script>'
    return jstag


def openfiles(fname:str,dirname:str):
    cdir = os.getcwd() 
    workdir = os.path.join(cdir, dirname,fname)
    ofile =  open(workdir,"r")
    ffile = ofile.read()
    html_string = ffile
    ofile.close()
    return html_string



st.set_page_config(
    page_title="Snowteller App",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#htmlfile = openfiles("index.html","/app/templates")
htmlfile = openfiles("index.html","templates")

components.html(htmlfile,height=600,)


