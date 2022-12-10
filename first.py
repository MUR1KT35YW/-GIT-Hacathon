import numpy as np
import pickle
import streamlit as st
import sklearn
import pandas as pd
import streamlit.components.v1 as components

with open('C:/Users\hp\Documents\Hackathon\style.css') as f:
   st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

loaded_model = pickle.load(open("C:/Users\hp\Documents\Hackathon\model_1.pkl", "rb"))

dis=['Drug_Reaction',
 'Malaria',
 'Allergy',
 'Hypothyroidism',
 'Psoriasis',
 'GERD',
 'Chronic_cholestasis',
 'hepatitis_A',
 'Osteoarthristis',
 '(vertigo)_Paroymsal__Positional_Vertigo',
 'Hypoglycemia',
 'Acne',
 'Diabetes',
 'Impetigo',
 'Hypertension ',
 'Peptic_ulcer_diseae',
 'Dimorphic_hemmorhoids(piles)',
 'Common_Cold',
 'Chicken_pox',
 'Cervical_spondylosis',
 'Hyperthyroidism',
 'Urinary_tract infection',
 'Varicose_veins',
 'AIDS',
 'Paralysis_(brain_hemorrhage)',
 'Typhoid',
 'Hepatitis_B',
 'Fungal_infection',
 'Hepatitis_C',
 'Migraine',
 'Bronchial_Asthma',
 'Alcoholic_hepatitis',
 'Jaundice',
 'Hepatitis_E',
 'Dengue',
 'Hepatitis_D',
 'Heart_attack',
 'Pneumonia',
 'Arthritis',
 'Gastroenteritis',
 'Tuberculosis']




list2=['lethargy','hip_joint_pain','muscle_weakness','irritability','muscle_pain','altered_sensorium',
'receiving_unsterile_injections','painful_walking','pus_filled_pimples','blackheads','scurring','silver_like_dusting'
'small_dents_in_nails','inflammatory_nails','red_sore_around_nose','lethargy']

list4=['nodal_skin_eruptions','continuous_sneezing','ulcers_on_tongue','fatigue'
'anxiety','cough','breathlessness','dark_urine','loss_of_appetite','pain_behind_the_eyes','constipation'
'abdominal_pain','yellow_urine','yellowing_of_eyes','throat_irritation','sinus_pressure','dizziness'
'cramps','bruising','obesity','excessive_hunger','drying_and_tingling_lips','slurred_speech'
'stiff_neck','loss_of_balance','unsteadiness','weakness_of_one_body_side','bladder_discomfort'
'internal_itching','belly_pain','watering_from_eyes','polyuria','mucoid_sputum','rusty_sputum'
'distention_of_abdomen','fluid_overload','palpitations']

list7=['high_fever','swelling_of_stomach','chest_pain','weakness_in_limbs','coma']
    
list6=['burning_micturition','spotting_urination','diarrhoea','acute_liver_failure'
'fluid_overload','swelled_lymph_nodes','malaise','pain_in_anal_region','irritation_in_anus'
'enlarged_thyroid','spinning_movements','continuous_feel_of_urine','abnormal_menstruation'
'stomach_bleeding','prominent_veins_on_calf','burning_micturition','spotting_urination'
'patches_in_throat']
    
list3=['skin_rash','chills','joint_pain','acidity','muscle_wasting','weight_gain',
    'mood_swings','weight_loss','sunken_eyes','sweating','headache','yellowish_skin',
    'back_pain','knee_pain','loss_of_smell','depression','red_spots_over_body',
    'lack_of_concentration','visual_disturbances','skin_peeling','yellow_crust_ooze']
    
list5=['shivering','stomach_pain','vomiting','cold_hands_and_feets','restlessness'
'irregular_sugar_level','indigestion','nausea','mild_fever','blurred_and_distorted_vision'
'phlegm','redness_of_eyes','runny_nose','congestion','fast_heart_rate','pain_during_bowel_movements'
'bloody_stool','neck_pain','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','brittle_nails'
'swollen_extremeties','extra_marital_contacts','swelling_joints','movement_stiffness','foul_smell_ofurine'
'passage_of_gases','toxic_look_(typhos)','increased_appetite','family_history','receiving_blood_transfusion'
'history_of_alcohol_consumption','blood_in_sputum','prognosis']

def main():
    st.title('Disease Prediction Web APP')
    st.number_input('AGE', 15, 100)


    st.selectbox('GENDER', ['MALE', 'FEMALE']) 
##def symptoms():
    symptom1= st.selectbox('SYMPTOM NO. 1', ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering',
    'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_urination',
    'fatigue','weight_gain','cold_hands_and_feets','mood_swings','weight_loss','lethargy','patches_in_throat',    
    'irregular_sugar_level','cough','high_fever','sunken_eyes',  'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine',
    'nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision',
    'phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising',
    'obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger',
    'extra_marital_contacts','drying_and_tingling_lips','slurred_speech',
    'knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance',
    'unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_ofurine','continuous_feel_of_urine','passage_of_gases',
    'internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum',
    'lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring',
    'skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze',
    'prognosis'])

    symptom2= st.selectbox('SYMPTOM NO. 2', ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering',
    'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_urination',
    'fatigue','weight_gain','cold_hands_and_feets','mood_swings','weight_loss','lethargy','patches_in_throat',    
    'irregular_sugar_level','cough','high_fever','sunken_eyes',  'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine',
    'nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision',
    'phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising',
    'obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger',
    'extra_marital_contacts','drying_and_tingling_lips','slurred_speech',
    'knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance',
    'unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_ofurine','continuous_feel_of_urine','passage_of_gases',
    'internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum',
    'lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring',
    'skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze',
    'prognosis'])
    
    symptom3= st.selectbox('SYMPTOM NO. 3', ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering',
    'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_urination',
    'fatigue','weight_gain','cold_hands_and_feets','mood_swings','weight_loss','lethargy','patches_in_throat',    
    'irregular_sugar_level','cough','high_fever','sunken_eyes',  'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine',
    'nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision',
    'phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising',
    'obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger',
    'extra_marital_contacts','drying_and_tingling_lips','slurred_speech',
    'knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance',
    'unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_ofurine','continuous_feel_of_urine','passage_of_gases',
    'internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum',
    'lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring',
    'skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze',
    'prognosis'])
    
    symptom4= st.selectbox('SYMPTOM NO. 4', ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering',
    'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_urination',
    'fatigue','weight_gain','cold_hands_and_feets','mood_swings','weight_loss','lethargy','patches_in_throat',    
    'irregular_sugar_level','cough','high_fever','sunken_eyes',  'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine',
    'nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision',
    'phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising',
    'obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger',
    'extra_marital_contacts','drying_and_tingling_lips','slurred_speech',
    'knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance',
    'unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_ofurine','continuous_feel_of_urine','passage_of_gases',
    'internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum',
    'lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring',
    'skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze',
    'prognosis'])
    
    symptom5= st.selectbox('SYMPTOM NO. 5', ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering',
    'chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_urination',
    'fatigue','weight_gain','cold_hands_and_feets','mood_swings','weight_loss','lethargy','patches_in_throat',    
    'irregular_sugar_level','cough','high_fever','sunken_eyes',  'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine',
    'nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision',
    'phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising',
    'obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger',
    'extra_marital_contacts','drying_and_tingling_lips','slurred_speech',
    'knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance',
    'unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_ofurine','continuous_feel_of_urine','passage_of_gases',
    'internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum',
    'lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring',
    'skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze',
    'prognosis'])
    list=[]
    def weight(x):
        if(x=='itching'):
            list.append(1)
        else: 
            for i in list2:
                    if(i==x):
                        list.append(2)
                    else:
                        pass
            for i in list3:
                    if(i==x):
                        list.append(3)
                    else:
                        pass
            for i in list4:
                if(i==x):
                    list.append(4)
                else:
                    pass
            for i in list5:
                if(i==x):
                    list.append(5)
                else:
                    pass
            for i in list6:
                if(i==x):
                    list.append(6)
                else:
                    pass
            for i in list7:
                if(i==x):
                    list.append(7)
                else:
                    pass
    weight(symptom1)
    weight(symptom2)
    weight(symptom3)
    weight(symptom4)
    weight(symptom5)
    prediction=' '
    
    if st.button('DIAGNOSE'):
        prediction=loaded_model.predict([list])
        if(len(list)<5):
            while((len(list)!=5) or len(list)<5):
                list.append(0)
        else:
            if(len(list)==5):
                l='Our Model has predicted that you have a '+prediction[0]+' Disease'
            
        
                st.success(l)
                def pre(x):
                    index=0
                    index=dis.index(x)
                    if (index==0):
                        h='hello'
                        st.success(h)
                    data=pd.read_csv('C:/Users\hp\Documents\Hackathon\symptom_precaution.csv')
                    p1='precaution 1 is:-',data.iloc[index,1]
                    p2='precaution 2 is:-',data.iloc[index,2]
                    p3='precaution 3 is:-',data.iloc[index,3]
                    p4='precaution 4 is:-',data.iloc[index,4]
           
                    para='Precautions:-'+' '+p1[1],p2[1],p3[1],p4[1]
                    for i in range(4):
                        st.success(para[i])
            
                pre(prediction[0])
       

    #return 'precaution 1 is:-',data.iloc[index,1]

 #C:/Users\hp\Documents\Hackathon\symptom_precaution.csv   
if __name__ == "__main__":
    main()