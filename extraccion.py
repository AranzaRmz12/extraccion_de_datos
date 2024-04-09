import pandas as pd

print('Aplicación de extracción de datos')
df = pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx')
# print(df.info)
# print(df.head())

# Filtro por objeto 
filtro1 = df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
# print(filtro1)
filtro1.to_csv("Entregable1.csv")

# Filtro por filas
filtro2 = df.iloc[2:8,: ]   
# print(filtro2)
filtro2.to_csv("Entregable2.csv")

# Filtro por columnas
filtro3 = df.iloc[:, [1, 3, 4, 10]]  
# print(filtro3)
filtro3.to_csv("Entregable3.csv")

df1 = pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx', index_col = 1)
# print(df1)

# Se filtro un filtro de filas con columnas. Mostrando únicamente las filas que tenga la fecha de doc (que es el índice) igual a 2022-11-22 y 2022-12-23. 
# Mostrando la columna de subtotal_partida.
filtro4 = df1.loc[["2022-11-22","'2022-12-23"], ["SUBTOTAL_PARTIDA"]]
# print(filtro4)
filtro4.to_csv("Entregable4.csv")

# Filtramos por cabecera para que muestre los primero 8 filas.
filtro5 = df.head(8)
# print(filtro5)
filtro5.to_csv("Entregable5.csv")

# Filtre por comparación, para obtener los datos donde el valor en subtotal_partida sea mayor a 77000
filtro6 = df[df["SUBTOTAL_PARTIDA"] > 77000]
# print(filtro6)
filtro6.to_csv("Entregable6.csv")

# Filtro Y tiene que cumplir las dos condiciones
filtro7 = df[(df["SUBTOTAL_PARTIDA"] > 77000) & (df["FECHA_DOC"] == "2022-05-24")]
# print(filtro7)
filtro7.to_csv("Entregable7.csv")

# Filtro con condición or
filtro8 = df[(df["SUBTOTAL_PARTIDA"] > 77000)| (df["FECHA_DOC"] == "2022-05-24")]
# print(filtro8)
filtro8.to_csv("Entregable8.csv")

#Filtro con condición not
filtro9 = df[~(df["SUBTOTAL_PARTIDA"] > 77000) & ~(df["FECHA_DOC"] == "2022-05-24")]
# print(filtro9)
filtro9.to_csv("Entregable9.csv")  