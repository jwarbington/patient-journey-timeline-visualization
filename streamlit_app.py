import streamlit as st
import pandas as pd
##import plotly.express as px

# Create sample data
data = {
    'Start_Date': pd.date_range(start='2023-01-01', periods=8),
    'End_Date': pd.date_range(start='2023-01-02', periods=8),  # Adding end dates
    'Event_Type': ['Urgent Care', 'Pharmacy', 'ED Visit', 'Inpatient', 
                   'Pharmacy', 'Appointment', 'Pharmacy', 'Urgent Care'],
    'Details': ['Visit for flu', 'Prescription filled', 'Severe pain', 
                'Hospital stay', 'Refill', 'Follow-up', 'New prescription',
                'Follow-up visit']
}

df = pd.DataFrame(data)

# Streamlit app
st.title('Patient Journey Timeline')
st.caption("Prototype Health Universe app")

## Timeline visualization using Plotly
##fig = px.timeline(df, x_start='Start_Date', x_end='End_Date', y='Event_Type', 
##                 hover_data=['Details'])
##st.plotly_chart(fig)

# Event details in table format
st.write('Event Details:')
st.dataframe(df)

st.markdown("____")
st.markdown("Learn more about Health Universe - the open-source platform dedicated to transofmring healthcare through data-driven apps: https://www.healthuniverse.com/")
