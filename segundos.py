segundos_str = input("Por favor, entre com o número de segundos desejado converter:")

total_segs = int(segundos_str)


dias = total_segs // 86400
total_segs_hora = total_segs % 86400
horas = total_segs_hora // 3600
segs_restantes = total_segs_hora % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")
