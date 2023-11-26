import pyterrier as pt

def create_index(documents):
    indexer = pt.IterDictIndexer(
        "./tmp/index", 
        overwrite=True, 
        stopwords="./stopwordlists/stopwords_english_long.txt", 
        meta={'docno': 100, 'text': 20480},
        stemmer='porter'
    )
    index_ref = indexer.index(({'docno': i.doc_id, 'text': i.text} for i in documents))
    return pt.IndexFactory.of(index_ref)
