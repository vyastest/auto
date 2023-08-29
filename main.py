import streamlit as st

# Sample list of suggestions
suggestions = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def autocomplete_input(suggestions):
    # Text input widget with autocomplete
    user_input = st.text_input("Type a fruit:", "")

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
