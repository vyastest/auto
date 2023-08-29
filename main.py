import streamlit as st

# Sample list of suggestions
suggestions = ['virat kohli', 'ab de villiers', 'sachin tendulkar', 'yuvraj singh', 'dhoni ms']

def autocomplete_input(suggestions):
    # Text input widget with autocomplete
    user_input = st.text_input("Type a name:", "")

    # Filter suggestions based on user input
    filtered_suggestions = [sugg for sugg in suggestions if user_input.lower() in sugg.lower()]

    # Display matching suggestions
    st.write("Matching suggestions:")
    for suggestion in filtered_suggestions:
        st.write(suggestion)

# Main Streamlit app
if __name__ == "__main__":
    st.title("Autocomplete Example")
    autocomplete_input(suggestions)
