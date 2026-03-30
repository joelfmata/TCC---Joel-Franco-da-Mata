import re

def normalizar_texto(texto):
    texto = str(texto).lower()

    substituicoes = {

        # principais
        "vsf": "vai se foder",
        "vsfd": "vai se foder",
        "vtnc": "vai tomar no cu",
        "tmnc": "toma no cu",
        "fdp": "filho da puta",
        "pqp": "puta que pariu",
        "krl": "caralho",
        "crl": "caralho",
        "fds": "foda se",
        "foda-se": "foda se",
        "foda se": "foda se",

        # variações
        "f0da": "foda",
        "f*d": "foda",
        "fda": "foda",
        "p0rra": "porra",
        "prr": "porra",
        "mrd": "merda",
        "merd": "merda",
        "m3rda": "merda",
        "bct": "buceta",
        "buc": "buceta",

        # números
        "l1xo": "lixo",
        "lix0": "lixo",
        "l1x0": "lixo",
        "b0sta": "bosta",
        "bost4": "bosta",

        # xingamentos
        "ot4rio": "otario",
        "idi0ta": "idiota",
        "imb3cil": "imbecil",
        "noj3nto": "nojento",
        "v4gabundo": "vagabundo",

        # censura
        "c*": "cu",
        "p*ta": "puta",
        "m*rda": "merda",
        "p*rra": "porra",
        "c*ralho": "caralho"
    }

    for k, v in substituicoes.items():
        texto = texto.replace(k, v)

    # remover caracteres estranhos
    texto = re.sub(r"[^a-zA-Zà-úÀ-Ú0-9\s]", "", texto)

    # remover espaços duplicados
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()