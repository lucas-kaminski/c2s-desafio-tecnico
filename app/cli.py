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
        1 - Responda apenas em português.
        2 - Se não souber a resposta, diga que não sabe.
        3 - Mande as informações do carro de forma simples, em uma linha.
        4 - Não invente informações, apenas busque no banco de dados.
        """

    messages.append({"role": "system", "content": SYSTEM_PROMPT})

    print("Digite 'sair' para encerrar a conversa.\n")

    while True:
        user_input = input("Insira sua pergunta: ")
        if user_input.lower() == "sair":
            print("Encerrando a conversa.")
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

        while hasattr(message, "function_call") and message.function_call:
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
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                functions=ALL_SCHEMAS,
                function_call="auto",
            )
            choice = response.choices[0]
            message = choice.message

        reply = message.content
        messages.append({"role": "assistant", "content": reply})

        print(f"\nResposta: {reply}\n")


if __name__ == "__main__":
    main()
