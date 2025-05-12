def formatar_numero_processo(numero_puro):
    """
    Converte um número de processo puro (só números) para o padrão CNJ.
    Ex.: 07012345620248070001 → 0701234-56.2024.8.07.0001
    """
    return f"{numero_puro[:7]}-{numero_puro[7:9]}.{numero_puro[9:13]}.{numero_puro[13]}.{numero_puro[14:16]}.{numero_puro[16:]}"
