import csv
import pandas as pd
import os

files_balance = ["1.csv", "2.csv", "Balancier.csv", "Balancier2.csv", "Balancier3.csv", "Balancier4.csv",
                 "Balancier5.csv", "Balancier6.csv", "Balancier7.csv"]
files_no_balance = ["1.csv", "Non_Balancier1.csv", "Non_Balancier2.csv", "Non_Balancier3.csv", "Non_Balancier4.csv",
                    "Non_Balancier6.csv"]

export_file = "data.csv"
if os.path.exists(export_file):
    os.remove(export_file)
nb_aquisition = 5
# en ms et multiple de 20
clean_time = 40

columns = ["AccX [mg]", "AccY [mg]", "AccZ [mg]"]


def generate_csv(file, _result):
    file_csv = pd.read_csv(file, usecols=columns)
    file_csv = file_csv[int(clean_time/20) : int(-clean_time/20)]

    test = [file_csv.shift(-i) for i in range(nb_aquisition)]
    data = pd.concat(test, axis=1).dropna()
    data = data.assign(result=_result)

    if os.path.exists(export_file):
        data.to_csv(export_file, mode='a', header=not os.path.exists(export_file))
    else:
        with open(export_file, 'w') as file:
            print("création fichier")
        data.to_csv(export_file, mode='a', header=True)


for file in files_no_balance:
    file = "data/noBalance/" + file
    generate_csv(file, 0)

for file in files_balance:
    file = "data/Balance/" + file
    generate_csv(file, 1)
