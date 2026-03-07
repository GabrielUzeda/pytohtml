# Instalação e Início Rápido

> **pytohtml** não tem dependências externas de Python — tudo roda via CDN no browser (Tailwind CSS, SweetAlert2, Brython opcional).

---

## Requisitos

| Requisito | Versão mínima |
|-----------|---------------|
| Python | 3.10+ |
| Conexão com internet (CDN) | — |

> 💡 O Python 3.10+ é necessário por causa dos type hints `X | Y` usados internamente.

---

## Instalação

### Opção 1 — Copiar a pasta (recomendado)

Copie a pasta `pytohtml/` para dentro do seu projeto:

```
meu-projeto/
├── pytohtml/        ← pasta copiada do repositório
│   ├── __init__.py
│   ├── pagina.py
│   ├── elementos.py
│   ├── layout.py
│   └── interatividade.py
└── meu_script.py
```

### Opção 2 — Clonar o repositório

```bash
git clone https://github.com/GabrielUzeda/pytohtml.git
cd pytohtml
```

Execute seus scripts a partir da raiz do repositório:

```bash
python meu_script.py
```

---

## Primeiro uso

Crie um arquivo `index.py` e execute:

```python
from pytohtml import *

pagina = html(
    titulo("Olá, Mundo!", tamanho="gigante"),
    paragrafo("Bem-vindo ao pytohtml — HTML gerado com Python puro."),
    botao("Começar"),
    titulo_pagina="Meu Primeiro Site"
)

salvar("index.html", pagina)
print("Arquivo gerado: index.html")
```

```bash
python index.py
```

Abra o `index.html` no navegador — ele já vem com Tailwind CSS e SweetAlert2 carregados via CDN.

---

## Exemplo com Brython (interatividade)

Para usar funções como `ao_clicar`, `estado`, `buscar_dados` e `enviar_formulario`, ative o Brython passando `brython=True` para `html()`:

```python
from pytohtml import *

pagina = html(
    espaco_dinamico("contador", "text-center text-4xl font-bold mt-8"),
    botao("Incrementar", variante="primario", classes='id="btn-inc"'),
    estado("contador", "0", "#contador"),
    ao_clicar("#btn-inc", '''
        contador_atual = int(_estado["contador"])
        set_estado("contador", contador_atual + 1)
    '''),
    titulo_pagina="Contador",
    brython=True,
)

salvar("contador.html", pagina)
```

> ⚠️ **Nota:** As funções de interatividade Brython (`ao_clicar`, `ao_carregar`, `estado`, `buscar_dados`, `enviar_formulario`, `inserir_html`, `script_python`) **só funcionam** com `brython=True` ativado em `html()`.

---

## Estrutura dos módulos

| Módulo | Funções |
|--------|---------|
| `pagina.py` | `html()`, `salvar()` |
| `elementos.py` | `titulo`, `paragrafo`, `botao`, `etiqueta`, `link`, `divisor`, `aviso_estatico`, `cartao`, `lista`, `tabela`, `imagem`, `avatar`, `codigo`, `animacao_carregando`, `accordion`, `rotulo`, `entrada`, `textarea`, `formulario` |
| `layout.py` | `linha`, `coluna`, `grade`, `container`, `secao`, `cabecalho`, `rodape`, `nav`, `modal`, `destaque` |
| `interatividade.py` | `ao_clicar`, `ao_carregar`, `script_python`, `espaco_dinamico`, `inserir_html`, `estado`, `buscar_dados`, `enviar_formulario`, `alerta`, `alerta_sucesso`, `alerta_erro`, `alerta_aviso`, `alerta_info`, `notificacao_rapida`, `alerta_ao_clicar`, `pedir_confirmacao`, `alerta_ao_enviar`, `abrir_modal_ao_clicar` |

---

[← Início](Home) · **Instalação** · [html e salvar →](html-e-salvar)
