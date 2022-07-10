
import streamlit as st
from forex_python.converter import CurrencyRates,CurrencyCodes

with open ("style.css") as f :
    st.markdown( f'<style>{f.read()}</style>',unsafe_allow_html=True)


st.title("Currency conveter")
col1,col2=st.columns(2)
global cs,number,change,output
c=CurrencyRates()
cs=CurrencyCodes()

number=0
froms=col1.selectbox("Change",['$ - USD', '€ - EUR', '£ - GBP', '$ - MXN', 'Kč - CZK', 'R$ - BRL', 'zł - PLN', '₱ - PHP', 'R - ZAR'])
change=col1.number_input("Amount",0,100000000000)

tos=col2.selectbox("To",['$ - USD', '€ - EUR', '£ - GBP', '$ - MXN', 'Kč - CZK', 'R$ - BRL', 'zł - PLN', '₱ - PHP', 'R - ZAR'])
output=st.header(float(number))




def convert():
    global c,cs,number,change,output
    
    output.empty()
    number=c.convert(froms[-3:], tos[-3:], change)  
   
    output=st.header("{} {}".format(str(cs.get_symbol(tos[-3:])),number))
    


convert_btn=st.button(label='Converted',on_click=convert())