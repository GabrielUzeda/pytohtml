"""
pytohtml.layout
=============
Elementos de layout: flex, grid, container, seção, cabeçalho, rodapé e nav.
Todas as funções aceitam *conteudo (filhos aninhados) e classes extras opcionais.
"""

import html

def _juntar(*conteudo: str) -> str:
    """Junta filhos em uma única string."""
    return "\n".join(str(c) for c in conteudo)

_DISTANCIAMENTO_CLASSES = {
    0: "gap-0", 1: "gap-1", 2: "gap-2", 3: "gap-3", 4: "gap-4", 
    5: "gap-5", 6: "gap-6", 8: "gap-8", 10: "gap-10", 12: "gap-12", 16: "gap-16", 20: "gap-20", 24: "gap-24", 32: "gap-32", 40: "gap-40", 48: "gap-48", 56: "gap-56", 64: "gap-64",
}


def linha(
    *conteudo: str,
    centralizado: bool = True,
    distanciamento: int = 4,
    classes: str | None = None,
) -> str:
    """
    Agrupa elementos um ao lado do outro na horizontal (linha).

    Args:
        *conteudo:   Elementos que ficarão lado a lado.
        centralizado: Se True, alinha tudo no centro da tela.
        gap:         Espaço vazio entre cada elemento (0-64).
        classes:     Classes adicionais do Tailwind.

    Exemplo:
        linha(botao("Confirmar"), botao("Cancelar"))
    """
    gap_cls = _DISTANCIAMENTO_CLASSES.get(distanciamento, f"gap-{distanciamento}")
    base = f"flex flex-row {gap_cls}"
    if centralizado:
        base += " items-center justify-center"
    if classes:
        base += f" {classes}"
    return f'<div class="{base}">\n{_juntar(*conteudo)}\n</div>'


def coluna(
    *conteudo: str,
    centralizado: bool = True,
    distanciamento: int = 4,
    classes: str | None = None,
) -> str:
    """
    Agrupa elementos um abaixo do outro na vertical (coluna).

    Args:
        *conteudo:   Elementos que ficarão empilhados.
        centralizado: Se True, alinha tudo no centro da tela.
        gap:         Espaço vazio entre cada elemento (0-64).
        classes:     Classes adicionais do Tailwind.

    Exemplo:
        coluna(titulo("Bem-vindo"), paragrafo("Preencha o formulário abaixo:"))
    """
    gap_cls = _DISTANCIAMENTO_CLASSES.get(distanciamento, f"gap-{distanciamento}")
    base = f"flex flex-col {gap_cls}"
    if centralizado:
        base += " items-center justify-center"
    if classes:
        base += f" {classes}"
    return f'<div class="{base}">\n{_juntar(*conteudo)}\n</div>'


# ─── Grade ───────────────────────────────────────────────────────────────────

_GRID_COL_CLASSES = {
    1: "md:grid-cols-1", 2: "md:grid-cols-2", 3: "md:grid-cols-3", 
    4: "md:grid-cols-4", 5: "md:grid-cols-5", 6: "md:grid-cols-6", 
    7: "md:grid-cols-7", 8: "md:grid-cols-8", 9: "md:grid-cols-9", 
    10: "md:grid-cols-10", 11: "md:grid-cols-11", 12: "md:grid-cols-12", 13: "md:grid-cols-13", 14: "md:grid-cols-14", 15: "md:grid-cols-15", 16: "md:grid-cols-16", 17: "md:grid-cols-17", 18: "md:grid-cols-18", 19: "md:grid-cols-19", 20: "md:grid-cols-20", 21: "md:grid-cols-21", 22: "md:grid-cols-22", 23: "md:grid-cols-23", 24: "md:grid-cols-24", 25: "md:grid-cols-25", 26: "md:grid-cols-26", 27: "md:grid-cols-27", 28: "md:grid-cols-28", 29: "md:grid-cols-29", 30: "md:grid-cols-30", 31: "md:grid-cols-31", 32: "md:grid-cols-32", 33: "md:grid-cols-33", 34: "md:grid-cols-34", 35: "md:grid-cols-35", 36: "md:grid-cols-36", 37: "md:grid-cols-37", 38: "md:grid-cols-38", 39: "md:grid-cols-39", 40: "md:grid-cols-40", 41: "md:grid-cols-41", 42: "md:grid-cols-42", 43: "md:grid-cols-43", 44: "md:grid-cols-44", 45: "md:grid-cols-45", 46: "md:grid-cols-46", 47: "md:grid-cols-47", 48: "md:grid-cols-48", 49: "md:grid-cols-49", 50: "md:grid-cols-50", 51: "md:grid-cols-51", 52: "md:grid-cols-52", 53: "md:grid-cols-53", 54: "md:grid-cols-54", 55: "md:grid-cols-55", 56: "md:grid-cols-56", 57: "md:grid-cols-57", 58: "md:grid-cols-58", 59: "md:grid-cols-59", 60: "md:grid-cols-60", 61: "md:grid-cols-61", 62: "md:grid-cols-62", 63: "md:grid-cols-63", 64: "md:grid-cols-64",
}

def grade(
    *conteudo: str,
    colunas: int = 1,
    distanciamento: int = 4,
    classes: str | None = None,
) -> str:
    """
    Cria uma parede/grade de elementos parecida com uma tabela.

    Args:
        *conteudo: Elementos que serão distribuídos na grade.
        colunas:   Número de colunas (responsivo via Tailwind, por padrão no md:).
        gap:       Espaçamento em grade.
        classes:   Classes adicionais.

    Exemplo:
        grade(cartao("1"), cartao("2"), cartao("3"), colunas=3)
    """
    col_cls = _GRID_COL_CLASSES.get(colunas, f"md:grid-cols-{colunas}")
    gap_cls = _DISTANCIAMENTO_CLASSES.get(distanciamento, f"gap-{distanciamento}")
    
    base = f"grid grid-cols-1 {col_cls} {gap_cls}"
    if classes:
        base += f" {classes}"
    return f'<div class="{base}">\n{_juntar(*conteudo)}\n</div>'


# ─── Container ───────────────────────────────────────────────────────────────

def container(*conteudo: str, classes: str | None = None) -> str:
    """
    Contêiner centralizado com largura máxima e padding lateral.

    Exemplo:
        container(titulo("Título"), paragrafo("..."))
    """
    base = "max-w-5xl mx-auto px-4 py-8"
    if classes:
        base += f" {classes}"
    return f'<div class="{base}">\n{_juntar(*conteudo)}\n</div>'


# ─── Seção ───────────────────────────────────────────────────────────────────

def secao(*conteudo: str, classes: str | None = None) -> str:
    """Bloco <section> com padding vertical padrão."""
    base = "py-12 px-4"
    if classes:
        base += f" {classes}"
    return f'<section class="{base}">\n{_juntar(*conteudo)}\n</section>'


# ─── Cabeçalho ───────────────────────────────────────────────────────────────

def cabecalho(*conteudo: str, classes: str | None = None) -> str:
    """
    Barra de cabeçalho (header) com fundo branco e sombra.

    Exemplo:
        cabecalho(titulo("Meu Site", nivel=3))
    """
    base = "bg-white shadow-sm py-4 px-6 flex items-center justify-between"
    if classes:
        base += f" {classes}"
    return f'<header class="{base}">\n{_juntar(*conteudo)}\n</header>'


# ─── Nav ─────────────────────────────────────────────────────────────────────

def nav(*conteudo: str, classes: str | None = None) -> str:
    """Barra de navegação horizontal."""
    base = "flex gap-6 items-center"
    if classes:
        base += f" {classes}"
    return f'<nav class="{base}">\n{_juntar(*conteudo)}\n</nav>'


# ─── Rodapé ──────────────────────────────────────────────────────────────────

def rodape(*conteudo: str, classes: str | None = None) -> str:
    """Rodapé com fundo escuro e texto claro."""
    base = "bg-gray-800 text-gray-300 text-sm py-6 px-6 text-center mt-auto"
    if classes:
        base += f" {classes}"
    return f'<footer class="{base}">\n{_juntar(*conteudo)}\n</footer>'


# ─── Modal ───────────────────────────────────────────────────────────────────

def modal(id_modal: str, titulo_texto: str, *conteudo: str, classes: str | None = None) -> str:
    """
    Modal flutuante na tela usando a tag nativa <dialog>.
    Para abrir o modal via JavaScript ou botão, chame: document.getElementById('{id_modal}').showModal()
    """
    base = "backdrop:bg-gray-800/60 backdrop:backdrop-blur-sm p-6 rounded-2xl shadow-2xl max-w-lg w-full border border-gray-100 outline-none m-auto"
    
    cabecalho = f"""
    <div class="flex justify-between items-center mb-4">
        <h3 class="text-xl font-bold text-gray-900">{html.escape(titulo_texto)}</h3>
        <button type="button" onclick="document.getElementById('{id_modal}').close()" class="text-gray-400 hover:text-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded p-1">
            ✕
        </button>
    </div>
    """
    
    corpo = f'<div class="text-gray-600">\n{_juntar(*conteudo)}\n</div>'
    classe_final = f"{base} {classes}" if classes else base
    return f'<dialog id="{id_modal}" class="{classe_final}">\n{cabecalho}\n{corpo}\n</dialog>'


# ─── Destaque ──────────────────────────────────────────────────────────────────

def destaque(titulo_destaque: str, subtitulo: str, *botoes: str, classes: str | None = None) -> str:
    """
    Uma seção gigante de destaque, comum em topo de páginas (antigo Hero).
    """
    base = "relative pt-24 pb-32 px-4 text-center overflow-hidden"
    
    h1 = f'<h1 class="text-5xl md:text-6xl font-extrabold tracking-tight mb-6">{html.escape(titulo_destaque)}</h1>'
    p = f'<p class="mt-4 text-xl md:text-2xl max-w-3xl mx-auto mb-10 opacity-80">{html.escape(subtitulo)}</p>'
    botoes_html = f'<div class="mt-8 flex justify-center gap-4">\n{_juntar(*botoes)}\n</div>' if botoes else ""
    
    if classes:
        base += f" {classes}"
    return f'<div class="{base}">\n{h1}\n{p}\n{botoes_html}\n</div>'
