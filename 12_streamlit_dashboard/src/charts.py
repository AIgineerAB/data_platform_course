import streamlit as st
from read_data import read_data
import duckdb


def approved_by_area():
    df = read_data()

    df = duckdb.query(
        """
                SELECT 
                    utbildningsområde, COUNT(*) AS Beviljade
                FROM 
                    df 
                WHERE 
                    beslut = 'Beviljad'
                GROUP BY 
                    utbildningsområde
                ORDER BY 
                    Beviljade
                DESC
        """
    ).df()

    st.bar_chart(df, x="Utbildningsområde", y="Beviljade")
