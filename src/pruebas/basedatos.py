<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="/static/js/libs/jQuery.min.js"></script>
    <link rel="stylesheet" href="//use.fontawesome.com/releases/v5.0.7/css/all.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

    <style>
        *{
            margin: 0;
            padding: 0;
        }

        body .page {
        width: 90%;
        max-width: 100%;
        margin: 20px auto;
        display: flex;
        flex-direction: column;
        align-items: start;
        }



        body *{
            box-sizing: border-box;
            text-rendering: auto;
            -webkit-font-smoothing: antialiased;
            font-family: "Roboto" , sans-serif;
            letter-spacing:0.4px;
            font-size: 14px;
        }

        .page{
            width: 100%;
        }

        .content{
            width: 100%;
        }
        table{
            width: 100%;
            height: auto;
            border-collapse: separate;
            max-width: 100%;
            border-bottom: solid 1px;

        }

        thead{
            width: 100%;
            text-align: center;
            color: #4285f4;
        }
        th{
            padding: 20px 0;
            color: black;
            border-bottom: solid 1px;

        }

        tr{
            background-color: #ececec;
            width: 100%;
        }

        tr:nth-child(odd) {
            background-color: white;
        }

        td{
            margin: 10px 0;
            width: 20%;
            max-width: 25%;
            height: 15%;
            padding: 2px 5px;
            text-align: center;
            color: black;
            word-break: break-word;
        }
        .filter {
            color: #446Ca9;
            font-size: 1.5rem;
            width: 20%;
            text-align: left;
        }
        .filter input{
            width: 100%;

        }
        label{
            font-size: 25px;
        }

        button{
            appearance: none;
            border: none;
            cursor: pointer;
        }

        @media (max-width: 1060px) {
            .container{
                display: flex;
                flex-direction: column;
            }
        }
        /*Posicion y tamaño de los botones añadir, eliminar y actualizar*/
        .fa-minus-circle,.fa-plus-circle,.fa-edit{
            cursor: pointer;
            font-size: 18px;
            margin: 0 10px;
        }
        /*Resaltar el boton de añadir*/
        .fa-plus-circle:hover{
            transform: scale(1.2);
            color: green;

        }
        /*Resaltar el boton de eliminar*/
        .fa-minus-circle:hover{
            transform: scale(1.2);
            color: red;
        }
        /*Resaltar el boton de editar*/
        .fa-edit:hover{
            transform: scale(1.2);
            color:blue;
        }
        /*Este es la posicion del popup*/
        .popup_wrapper_saved,.popup_wrapper_update{
            width: 100%;
            height: 95vh;
            position: absolute;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            /*Propiedad para mostrar (display) un elemento o no*/
            display: none;
        }
        /*Es necesario darle opacidad al popup para no poder pinchar fuera*/
        /*De el cuando esta fuera*/
        .opacity_saved,.opacity_update{
            width: 100%;
            height: 100vh;
            position: absolute;
        }
        /*Posicionamiento colores y datos del popupp*/
        .popup_content_saved,.popup_content_update{
            height: 15vh;
            width: 60%;
            background-color: rgba(68,108,169 ,1);
            position: absolute;
            display: flex;
            justify-content: center;
            align-items: center;border-radius: 10px;
            box-shadow: 0 0 30px grey;
        }
        /*Botones del enviar y cancelar dentro del popup*/
        .popup_buttons_saved,.popup_buttons_update{
            margin-top: 10px;
            display: flex;
            justify-content: center;
        }
        /*Posicion de los botones enviar y cancelar dentro del popup*/
        .popup_buttons_saved button,.popup_buttons_update button{
            width: 30%;
            margin: 0 0;
            margin: 0 1em;
        }

        img{
            width: 150px;
        }


    </style>
</head>

<body>

    <div class="popup_wrapper_saved">
        <div class="opacity_saved"></div>
        <div class="popup_content_saved">
            <div>

                <select name="collection" class="select_tipo data">
                <option selected disabled>Selecciona Libreria</option>
                    {% for i in tipos %}
                <option value='{{ i }}'>{{ i }}</option>
                    {%endfor%}
                </select>
                <input type="text" class="data" name="nombre" placeholder="Nombre">
                <input type="text" class="data" name="autor" placeholder="Autor">
                <input type="date" class="data" name="fecha" value="fecha">

                <div class="popup_buttons_saved">
                    <button id="send">Enviar</button>
                    <button id="cancel">Cancelar</button>
                </div>

            </div>
        </div>
    </div>
    <div class="popup_wrapper_update">
        <div class="opacity_update"></div>
        <div class="popup_content_update">
            <div>
<!--            El imnput se puede hacer de type="hidden para que no se muestre
                y que la informacion aunque se autocomplete no se viera"-->
                <input class="data_update" name="collection" readonly>
                <input class="data_update" name="id" readonly>
                <input type="text" class="data_update" name="nombre" placeholder="Nombre">
                <input type="text" class="data_update" name="autor" placeholder="Autor">
                <input type="date" class="data_update" name="fecha" value="fecha">

                <div class="popup_buttons_update">
                    <button id="update">Modificar</button>
                    <button id="cancelar">Cancelar</button>
                </div>

            </div>
        </div>
    </div>
    <div class="page">
        <div class = "filter">
            <label for="filtro">Filtro</label>
            <br>
            <input id="filtro" type="text">
        </div>
        <div class="content">

            <table>
                <thead>
                    <th>ID Coleccion</th>
                    <th>ID Documento</th>
                    <th>Nombre</th>
                    <th>Autor</th>
                    <th>Fecha</th>
                    <th><i class="fas fa-plus-circle"></i></th>
                    <th>IMAGEN</th>
                </thead>
                    <tbody id="myTable">
                    {% for k in dict.keys() %}
                        {% for x,v in dict[k].items() %}
                            <tr>
                                <td name="coleccion" id="coleccion">{{k}}</td>
                                <td name="id" id="documento">{{x}}</td>
                                <td name="nombre">{{v.nombre}}</td>
                                <td name="autor">{{v.autor}}</td>
                                <td name="fecha">{{v.fecha}}</td>
                                <td><i class="fas fa-edit"></i><i class="fas fa-minus-circle"></i></td>
<!--                                Para meter la imagen, entras en la imagen completamente hasta visualizarla -->
<!--                                dentro de firebase y copias esa url, dentro del campo le metes el campo tipo-->
<!--                                imagen como STR importante y pegas la url
                                    Ejemplo-->
                                <!--https://firebasestorage.googleapis.com/v0/b/projectoalvaro.appspot.com/o/gatoleyendo.gif?alt=media&token=1267d1b7-acbf-47f5-ac0c-c67fc8b6cf8f
-->
                                <td><img src="{{v.imagen}}" alt=""></td>
                            </tr>
                        {% endfor %}
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>

</html>
<script>

    $(document).ready(function(){

        //Función para filtrado de datos
        $("#filtro").on("keyup", function() {
            var value = $(this).val().toLowerCase();
            $("#myTable tr").filter(function() {
                $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        });
        // boton insertar
        $(".fa-plus-circle").click(function (){
            $(".popup_wrapper_saved").css("display", "flex")

        })
        //Boton actualizar
        $(".fa-edit").click(function(){
            $(".popup_wrapper_update").css("display", "flex")
            let id_coleccion = $(this).parent().siblings("#coleccion").text();
            let id_documento = $(this).parent().siblings("#documento").text();
            $("input[name='collection']").val(id_coleccion);
            $("input[name='id']").val(id_documento);

        })

        //Boton cancelar dentro del popup
         $("#cancel").on("click", function (){
            $(".popup_wrapper_saved").css("display", "none")
        });

        //Boton cancelar dentro del popup update
         $("#cancelar").on("click", function (){
            $(".popup_wrapper_update").css("display", "none")
        });


        //Función del botón enviar
        $("#send").on("click", function (){
            //data= son los datos del diccionario vacio
            let data={}
            //data_list= me va a devolver una lista de inputs
            let data_list = $(".data");
            //each es un for que recorre todos los inputs
            $.each(data_list, function (){
                //this hace referencia al elemento por el que va en cada vuelta
                //
                data[$(this).attr("name")] = $(this).val();
            })

            data["accion"] = "insertar";
            //Envio de datos a la base de datos nuevos con el post
            $.ajax({
                method: "POST",
                url: "/libreria",
                data: JSON.stringify(data),
                contentType: 'application/json',
                success: (response) =>{
                    if(response != ""){
                        console.log(response);
                        alert("libro o revista guardado con éxito");
                        // esto de window.location se pone para que actualice la pagina automatica
                        //nada mas darle al enviar
                        window.location.reload(window.location.href);
                    }
                }
            });
        })

        //Boton eliminar
        $(".fa-minus-circle").click(function (){
        let padre_boton = $(this).parent();
        let hermanos = padre_boton.siblings();
        let data ={}
        $.each(hermanos, function (){
            if (hermanos.index($(this)) === 0){
                data["coleccion"] = $(this).attr("id");
                data["documento"] = $(this).text();
            }
        })
        data["accion"] = "eliminar";


        $.ajax({
            method: "POST",
            url: "/libreria",
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: (response) => {
                console.log(response);
                alert("Datos eliminados");
                window.location.reload(window.location.href);
            }
        });
        })

        //Boton modificar
        $("#update").on('click',function(){
            let data={}
            let data_list = $(".data_update");
            $.each(data_list, function (){
                data[$(this).attr("name")] = $(this).val();
            })
        data["accion"] = "actualizar";
        console.log(data)
        $.ajax({
            method: "POST",
            url: "/libreria",
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: (response) => {
                console.log(response);
                alert("Datos Actualizados con exito");
                window.location.reload(window.location.href);
            }

        })
        })

  });

</script>
