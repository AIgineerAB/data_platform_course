import streamlit as st
from read_data import read_data
from kpis import (
    total_applications,
    number_approved,
    number_distance,
    approved_remote,
    approved_percentage,
    provider_kpis,
)
from charts import approved_by_area


def layout():
    df = read_data()

    st.markdown("# YH dashboard 2024 aplications")

    st.markdown(
        "This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard."
    )

    st.markdown("## KPIs in Sweden")

    cols = st.columns(5)
    labels = (
        "total applications",
        "number approved",
        "percentage approved",
        "remote educations",
        "approved remote",
    )

    kpis = (
        total_applications,
        number_approved,
        number_distance,
        approved_remote,
        approved_percentage,
    )

    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)

    st.markdown("## Approved educations per area")

    approved_by_area()

    st.markdown("## Simple statistics on a given provider")

    st.markdown("Search for an educational provider")
    provider = st.selectbox(
        "Choose educational provider", df["Utbildningsanordnare administrativ enhet"].unique()
    )

    applications, approved_applications = provider_kpis(provider)

    st.markdown(
        f"This educational provider {provider} has applied for {applications} educations and gotten {approved_applications} approved."
    )

    st.markdown("## Raw data")
    st.markdown(
        "This data shows the results of all applications from different educational providers"
    )
    st.dataframe(df)


if __name__ == "__main__":
    layout()
    df = read_data()

    # print(df.query(""))
