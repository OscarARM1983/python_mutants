import numpy as np
from flask import Flask, jsonify, request, Response
from flask_mysqldb import MySQL
from configuraciones import config

app=Flask(__name__)
conexion=MySQL(app)

"""API GET, Obtención de todos los dna registrados"""

@app.route('/mutant', methods=['GET'])
def listar_dna():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT id, dna0, dna1, dna2, dna3, dna4, dna5, mutante FROM dna_verificados"
        cursor.execute(sql)
        datos=cursor.fetchall() #Convierte toda la respuesta en algo entendible para python
        verificados=[]
        for fila in datos:
            verificado={'id':fila[0], 'dna0':fila[1], 'dna1':fila[2], 'dna2':fila[3], 'dna3':fila[4], 'dna4':fila[5], 'dna5':fila[6], 'mutante':fila[7]}
            verificados.append(verificado)
        return jsonify({'verificados':verificados, 'mensaje':"DNAs listados."})  
    except Exception as ex:
        return jsonify({'mensaje':"Error"}), 400
    

"""API POST, endpoint mutant: evaluación de DNA"""

@app.route('/mutant', methods={'POST'})
def isMutant():
    try:
        dna = request.json['dna']
        filas = len(dna)
        columnas =len(dna[0])

        #print(dna)
       
        """Generación de matríz"""

        def generar_matriz(dna):
            dna2 = []

            for i in range(0, len(dna), 1):
                dna2.append(dna[i:i+1])
            #print(dna2)

            fila1 = []

            for j, dna_n in enumerate(dna2):
                Strdna_n = "".join(dna_n)
                for k in Strdna_n:
                    fila1.append(k)

            #print(fila1)


            dna_new = []
            for i in range(0, len(fila1), 6):
                dna_new.append(fila1[i:i+6])

            #print(f"Nuevo dna = {dna_new}")

            dna_np = np.array(dna_new)

            return dna_np

        dna_np = generar_matriz(dna)

        print(dna_np)


        """Evaluación letras DNA"""

        def evaluar_dna(dna_np, filas, columnas):
            evalua_letra = 0
            for f in range(filas):
                for c in range(columnas):
                    #print(f"posición letra {f},{c}: {dna_np[f,c]}")
                    if dna_np[f,c] != "A" and dna_np[f,c] != "T" and dna_np[f,c] != "C" and dna_np[f,c] != "G":
                        evalua_letra = 1
            
            return evalua_letra
        
        evalua_letra = evaluar_dna(dna_np, filas, columnas)
        #print(f"evalua_letra: {evalua_letra}")

        if evalua_letra == 0:

            """Evaluación de dna horizontal"""
            def revision_horizontal(dna_np, columnas):
                colu=0
                fila=0
                cont=1
                letra_ev=0
                secuencia_filas=0
                while colu < columnas:
                    for m in range(columnas):
                        letra = dna_np[fila,m]
                        #print(f"letra: {letra}")
                        #print(f"letra_ev: {letra_ev}")
                        if m != 0:
                            if letra_ev == letra:
                                cont = cont + 1
                                #print(f"cont: {cont}")
                                if cont == 4:
                                    secuencia_filas = secuencia_filas + 1
                                    #print(f"secuencia: {secuencia}")
                                    cont = 0
                            else:
                                cont = 0
                                letra_ev = letra
                                if m == 5:
                                    letra_ev = 0
                        else:
                            letra_ev = letra
                    colu = colu + 1
                    fila = fila + 1
                return secuencia_filas
            
            secuencia_filas = revision_horizontal(dna_np, columnas)
            print(f"secuencias filas: {secuencia_filas}")

            """Evaluación de dna vertical"""
            def revision_vertical(dna_np, filas):
                colu = 0
                fila = 0
                cont = 1
                letra_ev = 0
                secuencia_columnas = 0
                while fila < filas:
                    for n in range(filas):
                        letra = dna_np[n,colu]
                        if n != 0:
                            if letra_ev == letra:
                                cont = cont + 1
                                if cont == 4:
                                    secuencia_columnas = secuencia_columnas + 1
                                    cont = 0
                            else:
                                cont = 0
                                letra_ev = letra
                                if n == 5:
                                    letra_ev = 0
                        else:
                            letra_ev = letra
                    fila = fila + 1
                    colu = colu + 1
                return secuencia_columnas
            
            secuencia_columnas = revision_vertical(dna_np, filas)
            print(f"secuencias columnas: {secuencia_columnas}")

            """Evaluación de dna oblicua"""
            def revision_oblicua(dna_np, filas, columnas):
                colu = 0
                fila = 0
                cont = 1
                conteo = 0
                secuencia_oblicuo = 0

                def eval_letra(letra_ev, fila, columna, secuencia_oblicuo, filas, columnas, cont):
                    contador = cont
                    fila_prov = fila + 1
                    colu_prov = columna + 1
                    secu = secuencia_oblicuo
                    if fila_prov < filas and colu_prov < columnas:
                        letra_f = dna_np[fila_prov, colu_prov]
                        if letra_ev == letra_f and fila_prov < filas and colu_prov < columnas:
                            contador = contador + 1            
                            if contador == 4:
                                secu = secuencia_oblicuo + 1
                                contador = 1
                        else:
                            secu = secuencia_oblicuo
                            contador = 1
                    else:
                        contador = 1
                    return secu, contador, fila_prov, colu_prov

                while fila < filas:    
                    for m in range(columnas):
                        letra_ev = dna_np[fila,m]
                        secuencia_oblicuo, cont, fila1, colu1 = eval_letra(letra_ev, fila, m, secuencia_oblicuo, filas, columnas, cont)
                        while cont != 1:
                            secuencia_oblicuo, cont, fila1, colu1 = eval_letra(letra_ev, fila1, colu1, secuencia_oblicuo, filas, columnas, cont)      
                    fila = fila + 1
                
                return secuencia_oblicuo

            secuencia_oblicuo = revision_oblicua(dna_np, filas, columnas)
            
            print(f"secuencias oblicuos: {secuencia_oblicuo}")

            total_secuencias = secuencia_filas + secuencia_columnas + secuencia_oblicuo
            print(f"total secuencias: {total_secuencias}")



            """Evaluación mutante"""

            if total_secuencias > 1:
                print(f"Es mutante: {True}")
                respuesta = True
            else:
                print(f"Es mutante: {False}")
                respuesta = False


            
            """Verificación DNA repetido"""
            
            cursor=conexion.connection.cursor()
            sql4="SELECT dna0, dna1, dna2, dna3, dna4, dna5 FROM dna_verificados"
            cursor.execute(sql4)
            datos=cursor.fetchall() #Convierte toda la respuesta en algo entendible para python

            def dna_repetido(datos, filas):
                verificados=[]
                evaluador=0               
                for fila in datos:
                    fil=0            
                    while fil < filas:
                        if fila[fil] == dna[fil]:
                            verificados.append(1)
                        else:                    
                            verificados.append(0) 
                        cantidad_rep= verificados.count(1)
                        if cantidad_rep == filas:
                            evaluador = 1
                            fil = filas         
                        else:
                            fil = fil + 1
                    if evaluador == 0:
                        verificados.clear()
                return evaluador
            
            evaluador = dna_repetido(datos, filas)


            """Inserción de dna si no ha sido incluido previamente"""

            if evaluador == 0: 
                cursor=conexion.connection.cursor()
                sql="""INSERT INTO dna_verificados (dna0, dna1, dna2, dna3, dna4, dna5) 
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(dna[0], dna[1], dna[2], dna[3], dna[4], dna[5])
                cursor.execute(sql)
                conexion.connection.commit() #Para confirmar la acción de registrar datos
                #return jsonify({'mensaje':"DNA registrado"})          
                """Se agrega a campo mutante 1 si es mutante o 0 si no lo es """
                if total_secuencias > 1:
                    cursor=conexion.connection.cursor()
                    sql2="SELECT MAX(id) FROM dna_verificados;"
                    cursor.execute(sql2)
                    max_id = cursor.fetchone()
                    cursor=conexion.connection.cursor()
                    sql3=f"UPDATE dna_verificados SET mutante = 1 WHERE id={max_id[0]};"
                    cursor.execute(sql3)
                    conexion.connection.commit()
                    return jsonify({'mutante':True}), 200
                else:
                    cursor=conexion.connection.cursor()
                    sql2="SELECT MAX(id) FROM dna_verificados;"
                    cursor.execute(sql2)
                    max_id = cursor.fetchone()
                    cursor=conexion.connection.cursor()
                    sql3=f"UPDATE dna_verificados SET mutante = 0 WHERE id={max_id[0]};"
                    cursor.execute(sql3)
                    conexion.connection.commit()
                    return jsonify({'mutante':False}), 403
            else:
                if total_secuencias > 1:
                    return jsonify({'mutante':True}), 200
                else:
                    return jsonify({'mutante':False}), 403
        else:
            return jsonify({'Secuencia DNA':'No es valida, hay una o más letras diferentes a A,T,C,G'}), 400
    except Exception as ex:
        return jsonify({'mensaje':"Error diferente"}), 404



"""API GET, endpoint stats: Estadísticas mutantes evaluados"""

@app.route('/stats', methods=['GET'])
def stats_dna():
    try:
        cursor=conexion.connection.cursor()
        sql5="SELECT mutante FROM dna_verificados"
        cursor.execute(sql5)
        datos2=cursor.fetchall() #Convierte toda la respuesta en algo entendible para python
        print(f"datos2: {datos2}")

        count_mutant_dna = 0
        count_human_dna = 0
        for dato in datos2:
            count_mutant_dna = count_mutant_dna + dato[0]
            count_human_dna = count_human_dna + 1
        ratio = count_mutant_dna * 100 /count_human_dna
     
        return jsonify({'Verificaciones ADN':{'count_mutant_dna':count_mutant_dna, 'count_human_dna':count_human_dna, 'ratio':ratio}})
    except Exception as ex:
        return jsonify({'mensaje':"Error"}), 400
    

def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development']) #Llama al archivo de configuraciones
    app.register_error_handler(404, pagina_no_encontrada) #Administrador de errores
    app.run() # Permite hacer cambios y actualizar automáticamente el servidor