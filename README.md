# Forense de Navegador

## Descrição
Esta ferramenta coleta informações de navegadores, incluindo histórico de navegação, cookies e credenciais salvas. Os dados extraídos são armazenados na pasta `outputs` em formato JSON.

## Requisitos
Antes de executar, certifique-se de instalar as dependências necessárias:
```sh
pip install -r requirements.txt
```

## Estrutura do Projeto
```
📂 browser_forensics/
│── 📂 modules/
│   │── history.py    # Coleta histórico
│   │── cookies.py    # Extrai cookies
│   │── credentials.py # Recupera credenciais
│   │── utils.py      # Funções auxiliares
│
│── 📂 outputs/       # Dados extraídos
│── main.py          # Script principal
│── requirements.txt # Dependências
│── README.md        # Documentação
```

## Como Usar
Execute o script principal:
```sh
python main.py
```
Os arquivos de saída serão gerados na pasta `outputs`.

## Aviso Legal
Esta ferramenta deve ser usada apenas para fins educacionais e de testes de segurança autorizados. O uso indevido pode violar leis de privacidade e segurança digital.
