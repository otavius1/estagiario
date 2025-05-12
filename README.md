
# Estagiário Jurídico Bot

Um bot de consulta automática de processos do TJDFT, integrado com FastAPI para servir como API REST.  
Possui também um cliente CLI para realizar consultas locais ou para testes.

---

## 🌟 Funcionalidades

* Consulta pública de processos no TJDFT
* Geração automática de relatório em HTML
* API pronta para produção
* Cliente de linha de comando (CLI) para consultas
* Script automatizado para inicializar o projeto

---

## 💻 Requisitos

* Python 3.11
* Windows, Linux ou macOS
* Navegadores Playwright instalados (`playwright install`)

---

## 🛠️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/estagiario-juridico.git
cd estagiario-juridico
```

2. Execute o instalador automático:

No **Windows**:

```bash
./start.bat
```

No **Linux/macOS ou Windows**:

```bash
python start.py
```

Esse comando:
- Cria e ativa o ambiente virtual
- Instala todas as dependências
- Instala os navegadores do Playwright
- Inicia o servidor FastAPI (`uvicorn`)

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```ini
# .env
USE_SUBPROCESS=True
```

- `USE_SUBPROCESS=True`: usa subprocesso para executar o navegador (recomendado no Windows)
- `USE_SUBPROCESS=False`: executa diretamente pelo código (mais rápido no Linux/macOS)

---

## 🚀 Como usar

Com o servidor já rodando:

1. Abra outra aba do terminal na pasta do projeto.
2. Execute o cliente CLI para consultar um processo:

```bash
python testa_api.py
```
```bash
python cli.py
```

Ele vai solicitar o número do processo e salvar o relatório HTML automaticamente na pasta `data/`.

---

## 📚 Exemplo de Requisição API

```bash
GET http://127.0.0.1:8000/consulta?numero_processo=07161081420218070016
```

Resposta:

```json
{
  "numero": "0716108-14.2021.8.07.0016",
  "relatorio_html": "<html>...</html>"
}
```

A documentação automática da API estará disponível em:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📂 Estrutura do Projeto

```
.
├── api.py
├── start.bat
├── start.py
├── .env
├── requirements.txt
├── testa_api.py
├── data/
├── bot/
│   ├── navegador.py
│   ├── scraper.py
│   ├── relatorio.py
│   ├── utils.py
│   └── services.py
```

---

## 📢 Notas Importantes

* **Windows**: obrigatório `USE_SUBPROCESS=True`
* **Linux/macOS**: recomendado `USE_SUBPROCESS=False` para melhor performance
* **Produção**: recomendado usar o modo Linux com Gunicorn + Uvicorn Worker

---

## 📄 Licença

Projeto privado de automação jurídica.  
Todos os direitos reservados.
