data = raw_input("Escribe algo: ")
vocales = "aeiou"
consonantes = "bcdfghijklmnopqrstuvwxy"
for v in vocales:
    print v, data.lower().count(v)
for c in consonantes:
    print c, data.lower().count(c)