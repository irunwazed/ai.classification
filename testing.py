from libs import helpers, llm, class_jenis
from libs import ner


def chat_bkn(question):
  jenis = class_jenis.check_class_once(question)
  entities = ner.search_entities_json(question)

  result = "Maaf saya tidak mengerti"
  try:
    if len(entities) > 0:
      if jenis == "request_what":
        result = llm.ollama_chat("Jelaskan secara singkat mengenai ini : "+entities[0]["desc"])
      elif jenis == "request_who":
        result = llm.ollama_chat("Jelaskan secara singkat Siapa itu : "+entities[0]["text"]+" dengan deskripsi singkat "+ entities[0]["desc"])
    else:
      result = llm.ollama_chat("Jawab secara singkat pertanyaan ini : "+question)
  except Exception as e:
    print("ERROR : ", e)

  return result



while True:
  # Take user input
  user_input = input("You: ")
  
  if user_input.lower() == 'exit':
    print("Exiting the conversation.")
    break

  try:
    response = chat_bkn(user_input)
    print("SuripAI :", response)
  except Exception as e:
    print(f"Error occurred: {e}")
    break





