get_all_vehicles_schema = {
    "name": "vehicles",
    "description": "Obtém veículos filtrando por qualquer parâmetro disponível. Todos os parâmetros são opcionais, exceto brand_id que é obrigatório.",
    "parameters": {
        "type": "object",
        "properties": {
            "brand_id": {
                "type": "integer",
                "description": "ID da marca (obrigatório, obtido da lista de marcas)",
            },
            "model": {
                "type": "string",
                "description": "Nome do modelo do veículo (opcional)",
            },
            "year": {
                "type": "integer",
                "description": "Ano do veículo (opcional)",
            },
            "color": {
                "type": "string",
                "description": "Nome da cor do veículo (opcional)",
            },
            "fuel_type": {
                "type": "string",
                "description": "Nome do tipo de combustível (opcional)",
            },
            "status": {
                "type": "string",
                "description": "Status que o veículo se encontra no momento (opcional)",
            },
        },
        "required": ["brand_id"],
    },
}
