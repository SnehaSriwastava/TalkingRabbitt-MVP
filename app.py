import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🐰 Talking Rabbitt - AI Data Assistant")

st.write("Upload your sales dataset and ask questions about it.")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Show dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Ask question
    question = st.text_input("Ask a question about your data")

    # Example questions for user guidance
    st.caption("Example questions: Which region has highest revenue? | Which product performs best?")

    if question:

        st.subheader("Answer")

        # Question: highest revenue by region
        if "region" in question.lower() and "highest" in question.lower():

            result = df.groupby("Region")["Revenue"].sum()
            top_region = result.idxmax()

            st.write(f"The region with the highest revenue is **{top_region}**.")

            # Chart
            st.subheader("Revenue by Region")
            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)
            st.pyplot(fig)

        # Question: best performing product
        elif "product" in question.lower():

            result = df.groupby("Product")["Revenue"].sum()
            top_product = result.idxmax()

            st.write(f"The best performing product is **{top_product}**.")

            # Chart
            st.subheader("Revenue by Product")
            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)
            st.pyplot(fig)

        else:

            st.write("Please ask about **region revenue** or **product performance**.")
