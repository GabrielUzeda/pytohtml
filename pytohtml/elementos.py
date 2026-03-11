"""
pytohtml.elementos
================
Elementos HTML individuais: textos, mídias, tabelas, formulários e utilitários.
"""

import html
from typing import Any


def _cls(base: str, extra: str | None) -> str:
    """Combina classes base com classes extras opcionais."""
    return f"{base} {extra}".strip() if extra else base


# ─── Animação Carregando ─────────────────────────────────────────────────────

def animacao_carregando(
    tipo: str = "texto",  # "texto", "imagem", "avatar"
    linhas: int = 1,
    classes: str | None = None,
) -> str:
    """
    Efeito de carregamento (skeleton loading) usado quando os dados estão carregando.

    Args:
        tipo:   "texto", "imagem", ou "avatar".
        linhas: Número de linhas para tipo="texto".

    Exemplo:
        animacao_carregando(tipo="avatar")
    """
    base = "animate-pulse bg-gray-200"
    if tipo == "avatar":
        base += " rounded-full w-12 h-12"
    elif tipo == "imagem":
        base += " rounded-xl w-full h-48"
    else:  # tipo == "texto"
        # Gera múltiplas linhas de texto skeleton
        linha_base = "animate-pulse bg-gray-200 rounded h-4 w-full"
        linhas_html = []
        for i in range(linhas):
            # Última linha um pouco mais curta para simular texto real
            current_line_classes = linha_base
            if i == linhas - 1 and linhas > 1:
                current_line_classes += " w-3/4"
            linhas_html.append(f'<div class="{_cls(current_line_classes, classes if i == 0 else None)}"></div>')
        return '<div class="space-y-2">' + "\n".join(linhas_html) + '</div>'
    
    return f'<div class="{_cls(base, classes)}"></div>'


# ─── Tipografia ──────────────────────────────────────────────────────────────

# Mapeamento de tamanho → tag e classes Tailwind para títulos
_TAMANHO_TITULO = {
    "gigante": ("h1", "text-4xl font-bold text-gray-900 leading-tight"),
    "grande":  ("h2", "text-3xl font-semibold text-gray-800 leading-snug"),
    "medio":   ("h3", "text-2xl font-semibold text-gray-800"),
    "pequeno": ("h4", "text-xl font-medium text-gray-700"),
}

def titulo(
    texto: str,
    tamanho: str = "grande",
    nivel: int | None = None,
    classes: str | None = None,
    escapar: bool = True,
) -> str:
    """
    Título semântico (<h1> até <h4>).
    
    Args:
        texto:   Conteúdo do título.
        tamanho: "pequeno" | "medio" | "grande" | "gigante".
        nivel:   (Legado) 1 a 4. Substituído por 'tamanho'.
        classes: Classes Tailwind extras.
        escapar: Escapar HTML do texto (proteção XSS).
    """
    # Suporte legado para 'nivel'
    if nivel is not None:
        mapeamento_legado = {1: "gigante", 2: "grande", 3: "medio", 4: "pequeno"}
        tamanho = mapeamento_legado.get(nivel, "grande")

    tag, base = _TAMANHO_TITULO.get(tamanho, _TAMANHO_TITULO["grande"])
    texto_seguro = html.escape(texto) if escapar else texto
    return f'<{tag} class="{_cls(base, classes)}">{texto_seguro}</{tag}>'


def paragrafo(texto: str, classes: str | None = None, escapar: bool = True) -> str:
    """
    Parágrafo de texto simples.

    Exemplo:
        paragrafo("Este é um parágrafo de exemplo.")
    """
    base = "text-base text-gray-600 leading-relaxed"
    texto_seguro = html.escape(texto) if escapar else texto
    return f'<p class="{_cls(base, classes)}">{texto_seguro}</p>'


def link(texto: str, href: str = "#", classes: str | None = None, escapar: bool = True) -> str:
    """
    Link estilizado.

    Args:
        texto: Texto visível.
        href:  URL de destino.
    """
    base = "text-blue-600 hover:text-blue-800 underline underline-offset-2 transition-colors"
    texto_seguro = html.escape(texto) if escapar else texto
    return f'<a href="{href}" class="{_cls(base, classes)}">{texto_seguro}</a>'


def codigo(texto: str, bloco: bool = False, classes: str | None = None, escapar: bool = True) -> str:
    """
    Código inline ou em bloco.

    Args:
        texto: Código a exibir.
        bloco: Se True, usa <pre><code> (bloco). Se False, usa <code> inline.
    """
    texto_seguro = html.escape(texto) if escapar else texto
    if bloco:
        base = "bg-gray-900 text-green-400 rounded-lg p-4 overflow-x-auto text-sm font-mono block"
        return f'<pre class="{_cls(base, classes)}"><code>{texto_seguro}</code></pre>'
    base = "bg-gray-100 text-pink-600 rounded px-1.5 py-0.5 text-sm font-mono"
    return f'<code class="{_cls(base, classes)}">{texto_seguro}</code>'


# ─── Mídia ───────────────────────────────────────────────────────────────────

def imagem(
    src: str,
    alt: str = "",
    arredondada: bool = True,
    classes: str | None = None,
) -> str:
    """
    Imagem responsiva.

    Args:
        src:          Caminho ou URL da imagem.
        alt:          Texto alternativo.
        arredondada:  Aplica rounded-xl quando True.
        classes:      Classes extras.
    """
    base = "max-w-full h-auto"
    if arredondada:
        base += " rounded-xl"
    return f'<img src="{src}" alt="{alt}" class="{_cls(base, classes)}" />'


# ─── Botão ───────────────────────────────────────────────────────────────────

# Variantes disponíveis para botões
_BOTAO_VARIANTES = {
    "primario":   "bg-blue-600 hover:bg-blue-700 text-white",
    "secundario": "bg-gray-200 hover:bg-gray-300 text-gray-800",
    "perigo":     "bg-red-600 hover:bg-red-700 text-white",
    "sucesso":    "bg-green-600 hover:bg-green-700 text-white",
    "fantasma":   "border border-gray-300 hover:bg-gray-100 text-gray-700",
    "texto":      "bg-transparent text-blue-600 hover:text-blue-800",
    "vazio":      "bg-transparent",
}


def botao(
    texto: str,
    variante: str = "primario",
    tipo: str = "button",
    classes: str | None = None,
    escapar: bool = True,
) -> str:
    """
    Botão com variantes de estilo.

    Args:
        texto:    Rótulo do botão.
        variante: "primario" | "secundario" | "perigo" | "sucesso" | "fantasma".
        tipo:     Atributo type do HTML (button, submit, reset).
        classes:  Classes extras.

    Exemplo:
        botao("Enviar", variante="sucesso")
    """
    cor = _BOTAO_VARIANTES.get(variante, _BOTAO_VARIANTES["primario"])
    base = f"px-5 py-2.5 rounded-lg font-medium text-sm transition-colors cursor-pointer {cor}"
    texto_seguro = html.escape(texto) if escapar else texto
    return f'<button type="{tipo}" class="{_cls(base, classes)}">{texto_seguro}</button>'


# ─── Tabela ──────────────────────────────────────────────────────────────────

def tabela(
    dados: list[list[Any]],
    cabecalho: bool = True,
    classes: str | None = None,
    escapar: bool = True,
) -> str:
    """
    Tabela a partir de uma lista de listas.

    Args:
        dados:     Lista de linhas; a primeira linha é o cabeçalho se cabecalho=True.
        cabecalho: Trata a primeira linha como cabeçalho (<thead>).
        classes:   Classes extras para a <table>.

    Exemplo:
        tabela([
            ["Nome", "Idade", "Cidade"],
            ["Ana",  28,      "SP"],
            ["João", 34,      "RJ"],
        ])
    """
    if not dados:
        return ""

    base = "w-full border-collapse text-sm"
    if classes:
        base += f" {classes}"

    linhas_html = []

    # Cabeçalho
    if cabecalho and len(dados) > 0:
        celulas = "".join(
            f'<th scope="col" class="bg-gray-100 text-gray-700 font-semibold px-4 py-2 text-left border border-gray-200">{html.escape(str(c)) if escapar else c}</th>'
            for c in dados[0]
        )
        linhas_html.append(f"<thead><tr>{celulas}</tr></thead>")
        linhas = dados[1:]
    else:
        linhas = dados

    # Corpo
    corpo = ""
    for i, linha in enumerate(linhas):
        bg = "bg-white" if i % 2 == 0 else "bg-gray-50"
        celulas = "".join(
            f'<td class="{bg} px-4 py-2 border border-gray-200 text-gray-700">{html.escape(str(c)) if escapar else c}</td>'
            for c in linha
        )
        corpo += f"<tr>{celulas}</tr>\n"

    linhas_html.append(f"<tbody>{corpo}</tbody>")

    return f'<div class="overflow-x-auto rounded-xl border border-gray-200 shadow-sm"><table class="{base}">{"".join(linhas_html)}</table></div>'


# ─── Lista ───────────────────────────────────────────────────────────────────

def lista(
    *itens: str,
    ordenada: bool = False,
    classes: str | None = None,
) -> str:
    """
    Lista de itens (ul ou ol).

    Args:
        *itens:   Textos ou HTML de cada item.
        ordenada: Se True, usa <ol>; caso contrário, <ul>.
        classes:  Classes extras.

    Exemplo:
        lista("Maçã", "Banana", "Laranja")
    """
    tag = "ol" if ordenada else "ul"
    tipo = "list-decimal" if ordenada else "list-disc"
    base = f"{tipo} list-inside space-y-1 text-gray-600 text-base"
    itens_html = "".join(
        f'<li class="leading-relaxed">{item}</li>' for item in itens
    )
    return f'<{tag} class="{_cls(base, classes)}">{itens_html}</{tag}>'


# ─── Divisor ─────────────────────────────────────────────────────────────────

def divisor(classes: str | None = None) -> str:
    """Linha horizontal de separação (<hr>)."""
    base = "border-0 border-t border-gray-200 my-6"
    return f'<hr class="{_cls(base, classes)}" />'


# ─── Etiqueta ────────────────────────────────────────────────────────────────

_BADGE_CORES = {
    "cinza":   "bg-gray-100 text-gray-700",
    "azul":    "bg-blue-100 text-blue-700",
    "verde":   "bg-green-100 text-green-700",
    "vermelho":"bg-red-100 text-red-700",
    "amarelo": "bg-yellow-100 text-yellow-700",
    "roxo":    "bg-purple-100 text-purple-700",
}


def etiqueta(texto: str, cor: str = "cinza", classes: str | None = None, escapar: bool = True) -> str:
    """
    Etiqueta/badge colorida.

    Args:
        texto: Texto da etiqueta.
        cor:   "cinza" | "azul" | "verde" | "vermelho" | "amarelo" | "roxo".

    Exemplo:
        etiqueta("Novo", cor="verde")
    """
    paleta = _BADGE_CORES.get(cor, _BADGE_CORES["cinza"])
    base = f"inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium {paleta}"
    texto_seguro = html.escape(texto) if escapar else texto
    return f'<span class="{_cls(base, classes)}">{texto_seguro}</span>'


# ─── Alerta ──────────────────────────────────────────────────────────────────

_ALERTA_ESTILOS = {
    "info":    "bg-blue-50 border-blue-200 text-blue-800",
    "sucesso": "bg-green-50 border-green-200 text-green-800",
    "aviso":   "bg-yellow-50 border-yellow-200 text-yellow-800",
    "erro":    "bg-red-50 border-red-200 text-red-800",
    "perigo":  "bg-red-50 border-red-200 text-red-800",
}


def aviso_estatico(
    texto: str,
    tipo: str = "info",
    classes: str | None = None,
    escapar: bool = True,
) -> str:
    """
    Uma caixa destacada (banner estático) para exibir mensagens importantes.
    
    Args:
        texto:   Conteúdo da mensagem.
        tipo:    "info" | "sucesso" | "aviso" | "perigo".
        classes: Classes extras.
    """
    estilo = _ALERTA_ESTILOS.get(tipo, _ALERTA_ESTILOS["info"])
    base = f"border rounded-lg px-4 py-3 my-2 text-sm {estilo}"
    texto_seguro = html.escape(texto) if escapar else texto
    return f'<div role="alert" class="{_cls(base, classes)}">{texto_seguro}</div>'


# ─── Formulários ─────────────────────────────────────────────────────────────

def rotulo(texto: str, para: str | None = None, classes: str | None = None) -> str:
    """
    Texto que fica em cima de um campo (label).

    Args:
        texto: Texto do rótulo.
        para:  ID do input associado ("for").

    Exemplo:
        rotulo("Email", para="email-input")
    """
    base = "block text-sm font-medium text-gray-700 mb-1"
    for_attr = f' for="{para}"' if para else ""
    return f'<label{for_attr} class="{_cls(base, classes)}">{html.escape(texto)}</label>'


def entrada(
    tipo: str = "text",
    nome: str = "",
    placeholder: str = "",
    valor: str = "",
    obrigatorio: bool = False,
    classes: str | None = None,
) -> str:
    """
    Campo de entrada (<input>).

    Args:
        tipo:        Tipo HTML (text, email, password, number...).
        nome:        Atributo name/id.
        placeholder: Texto de dica.
        valor:       Valor inicial.
        obrigatorio: Se True, impede o envio do form se vazio (atributo required).
        classes:     Classes extras.
    """
    base = "w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
    attrs = f'type="{tipo}"'
    if nome:
        attrs += f' name="{nome}" id="{nome}"'
    if placeholder:
        attrs += f' placeholder="{placeholder}"'
    if valor:
        attrs += f' value="{valor}"'
    if obrigatorio:
        attrs += ' required'
    return f'<input {attrs} class="{_cls(base, classes)}" />'


def textarea(
    nome: str = "",
    placeholder: str = "",
    linhas: int = 4,
    valor: str = "",
    obrigatorio: bool = False,
    classes: str | None = None,
) -> str:
    """Campo de texto longo (<textarea>)."""
    base = "w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-y"
    attrs = f'rows="{linhas}"'
    if nome:
        attrs += f' name="{nome}" id="{nome}"'
    if placeholder:
        attrs += f' placeholder="{placeholder}"'
    return f'<textarea {attrs} class="{_cls(base, classes)}"></textarea>'


def formulario(*conteudo: str, acao: str = "#", metodo: str = "post", classes: str | None = None) -> str:
    """
    Formulário HTML (<form>).

    Args:
        *conteudo: Campos e botões.
        acao:      Atributo action.
        metodo:    Atributo method (get | post).
    """
    base = "space-y-4"
    if classes:
        base += f" {classes}"
    return f'<form action="{acao}" method="{metodo}" class="{base}">\n' + "\n".join(conteudo) + "\n</form>"


# ─── Cartão ──────────────────────────────────────────────────────────────────

def cartao(*conteudo: str, sombra: bool = True, classes: str | None = None) -> str:
    """
    Contêiner no estilo cartão (card) com borda e fundo branco.

    Exemplo:
        cartao(titulo("Card", nivel=3), paragrafo("Conteúdo do card."))
    """
    base = "bg-white rounded-2xl border border-gray-200 p-6"
    if sombra:
        base += " shadow-md"
    if classes:
        base += f" {classes}"
    return f'<div class="{base}">\n' + "\n".join(str(c) for c in conteudo) + "\n</div>"


# ─── Avatar ──────────────────────────────────────────────────────────────────

def avatar(src: str = "", tamanho: int = 12, alt: str = "Avatar", iniciais: str = "", classes: str | None = None) -> str:
    """
    Imagem de perfil redonda. Se 'src' for vazio, tenta exibir as {iniciais}.
    Tamanhos Tailwind recomendados: 8, 10, 12, 16.
    """
    base = f"inline-flex items-center justify-center relative rounded-full overflow-hidden bg-gray-200 border border-gray-300 w-{tamanho} h-{tamanho} shrink-0"
    
    if src:
        conteudo = f'<img src="{src}" alt="{html.escape(alt)}" class="object-cover w-full h-full" />'
    else:
        conteudo = f'<span class="font-medium text-gray-600 uppercase">{html.escape(iniciais)}</span>'
        
    return f'<div class="{_cls(base, classes)}">\n{conteudo}\n</div>'


# ─── Accordion ───────────────────────────────────────────────────────────────

def accordion(titulo_aba: str, *conteudo: str, classes: str | None = None) -> str:
    """
    Painel retrátil expansível nativo usando <details> e <summary>.
    """
    base = "group border border-gray-200 rounded-xl bg-white overflow-hidden my-4"
    
    summary = f"""
    <summary class="cursor-pointer px-5 py-4 font-medium text-gray-800 bg-gray-50 hover:bg-gray-100 transition-colors select-none flex justify-between items-center outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500">
        {html.escape(titulo_aba)}
        <span class="text-gray-400 group-open:rotate-180 transition-transform duration-200">▼</span>
    </summary>
    """
    
    corpo = f'<div class="px-5 py-4 text-gray-600 bg-white border-t border-gray-200">\n{"\n".join(str(c) for c in conteudo)}\n</div>'
    
    return f'<details class="{_cls(base, classes)}">\n{summary}\n{corpo}\n</details>'
