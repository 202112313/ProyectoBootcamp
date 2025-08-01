import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
db = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="2025Valentina1002",     
    database="sabadoJulio" 
)
cursor = db.cursor(dictionary=True)
resultadosPersonas=[]
cursor.execute("SELECT * FROM persona")
resultadosPersonas = cursor.fetchall() 
print(resultadosPersonas)
personas = pd.DataFrame (resultadosPersonas)
print(personas)


nombre = ["Jorge", "ana", "luis"]
edad = [31,26,37]

plt.plot(personas["nombre"], personas["edad"])
plt.title("Grafico de edad por persona")
plt.show()

plt.bar(nombre, edad)
plt.title("Grafico de barras por persona")
plt.xlabel("nombre")
plt.ylabel("edad")
plt.show()

plt.scatter(nombre, edad)
plt.title("Grafico de dispersion edad por persona")
plt.xlabel("nombre")
plt.ylabel("edad")
plt.show()



#ventas por mes

labels = ["marzo","abril","mayo","junio"]

sizes =[23,56,12,32]
#Que no se nos olvide el formato es de la f%%

plt.pie(sizes, labels =labels, autopct="%1.1f%%", startangle=90)
plt.title("grafico de torta d eventa por mes")
plt.axis("equal")
plt.show()