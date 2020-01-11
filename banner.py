from datetime import datetime, timedelta

fecha_dia1_vuelta1 = datetime(2020, 1, 20, 8, 0, 0)


horarios_vuelta1 = {"1": fecha_dia1_vuelta1}
for i in range(2, 9):
    horarios_vuelta1[str(i)] = horarios_vuelta1[str(i - 1)] + timedelta(hours=1.5)

horarios_vuelta1["9"] = fecha_dia1_vuelta1 + timedelta(days=1)
for i in range (10, 17):
    horarios_vuelta1[str(i)] = horarios_vuelta1[str(i - 1)] + timedelta(hours=1.5)

horarios_vuelta2 = {i: horarios_vuelta1[i] + timedelta(days=2) for i in horarios_vuelta1}

def obtener_grupo(horarios):
    for horario in horarios:
        if horarios[horario] > datetime.now():
            return str(int(horario) - 1)
    return "16"


if datetime.now() < horarios_vuelta1["1"]:
    actual = " Aún no comienza la toma de ramos"
elif datetime.now() < horarios_vuelta2["1"]:
    actual = obtener_grupo(horarios_vuelta1) + " - " + "Vuelta: 1"
else:
    actual = obtener_grupo(horarios_vuelta2) + " - " + "Vuelta: 2"



