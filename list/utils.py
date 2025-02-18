from groq import Groq

client = Groq(
    # base_url='https://api.groq.com/openai/v1/chat/completions'
    api_key = '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'
)

def chatcompletion(messages):
    messages.insert(0,{
                "role" : "system",
                "content" : "You are a helpful assistant, Answer the customers in a polite way"
            })
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content