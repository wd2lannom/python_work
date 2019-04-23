## this the second script used to extract and view text inside a pdf
## this script takes the extracted text and puts it in an index for Elasticsearch to use

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(['localhost:9200'])

screened_file = "/Users/dave/python_work/file.txt"

docs = pdf2txt(screened_file)

index = "screened_file"

##good practice to delete an index if it already exists and you're overwriting
if es.indices.exists(index):
    es.indices.delete(index)

## elastic helper function to bulk index json
bulk(es, docs, index=index, doc_type='clue', raise_on_error=True)