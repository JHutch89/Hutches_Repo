import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv('replen_exit_questions.csv')  # Adjust sheet_name if necessary

topic_models = {}
topic_counts = {}

## Function to extract topics from Latent Dirichlet model
def extract_topics(model, feature_names, n_top_words):
    topics = {}
    for topic_idx, topic in enumerate(model.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
        topics[f'Topic {topic_idx}'] = top_words
    return topics

## Analyzing topics for each question in survey
for column in df.columns:
    if df[column].dtype == object:  ## Check to see if column contains text/data
        clean_column_name = column.replace(' ', '_').replace(':', '').replace('/', '_').replace('?', '')
        vectorizer = CountVectorizer(ngram_range=(3, 3), stop_words='english')  # Using trigrams
        X = vectorizer.fit_transform(df[column].dropna())
       
        lda = LatentDirichletAllocation(n_components=2, random_state=42)
        lda.fit(X)
       
        ## Extract topics
        feature_names = vectorizer.get_feature_names_out()
        topics = extract_topics(lda, feature_names, 7)
        topic_models[clean_column_name] = topics

        ## Assign topics to responses
        topic_assignments = lda.transform(X).argmax(axis=1)
        topic_df = pd.DataFrame(topic_assignments, columns=[clean_column_name + '_Topic'])
        topic_df = topic_df.set_index(df[column].dropna().index)
        df = df.join(topic_df, how='left')

        ## Count the number of responses for each topic
        topic_count = topic_df[clean_column_name + '_Topic'].value_counts().sort_index()
        topic_counts[clean_column_name] = topic_count

## Saving results to file path/csv
output_path_topics = '/mnt/data/topic_modeling_by_column_results.csv'
df.to_csv(output_path_topics, index=False)

## Saving topic counts to file path/csv
output_path_topic_counts = '/mnt/data/topic_counts_by_column_results.csv'
topic_counts_df = pd.DataFrame(topic_counts)
topic_counts_df.to_csv(output_path_topic_counts, index=True)

## Print out results
for column, topics in topic_models.items():
    print(f"Topics for {column.replace('_', ' ')}:")
    for topic, words in topics.items():
        print(f"  {topic}: {', '.join(words)}")
    print()

## Print out topic counts
for column, counts in topic_counts.items():
    print(f"Topic counts for {column.replace('_', ' ')}:")
    print(counts)
    print()
