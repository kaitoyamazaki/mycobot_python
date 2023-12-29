import csv
import pandas as pd
import numpy as np

class CsvOutput:

    def __init__(self):
        
        self.file_path = "../data/theta_data.csv"
        self.df = pd.read_csv(self.file_path, header=None)
        self.data = self.df.values

    def output(self):
        data = self.data
        for i in range(len(data)):
            print(f"{i}回目 : {data[i]}")
            now_data = data[i]
            print(f"type is {type(now_data)}")
            print(f"配列をそれぞれ別に出力")
            print(f"j2 : {now_data[0]}, j3 : {now_data[1]}, j4 : {now_data[2]}")



def main():

    try:
        csv = CsvOutput()
        csv.output()
    
    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")



if __name__ == "__main__":
    
    try:
        main()

    except KeyboardInterrupt:
        print(f"Ctrl-Cによる終了")