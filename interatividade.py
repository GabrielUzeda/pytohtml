"""
pytohtml.interatividade
=======================
Interatividade client-side via Brython: manipulação de DOM, requisições HTTP,
controle de estado reativo e renderização dinâmica.

Todas as funções geram strings HTML com blocos <script type="text/python">
que serão executados no navegador pelo Brython.

SweetAlert2: As funções swal_* usam JS puro (<script>) para evitar
problemas de compatibilidade com o proxy do Brython (window.Swal.fire
quebra o contexto `this` do SweetAlert2).
"""

import textwrap


def script_python(*codigo: str) -> str:
    """
    Encapsula código Python dentro de <script type="text/python">.

    Args:
        *codigo: Linhas ou blocos de código Python para Brython.

    Exemplo:
        script_python('''
            from browser import document, alert
            alert("Olá do Brython!")
        ''')
    """
    corpo = "\n".join(textwrap.dedent(c) for c in codigo)
    return f'<script type="text/python">\n{corpo}\n</script>'


def ao_clicar(seletor: str, codigo: str) -> str:
    """
    Gera um script Brython que vincula um handler de clique
    a um elemento do DOM via seletor CSS.

    Args:
        seletor: Seletor CSS do elemento (ex: "#meu-botao", ".classe").
        codigo:  Corpo da função handler (recebe 'ev' como argumento).

    Exemplo:
        ao_clicar("#btn-ola", '''
            from browser import alert
            alert("Botão clicado!")
        ''')
    """
    codigo_indentado = textwrap.indent(textwrap.dedent(codigo), "    ")
    return script_python(f"""
from browser import document

def _handler(ev):
{codigo_indentado}

document.select("{seletor}")[0].bind("click", _handler)
""")


def ao_carregar(codigo: str) -> str:
    """
    Gera um script Brython que executa código quando a página carrega.

    Args:
        codigo: Código Python a executar no carregamento.

    Exemplo:
        ao_carregar('''
            from browser import document
            document["status"].text = "Página carregada!"
        ''')
    """
    return script_python(textwrap.dedent(codigo))


def buscar_dados(
    url: str,
    metodo: str = "GET",
    callback_nome: str = "_on_response",
    corpo: str | None = None,
    seletor_resultado: str | None = None,
    silencioso: bool = False,
    gatilho_clique: str | None = None,
) -> str:
    """
    Gera código Brython que faz fetch HTTP para uma URL
    usando browser.ajax e chama uma função callback com o resultado.

    Args:
        url:                URL da API (ex: "https://api.exemplo.com/dados").
        metodo:             Método HTTP: "GET", "POST", "PUT", "DELETE".
        callback_nome:      Nome da função callback que recebe o request.
        corpo:              Corpo da requisição (para POST/PUT), como string JSON.
        seletor_resultado:  Se fornecido, renderiza req.text dentro do elemento.
        silencioso:         Se True, não exibe SweetAlert2 em erros.
        gatilho_clique:     Se fornecido, a busca só ocorre ao clicar neste seletor CSS.

    Exemplo:
        buscar_dados("https://dummyjson.com/quotes/random", seletor_resultado="#resultado", gatilho_clique="#btn-buscar")
    """
    metodo = metodo.upper()

    # Gera o código de tratamento de erro
    if silencioso:
        if seletor_resultado:
            erro_code = f"""document.select("{seletor_resultado}")[0].html = f'<span class="text-red-500">Erro {{req.status}}</span>'"""
        else:
            erro_code = "pass"
    else:
        # Usa window.eval para chamar SweetAlert2 sem quebrar o `this`
        erro_code = """from browser import window
        window.eval(f'Swal.fire({{icon: "error", title: "Erro na requisição", text: "Status {req.status} ao acessar a API.", confirmButtonColor: "#3085d6"}})')"""
        if seletor_resultado:
            erro_code += f'\n        document.select("{seletor_resultado}")[0].html = f\'<span class="text-red-500">Erro {{req.status}}</span>\''

    if seletor_resultado:
        callback_code = f"""
def {callback_nome}(req):
    from browser import document
    import json
    if req.status == 200:
        dados = json.loads(req.text)
        if isinstance(dados, list):
            html_items = "".join(f'<div class="p-3 border-b border-gray-200">{{item}}</div>' for item in dados)
            document.select("{seletor_resultado}")[0].html = html_items
        elif isinstance(dados, dict):
            html_items = "".join(
                f'<div class="flex gap-2 py-1"><span class="font-semibold text-gray-700">{{str(k).capitalize()}}:</span><span class="text-gray-600 truncate">{{v}}</span></div>'
                for k, v in dados.items()
            )
            document.select("{seletor_resultado}")[0].html = html_items
        else:
            document.select("{seletor_resultado}")[0].html = str(dados)
    else:
        {erro_code}
"""
    else:
        callback_code = f"""
def {callback_nome}(req):
    if req.status != 200:
        {erro_code}
"""

    ajax_call = f'ajax.{metodo.lower()}("{url}", oncomplete={callback_nome}'
    if corpo and metodo in ("POST", "PUT", "PATCH"):
        ajax_call += f', data={repr(corpo)}, headers={{"Content-Type": "application/json"}}'
    ajax_call += ")"
    
    if gatilho_clique:
        if seletor_resultado:
            loading_code = f"""document.select("{seletor_resultado}")[0].html = '<div class="animate-pulse bg-gray-200 h-8 w-full rounded"></div>'"""
        else:
            loading_code = ""
            
        exec_code = f"""
def _disparar_busca(ev):
    ev.preventDefault()
    {loading_code}
    {ajax_call}

from browser import document
els = document.select("{gatilho_clique}")
for el in els:
    el.bind("click", _disparar_busca)
"""
    else:
        exec_code = ajax_call

    return script_python(f"""
from browser import ajax
{callback_code}
{exec_code}
""")


def estado(nome_var: str, valor_inicial: str = '""', seletor_bind: str | None = None) -> str:
    """
    Gera um sistema de estado reativo simples: uma variável observável
    onde mudanças disparam a atualização automática de elementos vinculados.

    Args:
        nome_var:       Nome da variável de estado (ex: "contador").
        valor_inicial:  Valor inicial como expressão Python (ex: '0', '"texto"', '[]').
        seletor_bind:   Seletor CSS do elemento que será atualizado ao mudar o estado.

    O estado fica acessível via `_estado["nome_var"]` e pode ser atualizado
    com `set_estado("nome_var", novo_valor)`.

    Exemplo:
        estado("contador", "0", "#display-contador")
    """
    bind_code = ""
    if seletor_bind:
        bind_code = f"""
def _observer_{nome_var}(novo_valor):
    from browser import document
    els = document.select("{seletor_bind}")
    if els:
        els[0].html = str(novo_valor)

_observers.setdefault("{nome_var}", []).append(_observer_{nome_var})
"""

    return script_python(f"""
from browser import window

if not hasattr(window, '_pytohtml_estado'):
    window._pytohtml_estado = {{}}
    window._pytohtml_observers = {{}}

_estado = window._pytohtml_estado
_observers = window._pytohtml_observers

_estado["{nome_var}"] = {valor_inicial}

def set_estado(nome, valor):
    _estado[nome] = valor
    for obs in _observers.get(nome, []):
        obs(valor)

{bind_code}
""")


def inserir_html(seletor: str, template: str) -> str:
    """
    Gera código Brython que renderiza HTML dinâmico dentro de
    um elemento do DOM.

    Args:
        seletor:  Seletor CSS do container (ex: "#lista-usuarios").
        template: Código Python que define uma variável `html_resultado`
                  com o HTML a ser inserido.

    Exemplo:
        inserir_html("#container", '''
            itens = ["Maçã", "Banana", "Laranja"]
            html_resultado = "".join(
                f'<div class="p-2 border-b">{item}</div>'
                for item in itens
            )
        ''')
    """
    template_indentado = textwrap.dedent(template)
    return script_python(f"""
from browser import document

{template_indentado}

_el = document.select("{seletor}")
if _el:
    _el[0].html = html_resultado
""")


def espaco_dinamico(id_elemento: str, classes: str | None = None) -> str:
    """
    Cria um <div> vazio com um ID, pronto para receber conteúdo dinâmico
    via Brython (renderizar_em, buscar_api etc.).

    Args:
        id_elemento: ID do elemento HTML.
        classes:     Classes Tailwind extras.

    Exemplo:
        espaco_dinamico("resultado", "mt-4 p-4 bg-white rounded-xl")
    """
    cls = f' class="{classes}"' if classes else ""
    return f'<div id="{id_elemento}"{cls}></div>'


# ─── SweetAlert2 ─────────────────────────────────────────────────────────────
# Nota: Brython não consegue chamar window.Swal.fire() diretamente porque
# o proxy do Brython quebra o contexto `this` do SweetAlert2.
# Solução: usamos <script> JS puro para todas as funções swal_*.
# Para chamadas dinâmicas dentro de Brython (ex: buscar_api), usamos
# window.eval() que executa o JS no contexto global correto.


def _swal_js(opcoes: str) -> str:
    """Helper interno: gera <script> JS chamando Swal.fire."""
    return f'<script>Swal.fire({opcoes})</script>'


def alerta_sucesso(titulo: str = "Sucesso!", texto: str = "", **kwargs) -> str:
    """
    Exibe um SweetAlert2 de sucesso ao carregar a página.

    Args:
        titulo: Título do alerta.
        texto:  Texto descritivo.

    Exemplo:
        alerta_sucesso("Salvo!", "Suas alterações foram salvas.")
    """
    return _swal_js(f"{{icon: 'success', title: '{titulo}', text: '{texto}', confirmButtonColor: '#16a34a'}}")


def alerta_erro(titulo: str = "Erro!", texto: str = "", **kwargs) -> str:
    """
    Exibe um SweetAlert2 de erro ao carregar a página.

    Exemplo:
        alerta_erro("Falha!", "Não foi possível conectar.")
    """
    return _swal_js(f"{{icon: 'error', title: '{titulo}', text: '{texto}', confirmButtonColor: '#dc2626'}}")


def alerta_aviso(titulo: str = "Atenção!", texto: str = "", **kwargs) -> str:
    """
    Exibe um SweetAlert2 de aviso.

    Exemplo:
        alerta_aviso("Cuidado!", "Essa ação não pode ser desfeita.")
    """
    return _swal_js(f"{{icon: 'warning', title: '{titulo}', text: '{texto}', confirmButtonColor: '#f59e0b'}}")


def alerta_info(titulo: str = "Info", texto: str = "", **kwargs) -> str:
    """
    Exibe um SweetAlert2 informativo.

    Exemplo:
        alerta_info("Dica", "Clique no botão para começar.")
    """
    return _swal_js(f"{{icon: 'info', title: '{titulo}', text: '{texto}', confirmButtonColor: '#3b82f6'}}")


def alerta(titulo: str, texto: str = "", icone: str = "info") -> str:
    """
    Exibe um popup nativo (SweetAlert2) flexível.
    Pode ser usado como trigger ou injetado em scripts.
    
    Args:
        titulo: Título do alerta.
        texto:  Corpo da mensagem.
        icone:  "success" | "error" | "warning" | "info" | "question"
    """
    params = f"{{icon: '{icone}', title: '{titulo}', text: '{texto}', confirmButtonColor: '#3085d6'}}"
    return f"<script>window.Swal.fire({params});</script>"


def pedir_confirmacao(
    seletor: str,
    titulo: str = "Tem certeza?",
    texto: str = "",
    texto_confirmar: str = "Sim",
    texto_cancelar: str = "Cancelar",
    codigo_confirmado: str = "",
) -> str:
    """
    Vincula um SweetAlert2 de confirmação a um clique em um elemento.

    Args:
        seletor:            Seletor CSS do elemento que dispara a confirmação.
        titulo:             Título do diálogo.
        texto:              Texto descritivo.
        texto_confirmar:    Label do botão de confirmação.
        texto_cancelar:     Label do botão de cancelamento.
        codigo_confirmado:  Código JS a executar ao confirmar (opcional).

    Exemplo:
        pedir_confirmacao("#btn-deletar",
            titulo="Deletar item?",
            texto="Essa ação não pode ser desfeita.",
        )
    """
    on_confirm = codigo_confirmado if codigo_confirmado else ""
    return f"""<script>
document.querySelector("{seletor}").addEventListener("click", function() {{
    Swal.fire({{
        icon: "warning",
        title: "{titulo}",
        text: "{texto}",
        showCancelButton: true,
        confirmButtonText: "{texto_confirmar}",
        cancelButtonText: "{texto_cancelar}",
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
    }}).then(function(result) {{
        if (result.isConfirmed) {{
            {on_confirm}
            Swal.fire({{icon: "success", title: "Confirmado!", timer: 1500, showConfirmButton: false}});
        }}
    }});
}});
</script>"""


def notificacao_rapida(
    titulo: str,
    icone: str = "success",
    posicao: str = "top-end",
    duracao: int = 3000,
    **kwargs,
) -> str:
    """
    Exibe uma notificação toast (pequena, não intrusiva) com SweetAlert2.

    Args:
        titulo:   Texto do toast.
        icone:    "success" | "error" | "warning" | "info" | "question".
        posicao:  Posição na tela: "top-end", "top-start", "bottom-end", etc.
        duracao:  Duração em milissegundos.

    Exemplo:
        notificacao_rapida("Salvo com sucesso!")
    """
    return f"""<script>
Swal.mixin({{toast: true, showConfirmButton: false, timerProgressBar: true}}).fire({{
    icon: "{icone}", title: "{titulo}", position: "{posicao}", timer: {duracao}
}});
</script>"""


def alerta_ao_enviar(seletor_form: str, mensagem_sucesso: str = "Enviado com sucesso!") -> str:
    """
    Intercepta o submit de um formulário e exibe um SweetAlert2 de sucesso
    ao invés do comportamento padrão (recarregar a página).

    Args:
        seletor_form:      Seletor CSS do formulário.
        mensagem_sucesso:  Mensagem do SweetAlert2 de sucesso.

    Exemplo:
        alerta_ao_enviar("#form-contato", "Mensagem enviada com sucesso!")
    """
    return f"""<script>
document.addEventListener("DOMContentLoaded", function() {{
    var form = document.querySelector("{seletor_form}");
    if (form) {{
        form.addEventListener("submit", function(ev) {{
            ev.preventDefault();
            Swal.fire({{
                icon: "success",
                title: "{mensagem_sucesso}",
                confirmButtonColor: "#16a34a",
            }});
        }});
    }}
}});
</script>"""


def enviar_formulario(
    seletor_form: str,
    url: str,
    metodo: str = "POST",
    mensagem_sucesso: str = "Enviado com sucesso!",
    texto_carregando: str = "Enviando...",
) -> str:
    """
    Gera um script em Python (Brython) que intercepta o envio de um formulário,
    coleta todos os seus campos e os envia para a URL especificada.
    Mostra alertas automáticos dependendo do resultado (Sucesso ou Erro).

    Args:
        seletor_form:       Seletor CSS do formulário (ex: "form", "#meu-form").
        url:                URL de destino da API (ex: "https://api.com/post").
        metodo:             Método HTTP (padrão POST).
        mensagem_sucesso:   Mensagem do popup caso a requisição seja concluída.
        texto_carregando:   Texto que substituirá o botão de submit enquanto carrega.

    Exemplo:
        enviar_formulario("form", "https://jsonplaceholder.typicode.com/posts")
    """
    return script_python(f"""
from browser import document, ajax, window
import json

def _enviar_form(ev):
    ev.preventDefault()
    form = ev.target
    
    # Prepara o botão para bloqueio
    btn = form.querySelector('button[type="submit"]')
    if btn:
        texto_original = btn.text
        btn.text = "{texto_carregando}"
        btn.disabled = True
    else:
        texto_original = ""
    
    # Coleta todos os inputs do formulário
    dados = {{}}
    for inp in form.querySelectorAll("input, textarea, select"):
        if inp.name:
            dados[inp.name] = inp.value
            
    # Callback quando API responder
    def _pronto(req):
        if btn:
            btn.text = texto_original
            btn.disabled = False
            
        if req.status in [200, 201, 202, 204]:
            window.eval('Swal.fire({{icon: "success", title: "{mensagem_sucesso}", confirmButtonColor: "#16a34a"}})')
            form.reset()
        else:
            window.eval('Swal.fire({{icon: "error", title: "Erro " + str(req.status), text: "Falha ao enviar os dados.", confirmButtonColor: "#3085d6"}})')
            
    # Envio AJAX
    req = ajax.ajax()
    req.open("{metodo.upper()}", "{url}", True)
    req.bind("complete", _pronto)
    req.set_header("Content-Type", "application/json")
    req.send(json.dumps(dados))

# Vincula todos os formulários que batem com o seletor
for f in document.select("{seletor_form}"):
    f.bind("submit", _enviar_form)
""")


def abrir_modal_ao_clicar(seletor_abrir: str, id_modal: str) -> str:
    """
    Vincula a abertura de um modal nativo (<dialog>) ao clique de um elemento.

    Args:
        seletor_abrir: Seletor CSS do botão/elemento que abrirá o modal.
        id_modal:      Atributo 'id' do modal a ser aberto.

    Exemplo:
        abrir_modal_ao_clicar("#btn-abrir", "meu-modal")
    """
    return f"""<script>
document.addEventListener("DOMContentLoaded", function() {{
    const botoes = document.querySelectorAll("{seletor_abrir}");
    const modal = document.getElementById("{id_modal}");
    if (modal) {{
        botoes.forEach(btn => btn.addEventListener("click", () => modal.showModal()));
    }}
}});
</script>"""


def alerta_ao_clicar(
    seletor: str,
    titulo: str,
    texto: str = "",
    icone: str = "info",
) -> str:
    """
    Vincula um SweetAlert2 simples a um clique em um elemento.

    Args:
        seletor: Seletor CSS do elemento.
        titulo:  Título do alerta.
        texto:   Texto do alerta.
        icone:   Ícone: "success" | "error" | "warning" | "info" | "question".

    Exemplo:
        alerta_ao_clicar("#btn-ajuda", "Ajuda", "Clique nos botões para testar.", "question")
    """
    return f"""<script>
document.querySelector("{seletor}").addEventListener("click", function() {{
    Swal.fire({{icon: "{icone}", title: "{titulo}", text: "{texto}"}});
}});
</script>"""
