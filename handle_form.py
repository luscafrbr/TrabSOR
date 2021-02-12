# vamos começar

import cgitb
import cgi

cgitb.enable()

form = cgi.FieldStorage()

nome = form.getvalue('pnome')
email = form.getvalue('oemail')
escola = form.getvalue('escola')
cpf = form.getvalue('cpf')
comentario = form.getvalue('comentario')
disciplinas = []

if form.getvalue('sor1'):
    sor1 = "Sistemas Operacionais de Redes 1"
    disciplinas.append(sor1)
else:
    sor1 = 0

if form.getvalue('bd'):
    bd = "Bancos de Dados"
    disciplinas.append(bd)
else:
    bd = 0

print("Content-type:text/html\r\n\r\n")
print("""<html>
            <head>
                <meta charset=\"UTF-8\">
                <title>Título</title>
            </head>
            <body>""")

print("<h1>Dados do form</h1><hr>")

print("<table border=1>")
print("""
        <tr>
         <th>Nome</th>
         <th>Disciplinas favoritas</th>
         <th>Comentários</th>
        </tr>""")
print("""<tr>
        <td>{}</td>
         <td>{}</td>
         <td>{}</td>
        </tr>""".format(nome+email, disciplinas, comentario))
print("</table>")

# print(form.keys())
# print(form.value)

print("</body></html>")