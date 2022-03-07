from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

def main():
	filename = 'risk_model.pkl'
	clf2 = joblib.load(filename)
	result = clf2.predict_proba(np.array([[40, 0, 2, 140, 289, 0, 2, 172, 0, 0.0, 1]]))
	print(result)

if __name__ == '__main__':
	main()