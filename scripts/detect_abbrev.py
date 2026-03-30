import pandas as pd

# LISTA MASSIVA DE ABREVIAÇÕES / OBFSUCAÇÕES
abrev = [

# --- clássicas ---
"vsf","vsfd","vsfdd","vsfff","vtnc","tmnc","fdp","fdps","fdpz","fdpzao",
"pqp","ppqp","krl","crl","karai","carai","karalho","caralho","caralh0","c4ralh0",
"fds","fdc","foda","fods","f0da","f*d","fda","f0d4","fodase","foda-se","f*dase",
"bct","buc","b*ceta","bct4","buc3t4","bctinha",
"pnc","pnd","pncu","pn0","p4u","pau","p4uno","p4u n0 c",
"lixo","l1xo","lix0","l1x0","lixx0","lixao","lixoso",
"merda","mrd","merd","merd4","m3rd4","m*rda","merdao",
"porra","prr","porr","p0rr4","p*rra","porr4",
"cacete","kct","kctt","cct","cac3t3","caceteee",

# --- xingamentos ---
"arrombado","arromb4do","arrombad0","arromb@do","arrombada","arrombados",
"otario","ot4rio","otari0","ot@rio","otarios",
"idiota","idi0ta","1di0ta","idiot4",
"imbecil","imb3cil","imbecilzao",
"burro","burr0","burr00","burrao","burra",
"retardado","retard4do","retardad0","retardada",
"nojento","noj3nto","nojent0","nojentao",
"vagabundo","v4gabundo","vagabund0","vagabunda",
"corno","c0rno","corn0","corninho",
"escroto","3scroto","escrot0",

# --- ódio direcionado ---
"viado","viad0","vi4do","v1ad0",
"gay lixo","lgbt lixo",
"macaco","m4caco",
"nazista","n4z1sta",
"racista","r4cista",

# --- morte / agressão ---
"vxm","se mata","se m4ta","s m4t4",
"vai morrer","vai morr3r","vai morre",
"tomara que morra","tmq morra",

# --- frases ofensivas ---
"vai se foder","vai s foder","vai s f0der",
"vai tomar no cu","vai toma no cu","vai toma n c",
"vai pra puta que pariu","vppqp",
"filho da puta","filh0 d4 put4","f d p",
"pau no cu","pncu","pnc",
"vai tomar no meio do cu","vtnmdc",

# --- formas com censura ---
"c*","cu","cú","cuz4o","cuzão","cuzao",
"p*ta","put4","puta",
"m*rda","m3rda",
"p*rra","porr4",
"c*ralho","c4ralh0",

# --- variações com números ---
"f0d4","f0dido","fod1do",
"l1x0","lix0",
"v4g4bundo",
"b0sta","bost4",
"p0rra",
"c4cete",

# --- repetições ---
"kkkk lixo","kkkkk lixo","kkkkkk lixo",
"burroooo","idiotaaaa","lixoooo",

# --- combos ---
"fdp do krl","fdp krl","fdp do caralho",
"otario do krl","burro do krl","idiota do krl",
"seu lixo","seu l1xo",
"seu merda","seu mrd",
"seu idiota","seu 1di0ta",
"seu burro","seu burr0",
"seu otario","seu ot4rio",
"seu imbecil","seu imb3cil",
"seu arrombado","seu arromb4do",
"seu nojento","seu noj3nto",
"seu retardado","seu retard4do",

# --- mais variações ---
"bosta","b0sta","bost4","bostao",
"desgraça","desgraca","dsgraça","d3sgr4ca",
"inferno","inf3rno","infern0",
"maldito","m4ldito","maldit0",
"fdc","fodac","fds",
"vai se ferrar","vsferrar",
"vai pro inferno","vpi",

# --- extras pesados ---
"escoria","esc0ria",
"verme","v3rme",
"lixo humano","l1xo humano",
"animal","4nimal",
"doente","d0ente",
"psicopata","ps1copata",
"fdp lixo","fdp lixo humano",
"arrombado lixo","burro lixo"
]

df = pd.read_csv("data/processed/youtube_clean.csv")

def tem_abreviacao(texto):
    texto = str(texto)
    for a in abrev:
        if a in texto:
            return 1
    return 0

df["has_abbrev"] = df["text"].apply(tem_abreviacao)

df.to_csv("data/processed/youtube_abbrev.csv", index=False)

print("Abreviações detectadas (VERSÃO ULTRA COMPLETA)!")