from openai import OpenAI

import json
from app.config import OPENAI_API_KEY
from app.utils.schemas import ALL_SCHEMAS
from app.connectors.database.mcp import MCPClient

client = OpenAI(api_key=OPENAI_API_KEY)

mcp = MCPClient()


def main():
    print("Chat LLM + MCP CLI (digite 'sair' para encerrar)\n")

    messages = []
    SYSTEM_PROMPT = """
        Você é um assistente de concessionária. Siga estas regras:
        1. Sempre que um usuário perguntar da disponibilidade de um veículo, você deve chamar a função `brands` para pegar o id da marca no nosso banco de dados e procurar nos veículos disponíveis.
        """

    messages.append({"role": "system", "content": SYSTEM_PROMPT})

    while True:
        user_input = input("Você: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            functions=ALL_SCHEMAS,
            function_call="auto",
        )

        choice = response.choices[0]
        message = choice.message
        if message.function_call:
            func_call = message.function_call
            func_name = func_call.name
            arguments = json.loads(func_call.arguments)

            result = mcp.call_function(func_name, arguments)
            messages.append(
                {
                    "role": "function",
                    "name": func_name,
                    "content": json.dumps(result),
                }
            )

            followup = client.chat.completions.create(model="gpt-4", messages=messages)

            reply = followup.choices[0].message.content
        else:
            reply = message.content

        print(f"LLM: {reply}")
        # messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
