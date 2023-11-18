import pyterrier as pt
from load_dataset import load_dataset 

if not pt.started():
    pt.init()
custom_stopwordlist = pt.set_property("stopwords.filename", "/stopwordlists/stopwords_english_long.txt.txt")
documents, queries = load_dataset()


def create_index(documents):
    indexer = pt.IterDictIndexer("/output", stopwords=custom_stopwordlist, terrier='terrier', overwrite=True, meta={'docno': 100, 'text': 20480})
    index_ref = indexer.index(documents)
    return pt.IndexFactory.of(index_ref)
  

# we create a new index
index = create_index(documents)
bm25 = pt.BatchRetrieve(index, wmodel="BM25")