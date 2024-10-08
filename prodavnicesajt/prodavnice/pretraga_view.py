from django.apps.registry import apps
from django.shortcuts import render
from elasticsearch_dsl import Search, Q

from prodavnice.index import ArtikalDokument


def pretraga_artikala(request):
    title = apps.get_app_config('prodavnice').verbose_name
    return render(request, "pretraga_artikala.html", {"title": title})


def pretraga_naziv(request):
    title = apps.get_app_config('prodavnice').verbose_name
    naziv = request.POST["naziv"]
    must = [Q("match", **{"naziv": naziv})]
    query = Q('bool', must=must)
    highlight = ["naziv"]
    error = None
    try:
        result = __izvrsi_pretragu(query, highlight)
    except Exception as e:
        result = None
        error = f"Neuspesna pretraga: {str(e)}"
    return render(request, "pretraga_artikala.html", {"title": title, "rezultat": result,
                                                      "greska_pretraga_naziv": error})


def pretraga_opis_fraza(request):
    title = apps.get_app_config('prodavnice').verbose_name
    opis = request.POST["opis"]
    must = [Q("match_phrase", **{"opis": opis})]
    query = Q('bool', must=must)
    highlight = ["opis"]
    error = None
    try:
        result = __izvrsi_pretragu(query, highlight)
    except Exception as e:
        result = None
        error = f"Neuspesna pretraga: {str(e)}"
    return render(request, "pretraga_artikala.html", {"title": title, "rezultat": result,
                                                      "greska_pretraga_opis_fraza": error})


def pretraga_naziv_i_opis(request):
    title = apps.get_app_config('prodavnice').verbose_name
    naziv = request.POST["naziv"]
    opis = request.POST["opis"]
    must = [Q("match", **{"naziv": naziv}), Q("match", **{"opis": opis})]
    query = Q('bool', must=must)
    error = None
    highlight = ["naziv", "opis"]
    try:
        result = __izvrsi_pretragu(query, highlight)
    except Exception as e:
        result = None
        error = f"Neuspesna pretraga: {str(e)}"
    return render(request, "pretraga_artikala.html", {"title": title, "rezultat": result,
                                                      "greska_pretraga_naziv_i_opis": error})


def pretraga_naziv_ili_opis(request):
    title = apps.get_app_config('prodavnice').verbose_name
    naziv = request.POST["naziv"]
    opis = request.POST["opis"]
    should = [Q("match", **{"naziv": naziv}), Q("match", **{"opis": opis})]
    query = Q('bool', should=should)
    error = None
    highlight = ["naziv", "opis"]
    try:
        result = __izvrsi_pretragu(query, highlight)
    except Exception as e:
        result = None
        error = f"Neuspesna pretraga: {str(e)}"
    return render(request, "pretraga_artikala.html", {"title": title, "rezultat": result,
                                                      "greska_pretraga_naziv_ili_opis": error})


def pretraga_cena(request):
    title = apps.get_app_config('prodavnice').verbose_name
    cena_od = request.POST["cena_od"]
    cena_do = request.POST["cena_do"]
    filter = [Q("range", **{"cena": {'gt': cena_od, 'lte': cena_do}})]
    query = Q('bool', filter=filter)
    error = None
    highlight = ["cena"]
    try:
        result = __izvrsi_pretragu(query, highlight)
    except Exception as e:
        result = None
        error = f"Neuspesna pretraga: {str(e)}"
    return render(request, "pretraga_artikala.html", {"title": title, "rezultat": result,
                                                      "greska_pretraga_cena": error})


def pretraga_prodavnica(request):
    title = apps.get_app_config('prodavnice').verbose_name
    prodavnica = request.POST["prodavnica"]
    must = [Q("match", **{"prodavnica": prodavnica})]
    query = Q('bool', must=must)
    highlight = ["prodavnica"]
    error = None
    try:
        result = __izvrsi_pretragu(query, highlight)
    except Exception as e:
        result = None
        error = f"Neuspesna pretraga: {str(e)}"
    return render(request, "pretraga_artikala.html", {"title": title, "rezultat": result,
                                                      "greska_pretraga_prodavnica": error})


def __izvrsi_pretragu(query, highlight):
    search_request = Search(using='default', index=ArtikalDokument.Index.name)
    retrieved_fields = ['id', 'naziv', 'opis', 'cena', 'prodavnica']
    search_request = search_request.query(query).source(fields=retrieved_fields)
    search_request = search_request.highlight_options(order='score')
    for item in highlight:
        search_request = search_request.highlight(item)
    if search_request is None:
        raise Exception('Nevalidan upit')
    search_request = search_request[0:10]
    data = search_request.execute()

    results = []
    if 'hits' in data:
        if 'hits' in data['hits']:
            for hit in data:
                highlight = __generisanje_istaknutog_sadrzaja(hit)
                results.append({'id': hit['id'], 'naziv': hit['naziv'], 'opis': hit['opis'], 'cena': hit['cena'],
                                'prodavnica': hit['prodavnica'], 'izvor': highlight})
    return results


def __generisanje_istaknutog_sadrzaja(hit):
    highlight = []
    if hasattr(hit.meta, 'highlight'):
        for attr, val in hit.meta.highlight.__dict__.items():
            for key, value in val.items():
                highlight_value = f"<b>{key}</b>: "
                for i in value:
                    highlight_value += str(i) + ';'
                highlight.append(highlight_value)
    else:
        return "Nema istaknutog sadrzaja"

    return "<br/>".join(highlight)
