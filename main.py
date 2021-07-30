
import json
#   Malnutrition risk Low risk Enhanced risk Medium risk High risk
# Very high risk
BMI_CATAGORY = {
    "Underweight-Malnutrition risk": {
        "max": 18.4,
        "min": 0
    }, 
    "Normal weight-Low risk":{
        "max": 24.9,
        "min": 18.5
    },
    "Overweight-Enhanced risk":{
        "max": 29.9,
        "min": 25
    }, 
    "Moderately obese-Medium risk" : {
        "max": 34.9,
        "min": 30
    },
    "Severely obese-High risk": {
        "max": 39.9,
        "min": 35
    }, 
    "Very severely obese-Very high risk": {
        "max": 100,
        "min": 40
    }
}
def calculateBMI(data):
    # convert height from CM to M
    bmi = data["WeightKg"] / (data["HeightCm"] * 0.01)
    data['bmi'] = bmi
    if bmi > BMI_CATAGORY["Overweight-Enhanced risk"]["min"]:
        data['is_over_weight'] = True
    for item in BMI_CATAGORY:
        if bmi > BMI_CATAGORY[item]['min'] and bmi < BMI_CATAGORY[item]['max']:
           split = item.split("-")
           data['catagory'] = split[0]
           data['risk']=split[1]
    
    return data
    

# Opening JSON file
f = open('data.json',)
# returns JSON object as 
# a dictionary
data = json.load(f)
overWeightPpl = []
# Iterating through the json
# list
print("----------------------------\n")
for i in data:
    i = calculateBMI(i)
    
    if i['is_over_weight']: 
        for key in i:
            print(key, ":", i[key], "\n")
        
        print("----------------------------\n")

# Closing file
f.close()