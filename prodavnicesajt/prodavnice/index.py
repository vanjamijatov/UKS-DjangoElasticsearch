from elasticsearch_dsl import Document, Float, analyzer, Keyword, Text

text_analyzer = analyzer('text_analyzer', tokenizer="standard", filter=["lowercase", "stop", "snowball"],
                         char_filter=["html_strip"])


class ArtikalDokument(Document):
    id = Text()
    naziv = Text(analyzer=text_analyzer, fields={'raw': Keyword()})
    opis = Text(analyzer=text_analyzer)
    cena = Float()
    prodavnica = Text(analyzer=text_analyzer)

    class Index:
        name = 'artikli'
        settings = {
            "number_of_shards": 5,
            "number_of_replicas": 0
        }
