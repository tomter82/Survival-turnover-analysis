import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import LogisticRegression
from sklearn import datasets, metrics, model_selection, svm
from sklearn.metrics import log_loss, roc_auc_score, recall_score, precision_score, average_precision_score, f1_score, classification_report, accuracy_score
import pickle 
import pickle 

# load model
import pickle
loaded_model = pickle.load(open('clf_pippo1.sav', 'rb'))
#loaded_model = pickle.load(open('clf_pip.sav', 'rb'))
def predict_probability(stag,gender,age,profession,traffic,coach,greywage,way,extraversion,independ,selfcontrol,anxiety,novator):
    prediction=loaded_model.predict_proba(data_new)[:, 1]#predictions using our model
    return prediction 
def main():
    st.title("Employee turnover analysis") #simple title for the app
    html_temp="""
        <div>
        <h2></h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple 

    gender=st.selectbox("Sex",options=['f', 'm' ])
    age=st.slider("Age", 15, 67,step = 1)
    profession=st.selectbox("Professional area ",options=['BusinessDevelopment','Marketing' ,'IT' ,'HR' ,'other' ,'Consult' ,'Commercial','manage','Finance','Engineer','Teaching','Accounting','Law','PR'  ])
    coach = st.selectbox("Coach",options=['no' , 'yes' ,'my head'],help = "Do You have a coach or do you work as a coach?" )
    greywage = st.selectbox("Wage",options=['contract', 'self_emp' ])
    way= st.selectbox("Way to work",options=['bus', 'car', 'foot'])
    extraversion=st.number_input("Extraversion",0.0,10.0,5.,step =.1)
    independ=st.number_input("Independ",0.0,10.0,5.,step =.1)
    selfcontrol=st.number_input("Selfcontrol",0.0,10.0,5.,step =.1)
    anxiety=st.number_input("Anxiety",0.0,10.0,5.,step =.1)
    novator=st.number_input("Innovator",0.0,10.0,5.,step =.1,help = "creativity" )
    traffic = st.selectbox("Contact",options=['From friend' , 'Advertising' ,'Recruiting agency','Direct contact' , 'Friends in the company' , 'From company employee','Company contact','Job site'],help = "How did you hear about the position")
    stag=st.slider("Prevision time", 0, 356,step = 30,help = "Set the time to predict")
    import pandas as pd
    data_new = pd.DataFrame({
        'stag':[stag],
        'gender':[gender],
        'age':[age],
        'profession':[profession],
        'traffic':[traffic],
        'coach':[coach], 
        'greywage':[greywage],
        'way':[way],
        'extraversion':[extraversion], 
        'independ':[independ], 
        'selfcontrol':[selfcontrol],
        'anxiety':[anxiety],
        'novator':[novator]
})

    
    data_new["gender"] = data_new["gender"].astype("category")
    data_new["profession"] = data_new["profession"].astype("category")
    data_new["traffic"] = data_new["traffic"].astype("category")
    data_new["coach"] = data_new["coach"].astype("category")
    data_new["greywage"] = data_new["greywage"].astype("category")
    data_new["way"] = data_new["way"].astype("category") 
    
    result=""
    if st.button("Predict"):
        #prediction=loaded_model.predict_proba(data_new)[:, 1]
        result=loaded_model.predict_proba(data_new)[:, 1].round(3)*100   #result will be displayed if pressed
    st.success("Based on your characteristics, the probability of still working with the company is {}%" .format(result))
    
if __name__=='__main__':
    main()
