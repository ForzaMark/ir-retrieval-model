from tira.third_party_integrations import ir_datasets
import pyterrier as pt

def load_dataset():
    training_dataset = 'ir-lab-jena-leipzig-wise-2023/training-20231104-training'

    queries = pt.io.read_topics(ir_datasets.topics_file(training_dataset), format='trecxml')

    dataset = ir_datasets.load(training_dataset)
    documents = [{'docno': doc.doc_id, 'text': doc.text or ''} for doc in dataset.docs_iter()]
    return documents, queries
