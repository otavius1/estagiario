# Estagiário Jurídico Bot

Um bot de consulta automática de processos do TJDFT, integrado com FastAPI para servir como API REST.
Possui também um cliente CLI para realizar consultas locais ou para testes.

---

## 🌟 Funcionalidades

* Consulta pública de processos no TJDFT
* Geração automática de relatório em HTML
* API pronta para produção
* Cliente de linha de comando (CLI) para consultas

---

## 💻 Requisitos

* Python 3.11
* Windows, Linux ou MacOS
* Navegadores Playwright instalados (`playwright install`)

---

## 🛠️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/estagiario-juridico.git
cd estagiario-juridico
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
# Ativar no Linux/macOS
source venv/bin/activate
# Ativar no Windows
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Instale os navegadores Playwright:

```bash
playwright install
```

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```ini
# .env
USE_SUBPROCESS=True
```

* `USE_SUBPROCESS=True`: usa subprocesso para executar o navegador (recomendado no Windows)
* `USE_SUBPROCESS=False`: executa diretamente pelo código (mais rápido no Linux/macOS)

---

## 🚀 Rodando a API

Execute o servidor:

```bash
uvicorn api:app --reload
```

Acesse a documentação interativa:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🖥️ Usando o Cliente CLI

Execute o cliente para consultar um processo:

```bash
python testa_api.py
```

O programa solicitará o número do processo e salvará o relatório HTML automaticamente na pasta `data/`.

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

---

## 📅 Estrutura Principal

```
.
├── api.py
├── .env
├── requirements.txt
├── testa_api.py
├── data/
├── bot/
    ├── navegador.py
    ├── scraper.py
    ├── relatorio.py
    ├── utils.py
    └── services.py
```

---

## 📅 Notas Importantes

* **Windows**: obrigatório `USE_SUBPROCESS=True`
* **Linux/macOS**: recomendado `USE_SUBPROCESS=False` para melhor performance
* **Produção**: usar o modo Linux com Gunicorn + Uvicorn Worker

---

## 📄 Licença

Projeto privado de automação jurídica.
Todos os direitos reservados.
