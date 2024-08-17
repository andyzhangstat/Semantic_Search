import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import sys
import os
from dotenv import find_dotenv
from dotenv import load_dotenv

sys.path.append('../..')
_ = load_dotenv(find_dotenv()) # read local .env file

host_name = os.environ['HOST_NAME']
api_key = os.environ['API_KEY']



indexName = "all_news"


try:
    es = Elasticsearch(hosts=host_name, api_key=api_key)


except ConnectionError as e:
    print("Connection Error:", e)
    
if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")




def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
        "field": "TitleVector",
        "query_vector": vector_of_input_keyword,
        "k": 5,
        "num_candidates": 500
    }
    res = es.knn_search(index="all_news"
                        , knn=query 
                        , source=["Title","Abstract"]
                        )
    results = res["hits"]["hits"]

    return results


def main():
    # Set page config
    st.set_page_config(page_title="Microsoft News Search", layout="wide")

    # Define custom CSS styles for blue and red color scheme with smaller fonts and tighter layout
    st.markdown(
        """
        <style>
        .main-header {
            color: white;
            background-color: #1E90FF;
            padding: 8px;
            text-align: center;
            border-radius: 8px;
            font-size: 24px;  /* Smaller title font size */
        }
        .search-input input {
            border: 1px solid #FF4500;
            padding: 8px;
            border-radius: 4px;
            font-size: 14px;
            width: 100%;
        }
        .search-button button {
            background-color: #FF4500;
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            border: none;
            font-size: 14px;
            cursor: pointer;
        }
        .search-results h2 {
            color: #1E90FF;
            font-size: 18px;  /* Smaller result title font size */
            margin-bottom: 5px;
        }
        .search-results .description {
            color: #FF4500;
            font-size: 12px;  /* Smaller description font size */
            margin-bottom: 5px;
        }
        .divider {
            height: 1px;
            background-color: #1E90FF;
            margin: 8px 0;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Main title
    st.markdown('<div class="main-header"><h1>Search Microsoft News</h1></div>', unsafe_allow_html=True)

    # Input: User enters search query
    search_query = st.text_input("Enter your search query", key="search_input", placeholder="Search for news articles...")

    # Button: User triggers the search
    if st.button("Search", key="search_button"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)

            # Display search results
            st.markdown('<div class="search-results"><h2>Search Results</h2></div>', unsafe_allow_html=True)
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.markdown(f'<h2>{result["_source"]["Title"]}</h2>', unsafe_allow_html=True)
                        except Exception as e:
                            st.error(e)
                        
                        try:
                            st.markdown(f'<p class="description">Abstract: {result["_source"]["Abstract"]}</p>', unsafe_allow_html=True)
                        except Exception as e:
                            st.error(e)
                        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)




if __name__ == "__main__":
    main()
