#from hanaconnector import insertData
import csv
from operator import itemgetter
#Data Source: https://www.meteoblue.com/de/wetter/archive/export/mannheim_deutschland_2873891?daterange=2018-01-02+to+2018-01-09&params=&params%5B%5D=11%3B2+m+above+gnd&utc_offset=1&aggregation=hourly&temperatureunit=CELSIUS&windspeedunit=KILOMETER_PER_HOUR
class CSVLoader:

    def __init__(self, fullpath='', delimiter=';'):
        self.delimiter = delimiter
        self.fullpath = fullpath
        self.load()

        self.colMapping = dict(zip(self.header, range(0, len(self.header))))
        return

        # Load Data from .csv file

    def load(self, ):
        if self.fullpath == '':
            return

        with open(self.fullpath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter)
            self.header = next(reader, None)  # skip the header
            self.data = list(reader)


    def get_all_data(self):
        return self.data

    def get_header(self):
        return self.header


    def get_cols(self, cols=[]):
        if cols == []:
            return self.data
        else:
            print(self.colMapping)

            indexes = list(self.colMapping[c] for c in cols)
            res = [list([row[i] for i in indexes]) for row in self.data]
            return res




    #Write Data to .csv fiel
    def write(self, name='', header=[], data=[], newline='', delimiter=';'):
        if (name == '') | (len(header) != len(data)):
            return

        with open(name, 'w', newline='') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=';')
            writer.writeheader()
            for row in data:

                line = dict(zip(header, row))
                writer.writerow(line)




if __name__ == '__main__':
    pre = CSVLoader(fullpath='./data/data.csv')
    #print(pre.get_header())
    #print(pre.get_cols(['Body', 'Weight']))

    pre.write(name='./data/train.csv', header=['A', 'B', 'C'], data=[[1,2,3], [4,5,6], [7,8,9 ]])


