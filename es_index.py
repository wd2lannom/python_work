from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(['localhost:9200'])

docs = pdf2txt(pdf_path)

index = "mueller-report"

##good practice to delete an index if it already exists and you're overwriting
if es.indices.exists(index):
    es.indices.delete(index)

## elastic helper function to bulk index json
bulk(es, docs, index=index, doc_type='clue', raise_on_error=True)