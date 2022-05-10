import pickle

def result_condition(line):
    if line[0]<24:
        if line[7]==1 or line[8]==1 or line[9]==1:
            if line[10]==1 or line[11]==1 or line[12]==1:
                return 'Screen Immediately'
        if line[1]==1 or line[2]==1:
            if line[3]==1 or line[4]==1 or line[5]==1 or line[6]==1:
                return 'Screen after one Month'
        return 'No Risk'
    if line[0]<36:
        if line[6]==1 or line[7]==1 or line[8]==1 or line[9]==1 or line[10]==1 :
            if line[11]==1 or line[12]==1 or line[13]==1 or line[14]==1:
                return 'Screen Immediately'
        if line[1]==1:
            if line[2]==1 or line[3]==1 or line[4]==1 or line[5]==1:
                return 'Screen after one Month'
        return 'No Risk'
    if line[0]<48:
        if line[7]==1 or line[8]==1 or line[9]==1 or line[10]==1 or line[11]==1:
            if line[12]==1:
                return 'Screen Immediately'
        if line['Q1']==1:
            if line[2]==1 or line[3]==1 or line[4]==1 or line[5]==1 or line[6]==1:
                return 'Screen after one Month'
        return 'No Risk'

data1 = {"Patient_ID": 24,
         "Patient_Name": "Paula",
         "Age_months": 47,
         "Gender": 1,
         "Number_of_visits": 10,
         "Q1": "Yes",
         "Q2": "Yes",
         "Q3": "Yes",
         "Q4": "Yes",
         "Q5": "Yes",
         "Q6": "No",
         "Q7": "Yes",
         "Q8": "Yes",
         "Q9": "Yes",
         "Q10": "Yes",
         "Q11": "Yes",
         "Q12": "Yes",
         "Q13": "Yes",
         "Q14": "Yes",
}
sample = list(data1.values())
for a in range(len(data1)):
    if(sample[a] == 'Yes'):
        sample[a] = 1
    if(sample[a] == 'No'):
        sample[a] = 0
sample.pop(0)
sample.pop(0)
sample.pop(1)
sample.pop(1)
print(result_condition(sample))