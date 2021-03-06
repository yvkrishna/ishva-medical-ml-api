from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

def main():
	filename = 'risk_model.pkl'
	clf2 = joblib.load(filename)
	result = clf2.predict_proba(np.array([[40, 0, 2, 140, 289, 0, 2, 172, 0, 0.0, 1]]))
	result = [[round(result[0][0],6), round(result[0][1],6)]]
	outcome = '{"predictions_1":'+str(result[0][0])+',"predictions_2":'+str(result[0][1])+'}'
	print(outcome)

if __name__ == '__main__':
	main()