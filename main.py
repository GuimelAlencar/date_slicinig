from datetime import datetime, timedelta
import calendar
import streamlit as st

def tuple_from_a_period_of_dates(initial_date, final_date):
    if initial_date > final_date:
        # swap
        initial_date, final_date = final_date, initial_date
    
    date_list = []
    
    actual_date = initial_date
    while actual_date <= final_date:
        day_of_the_week = calendar.day_name[actual_date.weekday()]
        date_list.append((actual_date.strftime("%d/%m/%Y"), day_of_the_week))
        actual_date += timedelta(days=1)
    
    return tuple(date_list)

def search_for_day(date_tuple, day):
    list_of_days = []
    
    for date in date_tuple:
        if date[1] == day:
            list_of_days.append(date[0])
    
    return tuple(list_of_days)

def search_for_a_day_in_a_period(initial_date, final_date, day_of_the_week):
    period = tuple_from_a_period_of_dates(initial_date, final_date)
    list_of_days = search_for_day(period, day_of_the_week)
    return list_of_days

st.title("📆")
st.write(
    '''
    # Date_period_searching

    Hello! 👋 This app is made to search for a day of the week through an specific period,
    first, you chose the period, then, the day of the week as it follows:

    - Monday (segunda-feira)
    - Tuesday (terça-feira)
    - Wednesday (quarta-feira)
    - Thursday (quinta-feira)
    - Friday (sexta-feira)
    - Saturday (sábado)
    - Sunday (domingo)
    '''
)

today = datetime.now()
initial_date, final_date = st.date_input(
    "Period",
    (today, today + timedelta(days=7)),
    format="DD/MM/YYYY"
)

day_of_the_week = st.selectbox(
    "Day of the week",
    ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"),
    index=None,
    placeholder="Select The day of the week..."
)

if st.button("Run"):
    if day_of_the_week:
        list_of_days = search_for_a_day_in_a_period(initial_date, final_date, day_of_the_week)
        
        if list_of_days:
            for idx, day in enumerate(list_of_days, start=1):
                st.write(f"{idx}º {day_of_the_week}: {day}")
        else:
            st.write(f"No {day_of_the_week}s found in the selected period.")
    else:
        st.warning("Please select a day of the week")