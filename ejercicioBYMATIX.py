

import time; # lo que hace esta funcion es demorar en ingresar el texto
# EJERCICIO N°9 hecho  por el PROFE

#declarar variables y constantes
precio_churrasco=1500;
precio_completo=1000;
precio_vegetariano=2000;
precio_barrosLuco=3000;
#si quiere ingresar un codigo
condigo="1122";

respuesta="";

total_compra=0;

cantidad_churrasco=0;
cantidad_completo=0;
cantidad_vegetariano=0;
cantidad_barrosLuco=0;

descuento=0.1;
# mostrar los precios

print("\n bienvenido/a a la Sandwicheria \n");
time.sleep(2);# se agrega en un texto para demorar 2 segundos en aparecer
print("lista de precios\n");

print("1.churrasco-- $1.500\n2.completo-- $1.000\n 3.vegetariano-- $2.000\n4.barrosLuco-- $3.000");

# solicitar la cantidad de cada tipo

cantidad_churrasco=int(input("¿cuantos churrascos quiere? "));
cantidad_completo=int(input("¿cuantos completos quiere? "));
cantidad_vegetariano=int(input("¿cuantos vegetarianos quiere? "));
cantidad_barrosLuco=int(input("¿cuantos barros luco quiere? "));
# calcular el total a pagar
total_compra=total_compra+(cantidad_churrasco*precio_churrasco);
total_compra=total_compra+(cantidad_completo*precio_completo);
total_compra=total_compra+(cantidad_vegetariano*precio_vegetariano);
total_compra=total_compra+(cantidad_barrosLuco*precio_barrosLuco);
#mostrar el total a comprar
print(f"el total de la compra es $ {total_compra}\n");

#ahora viene el descuento y la validacion
print("ingresar la alternativa con mayuscula");
respuesta=input("¿ tiene un cupon de descuento? (SI/NO)");


if (respuesta=="SI"):
    total_compra=total_compra-(total_compra*descuento);
    print(" usted tiene un descuento del 10%")
    print(f"el total de la comprar con descuento es ${total_compra}");
elif (respuesta=="NO"):
    print("usted no tiene descuento.");
    print(f"total de la compra es $ {total_compra}\n");
else:
    print("se equivoco ... vuelva a intentarlo. ");
print("\n gracias por su compra. Disfrute su comida...\n");


# descuento con codigo
if (respuesta=="SI"):
    condigo=input("ingrese el codigo de descuento: ")
    if (condigo==condigo):
        total_compra=total_compra-(total_compra*descuento);
        print("usted tiene un descuento del 10%");
        print(f"el total de la compra con descuento es ${total_compra}");
else:
    print("codigo incorrecto");


# EJERCICIO HECHO POR MI
#DECLARAR VARIABLES  


precio_zapatosdeH=20000;
precio_zapatosdeM=15000;
precio_zapatosdeN=7000;
# ahora colocar las cantidades de zapatos de los 3  tipos que va a comprar
cantidad_zapatoH=0;
cantidad_zapatoM=0;
cantidad_zapatoN=0;

total_compra=0;
extra=3000;
# imprimir todo lo asignado 
print("bienvenido a la pagina de ZAPATOS ONLINE\n")
print("los tipos de zapatos que hay son \n1.ZAPATOS Hombre $ 20.000\n2.ZAPATOS Mujer $ 15.000\n3.ZAPATOS Niño $ 7.000\n")
print("OFERTA  UNICA\n")
print("al superar la comprar por sobre los 60.000 el envio es gratis\n")
print("si no supera el monto indicado se le agregara un extra de 3.000 por el envio\n")

# AHORA INGRESAR LA CANTIDAD DE ZAPATOS QUE QUIERE COMPRAR

print("ingrese la cantidad de zapatos que quiere comprar\n")
cantida_zapatoH=int(input("¿cuantos zapatos de HOMBRE quiere comprar? : "))
cantida_zapatoM=int(input("¿cuantos zapatos de MUJER quiere comprar? : "))
cantida_zapatoN=int(input("¿cuantos zapatos de NIÑO quiere comprar? : "))
# AHORA INGRESAR EL TOTAL DE LA COMRAR DE LOS PRODUCTOS ASIGNADOS "usando total comprar para sumar lo terminos cantidad y precio
total_compra=total_compra+(cantida_zapatoH*precio_zapatosdeH);
total_compra=total_compra+(cantida_zapatoM*precio_zapatosdeM);
total_compra=total_compra+(cantida_zapatoN*precio_zapatosdeN);


if (total_compra>=60000):
    print(f"el total de la comprar es ${total_compra}");
    print("usted obtiene un envio GRATISSSS")
    print("GRACIAS POR SU COMPRAR");
else:
    total_compra=total_compra+extra
    print("usted debe pagar por el envio igual a $ 3.000");
    print(f"el total de la comprar es $ {total_compra}");
    print("gracias por su comprar");



# ejercicio de ingresar un numero mayor que el otro

num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
if num1>num2:
    print(f"el numero mayor es {num1} ");
elif num2>num1:
    print(f"el numero mayor es {num2}");
else:
    print("se equivoco vuelva a intentar");

# ingrese por teclado dos números enteros e indique cuál de
# ellos es el mayor

num1=int(input("ingrese un numero: "));
num2=int(input("ingrese un numero: "));
num3=int(input("ingrese un numero: "));
if num1>num2 and num1>num3: # se puede hacer con (if num1>=num2 and num1>=num3) para no coloacar si todos son iguales
    print(f"el numero mayor es {num1}");
elif num2>num1 and num2>num3:
    print(f"el numero mayor es {num2}");
elif num3>num1 and num3>num2:
    print(f"el numero mayor es {num3}");
else:
    print("los numero ingresados son iguales");

# HACER OPERACIONES BASICAS CON LETRAS S,R,M,D ELIGIENDO UNA OPERACION


num1=int(input("ingrese un numero: "))
num2=int(input("ingrese un numero: "))

operacion=input("ingrese una operacion: ").upper()

if operacion=="S":
     suma=num1+num2
     print(f"el resultado de la suma es {suma}");
elif operacion=="R":
     resta=num1-num2
     print(f"el resultado de la resta es {resta}");
elif operacion=="M":
     multiplicacion=num1*num2
     print(f"el resulatdo de la multiplicacion es {multiplicacion}");
elif operacion=="D":
     division=num1/num2
     print(f"el resultado de la division es {division}");
else:
     print("se equivoco de operacion VUELVA A INTENTAR");


# INGRESAR A UN CAJERO AUTOMATICO I TENER 4 OPCIONES DIFERENTES
saldo=1000;

print("MENU DE  CAJERO AUTOMATICO\n");
print("1.-INGRESAR DINERO\n2.-RETIRAR DINERO\n3.-MOSTRAR DINERO DISPONIBLE\n4.-SALIR\n");

opcion=int(input("eliga una opcion "));

if opcion==1:
    extra=float(input("cuanto dinero desea ingresar-->"))
    extra=extra+saldo
    print(f"el dinero el la cuenta es ${extra}");
elif opcion==2:
    retirar=float(input("cuanto dinero desea retirar: "));
    if retirar>1000:
        print("usted esta superando el limite del cajero")
    else:
        retirar=retirar-saldo
        print(f"el dinero restante de su cuenta es ${retirar}")
elif opcion==3:
     print(f"el dinero el la cuenta es ${saldo}")   

elif opcion==4:
    print("gracias por usar el cajero automatico")
else:
    print("ERror VUElva a INtentar");
    
    # EJERCICIO 10

# ingresar variables

total=0;
comuna=1000;
aledaña=2000;
envio=3000;
precio=500;

print("VENTA DE MASCARILLAS\n")
print("si supera la compra por sobre los 15.000 el envio es gratis\n")
print("DE QUE COMUNA ES \n")
print("1.-misma COMUNA $.1000\n2.-comuna ALEDAÑA $.2.000\n3.-ENVIO $.3.000")

opcion=int(input("elija una OPCION: "));

if opcion==1:
    cantidad=int(input("ingrese cuantas mascarillas desea ingresar: "))
    total=cantidad*precio
    if total>15000:
        print("el envio es gratis")
        print(f"el total de la compra es de ${total}")
        print("GRACIAS POR SU COMPRA");
        
    elif total<15000:
        print(f"el total de la compra es de ${total}")

        print("usted es de la misma comuna el envio es de 1.000")
        total=total+comuna

        print(f"el total de la compra es de ${total}")
        print("GRACIAS POR SU COMPRA")
    else:
        print("se equivoco vuelva a intentar");


if opcion==2:
    cantidad=int(input("ingrese cuantas mascarillas desea ingresar: "))
    total=cantidad*precio
    if total>15000:
        print("el envio es gratis")
        print(f"el total de la compra es de ${total}")
        print("GRACIAS POR SU COMPRA");
        
    elif total<15000:
        print(f"el total de la compra es de ${total}")

        print("usted es de una comuna aledaña el envio es de $2.000")
        total=total+aledaña
        print(f"el total de la compra es de ${total}")
        print("GRACIAS POR SU COMPRA")
    else:
        print("se equivoco vuelva a intentar");

if opcion==3:
    cantidad=int(input("ingrese cuantas mascarillas desea ingresar: "))
    total=cantidad*precio
    if total>15000:
        print("el envio es gratis")
        print(f"el total de la compra es de ${total}")
        print("GRACIAS POR SU COMPRA")
    elif total<15000:
        print(f"el total de la compra es de ${total}")
        print("el envio es de 3.000")
        total=total+envio
        print(f"el total de la compra mas el envio es de ${total}")
        print("GRACIAS POR SU COMPRA")
    else:
        print("se equivoco vuelva a intentar");



# ejercicios usando if 
resultado=0;
i=1;
num=0;
num=int(input("ingresar un numero: "));
if num>1 and num<101:
    if num%2 ==0:
        print("el numero ingresado es numero par");
else:
    print("el numero ingresado es impar");

print("tabla de multiplicar")
# TABLA DE MULTIPLICAR USANDO FOR
# ingresar y mostrar datos
rango=range(1,11);
num=int(input("ingrese un numero: " ));
print(f"la tabla del {num} es\n");

# sentencia de decision y repeticion
for i in rango:
    resultado=num*i;
    print(f"{num} x {i}= {resultado}")

    #ejercicio 11

precio_agua=600;
precio_azucar=1200;
precio_aceite=1500;
precio_arroz=1250;


total_agua=0;
total_azucar=0;
total_aceite=0;
total_arroz=0;

cantidad_agua=0;
cantidad_azucar=0;
cantidad_aceite=0;
cantidad_arroz=0;


total=0;
descuento=0.25;


print("1.agua.$600\n2.azucar.$1.500\n")

respuesta=input("desea comprar agua si/no: ")
if respuesta=="si":
    cantidad_agua=int(input("cuantas botellas de agua desea comprar: "))
    total_agua=precio_agua*cantidad_agua
    print(f"el costo total es de ${total_agua}")
else:
    print("compre otro producto");
respuesta=input("desea comprar azucar si/no: ")
if respuesta=="si":
    cantidad_azucar=int(input("cuanta azucar desea comprar: "))
    total_azucar=precio_azucar*cantidad_azucar
    print(f"el costo total es de ${total_azucar}")
else:
    print("compre otro producto");

respuesta=input("desea comprar aceite si/no: ")
if respuesta=="si":
    cantidad_aceite=int(input("cuanto aceite desea comprar: "))
    total_aceite=precio_aceite*cantidad_aceite
    print(f"el costo total es de ${total_aceite}")
else:
    print("compre otro producto");
respuesta=input("desea comprar arroz si/no: ")
if respuesta=="si":
    cantidad_arroz=int(input("cuanto arroz desea comprar: "))
    total_arroz=precio_arroz*cantidad_arroz
    print(f"el costo de la compra es de $ {total_arroz}")
else:
    print("compre otro producto");


total=total_agua+total_azucar+total_aceite+total_arroz
print(f"el total de la compra es de {total}")
respuesta=input("¿usted es cliente preferencial? si/no: ")
if respuesta=="si":
    total=total-(total*descuento)
    print("usted tiene un  descuento del 25%")
    print(f"el total de la compra mas el descuento es de $ {total}")

    



  




 


