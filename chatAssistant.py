import openai
import gradio

openai.api_key = "sk-GPT_API_Key"

mess = [{"role":"system","content":"You are a Psychologist"}]

def chatGPT(input):
    mess.append({"role":"user","content": "userInput"})
    resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", mess=mess)

    chatReply = resp["choices"][0]["message"]["content"]
    mess.append({"role":"assistant", "content": chatReply})
    return chatReply

demo = gradio.Interface(fn=chatGPT,inputs="text",outputs="text",title="Your_Title")

#demo.launch()

#for external link
demo.launch(share=True)
