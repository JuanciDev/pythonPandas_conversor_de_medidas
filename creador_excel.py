import pandas as pd

data = {
    "Piezas" : ["Pata", "tablero", "Puerta", "Estante", "Panel lateral"],
    "Centimetros" : [40,120,60,10,180]
}

df = pd.DataFrame(data)

df.to_excel("muebles_medidas.xlsx", index=False)