# `estado()`

> Cria um sistema de estado reativo — uma variável observável que atualiza automaticamente elementos do DOM quando seu valor muda.

`interatividade.py` · `brython` · **Requer `brython=True`**

---

## Assinatura

```python
estado(nome_var: str, valor_inicial: str = '""', seletor_bind: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `nome_var` | `str` | — | Nome da variável de estado (obrigatório) |
| `valor_inicial` | `str` | `'""'` | Expressão Python do valor inicial (ex: `'0'`, `'"texto"'`, `'[]'`) |
| `seletor_bind` | `str \| None` | `None` | Seletor CSS do elemento que será atualizado automaticamente |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Contador simples reativo

```python
from pytohtml import html, espaco_dinamico, botao, estado, ao_clicar

pagina = html(
    espaco_dinamico("display", "text-4xl font-bold text-center mt-8"),
    botao("Incrementar", classes='id="btn"'),
    estado("contador", "0", "#display"),
    ao_clicar("#btn", '''
        n = int(_estado["contador"])
        set_estado("contador", n + 1)
    '''),
    titulo_pagina="Contador",
    brython=True,
)
```

**Como funciona:**
- `estado("contador", "0", "#display")` cria `_estado["contador"] = 0`
- Toda vez que `set_estado("contador", novo_valor)` é chamado, o elemento `#display` é atualizado automaticamente
- `_estado` e `set_estado` ficam disponíveis globalmente na página via `window._pytohtml_estado`

---

### 🔵 Nível 2 — Intermediário

> Múltiplos estados independentes

```python
from pytohtml import html, linha, coluna, espaco_dinamico, botao, estado, ao_clicar

pagina = html(
    coluna(
        linha(
            coluna(
                espaco_dinamico("display-a", "text-3xl font-bold text-blue-600 text-center"),
                linha(botao("−", classes='id="dec-a"'), botao("+", classes='id="inc-a"')),
            ),
            coluna(
                espaco_dinamico("display-b", "text-3xl font-bold text-green-600 text-center"),
                linha(botao("−", classes='id="dec-b"'), botao("+", classes='id="inc-b"')),
            ),
        ),
        espaco_dinamico("soma", "text-xl text-center text-gray-500"),
    ),
    estado("a", "0", "#display-a"),
    estado("b", "0", "#display-b"),
    ao_clicar("#inc-a", 'set_estado("a", int(_estado["a"]) + 1)\nfrom browser import document\ndocument["soma"].text = f\'Soma: {int(_estado["a"]) + int(_estado["b"])}\''),
    ao_clicar("#dec-a", 'set_estado("a", int(_estado["a"]) - 1)\nfrom browser import document\ndocument["soma"].text = f\'Soma: {int(_estado["a"]) + int(_estado["b"])}\''),
    ao_clicar("#inc-b", 'set_estado("b", int(_estado["b"]) + 1)\nfrom browser import document\ndocument["soma"].text = f\'Soma: {int(_estado["a"]) + int(_estado["b"])}\''),
    ao_clicar("#dec-b", 'set_estado("b", int(_estado["b"]) - 1)\nfrom browser import document\ndocument["soma"].text = f\'Soma: {int(_estado["a"]) + int(_estado["b"])}\''),
    titulo_pagina="Dois Contadores",
    brython=True,
)
```

> 💡 **Dica:** `_estado` é um dicionário global compartilhado entre todos os scripts da página. Acesse com `_estado["nome_var"]` e atualize com `set_estado("nome_var", novo_valor)`.

---

### 🟡 Nível 3 — Difícil

> Estado de lista com renderização customizada

```python
from pytohtml import html, coluna, linha, entrada, botao, espaco_dinamico, estado, ao_clicar, script_python

pagina = html(
    coluna(
        linha(
            entrada(nome="novo-item", placeholder="Novo item...", classes='id="inp"'),
            botao("+ Adicionar", variante="primario", classes='id="btn-add"'),
        ),
        espaco_dinamico("lista", "mt-4 space-y-2"),
    ),
    estado("itens", "[]"),
    script_python('''
        from browser import document

        def renderizar(novos_itens):
            if not novos_itens:
                document["lista"].html = "<p class='text-gray-400 text-sm'>Lista vazia.</p>"
                return
            html_itens = "".join(
                f\'<div class="flex justify-between p-3 bg-white border rounded-lg">\'
                f\'<span>{item}</span><span class="text-gray-300 text-xs">#{i+1}</span></div>\'
                for i, item in enumerate(novos_itens)
            )
            document["lista"].html = html_itens

        # Registra o observer para re-renderizar ao mudar o estado
        _observers.setdefault("itens", []).append(renderizar)
        renderizar(_estado["itens"])
    '''),
    ao_clicar("#btn-add", '''
        inp = document.select("#inp")[0]
        texto = inp.value.strip()
        if texto:
            lista_atual = list(_estado["itens"])
            lista_atual.append(texto)
            set_estado("itens", lista_atual)
            inp.value = ""
    '''),
    titulo_pagina="Lista Reativa",
    brython=True,
)
```

---

### 🟣 Nível 4 — Profissional

> Estado com valor inicial complexo (dicionário)

```python
from pytohtml import html, espaco_dinamico, estado, ao_clicar, botao

pagina = html(
    espaco_dinamico("perfil", "p-4 bg-white border rounded-xl"),
    botao("Promover para Admin", classes='id="btn-promover"'),
    estado("usuario", '{"nome": "Gabriel", "cargo": "Dev", "nivel": 1}'),
    ao_clicar("#btn-promover", '''
        from browser import document
        u = dict(_estado["usuario"])
        u["cargo"] = "Admin"
        u["nivel"] = 99
        set_estado("usuario", u)
        document["perfil"].html = f"""
            <p><strong>Nome:</strong> {u["nome"]}</p>
            <p><strong>Cargo:</strong> {u["cargo"]}</p>
            <p><strong>Nível:</strong> {u["nivel"]}</p>
        """
    '''),
    titulo_pagina="Perfil",
    brython=True,
)
```

---

## Referência Rápida

| Operação | Código |
|----------|--------|
| Ler estado | `_estado["nome"]` |
| Atualizar estado | `set_estado("nome", novo_valor)` |
| Estado numérico | `estado("n", "0", "#el")` |
| Estado texto | `estado("msg", '"inicial"', "#el")` |
| Estado lista | `estado("lista", "[]")` |
| Estado dict | `estado("obj", '{"chave": "valor"}')` |

---

← [inserir-html](inserir-html) · **estado** · [buscar-dados →](buscar-dados)
