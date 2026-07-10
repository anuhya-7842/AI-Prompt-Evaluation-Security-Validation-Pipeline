import streamlit as st
import pandas as pd

st.set_page_config(page_title="Golden Dataset", page_icon="📂")

st.title("📂 Golden Dataset")

df = pd.read_csv("datasets/golden_dataset.csv")

st.write(f"Total Test Cases: {len(df)}")

search = st.text_input("Search a Question")

if search:
    filtered = df[df["vars.question"].str.contains(search, case=False, na=False)]
    st.dataframe(filtered, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Golden Dataset",
    data=csv,
    file_name="golden_dataset.csv",
    mime="text/csv"
)