import urllib.request
from bs4 import BeautifulSoup

cursos = [('ICS2613', "2"), ('ICS2613', "2"), ('ICS2613', "2"), ('ICS2613', "2"), ('ICS2613', "2")]
año = "2019"
semestre = "1"

def consultar(sigla_input, seccion_input):
    resultados_parcial = list()
    data = urllib.request.urlopen(
        f"http://buscacursos.uc.cl/?cxml_semestre={año}-{semestre}&cxml_sigla={sigla_input}#resultados").read().decode()

    data_beautiful = BeautifulSoup(data)
    tags = data_beautiful("a")

    for tag in tags:
        curso = tag.get('onclick')
        if type(curso) == str:
            param = curso.split("&")
            index_nrc = param[0].find("nrc=")
            if index_nrc != -1:
                seccion = param[-1][8:-3]
                if seccion == seccion_input or seccion_input == "":
                    nrc = param[0][index_nrc + 4:]
                    c_disponible = param[2][13:]
                    c_total = param[3][13:]
                    sigla = param[-2][6:]
                    resultados_parcial.append(
                        {'nrc': nrc, 'c_disponible': c_disponible, 'c_total': c_total, 'sigla': sigla,
                         'seccion': seccion})
    return resultados_parcial


sigla_input = 0
resultados = list()
nuevos = input("Presione enter si desea mantener los cursos guardados. Ingrese 1 si desea seleccionar nuevos cursos.")

if nuevos != "":
    while sigla_input != "-1":
        sigla_input = input("Seleccione la sigla: ")
        if sigla_input == "-1":
            break
        seccion_input = input("Seleccione la sección: ")
        data = urllib.request.urlopen(
            f"http://buscacursos.uc.cl/?cxml_semestre=2019-1&cxml_sigla={sigla_input}#resultados").read().decode()

        resultados.extend(consultar(sigla_input, seccion_input))

else:
    for curso in cursos:
        sigla_input = curso[0]
        seccion_input = curso[1]
        data = urllib.request.urlopen(
            f"http://buscacursos.uc.cl/?cxml_semestre=2019-1&cxml_sigla={sigla_input}#resultados").read().decode()

        data_beautiful = BeautifulSoup(data)
        tags = data_beautiful("a")

        resultados.extend(consultar(sigla_input, seccion_input))

'''''
print()

print(resultados)
for curso in resultados:
    print(curso['sigla'] + "-" + curso['seccion'])
    print("Cupos disponibles: " + curso['c_disponible'])
    print("Cupos Totales: " + curso["c_total"])
    print("Porcentaje ocupado: " + str(int(100 * (int(curso["c_total"]) - int(curso["c_disponible"])) / int(curso["c_total"]))))

'''''
