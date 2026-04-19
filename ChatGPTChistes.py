# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Base de datos de conversaciones
conversations = ["Me encantan los mensajes de voz. Yo los detesto. Sí, esos también molan.",
"¿Qué hace un mudo bailando? Una mudanza.",
"Hola, busco trabajo. ¿Le interesa de jardinero? ¿Dejar dinero? ¡Si lo que busco es trabajo!",
"¿Qué le dice una impresora a otra? Esta hoja es tuya o es impresión mía.",
"¿Qué tal tu primer día de parkour? De futa madfre",
"Me acabo de tirar un pedo de esos silenciosos, ¿qué hago? Ahora nada, pero, cuando llegues a casa, cámbiale las pilas al audífono",
"Me han despedido ¿Y qué vas a hacer? Croquetas. Digo con tu vida. Pues comerme unas croquetas",
"¿Me da un café con leche corto? Se ha roto la máquina, cambio",
"Buenas, quería una camiseta de un personaje inspirador. ¿Ghandi? No, mediani",
"¿Sabes por qué no se puede discutir con un DJ? Porque siempre están cambiando de tema.",
"¿Qué le dice un semáforo a otro semáforo? No me mires, me estoy cambiando.",
"No sé si conseguiré enamorar a esa chica. ¿Tienes vacas y ovejas? Sí. Pues ya tienes mucho ganado",
"¿Qué hace un perro con un taladro? Ta-ladrando.",
"¿Qué le dice un pingüino a una pingüina? ¡Como tú ningüina!",
"¿Qué hace una abeja en el gimnasio? Zumba.",
"¿Sabes? Hoy me he comprado una paloma que cuesta diez mil euros ¿Mensajera? No no, no te exagero en absoluto.",
"¿Qué le dice la foca a su madre? I love you, mother foca.",
"¿Y qué le dice una morsa a otra morsa? ¿Almorsamos o qué?",
"¿Por qué los patos no tienen amigos? Porque son muy antipáticos.",
"¿Y qué le dice un pato a otro pato con el que estaba compitiendo en una carrera? Hemos empatado.",
"¿Qué le dice un chinche a una chinche? Te amo chincheramente.",
"¿Por qué las focas del circo miran siempre hacia arriba? Porque es donde están los focos.",
"Había una vez un niño tan, tan, tan despistado que... ¡da igual, me he olvidado del chiste!",
"¿Qué le dice un techo a otro? Techo de menos.",
"¿Qué le dice un árbol a otro? ¡Qué pasa tronco!",
"¿Cuál es el último animal que subió al arca de Noé? El del-fin.",
"¿Cómo se dice pañuelo en japonés? Saka-moko.",
"Hijo, me veo gorda, fea y vieja. ¿Qué tengo hijo, qué tengo? Mamá, tienes toda la razón.",
"¿Cuál es el colmo de Aladdín? Tener mal genio.",
"¿Qué es un pez en el cine? Pues un mero espectador...",
"¿Qué le dice un espagueti a otro? ¡Oye, mi cuerpo pide salsa!",
"¿Por qué los espejos no utilizan WhatsApp? Porque se reflejan en el pasado.",
"¿Qué le dice un pendrive a otro? Eres mi puerto USB de la vida.",
"¿Cómo se llama el campeón de programación? Juan Decódigo.",
"¿Por qué los programadores siempre llevan una chaqueta? Porque en el código siempre hace frío.",
"¿Cuál es el animal más peligroso de Internet? El mouse-tro.",
"¿Qué le dice un GIF animado a otro? Nos vemos en el próximo bucle.",
"¿Por qué los robots no tienen amigos? Porque son todos circuitos cerrados.",
"¿Cómo se llama el primer superhéroe que apareció en Internet? Spider-Manual.",
"¿Qué le dice un altavoz a otro? Nos vemos en el sonido.",
"¿Por qué el libro de matemáticas se volvió un influencer? Porque tenía muchos seguidores.",
"¿Por qué los cables de internet son tan tímidos? Porque siempre se esconden detrás de los routers.",
"¿Cómo se llama el sobrino del ratón Mickey que sabe programar? ¡Data!",
"¿Qué hace un celular en el gimnasio? ¡Ejercicios de flexión de aplicaciones!",
"¿Por qué el robot no va al gimnasio? Porque ya está bien programado.",
"¿Cómo llama un móvil a otro móvil? ¡Celular hermano!",
"¿Qué hace un perro en el espacio? ¡Un dog-italizador!",
"¿Por qué los peces no utilizan computadoras? Porque tienen miedo del spyware.",
"¿Por qué el smartphone fue al psicólogo? Porque tenía problemas de conexión emocional.",
"¿Qué le dijo el celular al enchufe? Eres mi media naranja.",
"¿Cuál es el animal más tecnológico? ¡El mouse!",
"¿Por qué el programador siempre está frío? Porque siempre está rodeado de ventiladores.",
"¿Cómo se llama el hijo de un laptop y una tablet? ¡Un niño portátil!",
"¿Cuál es el superhéroe favorito de un programador? ¡Ctrl + S (Guardar) Man!",
"¿Qué le dijo un bit al otro? ¡Nos vemos en el byte!",
"¿Por qué los robots no tienen hermanos? Porque son hijos únicos.",
"Me he comprado una mosquitera es tupidita. Vale gilipollitas",
"Papá papá, qué está más lejos, Murcia o la luna? Joder hijo, que tonterías preguntas, tu desde aquí puedes ver Murcia???"
]

# Eliminar caracteres especiales y convertir a minúsculas
def preprocess_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c.isalnum() or c.isspace()])
    return text

# Preprocesar la base de datos
preprocessed_conversations = [preprocess_text(conv) for conv in conversations]

# Tokenizar la base de datos
tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_conversations)
total_words = len(tokenizer.word_index) + 1

# Crear secuencias de entrada y salida
input_sequences = []
for line in preprocessed_conversations:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_length = max([len(seq) for seq in input_sequences])
padded_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

# Compilar el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 100, input_length=max_sequence_length-1),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(150)),
    tf.keras.layers.Dense(total_words, activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Crear datos de entrenamiento
X = padded_sequences[:, :-1]
y = padded_sequences[:, -1]

# Entrenar el modelo
model.fit(X, y, epochs=100, verbose=1)

# Función para generar respuestas
def generate_response(input_text, max_words=20):
    input_text = preprocess_text(input_text)
    input_sequence = tokenizer.texts_to_sequences([input_text])[0]
    input_sequence = pad_sequences([input_sequence], maxlen=max_sequence_length-1, padding='pre')
    
    generated_words = []
    for _ in range(max_words):
        predicted_probabilities = model.predict(input_sequence, verbose=0)[0]
        predicted_word_index = tf.argmax(predicted_probabilities).numpy()
        predicted_word = tokenizer.index_word[predicted_word_index]
        generated_words.append(predicted_word)
        
        input_sequence = pad_sequences([input_sequence[0].tolist() + [predicted_word_index]],
                                       maxlen=max_sequence_length-1, padding='pre')
        
        if predicted_word == '<eos>':  
            break
    
    return ' '.join(generated_words)

# Interacción con el usuario
print("¡Hola! Soy un ChatGPT. Puedes empezar la conversación.")
while True:
    user_input = input("Usuario: ")
    if user_input.lower() == 'salir':
        print("ChatGPT: ¡Hasta luego!")
        break
    response = generate_response(user_input)
    print("ChatGPT:", response)
