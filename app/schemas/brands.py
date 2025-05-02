get_all_brands_schema = {
    "name": "brands",
    "description": "Lista TODAS as marcas cadastradas com seus IDs. Use primeiro para obter brand_id quando o usuário mencionar nome da marca para depois chamar a lista de veículos de forma encadeada.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Nome parcial/exato da marca para filtrar (opcional)",
            }
        },
        "required": [],
    },
}
