texto = "La transformación digital, se ha convertido en el eje actual del desarrollo tecnológico, impregnando los comportamientos sociales, y en tal sentido, se ha originado una suerte de necesaria fusión del trabajo con la tecnología, de tal manera que nos encontramos inmersos en un proceso de cambios acelerados respecto del futuro del trabajo.Las revoluciones industriales se han dado en la historia como consecuencia de la búsqueda del ser humano para mejorar sus condiciones de vida, sin embargo, siempre ha existido el temor de que, con las innovaciones, el hombre quede “obsoleto” frente a las futuras actividades.Ya han ocurrido tres revoluciones industriales y en la actualidad estamos en proceso de la cuarta, la revolución 4.0, el trabajo se transforma: de la mecanización y la producción en serie, la deslocalización de los trabajadores del campo al trabajo en fábricas en las ciudades, al desarrollo de los medios de transporte y los medios de comunicación masiva, hasta la informática y la digitalización, se han atravesado fronteras y convertido los mercados laborales en globales y cada vez más interdependientes.Las innovaciones de la tecnología digital dan lugar a nuevas tareas y la digitalización de las empresas crece aceleradamente ofreciendo nuevos productos y servicios, la sociedad cambia a toda velocidad especialmente en la convergencia de las distintas tecnologías.En este sentido, se han producido cambios esenciales de los paradigmas del trabajo tradicional, al integrar a la prestación de tareas las herramientas digitales, la utilización del universo de las TICs (tecnologías de la información y comunicación), con la conectividad masiva de Internet, el manejo de datos e información (Big Data), el desarrollo de las denominadas, economía colaborativa, la Gig Economy y la economía bajo demanda, la incorporación de trabajadores asociados a las plataformas (App) y la interacción en el mundo digital a través de la Nube, la Robótica, el Internet de las cosas y la Inteligencia Artificial (IA)."

simbolos_a_quitar = ("," , "." , "(" , ")")

for simbolo in simbolos_a_quitar:
    texto = texto.replace(simbolo,"")

texto = texto.upper()#VUELVE MAYUSCULAS

vocablos = texto.split()#SEPARA CADA PALABRA EN UNA LISTA
palabras = {}
for vocablo in vocablos:
    if vocablo in palabras.keys():
        palabras[vocablo]=palabras[vocablo]+1#INCREMENTA EL VALOR
    else:
        palabras[vocablo]= 1

lista = list(palabras.items())

lista.sort(key= lambda palabra : palabra[1])#ORDENAR DE FORMA ALFABETICA solo sor //POR EL NUMERO DE ITERACIONES CON LAMBDA
print(lista)