import generation_data_set as gd
import evaluate_dataset as ed
import balance_ml as bml

if __name__ == '__main__':
    gd.generate()
    ed.evaluate()
    bml.train(50, 32)