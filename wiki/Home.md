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

## Início

| Página | Descrição |
|--------|-----------|
| [Instalação](Instalacao) | Requisitos, instalação e primeiro uso |
| [html e salvar](html-e-salvar) | Estrutura base da página e salvamento em disco |

---

## Elementos Básicos

Módulo: `elementos.py` · Blocos fundamentais de conteúdo

| # | Função | Descrição |
|---|--------|-----------|
| 01 | [titulo](titulo) | Títulos semânticos `<h1>`–`<h4>` |
| 02 | [paragrafo](paragrafo) | Parágrafo de texto simples |
| 03 | [link](link) | Link estilizado |
| 04 | [lista](lista) | Lista `<ul>` ou `<ol>` estilizada |
| 05 | [divisor](divisor) | Linha horizontal de separação |
| 06 | [imagem](imagem) | Imagem responsiva |
| 07 | [codigo](codigo) | Código inline ou em bloco |

---

## Componentes Visuais

Módulo: `elementos.py` · Elementos com comportamento e estilo próprio

| # | Função | Descrição |
|---|--------|-----------|
| 08 | [botao](botao) | Botão com variantes de estilo |
| 09 | [etiqueta](etiqueta) | Badge/etiqueta colorida |
| 10 | [avatar](avatar) | Foto de perfil circular |
| 11 | [aviso-estatico](aviso-estatico) | Banner estático de mensagens |
| 12 | [animacao-carregando](animacao-carregando) | Skeleton loading |

---

## Formulários

Módulo: `elementos.py` · Campos e estrutura de formulários

| # | Função | Descrição |
|---|--------|-----------|
| 13 | [rotulo e entrada](rotulo-e-entrada) | `<label>` + `<input>` estilizados |
| 14 | [textarea](textarea) | Campo de texto longo |
| 15 | [formulario](formulario) | Wrapper `<form>` |

---

## Layout

Módulo: `layout.py` · Estrutura e organização da página

| # | Função | Descrição |
|---|--------|-----------|
| 16 | [container](container) | Centralizador com largura máxima |
| 17 | [secao](secao) | Bloco `<section>` com padding |
| 18 | [linha e coluna](linha-e-coluna) | Flex horizontal e vertical |
| 19 | [grade](grade) | Grid responsivo |
| 20 | [cabecalho e rodape](cabecalho-e-rodape) | `<header>` e `<footer>` |
| 21 | [nav](nav) | Barra de navegação |
| 22 | [destaque](destaque) | Seção hero de destaque |

---

## Elementos Avançados

Módulo: `elementos.py` + `layout.py` · Componentes compostos

| # | Função | Descrição |
|---|--------|-----------|
| 23 | [cartao](cartao) | Container no estilo card |
| 24 | [accordion](accordion) | Painel expansível nativo |
| 25 | [tabela](tabela) | Tabela a partir de lista de listas |
| 26 | [modal](modal) | Modal nativo `<dialog>` |

---

## Interatividade — SweetAlert2

Módulo: `interatividade.py` · **Não** requer Brython

| # | Função | Descrição |
|---|--------|-----------|
| 27 | [alerta](alerta) | Popup flexível (e variantes `_sucesso`, `_erro`, `_aviso`, `_info`) |
| 28 | [notificacao-rapida](notificacao-rapida) | Toast não intrusivo |
| 29 | [alerta-ao-clicar](alerta-ao-clicar) | SweetAlert2 acionado por clique |
| 30 | [pedir-confirmacao](pedir-confirmacao) | Diálogo "Tem certeza?" |
| 31 | [alerta-ao-enviar](alerta-ao-enviar) | Alerta ao submeter formulário |
| 32 | [abrir-modal-ao-clicar](abrir-modal-ao-clicar) | Abre `<dialog>` ao clicar |

---

## Interatividade — Brython

Módulo: `interatividade.py` · Requer `brython=True` em `html()`

| # | Função | Descrição |
|---|--------|-----------|
| 33 | [ao-carregar](ao-carregar) | Executa código ao carregar a página |
| 34 | [ao-clicar](ao-clicar) | Handler de clique via Brython |
| 35 | [script-python](script-python) | Bloco Python livre no browser |
| 36 | [espaco-dinamico](espaco-dinamico) | `<div>` vazio para conteúdo dinâmico |
| 37 | [inserir-html](inserir-html) | Renderiza HTML dinâmico no DOM |
| 38 | [estado](estado) | Estado reativo com bind automático |
| 39 | [enviar-formulario](enviar-formulario) | Envio assíncrono de formulário |
| 40 | [buscar-dados](buscar-dados) | Fetch HTTP com `browser.ajax` |

---

> Documentação gerada com a própria biblioteca · [GabrielUzeda/pytohtml](https://github.com/GabrielUzeda/pytohtml)
