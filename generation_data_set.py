import csv
import pandas as pd
import os


def create_result_file(name):
    if os.path.exists(name):
        os.remove(name)
def generate_csv(file, _result, output_file):
    columns = ["AccX [mg]", "AccY [mg]", "AccZ [mg]"]
    file_csv = pd.read_csv(file, usecols=columns)
    file_csv = file_csv[int(clean_time/20) : int(-clean_time/20)]

    test = [file_csv.shift(-i) for i in range(nb_aquisition)]
    data = pd.concat(test, axis=1).dropna()
    data = data.assign(result=_result)

    if os.path.exists(output_file):
        data.to_csv(output_file, mode='a', header=not os.path.exists(output_file))
    else:
        with open(output_file, 'w') as file:
            print("création fichier")
        data.to_csv(output_file, mode='a', header=True)


def generate():
    output_file = "data.csv"
    create_result_file(output_file);
    files_no_balance = os.listdir("data/noBalance/")
    for file in files_no_balance:
        generate_csv("data/noBalance/"+file, 0, output_file)
    files_balance = os.listdir("data/Balance/")
    for file in files_balance:
        generate_csv("data/Balance/"+file, 1, output_file)

if __name__ == '__main__':
    nb_aquisition = 5
    # en ms et multiple de 20
    clean_time = 40
    generate()