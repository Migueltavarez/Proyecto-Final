
import time
import contextlib
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database ="nomina"
    )

mycursor = mydb.cursor()



def Datos():
    #Declaracion de las variables
    Nombre = input("Digite Su Nombre: ")
    Cedula = input("Digite Su Cedula: ")
    Puesto = input("Digite Su Puesto: ")
    Departamento = input("Digite Su Departamento: ")
    Sueldo_Bruto = int(input("Digite Su Sueldo Bruto: "))
    time.sleep(1)
    print("\n")

    #Identifiacion del cargo
    if Puesto == 'Gerente' or Puesto == 'gerente':
        gasto_pres =  5000
    elif Puesto == 'Secretaria' or Puesto == 'secretaria' or Puesto == 'Secretario' or Puesto == 'secretario':
        gasto_pres =  2000
    else:
        gasto_pres = 0

    #Calculo del ISR
    if Sueldo_Bruto > 37000:
        excedente = Sueldo_Bruto - 37000 
    else:
        excedente = 0
    isr = int (excedente * 0.10)    
    #Calculo del SS
    ss = int (Sueldo_Bruto * 0.018)
    #Calcuo AFP
    afp =  int (Sueldo_Bruto * 0.02)
    #Total de Descuento
    total_descuento = isr + ss + afp
    #Sueldo Neto
    sueldo_neto = Sueldo_Bruto + gasto_pres - total_descuento

    


    #Salida de Valores
    print ("[~] Realizando los calculos.......")
    print ("[~] Imprimiendo los resultados.......")
    print("\n")
    time.sleep(1)
    print  ("[+] Su Sueldo Bruto es: " + str(Sueldo_Bruto))
    print  ("[+] Gasto de Presentacion: " + str(gasto_pres))
    print  ("[+] Sueldo mas gasto de presentacion: " + str (Sueldo_Bruto + gasto_pres))
    print  ("[+] Impuesto sobre la Renta: " + str(isr))
    print  ("[+] Seguro Social: " + str(ss))
    print  ("[+] AFP: " + str(afp))
    print  ("[+] Total de retenciones: " + str(total_descuento))
    print  ("[+] Sueldo Neto: " + str(sueldo_neto))

    sql = "INSERT INTO empleados (Nombre, Cedula, Puesto, Departamento, Sueldo_Bruto, Sueldo_Neto) VALUES (%s, %s, %s, %s, %s, %s)"
    val = f"{Nombre}" ,f"{Cedula}" ,f"{Puesto}" ,f"{Departamento}" ,f"{Sueldo_Bruto}" ,f"{sueldo_neto}"
    mycursor.execute(sql, val)

    mydb.commit()
    
    # mycursor.execute('set sql_safe_updates = 0') 
    # sql = f"DELETE FROM empleados WHERE Cedula = '{Cedula}'"
    # mycursor.execute(sql)
    # mycursor.execute('set sql_safe_updates = 1')
    # mydb.commit()
if __name__ ==  '__main__':
    Datos()

time.sleep(10)

