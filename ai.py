import joblib # joblib library
knn = joblib.load('knn_digits') # import the model we trained

def ai(img) :
    y_pred = knn.predict(img.reshape(1,-1))
    y_pred = y_pred.astype('int')
    chiffre = y_pred[0]
    return chiffre