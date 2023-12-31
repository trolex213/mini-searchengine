# Mini Search Engine

!pip install pyspellchecker

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import wordnet
from spellchecker import SpellChecker
from collections import defaultdict
import pandas as pd

class SearchEngine():
  def __init__(self):
    # constructor
    self.documents = {} # key is index of document, value is the actual words of the document


  def add_document(self, index, content):
    self.documents[index] = content


  def load_documents(self, csv_file="cnbc_news_datase.csv"):

    docs_df = pd.read_csv(csv_file)

    for index, row in docs_df.iterrows():

      # Combine title + description as doc text
      doc_text = str(row['title']) + ' ' + str(row['description'])

      # Use url as doc id
      doc_id = str(row['url'])
      self.add_document(doc_id, doc_text)


  def normalize(self, document):
    # tokenize the word
    document = document.lower()
    tokens = word_tokenize(document) # list of strings

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    # stemmer.stem takes the tokens into its root form (i.e. jumping -> jump, dogs -> dog)

    return stemmed_tokens


  def search(self, query, numresults=3):
      query_words = self.normalize(query)
      matching_docs = defaultdict(int)
      for index, content in self.documents.items():
        doc_words = self.normalize(content)
        for word in query_words:
          if word in doc_words:
            matching_docs[index] += 1

      sorted_docs = sorted(matching_docs.items(), key=lambda pair: pair[1], reverse=True)

      sorted_docs = sorted_docs[:numresults]
      sorted_docs = [item1 for item1, item2 in sorted_docs]
      return sorted_docs

# Takes in a query, gives us terms that are synonyms to the query automatically without manually having to specify alternative words to the query.
class QueryExpander():
  def __init__(self):
    pass

  def get_syn(self, term):
    # find synonym for term
    synonyms = set()
    wordNetsynonyms = wordnet.synsets(term)
    for s in wordNetsynonyms:
      for lemma in s.lemmas():
        synonyms.add(lemma.name())

    return list(synonyms)

  def query_expand(self, query):
    query_terms = self.normalize(query)
    expanded_terms = []
    for term in query_terms:
      synonyms = self.get_syn(term)
      expanded_terms.extend(synonyms) #.extend merges two lists into one list
    return " ".join(expanded_terms)


  def normalize(self, query):
    query = query.lower()
    tokens = word_tokenize(query) # list of strings

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
  # stemmer.stem takes the tokens into its root form (i.e. jumping -> jump, dogs -> dog)

    return stemmed_tokens

def main():
  searchengine = SearchEngine()
  searchengine.load_documents()

  queryexpand = QueryExpander()
  while True:
    userinput = input("Enter your query: ")
    if userinput.lower() == "exit":
      break
    expandedQuery = queryexpand.query_expand(userinput)
    results = searchengine.search(expandedQuery)
    print(" ")
    print("expandedQuery: ", expandedQuery)
    if results:
      for i, result in enumerate(results, 1):
        print(result)
    else:
      print("No match found.")


if __name__ == "__main__":
  main()

search = SearchEngine()



