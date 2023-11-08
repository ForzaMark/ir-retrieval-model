from tira.third_party_integrations import ensure_pyterrier_is_loaded, persist_and_normalize_run
import pyterrier as pt

from load_dataset import load_dataset 
from create_index import create_index
from create_model import create_model
from test_model import test_model


if not pt.started():
    pt.init()

ensure_pyterrier_is_loaded()

# load data
load_dataset_result = load_dataset()
documents, queries = load_dataset_result['documents'], load_dataset_result['queries']
print("data load")

# create index
index = create_index(documents)
print("index created")

# create model
model = create_model(index)
print("model created")

# run model
run = model(queries)
persist_and_normalize_run(run, "initial_retrieval_system", "./")
print("model executed against queries")

# test model
test_model(model)
