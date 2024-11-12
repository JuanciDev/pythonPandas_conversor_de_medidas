import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.50

df = pd.read_excel("muebles_medidas.xlsx")

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print("Conversion completada y guardada un nuevo archivo llamado mueble_medidas_convertidas.xlsx ")