# 📂 Automação de Extração e Movimentação de Arquivos CSV via Selenium + Python

## 📌 Visão Geral

Este projeto implementa uma automação de ponta a ponta, responsável por:

✅ Fazer login em um site via Selenium
✅ Realizar download de arquivos CSV
✅ Realizar movimentação inteligente dos arquivos (arquivamento de antigos + organização dos novos)
✅ Registrar logs detalhados em tempo real (tanto em arquivo quanto no console)
✅ Exibir estatísticas básicas pós-execução (exemplo: número de linhas no CSV)

Essa solução foi desenhada para ambientes de **operações críticas**, com foco em **resiliência**, **tratamento de exceções** e **facilidade de manutenção**.

---

## 🧱 Estrutura de Pastas
```
Automacao-Extracao/
|--logs/
|-- src/
  ├── config.py
  ├── download_arquivo.py
  ├── login.py
  ├── logger.py
  ├── main.py
  ├── mover_arquivo.py
  ├── obter_arquivo_recente.py
  ├── requirements.txt
  └── README.md
```

---

## 🚀 Tecnologias Utilizadas

| Tecnologia                    | Finalidade              |
| ----------------------------- | ----------------------- |
| Python 3.x                    | Linguagem base          |
| Selenium                      | Automação Web           |
| Pandas                        | Manipulação de CSV      |
| Logging + RotatingFileHandler | Geração de Logs         |
| pathlib, shutil               | Manipulação de arquivos |
| Time                          | Tempo de espera         |

---

## ⚙️ Como Executar a Automação

### 1. Clone o repositório

```bash
git clone https://github.com/HericRibeiro/Automacao_Extracao.git
cd Automacao-Extracao
```

---

### 2. Instale as dependências

Recomenda-se utilizar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

### 3. Configure o `config.py`

Crie (ou ajuste) o arquivo `config.py` com os seguintes parâmetros (exemplo):

```python
config = {
    "pasta_logs": "logs",
    "nome_Arquivo": "*.csv",
    "diretorio_Origem": "arquivos/antigos",
    "diretorio_Destino": "arquivos/novos",
    "diretorio_Download": "C:/Users/SeuUsuario/Downloads",
    # Adicione aqui outras variáveis necessárias, como credenciais ou URLs
}
```

> **Dica corporativa:** Para produção, use um `.env` + `python-dotenv` e mantenha credenciais fora do repositório 👀.

---

### 4. Execute o projeto

```bash
python main.py
```

---

## 📝 Principais Módulos e Responsabilidades

| Arquivo                    | Função                                                         |
| -------------------------- | -------------------------------------------------------------- |
| `main.py`                  | Orquestração de toda a automação                               |
| `logger.py`                | Configuração avançada de logs com rotação de arquivos          |
| `mover_arquivo.py`         | Movimentação e organização de arquivos CSV                     |
| `login.py`                 | Login via Selenium                                             |
| `download_arquivo.py`      | Baixar os arquivos                                             |
| `obter_arquivo_recente.py` | Localiza o arquivo CSV mais recente no diretório de destino    |

---

## ✅ Funcionalidades Chave

* **Controle de Falhas:**
  Se algum passo da automação falhar (login, download, movimentação), o processo registra a falha nos logs com emoji de alerta ❌.

* **Rotação de Logs:**
  Os logs são limitados a 5MB por arquivo, com até 10 backups antigos.

* **Compatibilidade:**
  Testado com Selenium WebDriver Edge. Adaptável para Chrome ou Firefox com pequenas alterações.

---

## 📊 Exemplos de Saída no Log

```
✅ data/hora - INFO - Iniciando automação!
✅ data/hora - INFO - Iniciando locomoção de arquivo antigo!
❌ data/hora - ERROR - Falha na locomoção de arquivo para pasta de antigos!
✅ data/hora - INFO - Iniciando login!
✅ data/hora - INFO - Iniciando download!
✅ data/hora - INFO - Iniciando locomoção do arquivo!
✅ data/hora - INFO - Automação Concluída
✅ data/hora - INFO - Número de linhas no arquivo CSV: 157
```

---

## 🔮 Melhorias Futuras (Roadmap)

* [ ] Upload automático para armazenamento em nuvem (ex: AWS S3, Azure Blob)
* [ ] Dashboard de acompanhamento com Power BI ou Grafana
* [ ] Reprocessamento automático em caso de falha

---

## 🤝 Contribuições

Pull requests são bem-vindos! Para mudanças significativas, abra primeiro uma issue para discussão.

---

## 🛡️ Aviso Legal

Este projeto é fornecido "no estado em que se encontra". Use por sua conta e risco.
