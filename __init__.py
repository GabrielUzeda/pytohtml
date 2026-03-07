# pytohtml — Gere HTML com Tailwind CSS usando Python puro
# Importe tudo diretamente de pytohtml

from .pagina import html, salvar
from .layout import container, secao, cabecalho, nav, rodape, modal, destaque, linha, coluna, grade
from .elementos import (
    titulo, paragrafo, imagem, botao, link,
    tabela, lista, divisor, etiqueta, aviso_estatico,
    entrada, textarea, rotulo, formulario,
    cartao, codigo, animacao_carregando, avatar, accordion
)
from .interatividade import (
    script_python, ao_clicar, ao_carregar,
    buscar_dados, estado, inserir_html, espaco_dinamico,
    alerta_sucesso, alerta_erro, alerta_aviso, alerta_info, alerta,
    pedir_confirmacao, notificacao_rapida, alerta_ao_enviar, alerta_ao_clicar,
    abrir_modal_ao_clicar, enviar_formulario,
)

__all__ = [
    "html", "salvar",
    "container", "secao", "cabecalho", "nav", "rodape", "modal", "destaque", "linha", "coluna", "grade",
    "titulo", "paragrafo", "imagem", "botao", "link",
    "tabela", "lista", "divisor", "etiqueta", "aviso_estatico",
    "entrada", "textarea", "rotulo", "formulario",
    "cartao", "codigo", "animacao_carregando", "avatar", "accordion",
    "script_python", "ao_clicar", "ao_carregar",
    "buscar_dados", "estado", "inserir_html", "espaco_dinamico",
    "alerta", "alerta_sucesso", "alerta_erro", "alerta_aviso", "alerta_info",
    "pedir_confirmacao", "notificacao_rapida", "alerta_ao_enviar", "alerta_ao_clicar",
    "abrir_modal_ao_clicar", "enviar_formulario",
]

