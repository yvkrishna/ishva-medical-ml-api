from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

def main():
	filename = 'hazard_model.pkl'
	clf2 = joblib.load(filename)
	result = clf2.predict_proba([[ 1.58290900e-01,  1.00000000e+00,  3.80318174e-02,  0.00000000e+00,
        2.26033858e-01,  0.00000000e+00,  1.76395977e+00, -5.51188485e-01,
        9.43496482e-02,  1.00000000e+00,  1.00000000e+00,  1.23000000e+02]])
	result = [[round(result[0][0],6), round(result[0][1],6)]]
	outcome = '{"predictions_1":'+str(result[0][0])+',"predictions_2":'+str(result[0][1])+'}'
	print(outcome)

if __name__ == '__main__':
	main()