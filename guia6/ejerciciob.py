# b.	Crear un script en Python que imprima la hora entre las 14:00:00 y 15:00:00.

# 14:0:0
# 14:0:1
# 14:0:2
# ....
# 15:0:0

for hora in range(14, 15):
    for minutos in range(0, 60):
        for segundos in range(0, 60):
            print(f"{hora}:{minutos}:{segundos}")
            
print('15:0:0')