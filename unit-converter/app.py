import streamlit as st

st.title("Unit Converter")
#func
def distance_converter(from_unit,to_unit,value):
    units={"Meter" : 1,
           "Kilometer" :1000,
           "Miles":0.3048,
           "Feet":1609.34
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def tempertaure_converter(from_unit,to_unit,value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value
        return result
    
def weight_converter(from_unit,to_unit,value):
    units={"Kilogram": 1,
           "Grams": 0.001,
           "Ounces":0.453593,
           "Pounds": 0.0283495
    }
    result = value * units[from_unit] / units[to_unit]
    return result

def pressure_converter(from_unit,to_unit,value):
    units={"Pascals" : 1,
           "Hectopascals" : 100,
           "Kilopascals" : 1000,
           "Bar" : 100000
    }
    result = value * units[from_unit] / units[to_unit]
    return result




#UI
category=st.selectbox("Select catergory",["Distance", "Temperature", "Weight", "Pressure"])

if category=="Distance":
    from_unit = st.selectbox("From",["Meter", "Kilometer","Miles","Feet"])
    to_unit = st.selectbox("To",["Meter", "Kilometer","Miles","Feet"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = distance_converter = (from_unit,to_unit,value)
      

elif category == "Temperature":
    from_unit = st.selectbox("From",["Celsius", "Farenheit"])
    to_unit = st.selectbox("To",["Celsius", "Farenheit"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = distance_converter = (from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        

elif category == "Weight":
    from_unit = st.selectbox("From",["Kilogram","Grams","Ounces","Pound"])
    to_unit = st.selectbox("To",["Kilogram","Gram","Ounces","Pound"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = weight_converter = (from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From",["Pascals","Hectopascals","Kilopascals","Bar"])
    to_unit = st.selectbox("To",["Pascals","Hectopascals","Kilopascals","Bar"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = pressure_converter = (from_unit,to_unit,value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


