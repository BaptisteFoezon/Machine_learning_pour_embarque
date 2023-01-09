import csv
import pandas as pd
import os

files_balance = ["1.csv", "2.csv"]
files_no_balance = ["1.csv"]

export_file = "data.csv"
nb_aquisition = 5
# en ms et multiple de 20
clean_time = 40


def generate_csv(file, _result):
    file_csv = pd.read_csv(file)
    # file_csv = file_csv[int(clean_time/20) : int(-clean_time/20)]
    ax = file_csv["AccX [mg]"][int(clean_time / 20): int(-clean_time / 20)]
    ax_c = pd.concat([ax.shift(-i) for i in range(nb_aquisition)], axis=1).dropna()
    ay = file_csv["AccY [mg]"][int(clean_time / 20): int(-clean_time / 20)]
    ay_c = pd.concat([ay.shift(-i) for i in range(nb_aquisition)], axis=1).dropna()
    az = file_csv["AccZ [mg]"][int(clean_time / 20): int(-clean_time / 20)]
    az_c = pd.concat([az.shift(-i) for i in range(nb_aquisition)], axis=1).dropna()
    result = pd.concat([ax_c, ay_c, az_c], axis=1)
    print(result)
    result = result.assign(result=_result)
    if os.path.exists(export_file) == True:
        result.to_csv(export_file, mode='a', header=not os.path.exists(export_file))
    else:
        with open(export_file, 'w') as file:
            print("création fichier")
        result.to_csv(export_file, mode='a', header=True)


for file in files_no_balance:
    file = "data/noBalance/" + file
    generate_csv(file, 0)

for file in files_balance:
    file = "data/Balance/" + file
    generate_csv(file, 1)


nb_balance = 0;
nb_no_balance = 0.
with open('data.csv', 'r') as f:
