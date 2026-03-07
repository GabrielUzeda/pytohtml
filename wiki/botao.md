# `botao()`

> Gera um botão HTML estilizado com variantes de cor e comportamento.

`elementos.py` · `interação`

---

## Assinatura

```python
botao(texto: str, variante: str = "primario", tipo: str = "button", classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Rótulo visível do botão (obrigatório) |
| `variante` | `str` | `"primario"` | Estilo visual — veja tabela de variantes abaixo |
| `tipo` | `str` | `"button"` | Atributo `type` do HTML: `"button"`, `"submit"`, `"reset"` |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |
| `escapar` | `bool` | `True` | Escapa HTML para prevenir XSS |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Botão azul padrão — variante `"primario"`

```python
from pytohtml import botao

botao("Clique aqui")
```

**HTML gerado:**

```html
<button type="button" class="px-5 py-2.5 rounded-lg font-medium text-sm transition-colors cursor-pointer bg-blue-600 hover:bg-blue-700 text-white">Clique aqui</button>
```

---

### 🔵 Nível 2 — Intermediário

> Todas as variantes disponíveis

```python
from pytohtml import linha, botao

linha(
    botao("Primário",   variante="primario"),
    botao("Secundário", variante="secundario"),
    botao("Perigo",     variante="perigo"),
    botao("Sucesso",    variante="sucesso"),
    botao("Fantasma",   variante="fantasma"),
    botao("Texto",      variante="texto"),
)
```

> 💡 **Dica:** Use `"fantasma"` para ações secundárias que não devem chamar muito a atenção. Use `"perigo"` apenas para ações destrutivas como deletar ou cancelar.

---

### 🟡 Nível 3 — Difícil

> Personalizando com classes Tailwind e adicionando `id` via classes

```python
# Botão arredondado com sombra
botao("Começar agora", variante="primario", classes="rounded-full shadow-lg px-8")

# Botão de largura total
botao("Entrar", variante="sucesso", classes="w-full")

# Botão com ID para uso com JavaScript ou Brython
botao("Buscar", variante="primario", classes='id="btn-buscar"')
```

---

### 🟣 Nível 4 — Profissional

> Botão `type="submit"` dentro de um formulário real

```python
from pytohtml import formulario, rotulo, entrada, botao

formulario(
    rotulo("Email", para="email"),
    entrada(tipo="email", nome="email", placeholder="seu@email.com", obrigatorio=True),
    botao("Enviar", variante="primario", tipo="submit", classes="w-full mt-2"),
    acao="https://api.exemplo.com/contato",
    metodo="post",
)
```

---

## Referência Rápida

| `variante=` | Cor de fundo | Uso típico |
|-------------|-------------|------------|
| `"primario"` | Azul | Ação principal da página |
| `"secundario"` | Cinza claro | Ação secundária |
| `"perigo"` | Vermelho | Deletar, cancelar |
| `"sucesso"` | Verde | Confirmar, salvar |
| `"fantasma"` | Transparente com borda | Ação discreta |
| `"texto"` | Transparente sem borda | Links em forma de botão |
| `"vazio"` | Totalmente transparente | Customização total via `classes` |

---

← [paragrafo](paragrafo) · **botao** · [etiqueta →](etiqueta)
