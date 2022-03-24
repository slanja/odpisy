import math
from prettytable import PrettyTable

while True:
	######## Inputy ##########
	try:
		vstupni_cena = int(input("Zadej vstupní cenu: "))
		odpisova_skupina = input("Zadej odpisovou skupinu: ")
		typ_odpisu = input("[R]Rovnoměrný / [Z]Zrychlený: ").lower()
		print()
	except ValueError as e:
		print("Když to musí bejt")
	except Exception as e:
		print(e)

	######## Odpisová skupina - Rovnoměrná ##########
	try:
		if typ_odpisu.startswith("r"):
			match odpisova_skupina:
				case "1":
					odpis_prvni_rok = 20
					dalsi_roky = 40
					doba_odpisovani = 3
				case "2":
					odpis_prvni_rok = 11
					dalsi_roky = 22.25
					doba_odpisovani = 5
				case "3":
					odpis_prvni_rok = 5.5
					dalsi_roky = 10.5
					doba_odpisovani = 10
				case "4":
					odpis_prvni_rok = 2.15
					dalsi_roky = 5.15
					doba_odpisovani = 20
				case "5":
					odpis_prvni_rok = 1.4
					dalsi_roky = 3.4
					doba_odpisovani = 30
				case "6":
					odpis_prvni_rok = 1.02
					dalsi_roky = 2.02
					doba_odpisovani = 50

		######## Odpisová skupina - Zrychlená ##########
		elif typ_odpisu.startswith("z"):

			match odpisova_skupina:
				case "1":
					odpis_prvni_rok = 3
					dalsi_roky = 4
					doba_odpisovani = 3
				case "2":
					odpis_prvni_rok = 5
					dalsi_roky = 6
					doba_odpisovani = 5
				case "3":
					odpis_prvni_rok = 10
					dalsi_roky = 11
					doba_odpisovani = 10
				case "4":
					odpis_prvni_rok = 20
					dalsi_roky = 21
					doba_odpisovani = 20
				case "5":	
					odpis_prvni_rok = 30
					dalsi_roky = 31
					doba_odpisovani = 30
				case "6":
					odpis_prvni_rok = 50
					dalsi_roky = 51
					doba_odpisovani = 50

	except NameError as e:
		print("Takhle to nepůjde!")
	except Exception as e:
		print(e)

	######## Rovnoměrné ##########
	try:
		if typ_odpisu.startswith("r"):
			try:
				zustatek = vstupni_cena
				opravky = 0 

				table = PrettyTable(["Odpis", "Opravky", "Zůstatek"])
				
				for rok in range(doba_odpisovani):
					if rok == 0:
						odpis = math.ceil(vstupni_cena*odpis_prvni_rok*0.01)
					else:
						odpis = math.ceil(vstupni_cena*dalsi_roky*0.01)

					opravky += math.ceil(odpis)
					zustatek -= odpis
						
					table.add_row([odpis, opravky, zustatek])
				table.add_autoindex("Rok")
				print(table)

			except NameError as e:
				print("Zadej číslo né písmeno")
			except Exception as e:
				print(e)

		######## Zrychelené ##########
		elif typ_odpisu.startswith("z"): 
			try:

				zustatek = vstupni_cena
				opravky = 0

				table = PrettyTable(["Odpis", "Opravky", "Zůstatek"])

				for rok in range(doba_odpisovani):
					if rok == 0:
						odpis = math.ceil(zustatek / odpis_prvni_rok)
					else:
						odpis = math.ceil((2 * zustatek) / (dalsi_roky - rok))	       

					opravky += math.ceil(odpis)  
					zustatek -= odpis

					table.add_row([odpis, opravky, zustatek])
				table.add_autoindex("Rok")
				print(table)

			except NameError as e:
				print("Zadej číslo né písmeno")
			except Exception as e:
				print(e)

	except NameError as e:
		print("Vážně")
	except Exception as e:
		print(e)

	again = input("Chceš počítat dále? ano/ne ").lower()

	if again != "ano":
		break
	else:
		pass
