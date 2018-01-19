import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score


class LinearRegressionModel:
    def __init__(self):
        #Training Data
        self._x_train = []
        self._y_train = []

        #Test Data
        self._x_test = []
        self._y_test = []

        self._y_pred = []

        self.prepareData(fullpath="./data/train.csv", testSize=10)


    #Load Data from .csv file
    def prepareData(self, fullpath="./data/train.csv", testSize=10):
        print('Load data from '+ fullpath)
        with open(fullpath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            #skip the header
            next(reader, None)
            
            tmp = list(reader)
            self.rawData = np.asarray(tmp, dtype=float)



            
            #self.rawData = np.array([t for t in tmp]).reshape(-1,1)
            print('' + str(len(self.rawData)))


            #Make this statement simpler
            self.x = self.rawData[:,0]
            self.y = self.rawData[:,1]

            #Generate Trainings Data
            self._x_train = np.array(self.x, dtype=np.float)[:-testSize].reshape(-1,1)
            self._y_train = np.array(self.y, dtype=np.float)[:-testSize].reshape(-1,1)

            #Generate Testing Data
            self._x_test = np.array(self.x, dtype=np.float)[-testSize:].reshape(-1,1)
            self._y_test = np.array(self.y, dtype=np.float)[-testSize:].reshape(-1,1) 



    def trainModel(self):
        # Create linear regression object
        self.regr = linear_model.LinearRegression()

        # Train the model using the training sets
        x_train = self._x_train
        y_train =  self._y_train

        self.regr.fit(x_train, y_train)

    def testModel(self):
        print(self._x_test)
        _y_pred = np.array(self.regr.predict(self._x_test))
        print(_y_pred)

        # The coefficients
        print('Coefficients: \n', self.regr.coef_)
        
        # The mean squared error
        print("Mean squared error: %.2f"  % mean_squared_error(self._y_test.tolist(), _y_pred.tolist()))

        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % r2_score(self._y_test.tolist(), _y_pred.tolist()))
        

    def makePrediction(self, x_data=None):
        if (x_data is None ):
            return

        self._y_pred = np.array(self.regr.predict(x_data)).reshape(-1, 1)
        return self._y_pred



    def plot(self):
        _x_reshaped = np.array(self.x, dtype=np.float).reshape(-1, 1)

        print(_x_reshaped)
        y_pred = self.makePrediction(x_data= _x_reshaped)




        # Plot outputs
        plt.scatter(self.x, self.y, color='blue')
        plt.plot(self.x, y_pred, color='red', linewidth=1)

        plt.title('Simple Regression Model')
        plt.xlabel('X')
        plt.ylabel('Y')

     
        _min_y = int(min(self.y,key=float))
        _max_y = int(max(self.y, key=float))

        _min_x = int(min(self.x,key=float))
        _max_x = int(max(self.x, key=float))



        y_axis = np.arange(_min_y, _max_y, 10)

        #diff = 57600
        x_axis = np.arange(_min_x, _max_x, 10)
        #
       # str_x_axis = np.array(list([datetime.fromtimestamp(d).strftime('%D') for d in x_axis]), dtype=str)


        plt.xticks(x_axis, rotation=30)
        plt.yticks(y_axis, rotation=45)


        plt.show()



if __name__ == '__main__':
    la = LinearRegressionModel()

    #Prepare Model
    la.prepareData()

    #Train Model
    la.trainModel()

    #Test Model
    la.testModel()

    #Test Model
    la.makePrediction()

    # Plot Data
    la.plot()





