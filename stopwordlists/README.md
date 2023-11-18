To use a custom stopwordlist while indexing, follow these steps:
    	1. Copy the stopwordlists-folder to your project
        2. add the stopwordlist pt.property to your file
       
            custom_stopwordlist = pt.set_property("stopwords.filename", "/stopwordlists/stopwords_english_long.txt")
            documents, queries = load_dataset()


        3. Adjust the indexer of your project like this:

              indexer = pt.IterDictIndexer("./output", stopwords=custom_stopwordlist, terrier='terrier', overwrite=True, meta={'docno': 100, 'text': 20480}) 

        Just the part "stopwords=custom_stopwordlist" is relevant for the use of a custom stopwordlist, otherwise pyterrier is going to use a default list.
    
In general make sure to adjust the paths contained to your needs.


        