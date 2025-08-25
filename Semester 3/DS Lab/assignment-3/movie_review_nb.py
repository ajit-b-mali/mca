import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Download a sample movie review dataset (using NLTK's movie_reviews if available)
try:
    import nltk
    nltk.download('movie_reviews')
    from nltk.corpus import movie_reviews
    docs = [(movie_reviews.raw(fileid), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
    df = pd.DataFrame(docs, columns=['review', 'sentiment'])
except Exception:
    # Fallback: use a small hardcoded dataset
    data = {
        'review': [
            'I loved this movie, it was fantastic!',
            'Terrible film. Waste of time.',
            'Absolutely wonderful! A must watch.',
            'Not good. The plot was boring.',
            'Great acting and story.',
            'Awful. I hated every minute.',
            'Best movie ever!',
            'Worst movie I have seen.',
        ],
        'sentiment': [
            'pos', 'neg', 'pos', 'neg', 'pos', 'neg', 'pos', 'neg'
        ]
    }
    df = pd.DataFrame(data)

# Encode sentiment labels
label_map = {'pos': 1, 'neg': 0}
df['label'] = df['sentiment'].map(label_map)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['review'], df['label'], test_size=0.2, random_state=42, stratify=df['label']
)

# Vectorize text
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

# Predict
y_pred = clf.predict(X_test_vec)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=['Negative', 'Positive'])

print('--- Sentiment Analysis with Naive Bayes ---')
print(f'Accuracy: {accuracy:.4f}')
print('\n--- Classification Report ---')
print(report)
