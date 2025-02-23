def log(tag="", msg=""):
    with open("my_log.txt", "w+") as file:
        file.write(f"{tag} : {msg}\n")
