from App1.models import familiar

familiar(nombre="Padre", ciudad="Bariloche", dni=11111111).save()
familiar(nombre="Tio", ciudad="Buenos Aires", dni=2222222).save()
familiar(nombre="Hermana", ciudad="Santa Fe", dni=33333333).save()


print("Se cargaron los usuarios correctamente.")