import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

from flask import render_template, request
from flask.views import MethodView

from src.pruebas import app

cred = credentials.Certificate(
    "/Users/practicasbackend/Downloads/projectoalvaro-firebase-adminsdk-api39-1644f7c6bf.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/libreria", methods=["POST", "GET"])

def show_firebase():
    if request.method == "GET":
        libros_dict = {}
        revistas_dict = {}
        tipos=['libros','revistas']
        libros = db.collection("libros").get()
        for x in libros:
            libros_dict[x.id] = x.to_dict()

        print(libros_dict)


        revistas = db.collection("revistas").get()
        for x in revistas:
            revistas_dict[x.id] = x.to_dict()

        context = {
            "libros": libros_dict,
            "revistas": revistas_dict,
            'tipos': tipos
        }

        return render_template("BaseCalculadora.html", **context)

    if request.method == "POST":

        body = request.json

        if body.get("accion") == "insertar":
            db.collection(body.get("collection")).add({
                "nombre": body.get("nombre"),
                "autor": body.get("autor"),
                "fecha": body.get("fecha")
            })

            return "Datos creados"

        elif body.get("accion") == "eliminar":

            db.collection(body.get("coleccion")).document(body.get("documento")).delete()
            return "Datos elimianados"

        elif body.get("accion") == "actualizar":

            collection_ref = db.collection(body.get("collection")).document(body.get("id"))
            collection_ref.set({
                "nombre": body.get("nombre"),
                "autor": body.get("autor"),
                "fecha": body.get("fecha")
            })

            return "Datos actualizados correctamente"

        else:
            return "No inventes"












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






