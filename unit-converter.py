# import streamlit as st

# st.title("🔄 Unit Converter")
# st.markdown("### Converts Weight, Length and Time with Ease")
# st.write("Welcome! Choose a category, enter a value, and get instant conversions in real-time.")

# category = st.selectbox("Choose a Conversion Type", ["Weight", "Length", "Time"])

# def convert_units(category, value, unit):

#     if category == "Weight":
#         if unit == "Kilograms to Pounds":
#             return value * 2.20462
#         elif unit == "Pounds to Kilograms":
#             return value / 2.20462
#         elif unit == "Grams to Ounces":
#             return value * 0.035274
#         elif unit == "Ounces to Grams":
#             return value / 0.035274
#         elif unit == "Tons to Pounds":
#             return value * 2000
#         elif unit == "Pounds to Tons":
#             return value / 2000

#     elif category == "Length":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value / 0.621371
#         elif unit == "Meters to Feet":
#             return value * 3.28084
#         elif unit == "Feet to Meters":
#             return value / 3.28084
#         elif unit == "Yards to Inches":
#             return value * 36
#         elif unit == "Inches to Yards":
#             return value / 36
        
#     elif category == "Time":
#         if unit == "Seconds to Minutes":
#             return value / 60
#         elif unit == "Minutes to Seconds":
#             return value * 60
#         elif unit == "Hours to Minutes":
#             return value * 60
#         elif unit == "Minutes to Hours":
#             return value / 60
#         elif unit == "Days to Hours":
#             return value * 24
#         elif unit == "Hours to Days":
#             return value / 24
        
#     return 0
        
# if category == "Weight":
#     unit = st.selectbox("��️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams", "Tons to Pounds", "Pounds to Tons"])
# elif category == "Length":
#     unit = st.selectbox("��️ Select Conversion", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", "Yards to Inches", "Inches to Yards"])
# elif category == "Time":
#     unit = st.selectbox("���️ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Days to Hours", "Hours to Days"])

# value = st.number_input("Enter a value to convert")

# if st.button("Convert"):
#     converted_value = convert_units(category, value, unit)
#     st.success(f"The result is {converted_value: .2f}")


import streamlit as st

st.title("🔄 Unit Converter")
st.markdown("### ⚖️📏⏳ Effortless Conversion of Weight, Length, and Time")
st.write("🚀 Welcome! Choose a category, enter a value, and get instant conversions in real-time.")

category = st.selectbox("📂 Choose a Conversion Type", ["Weight", "Length", "Time"])

def convert_units(category, value, unit):

    if category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Ounces":
            return value * 0.035274
        elif unit == "Ounces to Grams":
            return value / 0.035274
        elif unit == "Tons to Pounds":
            return value * 2000
        elif unit == "Pounds to Tons":
            return value / 2000

    elif category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Yards to Inches":
            return value * 36
        elif unit == "Inches to Yards":
            return value / 36
        
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Hours to Days":
            return value / 24
        
    return 0
        
if category == "Weight":
    unit = st.selectbox("⚖️Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams", "Tons to Pounds", "Pounds to Tons"])
elif category == "Length":
    unit = st.selectbox("📏Select Conversion", ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", "Yards to Inches", "Inches to Yards"])
elif category == "Time":
    unit = st.selectbox("⏳Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Days to Hours", "Hours to Days"])

value = st.number_input("🔢 Enter a value to convert")

if st.button("🔄 Convert"):
    converted_value = convert_units(category, value, unit)
    st.success(f"✅ The result is {converted_value: .2f}")
