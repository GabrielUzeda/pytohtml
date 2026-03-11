"""
pytohtml.pagina
=============
Estrutura base da página HTML e função de salvamento.
"""


import logging


def html(*conteudo: str, titulo_pagina: str = "Página", lang: str = "pt-BR", head_extra: str = "", brython: bool = False, favicon: str = "") -> str:
    """
    Gera uma página HTML completa com Tailwind CSS via CDN.

    Args:
        *conteudo:     Elementos HTML filhos (strings geradas pelas outras funções).
        titulo_pagina: Texto do <title>.
        lang:          Idioma da página.
        head_extra:    Conteúdo extra para ser adicionado no <head>.
        brython:       Se True, inclui o Brython via CDN para scripts Python client-side.
        favicon:       URL para a imagem do favicon (opcional).

    Exemplo:
        pagina = html(
            titulo("Olá Mundo"),
            paragrafo("Bem-vindo!"),
            titulo_pagina="Meu Site",
            brython=True,
            favicon="icone.png"
        )
    """
    corpo = "\n".join(conteudo)

    brython_head = ""
    brython_onload = ""
    if brython:
        brython_head = """  <script src="https://cdn.jsdelivr.net/npm/brython@3.14.0/brython.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/brython@3.14.0/brython_stdlib.js"></script>"""
        brython_onload = ' onload="brython()"'
        
    favicon_tag = f'  <link rel="icon" href="{favicon}" />\n' if favicon else ""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{titulo_pagina}</title>
{favicon_tag}  {head_extra}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
{brython_head}
</head>
<body class="bg-gray-50 text-gray-800 antialiased min-h-screen"{brython_onload}>
{corpo}
</body>
</html>"""


def salvar(caminho: str, conteudo: str) -> None:
    """
    Salva o HTML em um arquivo no disco.

    Args:
        caminho:  Caminho do arquivo (ex: "index.html").
        conteudo: String HTML completa.
    """
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    logging.info(f"✅ Arquivo salvo: {caminho}")
