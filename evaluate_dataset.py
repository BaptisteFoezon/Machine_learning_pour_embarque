import pandas as pd



def evaluate():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data.csv')

    count_bal = df[df['result'] == 1].shape[0]
    count_no_bal = df[df['result'] == 0].shape[0]

    print(f'Nombre de balancier: {count_bal}   {(count_bal/(count_bal + count_no_bal))*100}% ')
    print(f'Nombre de non balancier: {count_no_bal}   {(count_no_bal/(count_bal + count_no_bal))*100}%')


if __name__ == '__main__':
    evaluate()