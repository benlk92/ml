import time
import datetime
import csv
import numpy as np
import pydot

from sklearn import tree
from sklearn.externals.six import StringIO

from HeartDiseaseParser import HeartDiseaseParser

class DecisionTree():
    def __init__(self, parser):
        self.parser = parser
        self.classifier = tree.DecisionTreeClassifier()

    def train(self, data, target):
        self.classifier = self.classifier.fit(data, target)

    def print_tree(self, filename):
        dot_data = StringIO()
        tree.export_graphviz(self.classifier, out_file=dot_data, feature_names=self.parser.ATTRIBUTES)
        graph = pydot.graph_from_dot_data(dot_data.getvalue())
        graph.write_pdf(filename)

    def test(self, test_percentage):
        data = self.parser.parse()
        training_data_length = int(len(data['data']) * (1 - test_percentage))

        training_data = data['data'][0:training_data_length,:]
        training_target = data['target'][0:training_data_length]

        self.train(training_data, training_target)

        test_data = data['data'][training_data_length:,:]
        test_target = data['target'][training_data_length:]

        results = self.classifier.predict(test_data)

        num_correct = 0
        for i in range(len(results)):
            if test_target[i] == results[i]:
                num_correct = num_correct + 1

        print "Number of tests:", len(results)
        print "Number correct:", num_correct
        print "--------------------------------------"
        print "Percentage correct:", (num_correct / float(len(results)))*100
        
        current_time = time.time()
        timestamp = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d_%H:%M:%S')
        self.print_tree("test_" + timestamp + ".pdf")

if __name__ == '__main__':
    heart_disease_parser = HeartDiseaseParser('cleve.mod')
    heart_disease_decision_tree = DecisionTree(heart_disease_parser)
    heart_disease_decision_tree.test(.1)
