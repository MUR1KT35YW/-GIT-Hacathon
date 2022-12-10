from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model_1.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")







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
            
@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        symptom_1 = request.form["SYMPTOM1"]
        symptom_2 = request.form["SYMPTOM2"]
        symptom_3 = request.form["SYMPTOM3"]
        symptom_4 = request.form["SYMPTOM4"]
        symptom_5 = request.form["SYMPTOM5"]
        weight(symptom_1)
        weight(symptom_2)
        weight(symptom_3)
        weight(symptom_4)
        weight(symptom_5)
        prediction=model.predict([list])
        return render_template('home.html',prediction_text="predicted diease is {}".format(prediction))     
  
if __name__ == "__main__":
    app.run(debug=True)