# Assignment 3: Sentiment Analysis using Naive Bayes

from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

# Download sample movie review dataset
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews

# Prepare data
# Prepare data (simplified)
docs = []
labels = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        docs.append(movie_reviews.raw(fileid))
        labels.append(1 if category == 'pos' else 0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(docs, labels, test_size=0.2, random_state=42)

# Convert text to numeric form
vectorizer = CountVectorizer(stop_words='english', max_features=2000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap="Blues", fmt='d')
plt.title("Confusion Matrix - Naive Bayes Sentiment Analysis")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
