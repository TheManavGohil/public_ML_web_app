# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:59:04 2025

@author: B A P S
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu 

##loading saved modelsdiabities_model
diabities_model = pickle.load(open('diabities.sav', 'rb'))

heart_diseases_model = pickle.load(open('heart_diseases.sav', 'rb'))

parkinsons_modle = pickle.load(open('parkisons.sav', 'rb'))


#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple diseases Pediction System using ML', 
                           
                           ['Diabities Prediction',
                            'Heart Diseases Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index=0)
    
#Diabities prediction page
if(selected == 'Diabities Prediction'):
    #page title
    st.title('Diabities Prediction using ML')
    
    #getting the input from the user
    # columns for the input field
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input(' Glucose level')
    with col3:
        BloodPressure = st.text_input('BP level')
    with col1:
        SkinThickness = st.text_input('SkinThickness value')
    with col2:
        Insulin = st.text_input('Insulin value')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    #code for prediction
    diabities_diagnosis = ''
    
    #creating button for prwediction
    if st.button('Diabities test Result'):
        diab_prediction = diabities_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction, Age]])
        
        if(diab_prediction[0] == 1):
            diabities_diagnosis = 'The person is Diabitic'
        else:
            diabities_diagnosis = 'The person is not Diabitic'
            
    st.success(diabities_diagnosis)

    
    
if(selected == 'Heart Diseases Prediction'):
    #page title
    st.title('Heart Diseases Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input('Man or Woman(only)')
    with col3:
        cp = st.text_input('cp of the person')
    with col1:
        trestbps = st.text_input('trest bps value')
    with col2:
        chol = st.text_input('Chol value')
    with col3:
        fbs = st.text_input('fbs value')
    with col1:
        restecg = st.text_input('ECG value')
    with col2:
        thalach = st.text_input('thalach value')
    with col3:
        exang = st.text_input('exang value')
    with col1:
        oldpeak =st.text_input('oldpeak value')
    with col2:
        slope = st.text_input('slope value')
    with col3:
        ca = st.text_input('ca value')
    with col1:
        thal = st.text_input('thal valuer')
        
    #code for prediction
    heart_diagnosis = ''
    
    #creating button for prwediction
    if st.button('heart test Result'):
        heart_prediction = heart_diseases_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0] == 1):
            heart_diagnosis = 'The person has heart diseases'
        else:
            heart_diagnosis = 'The person does not have heart diseases'
            
    st.success(heart_diagnosis)
        
                            
    
if(selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkisons Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_FoHz = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_FhiHz = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_FloHz = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter_= st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_ShimmerdB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimme_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNRR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFAR = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2R = st.text_input('D2')
    with col1:
        PPER = st.text_input('PPE')
        
    #code for prediction
    parkin_diagnosis = ''
    
    #creating button for prwediction
    if st.button('Parkison test Result'):
        parki_prediction = parkinsons_modle.predict([[MDVP_FoHz,MDVP_FhiHz,MDVP_FloHz,MDVP_Jitter_,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_ShimmerdB,Shimmer_APQ3,Shimmer_APQ5, MDVP_APQ,Shimme_DDA,NHR,HNRR,RPDE,DFAR,spread1,spread2,D2R,PPER]])
        
        if(parki_prediction[0] == 1):
            parkin_diagnosis = 'The person has Parkison diseases'
        else:
            parkin_diagnosis = 'The person does not have Parkison diseases'
            
    st.success(parkin_diagnosis)
