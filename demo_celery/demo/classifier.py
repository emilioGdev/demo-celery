def classify_alert(message: str) -> str:
    message = message.lower()

    if any(keyword in message for keyword in ['erro', 'falha', 'crítico', 'urgente']):
        return 'Crítico'
    elif any(keyword in message for keyword in ['aviso', 'alerta', 'atenção']):
        return 'Moderado'
    else:
        return 'Informativo'
