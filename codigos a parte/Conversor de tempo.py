segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
horas_restantes = total_segs % 86400
horas = horas_restantes // 3600 # 3600 é pela multiplicação de um minuto(60 segs) por uma hora (60 minutos)
segs_restantes = horas_restantes % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos. ")
'''
comentário em mais de uma linha.
'''
