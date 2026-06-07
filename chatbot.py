import streamlit as st
import requests

# --- Explain function ---
def explain_topic(topic):
    if topic.lower() == "python":
        return "Python is a beginner-friendly programming language."
    elif topic.lower() == "sdlc":
        return "SDLC is the Software Development Life Cycle."
    elif topic.lower() == "sql":
        return "SQL is used to query and manage databases."
    elif topic.lower() == "api":
        return "APIs let applications talk to each other. REST APIs use GET, POST, PUT, DELETE."
    else:
        return "Topic not found."

# --- Practice function ---
def practice_exercise(topic):
    if topic.lower() == "python":
        st.write("Python Practice Exercise:")
        st.write("1. Write a function that adds two numbers.")
        st.write("2. Bonus: Ask the user for input and add those numbers.")

    elif topic.lower() == "sql":
        st.write("SQL Practice Exercise:")
        st.write("1. SELECT * FROM students;")
        st.write("2. SELECT COUNT(*) FROM students;")

    elif topic.lower() == "sdlc":
        st.write("SDLC Practice Exercise:")
        st.write("List the phases of SDLC in order (Requirements, Design, Implementation, Testing, Deployment, Maintenance).")

    elif topic.lower() == "api":
        # --- GET Demo ---
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            data = response.json()
            st.write("GET Response Example:")
            st.write(f"Title: {data['title']}")
            st.write(f"Body: {data['body']}")
        else:
            st.write("GET request failed.")

        # --- POST Demo ---
        new_post = {"title": "Debojit's Chatbot Lesson", "body": "Learning how POST works!", "userId": 1}
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
        if response.status_code == 201:
            data = response.json()
            st.write("POST Response Example:")
            st.write(f"ID: {data['id']}")
            st.write(f"Title: {data['title']}")
            st.write(f"Body: {data['body']}")
        else:
            st.write("POST request failed.")

        # --- PUT Demo ---
        updated_post = {"id": 1, "title": "Updated Chatbot Lesson", "body": "This shows how PUT updates data!", "userId": 1}
        response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)
        if response.status_code == 200:
            data = response.json()
            st.write("PUT Response Example:")
            st.write(f"ID: {data['id']}")
            st.write(f"Title: {data['title']}")
            st.write(f"Body: {data['body']}")
        else:
            st.write("PUT request failed.")

        # --- DELETE Demo ---
        response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            st.write("DELETE Response Example:")
            st.write("Post deleted successfully (fake API, so nothing really removed).")
        else:
            st.write("DELETE request failed.")

    else:
        st.write("Practice exercise not available for this topic.")

# --- Streamlit App ---
st.title("Debojit's AI Chatbot")
st.header("Learn AI step by step")

topic = st.selectbox("Choose a topic:", ["Python", "SDLC", "SQL", "API"])

if st.button("Explain"):
    st.write(explain_topic(topic))

if st.button("Practice"):
    practice_exercise(topic)
