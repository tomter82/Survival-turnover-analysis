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
#loaded_model = pickle.load(open('clf_pipe5.sav', 'rb'))
loaded_model = pickle.load(open('logit1.pkl', 'rb'))
def predict_probability(stag,gender,age,industry,profession,traffic,coach,head_gender,greywage,way,extraversion,independ,selfcontrol,anxiety,novator):
    prediction=loaded_model.predict_proba(data_new)[:, 1]#predictions using our model
    return prediction 
def main():
    st.title("We are hiring!") #simple title for the app
    html_temp="""
        <div>
        <h2></h2>
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
    
    
    
    import pandas as pd
    data_new = pd.DataFrame({
        'stag':[stag],
        'gender':[gender],
        'age':[age],
        'industry':[industry],
        'profession':[profession],
        'traffic':[traffic],
        'coach':[coach], 
        'head_gender':[head_gender],
        'greywage':[greywage],
        'way':[way],
        'extraversion':[extraversion], 
        'independ':[independ], 
        'selfcontrol':[selfcontrol],
        'anxiety':[anxiety],
        'novator':[novator]
    })

    
    data_new["gender"] =  data_new["gender"].astype("category")
    data_new["profession"] =  data_new["profession"].astype("category")
    data_new["traffic"] =  data_new["traffic"].astype("category")
    data_new["coach"] =  data_new["coach"].astype("category")
    data_new["head_gender"] =  data_new["head_gender"].astype("category")
    data_new["greywage"] =  data_new["greywage"].astype("category")
    data_new["way"] =  data_new["way"].astype("category")
    data_new["industry"] =  data_new["industry"].astype("category")
    
    result=""
    if st.button("Predict"):
       # result=predict_probability(stag, gender, age, industry, profession, traffic,coach, head_gender, greywage, way, extraversion, independ, selfcontrol, anxiety, novator)

        
        #prediction=loaded_model.predict_proba(data_new)[:, 1]
        result=loaded_model.predict_proba(data_new)[:, 1].round(3)*100   #result will be displayed if pressed
    st.success("Based on your profile ,your probability to still working in the Company is {}%" .format(result))
    
if __name__=='__main__':
    main()
   
