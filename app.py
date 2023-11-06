import os
import json
import openai
import PyPDF2
from glob import glob
from flask_cors import CORS
from flask import Flask, render_template, request, jsonify, send_from_directory, redirect

openai.api_key = ''

app = Flask(__name__)
CORS(app)

# UPLOAD_FOLDER = './uploaded_files'  # Set the upload folder to the directory you created
UPLOAD_FOLDER = '/tmp/uploaded_files'  # Set the upload folder to the directory you created
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configure the Flask app to use this upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


deb = 'development' ### local deployment (my laptop, right now)
# deb = 'production' ### production deployment (google app engine, later)

@app.route('/')
def index():
    if deb == 'development':
        return redirect("http://localhost:8080/")  # Redirect to Vue.js dev server
    elif deb == 'production':
        return send_from_directory('./frontend/dist', 'index.html')  # Serve built static files

@app.route('/questions', methods=['GET'])
def get_questions():
    question_mapping = {
        1: "¿El solicitante provee Documento fundacional con nombre legal/operativo, Confirmación de estatus legal y áreas permitidas, Capacidad para acuerdos, incluido el AMA con el GCF, Titularidad beneficiaria de la AE., Capacidad para pagos con GCF? Se requiere opinión o certificado legal satisfactorio para el GCF, ya sea de una firma reconocida, un oficial del gobierno o el oficial legal más senior del solicitante.",
        2: "En terminos del tipo de institucion, ¿el solicitante selecciona el tipo de institución (por ejemplo, nacional, sector privado, etc.); y evidencia que demuestre experiencia con el 'tipo' de institución seleccionada?",
        3: "En terminos de Estructura organizativa, tamaño y ubicación de la institución, ¿el solicitante provee Documento sobre la estructura organizacional, Número total de empleados, Ubicación de la oficina principal y de cualquier otra oficina(s)?"
    }
    return jsonify(question_mapping)

@app.route('/upload/<int:questionNumber>', methods=['POST'])
def upload_file(questionNumber):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print(filename)
        file.save(filename)  # Save the file to the UPLOAD_FOLDER
        # Process the file right after it's saved
        message, answer = process_pdf(filename, questionNumber)
        # Return the answer
        return jsonify({"result":answer})

def process_pdf(pdf_path, questionNumber):
    
    # your provided code here, adjusted to work with the given pdf_path
    pdf_content = ''

    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(reader.pages)

        # Loop through each page
        for page_num in range(num_pages):
            # print(page_num)
            # Get a specific page
            page = reader.pages[page_num]

            # Extract text from the page
            text = page.extract_text()

            pdf_content+=text

            # print(f"Content from page {page_num + 1}:")
            # print(text)

            # if len(pdf_content)>18000:
            if len(pdf_content)>12000:
                break
    file.close()

    question_mapping = {
        1: "¿El solicitante provee Documento/Informacion fundacional con nombre legal/operativo, Confirmación de estatus legal y áreas permitidas, Capacidad para acuerdos, incluido el AMA con el GCF, Titularidad beneficiaria de la AE., o Capacidad para pagos con GCF?",
        # 1: "¿El solicitante provee Documento/Informacion fundacional con nombre legal/operativo, Confirmación de estatus legal y áreas permitidas, Capacidad para acuerdos, incluido el AMA con el GCF, Titularidad beneficiaria de la AE., Capacidad para pagos con GCF? Se requiere opinión o certificado legal satisfactorio para el GCF, ya sea de una firma reconocida, un oficial del gobierno o el oficial legal más senior del solicitante.",
        2: "En terminos del tipo de institucion, ¿el solicitante selecciona el tipo de institución (por ejemplo, nacional, sector privado, etc.); y evidencia que demuestre experiencia con el 'tipo' de institución seleccionada?",
        3: "En terminos de Estructura organizativa, tamaño y ubicación de la institución, ¿el solicitante provee Documento sobre la estructura organizacional, Número total de empleados, Ubicación de la oficina principal y de cualquier otra oficina(s)?"
        }

    keys_mapping = {
        1: "detalles_organizacionales",
        2: "type_organizacionales",
        3: "structure_organizacionales"
    }

    ans_mapping = {
        1: "Resultado de la consulta ...",
        2: "Resultado de la consulta ...",
        3: "Resultado de la consulta ...",
    }
    
    prompt = (
        f"Estoy buscando automatizar el proceso de lecturas de documentos legales en formato pdf para la extraccion de informacion de interes sobre."
        f"\nAnaliza el contenido del documento proporcionado en el contexto de la revisión del historial de proyectos de acuerdo al GCF (Green Climate Fund)."
        # f"\nLa entidad debe presentar ejemplos de proyectos que ha implementado en el pasado que sean similares al proyecto propuesto en términos de tamaño, categoría de riesgo E&S e instrumentos y modalidades de financiamiento. Se espera información indicativa sobre:"
        f"\nSe espera extraer información sobre:"
        f"\n'{keys_mapping[questionNumber]}': {question_mapping[questionNumber]}"
        #   f"\n\nEn caso de encontrar la información, retornala; en caso de no encontrar la información, indica explícitamente la información faltante en el documento; finalmente devuelve la última línea del documento en cuestión. Evita a toda costa devolver un valor vacio."
          f"\n\nEn caso de encontrar la información, brinda un resumen; en caso de no encontrar la información, indica explícitamente la información faltante en el documento. Evita a toda costa devolver un valor vacio."
          
          f"" + "El modelo debería responder unicamente con un JSON estructurado de la siguiente manera: {"
          f'"{keys_mapping[questionNumber]}": ' + f'"{ans_mapping[questionNumber]}"' + '}'
          " \nCualquier output diferente a un json estructurado podria afectar gravemente al funcionamiento de todo el sistema y con consecuencias economicas muy graves."
          
          f"\n\nContenido del documento pdf:\n\n{pdf_content}"
          )

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
                                            # model="gpt-3.5-turbo",
                                            model = 'gpt-3.5-turbo-16k',
                                            # model = 'gpt-4',
                                            messages=messages
                                            )

    message = response['choices'][0]['message']['content']
    print(message)
    
    json_object = json.loads(message)
    answer = json_object[keys_mapping[questionNumber]]
    if answer.endswith(".")==False:answer+="."
    # json_obj = (f"""¿El documento contiene información sobre la personalidad legal de la institución?\n{json_object['detalles_organizacionales']}\n\n¿El documento provee la estructura de la organización?\n{json_object['info_supervision']}\n\n¿Desde que año funciona en el país legalmente?\n{json_object['historial_previo']}""")
    
    # print(json_obj)

    # with open("json_cv_extraction.json", "w") as file:
    #     json.dump(json_obj, file)
    # file.close()

    # Saving the JSON to the download directory
    # json_file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], 'json_cv_extraction.json')
    # with open(json_file_path, "w") as file:
    #     json.dump(json_obj, file)
    # file.close()

    # return json_file_path, json_obj
    return message, answer

@app.route('/process_files', methods=['POST'])
def process_files():

    json_O = "{'detalles_organizacionales':'', 'info_supervision':'', 'historial_previo':''}"

    files = glob("/tmp/uploaded_files/*")
    for fiile in files:
        json_O = process_pdf(fiile, json_O)
    
    json_object = json.loads(json_O)

    # TODO: Implement your processing logic here.
    # For now, it will just return a dummy message.
    # return jsonify({'result': 'Files processed successfully'})
    return jsonify(json_object)

if __name__ == "__main__":
    app.run(debug=True)
