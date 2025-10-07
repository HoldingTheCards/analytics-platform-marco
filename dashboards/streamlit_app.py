import streamlit as st
import duckdb

st.set_page_config(page_title="AE Local Dashboard", layout="wide")

con = duckdb.connect("data/analytics.duckdb")
st.title("Events Dashboard (DuckDB)")

st.markdown("### Daily Events by Type")
df = con.execute("select * from marts.mrt_events_daily").fetchdf() if con.sql("show all schemas").filter("schema_name='marts'").fetchall() else con.execute("select 1 as day, 'page_view' as event_name, 1 as events").fetchdf()
st.dataframe(df)

st.markdown("ℹ️ Läuft lokal & kostenlos. Die Tabellen werden mit `dbt build` erzeugt.")
