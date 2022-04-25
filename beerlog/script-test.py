#print(1 + 1)
#print("python".upper())
#print(sum([1,2,3,4]))
################################################################################################################################################################


event = "Python Week"
topics = ["\N{snake} Python", "\N{whale} Containers", "\N{penguin} Linux"]

days = {
    1: "Introdução a Python",
    2: "Python para web",
    3: "Qualidade de código, testes e CI",
    4: "Análise de dados",
    5: "Perguntas"
}

print(f"Boas vindas a {event} - um evento de {len(days)} dias")
for topic in topics:
    print(f"{topic.upper()}")

for day, title in days.items():
    print(f"{day} -> {title}")
    if day == 1:
        print("\t é Hoje!!!")