import pandas as pd

def pregunta_09():
    df = pd.read_csv("files/input/tbl0.tsv", delimiter="\t")

    # Reemplazar manualmente la fecha inválida "1999-02-29" por "1999-02-28"
    df["c3"] = df["c3"].replace("1999-02-29", "1999-02-28")

    # Convertir a datetime y extraer año
    df["c3"] = pd.to_datetime(df["c3"])
    df["year"] = df["c3"].dt.year.astype(str)

    return df
