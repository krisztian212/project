def kozmetikaarak():
    #Előszöveg
    print("Hálózati eszközök megszámítása, és árának össze számolása")
    print("Add meg az üzletben lévő gépek árát!")

    #Árbekérések
    print()
    router= int(input("1db 'Router' beszerzési ára?:"))
    Switch= int(input("1db 'Switch' beszerzési ára?:"))
    Nyomtato= int(input("1db 'Nyomtató' beszerzési ára?:"))
    PC= int(input("2db 'Pc' beszerzési ára?:"))
    Laptop= int(input("1db 'Laptop' beszerzési ára?:"))
    print()

    #Árak listázása
    print("")
    print("(1db) Router ára:", router)
    print("(1db) Switch ára:", Switch)
    print("(1db) Nyomtató ára:", Nyomtato)
    print("(2db) Pc ára:", PC)
    print("(1db) Laptop ára:", Laptop)
    print("")

    #osszeszamitas
    print()
    print("Összesen:")
    print()
    print(router + Switch + Nyomtato + PC + Laptop, "FT")

#Főprogram
kozmetikaarak()