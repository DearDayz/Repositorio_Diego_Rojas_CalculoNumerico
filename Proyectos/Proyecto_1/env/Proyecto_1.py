import flet as ft
import re
import numpy as np  

Base_Seleccionada = ""
Base_Seleccionada2 =""
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 810
    page.window_height =640
    page.window_resizable = False
    txt_entrada = ft.TextField(value="1", text_align=ft.TextAlign.CENTER, width=250)
    txt_respuesta = ft.TextField(value="Resultado", text_align=ft.TextAlign.CENTER, width=250,read_only=True)

    global matriz_A
    global Vector_b
    global matriz_Respuesta
    
    def clear_txt_number(e):
        txt_entrada.value = ""
        txt_respuesta.value = ""
        page.update()

    def clear_all_fields(e):
        txt_entrada.value = ""
        txt_respuesta.value = ""
        Seleccion_1.value = ""
        Seleccion_2.value = ""
        page.update()
    def clear_all_fields2(e):
        matriz_A.value = ""
        Vector_b.value = ""
        matriz_Respuesta.value = ""
        Valor_n.value = ""
        page.update()
    def validar_n(n):
        try:          
            if not n:  
                return False
            elif not re.match(r'^\d+$', n):
                
                return False
            elif not n.isdigit():
            
                return False
            elif int(n) < 1 or int(n) > 9:
                return False
            else:
                return True
        except:
            return False
            
    def Validar_Matriz(matrix_str, n, vector_str):
        
        try:
            matrix_str  = matriz_A.value
            vector_str = Vector_b.value
            vector_str = vector_str.strip()
            matrix_str = matrix_str.strip()           
            
            if not matrix_str or not vector_str:               
                return False
                        
            rows = matrix_str.split('\n')
            rows2 = vector_str.split('\n')            
            
            
            if len(rows) != int(Valor_n.value) or len(rows2) != int(Valor_n.value):
                return False
             
            for row in rows:
                
                elements = row.split()    
                
                if len(elements) != int(n):
                    return False
                
                for elem in elements:
                    if not re.match(r'^-?\d+\.?\d*$', elem):
                        
                        return False
        
            for row in rows2:
            
                elements = row.split()
                
                if len(elements) != 1:     
                    return False
                     
                for elem in elements:
                    if not re.match(r'^-?\d+\.?\d*$', elem):
                        
                        return False
            
            return True
        except:
            return False
    
    def validar_base(numero):
        try:
        
            if not numero:
                show_banner()
                return "Vacio"
            elif(Base_Seleccionada == "" or Base_Seleccionada2 == ""):
                show_banner()
                return "Vacio"
            elif (re.search(r'\s', numero)or re.search(r'[^a-zA-Z0-9]', numero)):
                show_banner()
                return "Invalido"
            elif Base_Seleccionada == "Decimal":
                
                
                if str(numero).startswith("0") or not str(numero).isdigit():
                    show_banner()
                    return "Invalido"
                if(Base_Seleccionada2 == "Decimal"):
                    return str(numero)
                elif(Base_Seleccionada2 == "Binario"):
                    return Dec_Bin(int(numero))
                elif(Base_Seleccionada2 == "Octal"):
                    return Dec_Oct(int(numero))
                elif(Base_Seleccionada2 == "Hexadecimal"):
                    return Dec_Hex(int(numero))
                elif(Base_Seleccionada2 == "Cuartenar"):
                    return Dec_Cu(int(numero))
                elif(Base_Seleccionada2 == "Terciar"):
                    return Dec_Ter(int(numero))
                
            elif Base_Seleccionada == "Octal":
                
                for char in numero:
                    if not char.isdigit() or int(char) < 0 or int(char) > 7:
                        show_banner()
                        return "Invalido"
                if(Base_Seleccionada2 == "Octal"):
                    return str(numero)
                elif(Base_Seleccionada2 == "Binario"):
                    return OctalBinario(numero)
                elif(Base_Seleccionada2 == "Decimal"):
                    return aDecimal(numero, 8)
                
                elif(Base_Seleccionada2 == "Hexadecimal"):
                    return  OctalHex(numero)
                elif(Base_Seleccionada2 == "Cuartenar"):
                    return Bin_Cu(OctalBinario(numero))
                elif(Base_Seleccionada2 == "Terciar"):
                    return Bin_Ter(OctalBinario(numero))
                
                    
            elif Base_Seleccionada == "Binario":
                
                for char in numero:
                    if not char.isdigit() or int(char) < 0 or int(char) > 1:
                        show_banner()
                        return "Invalido"
                if(Base_Seleccionada2 == "Binario"):
                    return str(numero)
                elif(Base_Seleccionada2 == "Octal"):
                    return Bin_Oct(numero)
                
                elif(Base_Seleccionada2 == "Hexadecimal"):
                    return Bin_Hex(numero)
                
                elif(Base_Seleccionada2 == "Decimal"):
                    return aDecimal(numero, 2)
                elif(Base_Seleccionada2 == "Cuartenar"):
                    return Bin_Cu(numero)
                elif(Base_Seleccionada2 == "Terciar"):
                    return Bin_Ter(numero)
                
            elif Base_Seleccionada == "Hexadecimal":
                
            
                for char in numero:
                    if not (char.isdigit() or char.upper() in 'ABCDEF'):
                        show_banner()
                        
                        return "Invalido"
                if(Base_Seleccionada2 == "Hexadecimal"):
                    
                    return str(numero)
                elif(Base_Seleccionada2 == "Binario"):
                    return HexBin(numero)
                
                elif(Base_Seleccionada2 == "Octal"):
                    return Bin_Oct(HexBin(numero))
                
                elif(Base_Seleccionada2 == "Decimal"):
                    return  aDecimal(HexBin(numero), 2)
                elif(Base_Seleccionada2 == "Cuartenar"):
                    return Hex_Cu(numero)
                elif(Base_Seleccionada2 == "Terciar"):
                    return Hex_Ter(numero)
            elif Base_Seleccionada == "Cuartenar":
                if not str(numero).isdigit() or not re.match(r'^[0-3]+$', numero):
                    show_banner()
                    return "Invalido"
                if Base_Seleccionada2 == "Cuartenar":
                    return str(numero)
                elif Base_Seleccionada2 == "Decimal":
                    return aDecimal(numero, 4)
                elif Base_Seleccionada2 == "Binario":
                    return Cuater_Bin(numero)
                elif Base_Seleccionada2 == "Octal":
                    return Bin_Oct(Cuater_Bin(numero))
                elif Base_Seleccionada2 == "Hexadecimal":
                    return Bin_Hex(Cuater_Bin(numero))
                elif Base_Seleccionada2 == "Terciar":
                    return  cuartenar_a_terciar(numero)
                    
            elif Base_Seleccionada == "Terciar":
                if not str(numero).isdigit() or not re.match(r'^[0-2]+$', numero):
                    show_banner()
                    return "Invalido"
                if Base_Seleccionada2 == "Terciar":
                    return str(numero)
                elif Base_Seleccionada2 == "Decimal":
                    return aDecimal(numero, 3)
                elif Base_Seleccionada2 == "Binario":
                    return TerciarBinario(numero)
                elif Base_Seleccionada2 == "Octal":
                    return Bin_Oct(TerciarBinario(numero))
                elif Base_Seleccionada2 == "Hexadecimal":
                    return Bin_Hex(TerciarBinario(numero))
                elif Base_Seleccionada2 == "Cuartenar":
                    return  Ter_Cua(numero)
        except:
            show_banner()
            return "Invalido"
        
    def button_clicked(e):
        txt_respuesta.value = validar_base(str(txt_entrada.value.strip()))
        page.update()

    def dropdown_changed(e):
        global Base_Seleccionada, Base_Seleccionada2
        
        if e.control.data == "Seleccion_1":
            
            Base_Seleccionada = e.control.value
        elif e.control.data == "Seleccion_2":
           
            Base_Seleccionada2 = e.control.value
        page.update()

    b = ft.ElevatedButton("Convertir", on_click=button_clicked, data=0)

    Seleccion_1 = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Cuartenar"),
            ft.dropdown.Option("Terciar"),
        ],
        width=120,
        data="Seleccion_1"
    )
    Seleccion_2 = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Cuartenar"),
            ft.dropdown.Option("Terciar"),
        ],
        width=120,
        data="Seleccion_2"
    )
    def close_banner(e):
        page.banner.open = False
        page.update()
    def show_banner():
        page.banner.open = True
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            """Revise los datos ingresados: 
            - No puede haber espacios en blanco
            - No puede haber caracteres especiales
            - No puede haber letras en bases numéricas distintas a la hexadecimal (A-F)
            - No puede haber números negativos
            - No puede haber números decimales
            - Recuerda: (0-7)octal, (0-1)binaria, (0-9,A-F)hexadecimal, (0-9)decimal,(0-3)cuartenar y (0-2)terciar

            """,
        ),
        actions=[
            ft.TextButton("Reintentar", on_click=close_banner),
            ft.TextButton("Ignorar", on_click=close_banner),
            ft.TextButton("Cancelar", on_click=close_banner),
        ],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    blimpiar = ft.IconButton(
        icon=ft.icons.DELETE_FOREVER_ROUNDED,
        icon_color="pink600",
        icon_size=40,
        tooltip="Limpiar campos",
        on_click=clear_all_fields,
        
    )
    blimpiar2 = ft.IconButton(
        icon=ft.icons.DELETE_FOREVER_ROUNDED,
        icon_color="pink600",
        icon_size=40,
        tooltip="Limpiar campos",
        on_click=clear_all_fields2,
        
    )
    bborra = ft.IconButton(
        icon=ft.icons.CLEAR,
        icon_color="red600",
        icon_size=40,
        tooltip="Restablecer",
        on_click=clear_txt_number,
    )
    icon = ft.Icon(ft.icons.CALCULATE, size=40)
    titulo = ft.Text("Calculadora de Converciones", size=20)
    banner = ft.ElevatedButton("Información", on_click=show_banner_click,icon=ft.icons.INFO)
    Valor_n = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=50)
    matriz_A = ft.TextField(value=" ", width=250, height=150, multiline=True, disabled=False)
    Vector_b = ft.TextField(value=" ", width=70, height=150, multiline=True, disabled=False)
    matriz_Respuesta = ft.TextField(value=" ", width=250, height=150, multiline=True, read_only=True)
    Boton_Aleatorio = ft.ElevatedButton("Aleatoria", on_click=lambda e: aleatorio(page, Valor_n))
    Boton_Operar = ft.ElevatedButton("Operar", on_click=lambda e: normal(page, matriz_A, Vector_b))

    def aleatorio(page, Valor_n):
        try:
            if not validar_n(Valor_n.value):
                open_dlg(None)
            else:
                n = int(Valor_n.value)
                matriz = np.random.randint(0, 100, size=(n, n))
                vector_b = np.random.randint(0, 100, size=(n, 1))
    
                X_str = "\n".join(" ".join(str(elemento) for elemento in fila) for fila in gauss_jordan(matriz, vector_b))              
                matriz_str = "\n".join(" ".join(str(elemento) for elemento in fila) for fila in matriz)                
                vector_b_str = "\n".join(str(elemento[0]) for elemento in vector_b)
                

                matriz_A.value = matriz_str
                Vector_b.value =  vector_b_str
                matriz_Respuesta.value = X_str
                
                page.update()
        except:
            open_dlg(None)


    def normal(page, matrix_input, vector_input):
        try:
            if not Validar_Matriz(matrix_input.value, Valor_n.value, vector_input.value):
                open_dlg(None)
            else:
                
                matriz = np.array([list(map(float, row.split())) for row in matrix_input.value.split("\n")])
                vector_b = np.array([list(map(float, row.split())) for row in vector_input.value.split("\t")], ndmin=2).T
                X_str = "\n".join(" ".join(str(elemento) for elemento in fila) for fila in gauss_jordan(matriz, vector_b))
                
                matriz_Respuesta.value = X_str
                page.update()
        except:
            open_dlg(None)
           
    def gauss_jordan(A, B):

        try:
            casicero = 1e-15  # Considerar como 0
            
            # Evitar truncamiento en operaciones
            A = np.array(A, dtype=float)
            B = np.array(B, dtype=float)
            
            # Matriz aumentada
            AB = np.concatenate((A, B), axis=1)
            
            
            # Pivoteo parcial por filas
            tamano = np.shape(AB)
            n = tamano[0]
            m = tamano[1]
            
            # Para cada fila en AB
            for i in range(0, n):
                # columna desde diagonal i en adelante
                columna = abs(AB[i:, i])
                dondemax = i + np.argmax(columna)
                
                # Intercambiar filas si el pivote es cero
                if abs(AB[dondemax, i]) < casicero:
                    return None
                
                # Intercambiar filas i y dondemax
                AB[[i, dondemax]] = AB[[dondemax, i]]
                
                # eliminacion hacia adelante
                for k in range(i+1, n):
                    factor = AB[k, i] / AB[i, i]
                    AB[k, :] -= factor * AB[i, :]
            
            # eliminacion hacia atras
            for i in range(n-1, -1, -1):
                # Asegurarse de que el pivote sea 1
                pivote = AB[i, i]
                AB[i, :] /= pivote
                
                for k in range(i):
                    factor = AB[k, i]
                    AB[k, :] -= factor * AB[i, :]
            
            # Extraer la solución X
            X = AB[:, n:]
            
            return X
        except:
            open_dlg(None)

    dlg = ft.AlertDialog(
        title=ft.Text("""Atención Gauss-Jordan: Para Resolver un Problema del tipo Ax=b colocar Matriz A y vector b en los Espacios en blaco para encontrar valores de X(debe de tener solución):
    -Ingresar la matriz A en el espacio de la izquierda
    -Ingresar el vector b en el espacio de la derecha
    -Presionar el botón Operar para obtener el resultado
    -Presionar el botón Aleatorio y coloca valor de N para 
        generar una matriz y vector b aleatorios
    -Colocar valor n para la matriz cuadrada
    -No se permiten espacios en blanco
    -No se permiten caracteres especiales
    -El vector b y matriz A misma cantidad de filas
    -El tamaño de la matriz debe ser de 1 a 10
    -No se permiten números negativos ni decimales en n
    -La matriz A y el vector b deben ser n*n y n*1 
                       """),)
    
    def close_dlg(e):
        dlg.open = False
        page.update()

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    #Añadir elementos a la página
    page.add(
    ft.Row(
        [
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [
                                titulo
                            ],
                        ),
                        ft.Row(
                            [
                                txt_entrada,
                                bborra
                            ],
                        ),
                        ft.Row(
                            [
                                Seleccion_1,
                                Seleccion_2,
                                icon
                            ],
                        ),
                        ft.Row(
                            [
                                txt_respuesta
                            ],
                        ),
                        ft.Row(
                            [
                                b,
                                ft.Container(width=30),
                                blimpiar
                            ],
                        ),
                        ft.Row(
                            [
                                banner
                            ],
                        ),
                    ],
                    alignment="flex-start",  # Alinea el contenido del contenedor arriba
                ),
                padding=10,
                border_radius=20,
                bgcolor="blue200",
                height=580,
            ),
            ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Calculadora Gauss-Jordan     Ax=b", size=20)
                            ],
                        ),
                        ft.Row(
                            [
                                ft.Text("n=", size=20),
                                Valor_n,
                                Boton_Aleatorio,
                                Boton_Operar,
                            ],
                        ),
                        ft.Row(
                            [
                                ft.Text("Matriz A", size=20),
                                ft.Text("                                   b", size=20),
                            ],
                        ),
                        ft.Row(
                            [
                                matriz_A,
                                Vector_b,
                            ],
                        ),
                        ft.Row(
                            [
                                ft.Text("Resultado", size=20),
                            ],
                        ),
                        ft.Row(
                            [
                                matriz_Respuesta,
                                ft.ElevatedButton("Información", on_click=open_dlg,icon=ft.icons.INFO),
                            ],
                        ),
                        ft.Row(
                            [
                                blimpiar2
                            ],
                        ),
                    ],
                    alignment="flex-start",
                ),
                padding=10,
                #bgcolor="yellow100",
                bgcolor="blue400",
                border_radius=20,
                height=580,
            ),
        ],
        alignment="flex-start",
    )
)
    #Formulas Conversiones
    def Dec_Bin(numero):
        try:
            if numero == 0:
                return '0'

            binario = ''
            abs_num = abs(numero)

            while abs_num > 0:
                binario = str(abs_num % 2) + binario
                abs_num //= 2

            return binario
        except:
            show_banner()
            return "Invalido"

    def Dec_Oct(numero):
        try:
            Octal_digito = '01234567'
            octal = ''

            while numero > 0:
                octal = Octal_digito[numero % 8] + octal
                numero //= 8

            return octal or '0'
        except:
            show_banner()
            return "Invalido"

    def Dec_Hex(numero):
        try:
            Hex_digito = '0123456789ABCDEF'
            hex_num = ''

            while numero > 0:
                hex_num = Hex_digito[numero % 16] + hex_num
                numero //= 16

            return hex_num or '0'
        except:
            show_banner()
            return "Invalido"
    
    def OctalBinario(n):
        try:
            octal = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
            bin = str(''.join(octal[num] for num in n))
            return bin.lstrip('0')
        except:
            show_banner()
            return "Invalido"
        
    def aDecimal(num, c):
        try:
            result = 0
            count = len(num)-1
            for n in num:
                result += int(n)*((c)**count)
                count -= 1
            return result
        except:
            show_banner()
            return "Invalido"
    
    def HexBin(n):
        try:
            num=""
            n = list(n.upper())
            for i in n:
                if i.isnumeric():
                    num += (bin(int(i))[2:].zfill(4))
                else:   
                    if i == "A":
                        num += "1010"
                    elif i == "B":
                        num += "1011"
                    elif i == "C":
                        num += "1100"
                    elif i == "D":
                        num += "1101"
                    elif i == "E":
                        num += "1110"
                    elif i == "F":
                        num += "1111"
            return num
        except:
            show_banner()
            return "Invalido"
    
    def OctalHex(n):
        try:
            return Bin_Hex(OctalBinario(n))
        except:
            show_banner()
            return "Invalido"
    def BinarioDecimal(n):
        try:
            if len(n) == 1:
                return int(n)
            return 2 * BinarioDecimal(n[:-1]) + int(n[-1])
        except: 
            show_banner()
            return "Invalido"
    def Bin_Hex(N_binario):
        try:
            while len(N_binario) % 4 != 0:
                N_binario = '0' + N_binario
       
            Diccionario = {
                '0000': '0', '0001': '1', '0010': '2', '0011': '3',
                '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
            }

            hex_num = ''
            
            for i in range(0, len(N_binario), 4):
                grupo = N_binario[i:i+4]
                hex_digit = Diccionario[grupo]
                hex_num += hex_digit

            return hex_num
        except:
            show_banner()
            return "Invalido"
    def Bin_Oct(N_binario):
        try:
            while len(N_binario) % 3 != 0:
                N_binario = '0' + N_binario
           
            octal_mapping = {
                '000': '0', '001': '1', '010': '2', '011': '3',
                '100': '4', '101': '5', '110': '6', '111': '7'
            }

            octal_num = ''
            
            for i in range(0, len(N_binario), 3):
                grupo = N_binario[i:i+3]
                octal_digit = octal_mapping[grupo]
                octal_num += octal_digit

            return octal_num
        except:
            show_banner()
            return "Invalido"
    def Cuater_Bin(n):
        try:
            Cu_Bin = {'0': '00', '1': '01', '2': '10', '3': '11'}
            binario = str(''.join(Cu_Bin[num] for num in n))
            return binario.lstrip('0')
        except:
            show_banner()
            return "Invalido"

    def TerciarBinario(n):
        try:
            Valor_Dec = 0
            base = 1
            for digit in reversed(n):
                
                Valor_Dec += int(digit) * base
                base *= 3
            
            resultado_Bin = bin(Valor_Dec)[2:]
            return resultado_Bin
        except:
            show_banner()
            return "Invalido"

    def Bin_Cu(N_binario):
        try:
        
            while len(N_binario) % 2 != 0:
                N_binario = '0' + N_binario

            Diccionario = {
                '00': '0', '01': '1', '10': '2', '11': '3'
            }

            Cu_numero = ''
            for i in range(0, len(N_binario), 2):
                grupo = N_binario[i:i+2]
                Cuaternar_digito = Diccionario[grupo]
                Cu_numero += Cuaternar_digito

            return Cu_numero
        except:
            show_banner()
            return "Invalido"

    def Bin_Ter(N_binario):
        try:
            while len(N_binario) % 2 != 0:
                N_binario = '0' + N_binario

            Valor_Dec = 0
            for i in range(len(N_binario)):
                Valor_Dec = Valor_Dec * 2 + int(N_binario[i])

            third_num = ''
            while Valor_Dec > 0:
                third_num = str(Valor_Dec % 3) + third_num
                Valor_Dec //= 3

            return third_num or '0'
        except: 
            show_banner()
            return "Invalido"

    def Hex_Cu(hex_num):
        try:
            binario = ''
            for digit in hex_num:
                binario += format(int(digit, 16), '04b')
            return Bin_Cu(binario)
        except:
            show_banner()
            return "Invalido"

    def Hex_Ter(hex_num):
        try:
            binario = ''
            for digit in hex_num:
                binario += format(int(digit, 16), '04b')
            return Bin_Ter(binario)
        except:
            show_banner()
            return "Invalido"
    
    def Dec_Ter(numero):
        try:
            Ter_digito = '012'
            ter = ''

            while numero > 0:
                ter = Ter_digito[numero % 3] + ter
                numero //= 3

            return ter or '0'
        except:
            show_banner()
            return "Invalido"
    def Dec_Cu(numero):
        try:
            digito_Cu = '0123'
            Cuart = ''

            while numero > 0:
                Cuart = digito_Cu[numero % 4] + Cuart
                numero //= 4

            return Cuart or '0'
        except:
            show_banner()
            return "Invalido"
        
    def cuartenar_a_terciar(numero_cuartenar):
        try:
            decimal = 0
            base = 1
            for digito in reversed(numero_cuartenar):
                decimal += int(digito) * base
                base *= 4

        
            terciar = ''
            while decimal > 0:
                terciar = str(decimal % 3) + terciar
                decimal //= 3

            return terciar
        except:
            show_banner()
            return "Invalido"
    
    def Ter_Cua(numero_terciar):
        try:
        
            decimal = 0
            base = 1
            for digito in reversed(numero_terciar):
                decimal += int(digito) * base
                base *= 3

            
            cuartenar = ''
            while decimal > 0:
                cuartenar = str(decimal % 4) + cuartenar
                decimal //= 4

            return cuartenar
        except:
            show_banner()
            return "Invalido"

ft.app(target=main)
