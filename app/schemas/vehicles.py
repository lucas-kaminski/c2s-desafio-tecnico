get_all_vehicles_by_brand_schema = {
    "name": "vehicles",
    "description": "Obtém veículos de uma marca ESPECÍFICA. Requer brand_id obtido através de brands",
    "parameters": {
        "type": "object",
        "properties": {
            "brand_id": {
                "type": "integer",
                "description": "ID obtido EXCLUSIVAMENTE da lista de marcas (chamar brands primeiro se não souber)",
            },
            "model_name": {
                "type": "string",
                "description": "Nome do modelo do veículo (opcional)",
            },
        },
        "required": ["brand_id"],
    },
}
