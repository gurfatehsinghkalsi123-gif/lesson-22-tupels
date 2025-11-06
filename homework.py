gurfateh = (1, 3, 4)
vardaan = (1, 4, 5)


result = tuple(gurfateh[i] * vardaan[i] for i in range(len(gurfateh)))

print("Gurfateh:", gurfateh)
print("Vardaan:", vardaan)
print("Result:", result)
