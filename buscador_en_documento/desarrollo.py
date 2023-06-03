import PyPDF2
print ('Vamos a hacer cosas con un pdf...')
biblioteca = open('Biblioteca.pdf', 'rb')

lectura = PyPDF2.PdfReader(biblioteca)
print (lectura)


