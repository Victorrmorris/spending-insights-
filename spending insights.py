import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Cross-Border Spending Insights",
    layout="wide",
    page_icon="🌍",
)

# Sample Data
us_data = {
    "Total Spent": "$4,200.50",
    "Categories": {
        "Transportation": "$650.00",
        "Rent": "$2,100.00",
        "Entertainment": "$450.50",
        "Utilities": "$300.00",
        "Groceries": "$700.00",
    },
}
italy_data = {
    "Total Spent": "€3,800.75",
    "Categories": {
        "Transportation": "€450.00",
        "Rent": "€1,800.75",
        "Entertainment": "€300.00",
        "Utilities": "€500.00",
        "Groceries": "€750.00",
    },
}

# Helper Functions
def display_budget_data(country, data):
    st.metric(label=f"{country} Total Spent", value=data["Total Spent"])
    st.write("**Category Breakdown:**")
    for category, amount in data["Categories"].items():
        st.markdown(f"- **{category}:** {amount}")

# Main Content
st.title("🌍 Cross-Border Spending Insights")
st.markdown(
    """
    Welcome to the Cross-Border Spending Insights Dashboard! This app provides actionable 
    insights into household spending in the US and Italy.
    """
)
st.markdown("---")

# US and Italy Insights Section
col1, col2 = st.columns(2)
with col1:
    st.subheader("US Household Spending")
    display_budget_data("US", us_data)

with col2:
    st.subheader("Italy Household Spending")
    display_budget_data("Italy", italy_data)

# Chatbot Section
st.markdown("---")
st.subheader("💬 Chat with Your Spending Assistant")
user_query = st.text_input("Ask a question about cross-border spending insights:")
if user_query:
    st.write(f"**Your Question:** {user_query}")
    st.info("Chatbot Response: This is a demo. Responses will appear here.")
else:
    st.write("Try asking questions like:")
    st.markdown("- **What is the biggest expense in the US?**")
    st.markdown("- **What is the biggest expense in Italy?**")
