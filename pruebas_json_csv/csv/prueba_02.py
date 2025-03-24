import os,csv
os.system('cls')


with open('prueba_02.csv', 'w', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerow(['nombre', 'edad', 'gmail'])
    escritor.writerow(['Pedro', 30, 'pedro@gmail.com'])


with open('prueba_02.csv', 'r') as f:
    lector = csv.reader(f)
    
    for fila in lector:
        print(fila)