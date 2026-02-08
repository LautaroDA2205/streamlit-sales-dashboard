import streamlit as st
from backend import load_data, get_summary, plot_sales_over_time


def main():

    st.title("Supermarket Sales Dashboard")

    # Load data
    data = load_data()

    # Sidebar controls
    st.sidebar.header("Controls")
    min_rating = st.sidebar.slider(
        "Minimum Rating",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )

    # Filter data
    filtered_data = data[data["Rating"] >= min_rating]

    # Summary
    updated_summary = get_summary(filtered_data)

    st.write("### Summary Statistics")
    st.table(updated_summary)

    # Raw data
    st.write("### Raw Data")
    st.dataframe(filtered_data)

    # Plot
    st.write("### Sales Over Time")
    fig = plot_sales_over_time(filtered_data)
    st.pyplot(fig)


if __name__ == "__main__":
    main()
