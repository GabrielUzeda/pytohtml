# pytohtml — Documentação

> Biblioteca Python pura para gerar HTML com Tailwind CSS diretamente de código Python, sem escrever HTML, CSS ou JavaScript manualmente.

```python
from pytohtml import *

pagina = html(
    titulo("Olá, Mundo!", tamanho="gigante"),
    paragrafo("Bem-vindo ao pytohtml."),
    titulo_pagina="Meu Site"
)
salvar("index.html", pagina)
```

---

## Primeiros Passos

| Página | Descrição |
|--------|-----------|
| [Instalação](Instalacao) | Requisitos, instalação e primeiro uso |
| [html e salvar](html-e-salvar) | Estrutura base da página e salvamento em disco |

---

## Fundamentos Visuais

Módulo: `elementos.py`

| # | Função | Descrição |
|---|--------|-----------|
| 01 | [titulo](titulo) | Títulos semânticos `<h1>`–`<h4>` |
| 02 | [paragrafo](paragrafo) | Parágrafo de texto simples |
| 03 | [botao](botao) | Botão com variantes de estilo |
| 04 | [etiqueta](etiqueta) | Badge/etiqueta colorida |
| 05 | [link](link) | Link estilizado |

---

## Estrutura e Layout

Módulo: `elementos.py`

| # | Função | Descrição |
|---|--------|-----------|
| 06 | [divisor](divisor) | Linha horizontal de separação |
| 07 | [aviso-estatico](aviso-estatico) | Banner estático de mensagens |
| 08 | [cartao](cartao) | Container no estilo card |
| 09 | [lista](lista) | Lista `<ul>` ou `<ol>` estilizada |
| 10 | [tabela](tabela) | Tabela a partir de lista de listas |

---

## Componentes Ricos

Módulo: `elementos.py`

| # | Função | Descrição |
|---|--------|-----------|
| 11 | [imagem](imagem) | Imagem responsiva |
| 12 | [avatar](avatar) | Foto de perfil circular |
| 13 | [codigo](codigo) | Código inline ou em bloco |
| 14 | [animacao-carregando](animacao-carregando) | Skeleton loading |
| 15 | [accordion](accordion) | Painel expansível nativo |

---

## Formulários

Módulo: `elementos.py`

| # | Função | Descrição |
|---|--------|-----------|
| 16 | [rotulo e entrada](rotulo-e-entrada) | `<label>` + `<input>` estilizados |
| 17 | [textarea](textarea) | Campo de texto longo |
| 18 | [formulario](formulario) | Wrapper `<form>` |

---

## Layout Composto

Módulo: `layout.py`

| # | Função | Descrição |
|---|--------|-----------|
| 19 | [linha e coluna](linha-e-coluna) | Flex horizontal e vertical |
| 20 | [grade](grade) | Grid responsivo |
| 21 | [container](container) | Centralizador com largura máxima |
| 22 | [secao](secao) | Bloco `<section>` com padding |
| 23 | [cabecalho e rodape](cabecalho-e-rodape) | `<header>` e `<footer>` |
| 24 | [nav](nav) | Barra de navegação |
| 25 | [destaque](destaque) | Seção hero de destaque |
| 26 | [modal](modal) | Modal nativo `<dialog>` |

---

## Interatividade — Brython

Módulo: `interatividade.py` · Requer `brython=True` em `html()`

| # | Função | Descrição |
|---|--------|-----------|
| 27 | [ao-clicar](ao-clicar) | Handler de clique via Brython |
| 28 | [ao-carregar](ao-carregar) | Executa código ao carregar a página |
| 29 | [script-python](script-python) | Bloco Python livre no browser |
| 30 | [espaco-dinamico](espaco-dinamico) | `<div>` vazio para conteúdo dinâmico |
| 31 | [inserir-html](inserir-html) | Renderiza HTML dinâmico no DOM |
| 32 | [estado](estado) | Estado reativo com bind automático |
| 33 | [buscar-dados](buscar-dados) | Fetch HTTP com `browser.ajax` |
| 34 | [enviar-formulario](enviar-formulario) | Envio assíncrono de formulário |

---

## Popups e Alertas — SweetAlert2

Módulo: `interatividade.py` · **Não** requer Brython

| # | Função | Descrição |
|---|--------|-----------|
| 35 | [alerta](alerta) | Popup flexível (e variantes `_sucesso`, `_erro`, `_aviso`, `_info`) |
| 36 | [notificacao-rapida](notificacao-rapida) | Toast não intrusivo |
| 37 | [alerta-ao-clicar](alerta-ao-clicar) | SweetAlert2 acionado por clique |
| 38 | [pedir-confirmacao](pedir-confirmacao) | Diálogo "Tem certeza?" |
| 39 | [alerta-ao-enviar](alerta-ao-enviar) | Alerta ao submeter formulário |
| 40 | [abrir-modal-ao-clicar](abrir-modal-ao-clicar) | Abre `<dialog>` ao clicar |

---

> Documentação gerada com a própria biblioteca · [GabrielUzeda/pytohtml](https://github.com/GabrielUzeda/pytohtml)
