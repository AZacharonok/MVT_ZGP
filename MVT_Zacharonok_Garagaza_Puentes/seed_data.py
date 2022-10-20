from App1.models import familiar

familiar(nombre="Tia", ciudad="Bariloche", dni=21111111, fecha_nacimiento="1960-02-04").save()
familiar(nombre="Primo", ciudad="Buenos Aires", dni=1222222, fecha_nacimiento="1965-04-05").save()
familiar(nombre="Abuela", ciudad="Santa Fe", dni=4333333, fecha_nacimiento="1940-12-03").save()


print("Se cargaron los usuarios correctamente.")