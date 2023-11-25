import pandas as pd
from google.cloud import language_v1
from google.oauth2 import service_account

# Task 1: Read the file “productreviews.csv” into a data frame
reviews_df = pd.read_csv("/Users/brocktbennett/GitHub/Project Data/Data Science Programming Data/productreviews.csv", nrows=5000)

# Initialize a global counter for tracking progress
global_counter = 0

# Define a function to analyze the sentiment of a text
def analyze_text_sentiment(text):
    global global_counter
    global_counter += 1

    # Display the current progress
    print(f"Processing row {global_counter}/{len(reviews_df)}")

    # Load the key file
    creds = service_account.Credentials.from_service_account_file('/Users/brocktbennett/GitHub/MSIS-5193-Data-Science-Lab-Work/Module 11: Web Services for Data Analytics/03GoogleNLPAPI/my-msis-5193-projects-7e4b655258b4.json')
    client = language_v1.LanguageServiceClient(credentials=creds)

    # Convert the text into a document type
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Call function to analyze the sentiment of the text
    try:
        response = client.analyze_sentiment(document=document)
        sentiment = response.document_sentiment
        return sentiment.score, sentiment.magnitude
    except Exception as e:
        print(f"Error analyzing text: {e}")
        return None, None

# Filter out null or empty reviews
filtered_reviews = reviews_df[reviews_df['Review'].notnull() & (reviews_df['Review'] != '')]

# Analyze sentiment of filtered reviews
sentiment_results = filtered_reviews['Review'].apply(lambda x: analyze_text_sentiment(x) if x else (None, None))

# Split results into two columns and join back to the original DataFrame
reviews_df = reviews_df.join(pd.DataFrame(sentiment_results.tolist(), index=filtered_reviews.index, columns=['sentiment_score', 'sentiment_magnitude']))

# Task 3: Save the results into a new file
reviews_df.to_csv("/Users/brocktbennett/GitHub/MSIS-5193-Assignments/Assignment8/productreviewssentiment.csv", index=False)
