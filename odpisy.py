while True:
	######## Inputy ##########
	vstupni_cena = int(input("Zadej vstupní cenu: "))
	odpisova_skupina = input("Zadej odpisovou skupinu: ")
	typ_odpisu = input("[R]Rovnoměrný / [Z]Zrychlený: ").lower()
	print()

	######## Odpisová skupina - Rovnoměrná ##########
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

	######## Rovnoměrné ##########
	if typ_odpisu.startswith("r"): 
		odpis_jedna = vstupni_cena*odpis_prvni_rok*0.01

		print(" o₁ = {},-".format(round(odpis_jedna)))

		for i in range(doba_odpisovani):
			odpis_dve = vstupni_cena*dalsi_roky*0.01
			print(" o = {},-".format(round(odpis_dve)))
	 
	######## Zrychelené ##########
	elif typ_odpisu.startswith("z"): 
		odpis_jedna = vstupni_cena/doba_odpisovani-1
		for i in range(doba_odpisovani):
			odpis_dve = (vstupni_cena-odpis_jedna)*2/doba_odpisovani-2
			odpis_tri = (vstupni_cena-odpis_dve)*2/doba_odpisovani-3
			odpis_ctyri = (vstupni_cena-odpis_tri)*2/doba_odpisovani-4
			odpis_pet = (vstupni_cena-odpis_ctyri)*2/doba_odpisovani-5
			print(" o₁ = {},- \n o₂ = {},- \n o₃ = {},- \n o₄ = {},- \n o₅ = {},-".format(round(odpis_jedna), round(odpis_dve), round(odpis_tri), round(odpis_ctyri), round(odpis_pet)))

	again = input("Chceš počítat dále? ano/ne ").lower()

	if again != "ano":
		break
	else:
		print("")
		pass