# Nicole Robles NC 0120
#  ejemplo 1 ( del 1 al 30 )
import cv2

# Cargar la imagen asignada
# Asegúrate de colocar la ruta correcta o el nombre de la imagen de tu actividad
imagen = cv2.imread('garza 0120..jpg')

if imagen is None:
    print("Error al cargar la imagen. Revisa la ruta.")
else:
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar un filtro de desfoque Gaussiano (Gaussian Blur)
    suavizada = cv2.GaussianBlur(gris, (7, 7), 0)

    # Mostrar resultados
    cv2.imshow('Imagen Original 0120', imagen)
    cv2.imshow('Escala de Grises 0120', gris)
    cv2.imshow('Filtro Gaussiano 0120 (Ejemplo 1)', suavizada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ejemplo 4 (31 al 60 )

    import cv2

# Cargar la imagen asignada
imagen = cv2.imread('garza 0120..jpg')

if imagen is None:
    print("Error al cargar la imagen. Revisa la ruta.")
else:
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detección de bordes con Canny
    bordes = cv2.Canny(gris, threshold1=100, threshold2=200)

    # Mostrar resultados
    cv2.imshow('Imagen Original 0120', imagen)
    cv2.imshow('Deteccion de Bordes 0120 (Ejemplo 4)', bordes)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("Nicole Robles NC 0120")
