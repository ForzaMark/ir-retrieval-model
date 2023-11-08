
from trectools import TrecRun, TrecQrel, TrecEval
from tira.rest_api_client import Client
from glob import glob
import pandas as pd
tira = Client()


def load_qrels(dataset):
    return TrecQrel(tira.download_dataset('ir-lab-jena-leipzig-wise-2023', dataset, truth_dataset=True) + '/qrels.txt')

def evaluate_run(qrels):
    run = TrecRun('./run.txt')
    trec_eval = TrecEval(run, qrels)

    return {
        'run': run.get_runid(),
        'nDCG@10': trec_eval.get_ndcg(depth=10),
        'nDCG@10 (unjudgedRemoved)': trec_eval.get_ndcg(depth=10, removeUnjudged=True),
        'MAP': trec_eval.get_map(depth=10),
        'MRR': trec_eval.get_reciprocal_rank()
    }

def test_model(model):
    training_qrels = load_qrels('training-20231104-training')

    print("Overall performance:\n")
    print(evaluate_run(training_qrels))
    print("\n")

    print("Single word search:\n")
    print(model.search("cardiovascular disease"))
    print("\n")