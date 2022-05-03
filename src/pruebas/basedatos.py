import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

from flask import render_template

from src.pruebas import app

cred = credentials.Certificate(
    "/Users/practicasbackend/Downloads/projectoalvaro-firebase-adminsdk-api39-1644f7c6bf.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/libreria", methods=["POST", "GET"])
#     El lunes vamos a recuperar datos del popup y añadirlos al servidor
#def add_data(añadir):
#     data = {
#         u'autor': autor,
#         u'fecha': fecha,
#         u'nombre': nombre
#
#     }
#     users_ref = db.collection(collection)
#     docs = users_ref.stream()
#     db.collection(collection).document(document).set(data)
#     for i in docs:
#         return(collection +" "+ f'{i.id} => {i.to_dict()}')

def show_firebase():
    lista_libros = []
    lista_revistas = []
    libros = db.collection("libros").get()
    for x in libros:
        lista_libros.append(x.to_dict())

    revistas = db.collection("revistas").get()
    for x in revistas:
        lista_revistas.append(x.to_dict())

    print(lista_libros)
    print(lista_revistas)

    context = {
        "libros": lista_libros,
        "revistas": lista_revistas
    }

    return render_template("BaseCalculadora.html", **context )



    # for doc in db.collection(search):
    #     print("hola")
    #     lista.append(doc.to_dict())
    # for doc in db.collection(search2):
    #     lista.append(doc.to_dict())
    #
    # cosas= db.collection('libros').document('0').get()
    # print(cosas)
    #
    # context = {
    #     'cosas': cosas
    #
    #
    # }

    #return render_template("BaseCalculadora.html", **context)

#add_data("libros","5",'jonan', 'comon','25-5-2021')
#return render_template("BaseCalculadora.html", **context)
#def search_database(collection, collection2):



    #  return render_template("BaseCalculadora.html", **context)
#     return ('holamundo')

#db.collection('jode').delete()
#search_database("libros","revistas")

# def delete_collection(collection):
#     docs = collection.stream()
#     deleted = 0
#
#     for doc in docs:
#         print(f'Deleting doc {doc.id} => {doc.to_dict()}')
#         doc.reference.delete()
#         deleted = deleted + 1


#delete_collection("data")
# def filter_list(lista:list, fecha:str):
#
#     for x in lista:
#         if fecha <= x["fecha"]:
#             print(x)


# filter_list(search_database('libros','revistas','autor','Alvaro'), "01-01-2020")
