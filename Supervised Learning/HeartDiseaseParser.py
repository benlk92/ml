import numpy as np
import csv

class HeartDiseaseParser():

    ATTRIBUTES = [
        'Age',
        'Sex',
        'Chest Pain Type',
        'Resting Blood Pressure',
        'Cholesteral',
        'Fasting Blood Pressure < 120',
        'Resting ECG',
        'Max Heart Rate',
        'Exercise Induced Angina',
        'Oldpeak',
        'Slope',
        'Number of Vessels',
        'Thal',
        'Heart Disease?'
    ]

    ATTRIBUTE_FORMATS = [
        np.uint,
        np.bool_, # male ? 1 : 0
        np.uint, # (angina, abnang, notang, asympt)
        np.uint,
        np.uint,
        np.bool_,
        np.uint, # (norm, abn, hyper)
        np.uint,
        np.bool_,
        np.float_,
        np.uint, # (up, flat, down)
        np.float_,
        np.uint, # (norm, fixed, rever)
        np.bool_
    ]

    ATTRIBUTE_VALUE_NAMES = {
        1: ['female', 'male'],
        2: ['angina', 'abnang', 'notang', 'asympt'],
        6: ['norm', 'abn', 'hyper'],
        10: ['up', 'flat', 'down'],
        12: ['norm', 'fixed', 'rever']
    }

    TARGET_NAMES = [
        'Has heart disease',
        'Does not have heart disease'
    ]

    def __init__(self, filename):
        self.filename = filename 

    def preprocess(self, row):
        row[0] = int(float(row[0]))
        row[1] = {'fem':0, 'male':1}[row[1]]
        row[2] = {'angina':0, 'abnang':1, 'notang':2, 'asympt':3}[row[2]]
        row[3] = int(float(row[3]))
        row[4] = int(float(row[4]))
        row[5] = {'fal':0, 'true':1}[row[5]]
        row[6] = {'norm':0, 'abn':1, 'hyp':2}[row[6]]
        row[7] = int(float(row[7]))
        row[8] = {'fal':0, 'true':1}[row[8]]
        row[9] = float(row[9])
        row[10] = {'up':0, 'flat':1, 'down':2}[row[10]]
        row[11] = int(float(row[11]))
        row[12] = {'norm':0, 'fix':1, 'rev':2}[row[12]]
        row[13] = 0 if row[13] == 'buff' else 1
        row.pop()
        return row

    def parse(self):
        data = []

        with open(self.filename, 'rb') as datafile:
            reader = csv.reader(datafile, delimiter=' ')

            for idx,row in enumerate(reader):
                # only start preprocessing after comments
                if idx < 20 or len(row) == 0:
                    continue

                data.append(self.preprocess(row))

        data = np.array(data)

        return {
            'data': data[:,0:-1],
            'target': data[:,-1]
        }
