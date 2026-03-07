# `inserir_html()`

> Gera código Brython que renderiza HTML dinâmico dentro de um elemento do DOM a partir de um template Python.

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
inserir_html(seletor: str, template: str) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `seletor` | `str` | — | Seletor CSS do elemento container (ex: `"#lista"`) |
| `template` | `str` | — | Código Python que define a variável `html_resultado` com o HTML a inserir |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Renderizar uma lista de itens

```python
from pytohtml import html, espaco_dinamico, inserir_html

pagina = html(
    espaco_dinamico("lista"),
    inserir_html("#lista", '''
        itens = ["Python", "Tailwind CSS", "Brython"]
        html_resultado = "".join(
            f'<div class="p-2 border-b border-gray-200">{item}</div>'
            for item in itens
        )
    '''),
    titulo_pagina="Lista",
    brython=True,
)
```

**Script gerado:**

```html
<script type="text/python">
from browser import document

itens = ["Python", "Tailwind CSS", "Brython"]
html_resultado = "".join(
    f'<div class="p-2 border-b border-gray-200">{item}</div>'
    for item in itens
)

_el = document.select("#lista")
if _el:
    _el[0].html = html_resultado
</script>
```

---

### 🔵 Nível 2 — Intermediário

> Grid de cards gerado dinamicamente

```python
from pytohtml import html, espaco_dinamico, inserir_html

pagina = html(
    espaco_dinamico("grade-produtos", "grid grid-cols-1 md:grid-cols-3 gap-4"),
    inserir_html("#grade-produtos", '''
        produtos = [
            {"nome": "pytohtml", "versao": "1.0", "cor": "blue"},
            {"nome": "Tailwind",  "versao": "3.x", "cor": "purple"},
            {"nome": "Brython",   "versao": "3.14", "cor": "green"},
        ]

        def card(p):
            return f\'\'\'
            <div class="bg-white rounded-2xl border border-gray-200 p-6 shadow-md">
                <span class="bg-{p["cor"]}-100 text-{p["cor"]}-700 text-xs font-medium px-2.5 py-0.5 rounded-full">{p["versao"]}</span>
                <h3 class="text-xl font-semibold mt-3">{p["nome"]}</h3>
            </div>
            \'\'\'

        html_resultado = "".join(card(p) for p in produtos)
    '''),
    titulo_pagina="Produtos",
    brython=True,
)
```

> 💡 **Dica:** O código no `template` deve **obrigatoriamente** definir uma variável chamada `html_resultado` com o HTML final a ser inserido. Qualquer outro código (funções auxiliares, variáveis) também pode ser definido no template.

---

### 🟡 Nível 3 — Difícil

> Tabela HTML construída com Python puro

```python
from pytohtml import html, espaco_dinamico, inserir_html

pagina = html(
    espaco_dinamico("tabela-vendas"),
    inserir_html("#tabela-vendas", '''
        vendas = [
            ("Janeiro",  12500, "+8%"),
            ("Fevereiro", 9800, "-4%"),
            ("Março",    15200, "+15%"),
        ]

        linhas = "".join(
            f"""<tr class="{'bg-white' if i % 2 == 0 else 'bg-gray-50'}">
                <td class="px-4 py-2 border border-gray-200">{mes}</td>
                <td class="px-4 py-2 border border-gray-200 font-mono">R$ {valor:,.0f}</td>
                <td class="px-4 py-2 border border-gray-200 text-{'green' if '+' in var else 'red'}-600">{var}</td>
            </tr>"""
            for i, (mes, valor, var) in enumerate(vendas)
        )

        html_resultado = f"""
        <div class="overflow-x-auto rounded-xl border border-gray-200">
            <table class="w-full text-sm border-collapse">
                <thead>
                    <tr>
                        <th class="bg-gray-100 px-4 py-2 text-left">Mês</th>
                        <th class="bg-gray-100 px-4 py-2 text-left">Receita</th>
                        <th class="bg-gray-100 px-4 py-2 text-left">Variação</th>
                    </tr>
                </thead>
                <tbody>{linhas}</tbody>
            </table>
        </div>
        """
    '''),
    titulo_pagina="Vendas",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Renderizar dados de API com template complexo

```python
from pytohtml import html, espaco_dinamico, ao_clicar, botao, inserir_html, buscar_dados

pagina = html(
    espaco_dinamico("resultado", "mt-4 space-y-3"),
    botao("Buscar posts", variante="primario", classes='id="btn-buscar"'),
    buscar_dados(
        "https://dummyjson.com/posts?limit=5",
        seletor_resultado="#resultado",
        gatilho_clique="#btn-buscar",
    ),
    titulo_pagina="Posts",
    brython=True,
)
```

---

← [espaco-dinamico](espaco-dinamico) · **inserir-html** · [estado →](estado)
