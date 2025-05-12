def gerar_html(dados_processo, andamentos):
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                padding: 20px;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                max-width: 900px;
                margin: auto;
            }}
            h2 {{
                color: #004085;
                border-bottom: 2px solid #004085;
                padding-bottom: 5px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #004085;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Estagiário Jurídico - Relatório do Processo</h2>
            <p><b>Número do Processo:</b> {dados_processo['numero']}</p>
            <p><b>Classe Judicial:</b> {dados_processo['classe']}</p>
            <p><b>Assunto:</b> {dados_processo['assunto']}</p>
            <p><b>Vara:</b> {dados_processo['vara']}</p>

            <h3>Movimentações do Processo</h3>
            <table>
                <tr><th>Movimento</th><th>Documento</th></tr>"""

    for andamento in andamentos:
        html += f"""
                <tr>
                    <td>{andamento['movimento']}</td>
                    <td>{andamento['documento']}</td>
                </tr>"""

    html += """
            </table>
            <footer style='margin-top: 20px; text-align:center; font-size:12px; color:#777;'>Enviado automaticamente pelo Estagiário Jurídico.</footer>
        </div>
    </body>
    </html>"""
    return html
