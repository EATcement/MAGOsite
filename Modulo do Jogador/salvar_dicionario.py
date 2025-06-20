# salvar_dicionario.py
import pickle

# Seu dicionário original
dicionarios = {
    "1": {"nome": "João Silva", "idade": 30, "habilidades": ["Python", "SQL"]},
    "2": {"nome": "Maria Oliveira", "idade": 28, "habilidades": ["Java", "C++"]},
    "3": {"nome": "Pedro Santos", "idade": 35, "habilidades": ["JavaScript", "HTML", "CSS"]}
}

# Salvar em arquivo .pkl
with open("dicionarios.pkl", "wb") as f:
    pickle.dump(dicionarios, f)

print("Arquivo dicionarios.pkl salvo com sucesso.")
