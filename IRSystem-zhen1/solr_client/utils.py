import pysolr

def add_solr(id, author_id, text):
    solr = pysolr.Solr('http://localhost:8983/solr/test2')

    # print(type(id))
    # print(type(author_id))
    # print(type(text))
    res = solr.add([
        {
            "id": id,
            "author_id": author_id,
            "text": text,
        }
    ])
    print(res)