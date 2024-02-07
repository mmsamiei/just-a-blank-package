class DummyClassifier():

    def __init__(self):
        pass

    def predict(self, text):
        if 'a' in text:
            return 'A'
        elif 'b' in text:
            return 'B'
        else:
            return 'C'
