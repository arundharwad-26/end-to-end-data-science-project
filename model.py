import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df=pd.read_csv("C:\\Users\\arund\\Desktop\\internship\\Student Performance\\dataset.csv")

# Features and target
x=df[['hours','attendance','previous_score']]
y=df['result']

# Train test split
x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.2, random_state=42
)

#Train model
model = LogisticRegression()
model.fit(x_train,y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully")