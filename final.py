import streamlit as st
import pandas as pd
import numpy as np
install scikit-learn
import pickle 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, roc_auc_score, recall_score, precision_score, average_precision_score, f1_score, classification_report, accuracy_score, plot_roc_curve, plot_precision_recall_curve, plot_confusion_matrix
import pickle 
# load model
import pickle
loaded_model = pickle.load(open('clf_pipe1.sav', 'rb'))

def predict_probability(stag,profession,traffic,coach,greywage,extraversion,independ,selfcontrol,anxiety,novator):
    prediction=loaded_model.predict_proba(data_new)[:, 1]#predictions using our model
    return prediction 
def main():
    st.title("Turnover analysis") #simple title for the app
    html_temp="""
        <div>
        <h2> Survival app for employee</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    stag=st.slider("stag", 0, 180,step = 30,help = "Set the time to prediction from 1 month to 6 months")
    extraversion=st.number_input("extraversion",0.0,10.0,.1,step =.1)
    independ=st.number_input("independ",0.0,10.0,.1,step =.1)
    selfcontrol=st.number_input("selfcontrol",0.0,10.0,.1,step =.1)
    anxiety=st.number_input("anxiety",0.0,10.0,.1,step =.1)
    novator=st.number_input("novator",0.0,10.0,.1,step =.1,help = "creativity" )
    greywage = st.selectbox("greywage",options=['white' , 'grey' ])
    traffic = st.selectbox("traffic",options=['recNErab' , 'advert' ,'KA','referal' , 'friends' ,'rabrecNErab','empjs','youjs'],help =
"From what pipelene employee came to the company:                                                              -                                 "   
"ADVERT  You contacted the company directly after learning from advertising, knowing the company's brand, etc."
"recNErab You contacted the company directly on the recommendation of your friend - NOT an employee of this company "
"referal You contacted the company directly on the recommendation of your friend - an employee of this company  "
"KA  You have applied for a vacancy on the job site "
"KA The recruiting agency brought you to the employer "
"friends  Invited by the Employer, we knew him before the employment "
"rabrecNErab The employer contacted you on the recommendation of a person who knows you "
"empjs  The employer reached you through your resume on the job site ")
    coach = st.selectbox("coach",options=['no' , 'yes' ,'my head'],help = "select if the cantidate will have a surpervisor/no supervisor /or will be a supervisor" )
    profession=st.selectbox("profession",options=['BusinessDevelopment','Marketing' ,'IT' ,'HR' ,'etc' ,'Consult' ,'Commercial','manage','Finanñe','Engineer','Teaching','Accounting','Law','PR' ])
    
   
    import pandas as pd
    data_new = pd.DataFrame({
        'stag':[stag],
        'profession':[profession],
        'traffic':[traffic],
        'coach':[coach], 
        'greywage':[greywage],
        'extraversion':[extraversion], 
        'independ':[independ], 
        'selfcontrol':[selfcontrol],
        'anxiety':[anxiety],
        'novator':[novator]
})

    data_new["profession"] = data_new["profession"].astype("category")
    data_new["traffic"] = data_new["traffic"].astype("category")
    data_new["coach"] = data_new["coach"].astype("category")
    data_new["greywage"] = data_new["greywage"].astype("category")
   

    result=""
    if st.button("Predict"):
        #prediction=loaded_model.predict_proba(data_new)[:, 1]
        result=loaded_model.predict_proba(data_new)[:, 1].round(3) #result will be displayed if pressed
    st.success("The probability to stay in the company  is {}" .format(result))
        
if __name__=='__main__':
    main()
   
