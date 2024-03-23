import numpy as np
import pandas as pd
import pickle 
import streamlit as st

pickle_a=open("logit.pkl","rb")
regressor=pickle.load(pickle_a) # our model
#event var 
def predict_chance(stag, gender, age, industry, profession, traffic,
       coach, head_gender, greywage, way, extraversion, independ,
       selfcontrol, anxiety, novator):
    prediction=regressor.predict([[stag, event, gender, age, industry, profession, traffic,
       coach, head_gender, greywage, way, extraversion, independ,
       selfcontrol, anxiety, novator]]) #predictions using our model
    return prediction 


def main():
    st.title("Probability APP using ML") #simple title for the app
    html_temp="""
        <div>
        <h2> Prediction ML app</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    stag=st.slider("stag", 0, 180,1)
    extraversion=st.slider("extraversion",0,10,0,1)
    independ=st.slider("independ",0,10,0,1)
    selfcontrol=st.slider("selfcontrol",0,10,0,1)
    anxiety=st.slider("anxiety",0,10,0,1)
    novator=st.slider("novator",0,10,0,1)
    gender = st.selectbox("gender",options=['m' , 'f'])
    age = st.slider("Age", 18, 54,1)
    way = st.selectbox("way",options=['foot' , 'car' ,'bus'])
    head_gender = st.selectbox("head_gender",options=['m' , 'f' ])
    greywage = st.selectbox("greywage",options=['white' , 'grey' ])
    traffic = st.selectbox("traffic",options=['recNErab' , 'advert' ,'KA','referal' , 'friends' ,'rabrecNErab','empjs','youjs'])
    coach = st.selectbox("coach",options=['no' , 'yes' ,'my head'])
    industry=st.selectbox("industry",options=['Retail','manufacture' ,'IT' ,'Banks' ,'etc' ,'Consult' ,'State','Building','PowerGeneration','transport','Telecom','Mining','Pharma','Agriculture' ,'RealEstate',' HoReCa' ])
    profession=st.selectbox("profession",options=['BusinessDevelopment','Marketing' ,'IT' ,'HR' ,'etc' ,'Consult' ,'Commercial','manage','Finanñe','Engineer','Teaching','Accounting','Law','PR' ])
    result=""
    if st.button("Predict"):
        result=predict_chance(stag, gender, age, industry, profession, traffic,
        coach, head_gender, greywage, way, extraversion, independ,
        selfcontrol, anxiety, novator) #result will be displayed if button is pressed
    st.success("The probability to stay in the company  is{}".format(result))
        
if __name__=='__main__':
    main()
