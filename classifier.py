import joblib
# from sklearn.datasets import fetch_20newsgroups


class Classifier(object):
    def __init__(self):
        self.vectorizer = joblib.load("vectorizer_check_surname.pkl")
        self.model = joblib.load("model_check_surname.pkl")
        # self.target_names = fetch_20newsgroups(subset = 'test').target_names
    
    # def get_name_by_label(self, label):
    #     try:
    #         return self.target_names[label]
    #     except:
    #         return "label error"

    def predict_text(self, text):
        try:
            vectorized = self.vectorizer.transform([text])
            return self.model.predict_proba(vectorized)[0] 
        except:
            print("prediction error")
            return None 

    def get_result_message(self, text):
        prediction = self.predict_text(text)
        # return self.get_name_by_label(prediction)
        #return str(prediction)
        if prediction > 0.11:
            return "Это фамилия"
        else:
            return "Это не фамилия"
        
