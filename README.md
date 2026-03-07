# pytohtml

> Biblioteca Python pura para criar páginas HTML modernas com Tailwind CSS — sem escrever HTML, CSS ou JavaScript.

![Hero](screenshots/hero.png)

---

## O que é

**pytohtml** transforma código Python em HTML completo, estilizado com Tailwind CSS e pronto para abrir no navegador. Você escreve funções Python, ela gera o arquivo `.html`.

Sem templates. Sem frameworks front-end. Sem npm.

---

## Instalação

Copie a pasta `pytohtml/` para dentro do seu projeto:

```
meu-projeto/
├── pytohtml/
│   ├── __init__.py
│   ├── pagina.py
│   ├── elementos.py
│   ├── layout.py
│   └── interatividade.py
└── meu_script.py
```

**Requisitos:** Python 3.10+ · Conexão com internet (Tailwind via CDN)

---

## Início rápido

```python
from pytohtml import *

pagina = html(
    titulo("Olá, Mundo!", tamanho="gigante"),
    paragrafo("Bem-vindo ao pytohtml."),
    botao("Começar", variante="primario"),
    titulo_pagina="Meu Site"
)

salvar("index.html", pagina)
```

```bash
python meu_script.py
# Abra index.html no navegador
```

---

## O que você pode construir

### Elementos e tipografia

![Elementos Básicos](screenshots/elementos-basicos.png)

Títulos, parágrafos, links, listas, botões com variantes de cor, avatares, badges e muito mais — tudo com uma linha de Python.

---

### Componentes estruturais

![Componentes](screenshots/componentes.png)

Alertas estáticos, tabelas, cards, accordion, skeleton loading, código com destaque — componentes prontos para uso imediato.

---

### Formulários

![Formulários](screenshots/formularios.png)

Campos, labels, textarea e o wrapper `formulario()` organizam tudo com espaçamento automático e estilos consistentes.

---

### Interatividade

![Interatividade](screenshots/interatividade.png)

Popups e confirmações via SweetAlert2 sem escrever JavaScript. Para interações mais complexas, use Brython — Python rodando diretamente no navegador.

---

## Módulos

| Módulo | Funções |
|--------|---------|
| `pagina.py` | `html()`, `salvar()` |
| `elementos.py` | `titulo`, `paragrafo`, `botao`, `etiqueta`, `link`, `divisor`, `aviso_estatico`, `cartao`, `lista`, `tabela`, `imagem`, `avatar`, `codigo`, `animacao_carregando`, `accordion`, `rotulo`, `entrada`, `textarea`, `formulario` |
| `layout.py` | `linha`, `coluna`, `grade`, `container`, `secao`, `cabecalho`, `rodape`, `nav`, `modal`, `destaque` |
| `interatividade.py` | `ao_clicar`, `ao_carregar`, `script_python`, `espaco_dinamico`, `inserir_html`, `estado`, `buscar_dados`, `enviar_formulario`, `alerta`, `alerta_sucesso`, `alerta_erro`, `alerta_aviso`, `alerta_info`, `notificacao_rapida`, `alerta_ao_clicar`, `pedir_confirmacao`, `alerta_ao_enviar`, `abrir_modal_ao_clicar` |

---

## Exemplo com Brython

Ative `brython=True` para usar Python como linguagem de interatividade no browser:

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

---

## Documentação

A documentação completa com exemplos de cada função está disponível na **[Wiki do projeto](https://github.com/GabrielUzeda/pytohtml/wiki)**.

| Seção | O que cobre |
|-------|-------------|
| [Instalação](https://github.com/GabrielUzeda/pytohtml/wiki/Instalacao) | Requisitos, setup e primeiro uso |
| [Elementos Básicos](https://github.com/GabrielUzeda/pytohtml/wiki/titulo) | titulo, paragrafo, link, lista, imagem, codigo |
| [Componentes Visuais](https://github.com/GabrielUzeda/pytohtml/wiki/botao) | botao, etiqueta, avatar, aviso, skeleton |
| [Formulários](https://github.com/GabrielUzeda/pytohtml/wiki/formulario) | rotulo, entrada, textarea, formulario |
| [Layout](https://github.com/GabrielUzeda/pytohtml/wiki/container) | container, grade, linha, coluna, nav, cabecalho |
| [Elementos Avançados](https://github.com/GabrielUzeda/pytohtml/wiki/cartao) | cartao, accordion, tabela, modal |
| [SweetAlert2](https://github.com/GabrielUzeda/pytohtml/wiki/alerta) | alerta, toast, confirmação, modal ao clicar |
| [Brython](https://github.com/GabrielUzeda/pytohtml/wiki/ao-clicar) | ao_clicar, estado, buscar_dados, enviar_formulario |

---

## Licença

[MIT](LICENSE)
