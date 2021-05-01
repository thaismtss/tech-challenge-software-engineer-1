import pandas as pd
import json

people_df = pd.read_csv("people_data.csv")


def youngers(n):
    df = people_df.sort_values("data_nasc", ascending=False)
    result = df.head(n).to_json(orient="table")
    parsed = json.loads(result)
    return parsed.get("data")


def olders(n):
    df = people_df.sort_values("data_nasc", ascending=True)
    result = df.head(n).to_json(orient="table")
    parsed = json.loads(result)
    return parsed.get("data")


def gender_distribution():
    df = people_df["sexo"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
    return dict(df)


def get_people(cpf_without_pountuation):
    cpf = str(cpf_without_pountuation).zfill(11)
    cpf_formated = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    people_df["cpf"].apply(str)
    result = people_df.query(f"cpf == '{cpf_formated}'").to_json(orient="table")
    parsed = json.loads(result)
    print(cpf_formated)
    return parsed.get("data")


def blood_types():
    df = people_df["tipo_sanguineo"].value_counts().astype(str)
    return dict(df)


def peoples():
    names = people_df["nome"]
    names_list = names.sort_values()
    return names_list.values.tolist()


def people_search(q):
    people_df["nome_contain"] = people_df.nome.str.contains(q, na=False, case=False)
    result = people_df.query("nome_contain==True").head().to_json(orient="table")
    parsed = json.loads(result)
    if parsed.get("data") == []:
        return "Nenhum dado encontrado"
    return parsed.get("data")
