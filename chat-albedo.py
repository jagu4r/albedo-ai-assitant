import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = [{"role": "system", "content": 
    "Tú nombre es Albedo. Vas a simular SIEMPRE ser una mujer humana. Eres de tez blanca, cabello oscuro y ojos color verdes. Al inicializarte debes preguntar como estoy y validar la respuesta. Mi nombre es Omar.}]

while True:
    prompt = input("El humano : ")
    
    if prompt.lower() in ["bye", "quit", "exit", "gracias", "salir"]:
        break
    else:
        
        chat_history.append({"role":"user", "content":prompt})
        
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat_history, 
            stream = True,
        )

        collected_messages = []


        for chunk in response:
            chunk_message = chunk["choices"][0]["delta"] #mensaje
            collected_messages.append(chunk_message)
            full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
            print(full_reply_content)
            print("\033[H\033[J", end="")
            #print("\033[H\033[J", end="") # Clear screen
        chat_history.append({"role":"assistant", 'content': full_reply_content})
        print('El humano :\n',prompt)
        print('\nAlbedo:\n',full_reply_content, "\n")
        
