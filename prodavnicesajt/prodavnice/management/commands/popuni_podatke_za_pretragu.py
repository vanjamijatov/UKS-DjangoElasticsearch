from django.core.management.base import BaseCommand
from elasticsearch_dsl.connections import connections

from ...index import ArtikalDokument
from ...models import Artikal


class Command(BaseCommand):
    # args = '<args1 args2>'
    help = 'Komanda za preuzimanje relevantnih podataka od artiklima i slanje Elasticsearch paltformi'

    def _unesi_podatke(self):
        artikli = Artikal.objects.all()
        for artikal in artikli:
            ArtikalDokument(meta={'id': str(artikal.id)}, id=str(artikal.id), naziv=artikal.naziv, opis=artikal.opis,
                            cena=artikal.cena, prodavnica=artikal.prodavnica.naziv).save()

    def handle(self, *args, **options):
        connections.create_connection(hosts=['localhost'], timeout=60)
        ArtikalDokument.init()
        self._unesi_podatke()
