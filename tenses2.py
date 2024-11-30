import streamlit as st

# Define questions based on grammar topics
grammar_questions = {
    "Present Simple": [
        ("She ___ (like) ice cream.", "likes"),
        ("They ___ (not/work) on Sundays.", "don't work"),
        ("We ___ (play) football every weekend.", "play"),
        ("He ___ (not/watch) TV often.", "doesn't watch"),
        ("Do you ___ (go) to the gym?", "go"),
        ("The train ___ (leave) at 8 AM.", "leaves"),
        ("I ___ (not/know) the answer.", "don't know"),
        ("The sun ___ (rise) in the east.", "rises"),
        ("She always ___ (read) before bed.", "reads"),
        ("Why ___ (you/speak) so loudly?", "do you speak"),
    ],
    "Past Simple": [
        ("He ___ (go) to the park yesterday.", "went"),
        ("They ___ (not/see) the movie last week.", "didn't see"),
        ("We ___ (play) a great game of chess.", "played"),
        ("She ___ (not/know) the answer.", "didn't know"),
        ("Did you ___ (visit) your grandparents?", "visit"),
        ("I ___ (buy) a new laptop last month.", "bought"),
        ("He ___ (speak) to her two days ago.", "spoke"),
        ("They ___ (win) the match last weekend.", "won"),
        ("The train ___ (arrive) late yesterday.", "arrived"),
        ("Why ___ (you/leave) the party early?", "did you leave"),
    ],
    "Future Simple": [
        ("I ___ (travel) to Paris next month.", "will travel"),
        ("She ___ (not/attend) the meeting tomorrow.", "won't attend"),
        ("We ___ (visit) the museum next weekend.", "will visit"),
        ("They ___ (not/finish) the project on time.", "won't finish"),
        ("Will you ___ (help) me with my homework?", "help"),
        ("He ___ (go) to the doctor next week.", "will go"),
        ("She ___ (speak) at the conference.", "will speak"),
        ("The train ___ (arrive) at 10 PM.", "will arrive"),
        ("I ___ (not/buy) that expensive car.", "won't buy"),
        ("Why ___ (you/call) him tomorrow?", "will you call"),
    ],
}

# App logic
def main():
    st.title("Grammar Trainer")
    st.write("Welcome! Select a tense and practice your grammar step by step.")
    
    # Select a tense
    tense = st.selectbox("Choose a tense to practice:", options=["Select"] + list(grammar_questions.keys()))
    if tense != "Select":
        # Initialize session state variables
        if "current_question_index" not in st.session_state:
            st.session_state.current_question_index = 0
        if "score" not in st.session_state:
            st.session_state.score = 0
        if "completed" not in st.session_state:
            st.session_state.completed = False

        # Get current question
        questions = grammar_questions[tense]
        index = st.session_state.current_question_index

        if not st.session_state.completed:
            question, correct_answer = questions[index]

            # Display question
            st.write(f"Question {index + 1}/{len(questions)}:")
            user_answer = st.text_input(question, key=f"q{index}")

            # Submit button
            if st.button("Submit", key=f"submit{index}"):
                if user_answer.lower().strip() == correct_answer.lower():
                    st.success("Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"Incorrect! The correct answer is: {correct_answer}")

                # Move to the next question
                if index + 1 < len(questions):
                    st.session_state.current_question_index += 1
                else:
                    st.session_state.completed = True

        # Display final score
        if st.session_state.completed:
            st.write(f"Well done! You completed the quiz.")
            st.write(f"Your final score: {st.session_state.score}/{len(questions)}")
            if st.button("Restart"):
                st.session_state.current_question_index = 0
                st.session_state.score = 0
                st.session_state.completed = False

if __name__ == "__main__":
    main()
