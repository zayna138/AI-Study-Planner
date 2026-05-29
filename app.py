import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.title("📚 AI Study Planner")

st.write("Generate your personalized study timetable")

subjects = st.text_area(
    "Enter subjects (comma separated)"
)

hours_per_day = st.number_input(
    "Study hours per day",
    min_value=1,
    max_value=24,
    value=4
)

exam_date = st.date_input("Enter exam date")

if st.button("Generate Plan"):

    subject_list = subjects.split(",")

    days_left = (exam_date - datetime.today().date()).days

    if days_left <= 0:
        st.error("Exam date must be in future")
    else:

        hours_per_subject = round(
            hours_per_day / len(subject_list), 2
        )

        data = []

        for subject in subject_list:
            data.append({
                "Subject": subject.strip(),
                "Hours Per Day": hours_per_subject
            })

        df = pd.DataFrame(data)

        st.success("Study Plan Generated!")

        st.table(df)