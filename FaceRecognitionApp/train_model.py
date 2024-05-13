# Random Forest
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

print("[INFO] loading face embeddings...")
data = pickle.loads(open('output/embeddings.pickle', "rb").read())

print("[INFO] encoding labels...")
le = LabelEncoder()
labels = le.fit_transform(data["names"])

print("[INFO] training model...")

recognizer = RandomForestClassifier(n_estimators=100, random_state=42)
recognizer.fit(data["embeddings"], labels)

with open('output/recognizer.pickle', "wb") as f:
    pickle.dump(recognizer, f)

# write the label encoder to disk
with open('output/le.pickle', "wb") as f:
    pickle.dump(le, f)



# # import the necessary packages
# from sklearn.preprocessing import LabelEncoder
# from sklearn.svm import SVC
# import pickle

# # load the face embeddings
# print("[INFO] loading face embeddings...")
# data = pickle.loads(open('output/embeddings.pickle', "rb").read())
# # encode the labels
# print("[INFO] encoding labels...")
# le = LabelEncoder()
# labels = le.fit_transform(data["names"])

# # train the model used to accept the 128-d embeddings of the face and
# # then produce the actual face recognition
# print("[INFO] training model...")
# recognizer = SVC(C=2.0, kernel="linear", tol=0.0001, decision_function_shape='ovo', probability=True)
# recognizer.fit(data["embeddings"], labels)

# # write the actual face recognition model to disk
# f = open('output/recognizer.pickle', "wb")
# f.write(pickle.dumps(recognizer))
# f.close()
# # write the label encoder to disk
# f = open('output/le.pickle', "wb")
# f.write(pickle.dumps(le))
# f.close()
