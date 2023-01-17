import generation_data_set as gd
import evaluate_dataset as ed
import balance_ml as bml

if __name__ == '__main__':
    nb_aquisition = 5
    # en ms et multiple de 20
    clean_time = 40
    gd.generate(nb_aquisition, clean_time)
    ed.evaluate()
    bml.train(50, 32)