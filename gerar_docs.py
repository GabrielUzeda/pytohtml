import sys
sys.path.insert(0, ".")
from pytohtml import *

# ══════════════════════════════════════════════════════════════════════════════
# ESTILOS E HELPERS INTERNOS
# (tudo que a lib não cobre nativamente é injetado via head_extra ou classes)
# ══════════════════════════════════════════════════════════════════════════════

HEAD_EXTRA = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  body { font-family: 'DM Sans', sans-serif; }
  .mono { font-family: 'JetBrains Mono', monospace; }
  .code-block { background:#0f172a; border-radius:12px; overflow:hidden; }
  .code-block pre { padding:1.25rem; overflow-x:auto; font-size:0.82rem; line-height:1.7; font-family:'JetBrains Mono',monospace; color:#e2e8f0; margin:0; }
  .kw  { color:#7dd3fc; }
  .fn  { color:#c4b5fd; }
  .st  { color:#86efac; }
  .ar  { color:#fde68a; }
  .cm  { color:#64748b; }
  .nb  { color:#f9a8d4; }
  .badge-iniciante     { background:#dcfce7; color:#15803d; }
  .badge-intermediario { background:#dbeafe; color:#1d4ed8; }
  .badge-dificil       { background:#fef9c3; color:#b45309; }
  .badge-profissional  { background:#f3e8ff; color:#7c3aed; }
  .nav-item { border-left:3px solid transparent; }
  .nav-item.ativo { background:#eff6ff; color:#2563eb; font-weight:600; border-left:3px solid #2563eb; }
  .preview-panel { background:repeating-linear-gradient(45deg,#f8fafc,#f8fafc 10px,#f1f5f9 10px,#f1f5f9 20px); }
  .copy-btn { opacity:0; transition:opacity 0.2s; }
  .code-block:hover .copy-btn { opacity:1; }
  @keyframes fadeUp { from{opacity:0;transform:translateY(12px)} to{opacity:1;transform:translateY(0)} }
  .fade-up { animation:fadeUp 0.4s ease both; }
  .delay-1 { animation-delay:0.05s; }
  .delay-2 { animation-delay:0.10s; }
  .delay-3 { animation-delay:0.15s; }
  .delay-4 { animation-delay:0.20s; }
  .doc-grid { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
  @media(max-width:1024px){ .doc-grid { grid-template-columns:1fr; } }
  details summary { cursor:pointer; font-size:0.75rem; color:#9ca3af; user-select:none; display:flex; align-items:center; gap:4px; margin-top:0.5rem; }
  details summary:hover { color:#4b5563; }
  .page-layout { display:flex; max-width:80rem; margin:0 auto; }
  .sidebar { width:16rem; flex-shrink:0; position:sticky; top:3.5rem; height:calc(100vh - 3.5rem); overflow-y:auto; padding:2rem 1rem; border-right:1px solid #e5e7eb; background:white; }
  @media(max-width:1024px){ .sidebar { display:none; } }
  .main-content { flex:1; min-width:0; padding:2.5rem 2.5rem; }
  @media(max-width:768px){ .main-content { padding:1.5rem 1rem; } }
</style>
"""

COPY_SCRIPT = """
<script>
function copiar(btn, texto) {
  const limpo = texto.replace(/&quot;/g,'"').replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>');
  navigator.clipboard.writeText(limpo).then(() => {
    const orig = btn.textContent;
    btn.textContent = 'Copiado!';
    btn.classList.add('text-green-400');
    setTimeout(()=>{ btn.textContent = orig; btn.classList.remove('text-green-400'); }, 2000);
  });
}
</script>
"""

# ── helpers internos não cobertos pela lib ────────────────────────────────────

def _code_block(lang: str, code_html: str, copy_raw: str = "") -> str:
    copy_btn = (
        f'<button onclick="copiar(this, `{copy_raw}`)" '
        'class="copy-btn mono" style="font-size:0.7rem;color:#94a3b8;padding:0.2rem 0.5rem;'
        'border-radius:4px;background:transparent;border:none;cursor:pointer;">Copiar</button>'
    ) if copy_raw else ""
    header = (
        '<div style="display:flex;align-items:center;justify-content:space-between;'
        'padding:0.4rem 1rem;border-bottom:1px solid #1e293b;">'
        f'<span class="mono" style="font-size:0.7rem;color:#94a3b8;">{lang}</span>'
        f'{copy_btn}</div>'
    )
    return f'<div class="code-block">{header}<pre>{code_html}</pre></div>'


def _preview(conteudo_html: str) -> str:
    return (
        '<div class="preview-panel" style="border-radius:12px;border:1px solid #e5e7eb;'
        'padding:1.5rem;display:flex;align-items:center;justify-content:center;min-height:100px;">'
        f'{conteudo_html}'
        '</div>'
    )


def _doc_grid(code_html: str, preview_html: str) -> str:
    return f'<div class="doc-grid">{code_html}{preview_html}</div>'


def _badge_estagio(numero: int, nome: str, descricao: str) -> str:
    labels = {1: "Iniciante", 2: "Intermediário", 3: "Difícil", 4: "Profissional"}
    cor_num = {1: "#15803d", 2: "#1d4ed8", 3: "#b45309", 4: "#7c3aed"}[numero]
    cor_bg  = {1: "#dcfce7", 2: "#dbeafe", 3: "#fef9c3", 4: "#f3e8ff"}[numero]
    cls     = {1: "iniciante", 2: "intermediario", 3: "dificil", 4: "profissional"}[numero]
    circulo = (
        f'<div style="width:2rem;height:2rem;border-radius:9999px;background:{cor_bg};'
        f'color:{cor_num};display:flex;align-items:center;justify-content:center;'
        f'font-weight:700;font-size:0.875rem;flex-shrink:0;">{numero}</div>'
    )
    span_b = (
        f'<span class="badge-{cls} mono" style="font-size:0.65rem;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:0.1em;padding:0.2rem 0.6rem;border-radius:9999px;">'
        f'{labels[numero]}</span>'
    )
    desc = f'<p style="font-size:0.7rem;color:#9ca3af;margin:2px 0 0 0;">{descricao}</p>'
    return (
        '<div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:1.25rem;">'
        f'{circulo}<div>{span_b}{desc}</div></div>'
    )


def _dica(emoji: str, texto_html: str, tipo: str = "blue") -> str:
    cores = {
        "blue":   ("#eff6ff", "#bfdbfe", "#1d4ed8"),
        "purple": ("#faf5ff", "#e9d5ff", "#6d28d9"),
        "green":  ("#f0fdf4", "#bbf7d0", "#15803d"),
    }
    bg, border, color = cores.get(tipo, cores["blue"])
    return (
        f'<div style="background:{bg};border:1px solid {border};border-radius:12px;'
        f'padding:0.75rem 1rem;font-size:0.875rem;margin-top:1rem;color:{color};">'
        f'{emoji} {texto_html}</div>'
    )


def _tabela_params(linhas: list) -> str:
    ths = "".join(
        f'<th style="text-align:left;padding:0.75rem 1rem;font-size:0.7rem;font-weight:600;'
        f'color:#6b7280;text-transform:uppercase;letter-spacing:0.05em;background:#f9fafb;">{h}</th>'
        for h in ["Nome", "Tipo", "Padrão", "Descrição"]
    )
    rows = ""
    for nome, tipo, pad, desc in linhas:
        rows += (
            '<tr style="border-top:1px solid #f3f4f6;">'
            f'<td style="padding:0.75rem 1rem;"><code style="color:#2563eb;font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;">{nome}</code></td>'
            f'<td style="padding:0.75rem 1rem;"><code style="color:#db2777;font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;">{tipo}</code></td>'
            f'<td style="padding:0.75rem 1rem;color:#9ca3af;font-family:\'JetBrains Mono\',monospace;font-size:0.78rem;">{pad}</td>'
            f'<td style="padding:0.75rem 1rem;color:#4b5563;font-size:0.875rem;">{desc}</td>'
            '</tr>'
        )
    return (
        '<div style="background:white;border-radius:12px;border:1px solid #e5e7eb;'
        'overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.06);margin-bottom:2.5rem;">'
        f'<table style="width:100%;border-collapse:collapse;font-size:0.875rem;">'
        f'<thead><tr>{ths}</tr></thead><tbody>{rows}</tbody></table></div>'
    )


def _nav_item(num: str, nome: str, href: str = "#", ativo: bool = False, breve: bool = False) -> str:
    num_style = "background:#dbeafe;color:#1d4ed8;" if ativo else "background:#f3f4f6;color:#6b7280;"
    item_cls  = "nav-item ativo" if ativo else "nav-item"
    color     = "#2563eb" if ativo else "#6b7280"
    breve_tag = '<span style="margin-left:auto;font-size:0.7rem;color:#d1d5db;">em breve</span>' if breve else ""
    return (
        f'<a href="{href}" class="{item_cls}" style="display:flex;align-items:center;gap:0.5rem;'
        f'padding:0.5rem 0.75rem;border-radius:0 8px 8px 0;font-size:0.875rem;'
        f'text-decoration:none;color:{color};transition:color 0.15s;">'
        f'<span class="mono" style="font-size:0.7rem;padding:0.15rem 0.4rem;border-radius:4px;{num_style}">{num}</span>'
        f'{nome}{breve_tag}</a>'
    )


def _secao_label(texto: str) -> str:
    return (
        f'<p style="font-size:0.7rem;font-weight:600;color:#9ca3af;text-transform:uppercase;'
        f'letter-spacing:0.1em;padding:0 0.75rem;margin:1.25rem 0 0.25rem 0;">{texto}</p>'
    )


# ══════════════════════════════════════════════════════════════════════════════
# HEADER  (usa: cabecalho, linha, nav, imagem, titulo, botao)
# ══════════════════════════════════════════════════════════════════════════════

logo = imagem(
    "https://www.python.org/static/favicon.ico",
    alt="Logo PYTOHTML", arredondada=False,
    classes="h-7 w-7 drop-shadow-sm",
)

nome_lib = titulo(
    "PYTOHTML", tamanho="medio", escapar=False,
    classes="mono text-xl font-black tracking-tighter bg-clip-text text-transparent "
            "bg-gradient-to-r from-blue-600 to-yellow-500",
)

logo_area = linha(
    logo, nome_lib,
    '<span style="color:#d1d5db;font-size:1.125rem;margin:0 4px;">/</span>',
    '<span class="mono" style="font-size:0.875rem;color:#6b7280;font-weight:500;">docs</span>',
    centralizado=True, distanciamento=2,
)

header_el = cabecalho(
    linha(
        logo_area,
        nav(
            botao("Início",   variante="texto",    classes="text-slate-600 hover:text-blue-600 text-sm"),
            botao("Começar",  variante="primario",  classes="rounded-full text-sm shadow-md"),
        ),
        centralizado=False, distanciamento=0, classes="w-full justify-between",
    ),
    classes="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm",
)


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════

sidebar_items = (
    _secao_label("Fundamentos Visuais")
    + _nav_item("01", "titulo",    href="#secao-titulo", ativo=True)
    + _nav_item("02", "paragrafo", breve=True)
    + _nav_item("03", "botao",     breve=True)
    + _nav_item("04", "etiqueta",  breve=True)
    + _nav_item("05", "link",      breve=True)
    + _secao_label("Estrutura e Layout")
    + _nav_item("06", "divisor",        breve=True)
    + _nav_item("07", "aviso_estatico", breve=True)
    + _nav_item("08", "cartao",         breve=True)
    + _nav_item("09", "lista",          breve=True)
    + _nav_item("10", "tabela",         breve=True)
    + _secao_label("Componentes Ricos")
    + _nav_item("11", "imagem",              breve=True)
    + _nav_item("12", "avatar",              breve=True)
    + _nav_item("13", "codigo",              breve=True)
    + _nav_item("14", "animacao_carregando", breve=True)
    + _nav_item("15", "accordion",           breve=True)
    + _secao_label("Formulários")
    + _nav_item("16", "rotulo + entrada", breve=True)
    + _nav_item("17", "textarea",         breve=True)
    + _nav_item("18", "formulario",       breve=True)
    + _secao_label("Layout Composto")
    + _nav_item("19", "linha / coluna", breve=True)
    + _nav_item("20", "grade",          breve=True)
    + _nav_item("21", "container",      breve=True)
    + _nav_item("22", "cabecalho / rodape", breve=True)
    + _nav_item("23", "destaque",       breve=True)
    + _nav_item("24", "modal",          breve=True)
    + _secao_label("Interatividade")
    + _nav_item("25", "ao_clicar",          breve=True)
    + _nav_item("26", "alerta_ao_clicar",   breve=True)
    + _nav_item("27", "pedir_confirmacao",  breve=True)
    + _nav_item("28", "estado",             breve=True)
    + _nav_item("29", "buscar_dados",       breve=True)
    + _nav_item("30", "enviar_formulario",  breve=True)
)

sidebar = f'<aside class="sidebar">{sidebar_items}</aside>'


# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO: titulo()
# ══════════════════════════════════════════════════════════════════════════════

# breadcrumb
breadcrumb = (
    '<div class="mono" style="display:flex;align-items:center;gap:0.5rem;'
    'font-size:0.875rem;color:#9ca3af;margin-bottom:2rem;">'
    '<span>pytohtml</span><span>/</span><span>elementos</span><span>/</span>'
    '<span style="color:#2563eb;font-weight:600;">titulo</span></div>'
)

# cabeçalho da função
fn_header = linha(
    coluna(
        titulo("titulo()", tamanho="grande", classes="mono tracking-tight"),
        paragrafo(
            "Gera títulos semânticos HTML — do &lt;h1&gt; ao &lt;h4&gt; com estilos automáticos via Tailwind.",
            escapar=False, classes="text-gray-500 mt-1",
        ),
        centralizado=False, distanciamento=1,
    ),
    linha(
        etiqueta("elementos.py", cor="cinza", classes="mono text-xs"),
        etiqueta("tipografia",   cor="azul",  classes="mono text-xs"),
        centralizado=True, distanciamento=2,
    ),
    centralizado=False, distanciamento=0,
    classes="w-full justify-between items-start flex-wrap gap-4",
)

# assinatura
assinatura_code = (
    '<span class="fn">titulo</span>('
    '<span class="ar">texto</span>: <span class="nb">str</span>, '
    '<span class="ar">tamanho</span>: <span class="nb">str</span> = <span class="st">"grande"</span>, '
    '<span class="ar">nivel</span>: <span class="nb">int | None</span> = <span class="nb">None</span>, '
    '<span class="ar">classes</span>: <span class="nb">str | None</span> = <span class="nb">None</span>, '
    '<span class="ar">escapar</span>: <span class="nb">bool</span> = <span class="nb">True</span>'
    ') → <span class="nb">str</span>'
)
bloco_assinatura = _code_block("assinatura", assinatura_code)

# tabela de parâmetros
tabela_params = _tabela_params([
    ("texto",   "str",        "—",         "Conteúdo do título (obrigatório)"),
    ("tamanho", "str",        '"grande"',  '"pequeno" / "medio" / "grande" / "gigante"'),
    ("classes", "str | None", "None",      "Classes Tailwind extras para personalizar o estilo"),
    ("escapar", "bool",       "True",      "Escapa HTML para prevenir XSS (desative ao compor HTML)"),
])

# ── Estágio 1: Iniciante ─────────────────────────────────────────────────────
code_1 = _code_block(
    "Python",
    '<span class="kw">from</span> pytohtml <span class="kw">import</span> titulo\n\n'
    '<span class="fn">titulo</span>(<span class="st">"Olá, Mundo!"</span>)',
    copy_raw='from pytohtml import titulo\n\ntitulo(&quot;Olá, Mundo!&quot;)',
)
prev_1 = _preview(titulo("Olá, Mundo!"))
saida_1 = (
    '<details><summary><span>▶</span> Ver HTML gerado</summary>'
    + _code_block("HTML",
        '&lt;<span class="kw">h2</span> <span class="ar">class</span>=<span class="st">"text-3xl font-semibold text-gray-800 leading-snug"</span>'
        '&gt;Olá, Mundo!&lt;/<span class="kw">h2</span>&gt;')
    + '</details>'
)
estagio_1 = (
    '<div class="fade-up delay-1" style="margin-bottom:3rem;">'
    + _badge_estagio(1, "Iniciante", "Uso mais básico — um título com configuração padrão")
    + _doc_grid(code_1, prev_1) + saida_1 + '</div>'
)

# ── Estágio 2: Intermediário ─────────────────────────────────────────────────
code_2 = _code_block(
    "Python",
    '<span class="fn">titulo</span>(<span class="st">"Título Gigante"</span>, <span class="ar">tamanho</span>=<span class="st">"gigante"</span>)\n'
    '<span class="fn">titulo</span>(<span class="st">"Título Grande"</span>,  <span class="ar">tamanho</span>=<span class="st">"grande"</span>)\n'
    '<span class="fn">titulo</span>(<span class="st">"Título Médio"</span>,   <span class="ar">tamanho</span>=<span class="st">"medio"</span>)\n'
    '<span class="fn">titulo</span>(<span class="st">"Título Pequeno"</span>, <span class="ar">tamanho</span>=<span class="st">"pequeno"</span>)',
    copy_raw='titulo(&quot;Título Gigante&quot;, tamanho=&quot;gigante&quot;)\ntitulo(&quot;Título Grande&quot;, tamanho=&quot;grande&quot;)\ntitulo(&quot;Título Médio&quot;, tamanho=&quot;medio&quot;)\ntitulo(&quot;Título Pequeno&quot;, tamanho=&quot;pequeno&quot;)',
)
prev_2 = _preview(coluna(
    titulo("Título Gigante", tamanho="gigante"),
    titulo("Título Grande",  tamanho="grande"),
    titulo("Título Médio",   tamanho="medio"),
    titulo("Título Pequeno", tamanho="pequeno"),
    centralizado=False, distanciamento=2,
))
dica_2 = _dica("💡",
    '<strong>Dica:</strong> Cada tamanho gera uma tag semântica diferente: '
    '<code style="background:#dbeafe;padding:1px 5px;border-radius:4px;font-size:0.75rem;font-family:monospace;">gigante→h1</code> '
    '<code style="background:#dbeafe;padding:1px 5px;border-radius:4px;font-size:0.75rem;font-family:monospace;">grande→h2</code> '
    '<code style="background:#dbeafe;padding:1px 5px;border-radius:4px;font-size:0.75rem;font-family:monospace;">medio→h3</code> '
    '<code style="background:#dbeafe;padding:1px 5px;border-radius:4px;font-size:0.75rem;font-family:monospace;">pequeno→h4</code>. '
    'Isso é importante para SEO e acessibilidade.'
)
estagio_2 = (
    '<div class="fade-up delay-2" style="margin-bottom:3rem;">'
    + _badge_estagio(2, "Intermediário", "Todos os tamanhos — construindo hierarquia visual")
    + _doc_grid(code_2, prev_2) + dica_2 + '</div>'
)

# ── Estágio 3: Difícil ───────────────────────────────────────────────────────
code_3 = _code_block(
    "Python",
    '<span class="cm"># Título com gradiente via classes Tailwind</span>\n'
    '<span class="fn">titulo</span>(\n'
    '    <span class="st">"Design Moderno"</span>,\n'
    '    <span class="ar">tamanho</span>=<span class="st">"gigante"</span>,\n'
    '    <span class="ar">classes</span>=<span class="st">"bg-clip-text text-transparent\n'
    '             bg-gradient-to-r from-blue-600 to-purple-600"</span>\n'
    ')\n\n'
    '<span class="cm"># Título centralizado com cor customizada</span>\n'
    '<span class="fn">titulo</span>(\n'
    '    <span class="st">"Seção de Destaque"</span>,\n'
    '    <span class="ar">tamanho</span>=<span class="st">"medio"</span>,\n'
    '    <span class="ar">classes</span>=<span class="st">"text-center text-indigo-700"</span>\n'
    ')'
)
prev_3 = _preview(coluna(
    titulo("Design Moderno",    tamanho="gigante", classes="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-purple-600"),
    titulo("Seção de Destaque", tamanho="medio",   classes="text-center text-indigo-700"),
    centralizado=False, distanciamento=3,
))
estagio_3 = (
    '<div class="fade-up delay-3" style="margin-bottom:3rem;">'
    + _badge_estagio(3, "Difícil", "Personalizando com classes Tailwind extras")
    + _doc_grid(code_3, prev_3) + '</div>'
)

# ── Estágio 4: Profissional ──────────────────────────────────────────────────
code_4 = _code_block(
    "Python",
    '<span class="cm"># escapar=False permite embutir HTML confiável no título</span>\n'
    '<span class="cm"># Útil para ícones SVG, spans coloridos ou formatação inline</span>\n\n'
    '<span class="ar">icone_python</span> = <span class="st">\'&lt;img src="https://www.python.org/static/favicon.ico" class="inline w-8 h-8 mr-2 align-middle" /&gt;\'</span>\n\n'
    '<span class="fn">titulo</span>(\n'
    '    icone_python + <span class="st">"Bem-vindo ao pytohtml"</span>,\n'
    '    <span class="ar">tamanho</span>=<span class="st">"gigante"</span>,\n'
    '    <span class="ar">escapar</span>=<span class="nb">False</span>,  <span class="cm"># HTML do icone_python não será escapado</span>\n'
    ')\n\n'
    '<span class="cm"># Parte do texto em destaque com span colorido</span>\n'
    '<span class="ar">texto_misto</span> = <span class="st">\'Python &lt;span class="text-blue-600"&gt;puro&lt;/span&gt; e simples\'</span>\n\n'
    '<span class="fn">titulo</span>(\n'
    '    texto_misto,\n'
    '    <span class="ar">tamanho</span>=<span class="st">"medio"</span>,\n'
    '    <span class="ar">escapar</span>=<span class="nb">False</span>,\n'
    ')',
    copy_raw='icone_python = \'&lt;img src="https://www.python.org/static/favicon.ico" class="inline w-8 h-8 mr-2 align-middle" /&gt;\'\n\ntitulo(\n    icone_python + "Bem-vindo ao pytohtml",\n    tamanho="gigante",\n    escapar=False,\n)\n\ntexto_misto = \'Python &lt;span class="text-blue-600"&gt;puro&lt;/span&gt; e simples\'\n\ntitulo(\n    texto_misto,\n    tamanho="medio",\n    escapar=False,\n)',
)

icone_python = '<img src="https://www.python.org/static/favicon.ico" class="inline w-8 h-8 mr-2 align-middle" />'
texto_misto  = 'Python <span class="text-blue-600 font-bold">puro</span> e simples'

prev_4 = _preview(
    titulo(icone_python + "Bem-vindo ao pytohtml", tamanho="gigante", escapar=False)
    + '<div style="margin-top:0.75rem;">'
    + titulo(texto_misto, tamanho="medio", escapar=False)
    + '</div>'
)
dica_4 = _dica("⚠️",
    '<strong>Atenção:</strong> Com <code style="background:#f3e8ff;padding:1px 5px;border-radius:4px;font-family:monospace;font-size:0.75rem;">escapar=False</code> '
    'o texto é inserido como HTML bruto — nunca passe texto vindo do usuário assim, pois isso abre falha <strong>XSS</strong>. '
    'Use apenas com strings que você mesmo construiu no Python.',
    tipo="purple",
)
estagio_4 = (
    '<div class="fade-up delay-4" style="margin-bottom:3rem;">'
    + _badge_estagio(4, "Profissional", "Usando escapar=False para embutir HTML confiável no título")
    + _doc_grid(code_4, prev_4) + dica_4 + '</div>'
)

# ── Referência rápida ─────────────────────────────────────────────────────────
ref_rapida = cartao(
    titulo("⚡ Referência rápida — todos os tamanhos", tamanho="pequeno", classes="mb-4"),
    tabela(
        [
            ["tamanho=",   "Tag HTML", "Uso típico",             "Fonte gerada"],
            ['"gigante"',  "<h1>",     "Hero, título da página", "text-4xl font-bold"],
            ['"grande"',   "<h2>",     "Seções principais",      "text-3xl font-semibold"],
            ['"medio"',    "<h3>",     "Subseções, cards",        "text-2xl font-semibold"],
            ['"pequeno"',  "<h4>",     "Rótulos, subtítulos",    "text-xl font-medium"],
        ],
        cabecalho=True,
    ),
    sombra=True, classes="mb-10",
)

# ── Navegação ─────────────────────────────────────────────────────────────────
nav_elementos = (
    '<div style="display:flex;justify-content:space-between;align-items:center;'
    'padding-top:1.5rem;border-top:1px solid #e5e7eb;margin-top:2rem;">'
    '<span style="color:#9ca3af;font-size:0.875rem;">← Elemento anterior</span>'
    '<span style="font-size:0.875rem;color:#9ca3af;">Próximo: '
    '<a href="#" class="mono" style="color:#2563eb;font-weight:500;">paragrafo()</a> →</span>'
    '</div>'
)

# montar seção completa
secao_titulo_el = secao(
    breadcrumb
    + fn_header
    + '<div style="margin:1.5rem 0;">' + bloco_assinatura + '</div>'
    + '<h3 style="font-size:0.75rem;font-weight:600;color:#374151;text-transform:uppercase;'
      'letter-spacing:0.1em;margin-bottom:0.75rem;">Parâmetros</h3>'
    + tabela_params
    + estagio_1 + estagio_2 + estagio_3 + estagio_4
    + ref_rapida
    + nav_elementos,
    classes="fade-up",
)


# ══════════════════════════════════════════════════════════════════════════════
# PÁGINA FINAL
# ══════════════════════════════════════════════════════════════════════════════

main_content = f'<main class="main-content">{secao_titulo_el}</main>'
page_layout  = f'<div class="page-layout">{sidebar}{main_content}</div>'

footer_el = rodape(
    coluna(
        paragrafo("© 2024 pytohtml — Documentação gerada com a própria biblioteca 🐍",
                  classes="text-gray-400"),
        linha(
            link("GitHub",  href="#", classes="text-gray-400 hover:text-white"),
            link("Twitter", href="#", classes="text-gray-400 hover:text-white"),
            centralizado=True, distanciamento=4,
        ),
        centralizado=True, distanciamento=2,
    )
)

pagina = html(
    header_el,
    page_layout,
    footer_el,
    COPY_SCRIPT,
    titulo_pagina="pytohtml — Documentação",
    favicon="https://www.python.org/static/favicon.ico",
    head_extra=HEAD_EXTRA,
    brython=False,
)

salvar("docs_titulo.html", pagina)
print("✅ docs_titulo.html gerado com sucesso!")