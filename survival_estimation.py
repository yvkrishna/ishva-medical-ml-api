import lifelines
import numpy as np
import joblib
import pickle

def main():
    with open('survival_model.pkl', 'rb') as inp:
        survival_model = pickle.load(inp)
        result = round(survival_model.survival_function_at_times(100).values[0],6)
        outcome = '{"prediction":' + str(result) + '}'
        print(outcome)


if __name__ == '__main__':
	main()