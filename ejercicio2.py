#Crea una función llamada invertir_cadena que utilice la recursividad para revertir una
#cadena dada. La función debería tomar una cadena como argumento y devolver una nueva
#cadena que sea la versión invertida de la original.?

def reverse_version(version):
    if isinstance(version, str):
        version_parts = version.split('.')
        reversed_version_parts = version_parts[::-1]
        reversed_version = '.'.join(reversed_version_parts)
        return reversed_version
    else:
        raise TypeError('version must be a string')

version = '1.2.3'
print(reverse_version(version)) 