# Mini Search Engine 
This code implements a simple search engine that can index documents, normalize search queries and document text, expand search queries to include synonyms, and return the most relevant search results. It utilizes several NLP techniques like tokenization, stemming, and synonym finding to facilitate robust text search.

In my code, I used the cnbc_news_datase.csv dataset which I attached in this repository for your reference. But any dataset with the same or similar column name types would suffice. If not, then preprocessing of dataset would be best before proceeding. 

## Basic Overview of the Code
The SearchEngine class is the main component, handling indexing documents, normalizing text, and ranking search results. 

The normalize() method tokenizes text, converts it to lowercase, stems words to their root form, and returns a cleaned token list. 

The search() method takes a search query, normalizes it, compares it against normalized document text to find matches, ranks matching documents by match count, and returns the top n results. 

Additional functionality includes the QueryExpander to automatically find and add synonyms to search queries to improve results. Overall, it provides a simple yet effective search engine that demonstrates several key information retrieval techniques. T

he main() function ties it together by loading documents, getting user input search queries, expanding them, running searches, and displaying results.
