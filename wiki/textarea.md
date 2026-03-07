# `textarea()`

> Gera um campo de texto longo (`<textarea>`) estilizado, com redimensionamento vertical.

`elementos.py` · `formulários`

---

## Assinatura

```python
textarea(
    nome: str = "",
    placeholder: str = "",
    linhas: int = 4,
    valor: str = "",
    obrigatorio: bool = False,
    classes: str | None = None,
) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `nome` | `str` | `""` | Atributo `name` e `id` do campo |
| `placeholder` | `str` | `""` | Texto de dica exibido quando vazio |
| `linhas` | `int` | `4` | Altura inicial em linhas (atributo `rows`) |
| `valor` | `str` | `""` | Valor inicial pré-preenchido |
| `obrigatorio` | `bool` | `False` | Impede o envio do form se vazio (atributo `required`) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Campo de mensagem simples

```python
from pytohtml import rotulo, textarea

rotulo("Mensagem", para="mensagem")
textarea(nome="mensagem", placeholder="Escreva sua mensagem aqui...")
```

**HTML gerado:**

```html
<textarea rows="4" name="mensagem" id="mensagem"
          placeholder="Escreva sua mensagem aqui..."
          class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-y">
</textarea>
```

---

### 🔵 Nível 2 — Intermediário

> Variações de altura e uso obrigatório

```python
# Campo compacto (2 linhas)
textarea(nome="bio", placeholder="Breve bio...", linhas=2)

# Campo grande para texto longo
textarea(nome="descricao", placeholder="Descreva detalhadamente...", linhas=8)

# Campo obrigatório com placeholder de instrução
textarea(
    nome="feedback",
    placeholder="Por favor, descreva o problema encontrado (mínimo 20 caracteres).",
    linhas=5,
    obrigatorio=True,
)
```

> 💡 **Dica:** `resize-y` já vem aplicado por padrão, permitindo que o usuário aumente verticalmente o campo conforme digita. Para desabilitar: `classes="resize-none"`.

---

### 🟡 Nível 3 — Difícil

> Textarea pré-preenchida com conteúdo de edição

```python
from pytohtml import formulario, rotulo, textarea, botao

# Simula edição de post existente
post_existente = """# Título do Post

Este é o conteúdo atual do post que está sendo editado.
Pode ter múltiplas linhas."""

formulario(
    rotulo("Conteúdo", para="conteudo"),
    textarea(
        nome="conteudo",
        valor=post_existente,
        linhas=12,
        classes="font-mono text-sm",
    ),
    botao("Salvar post", variante="primario", tipo="submit"),
    acao="/posts/editar",
    metodo="post",
)
```

---

### 🟣 Nível 4 — Profissional

> Formulário de contato completo com textarea e envio assíncrono

```python
from pytohtml import html, cartao, titulo, formulario, rotulo, entrada, textarea, botao, enviar_formulario

pagina = html(
    cartao(
        titulo("Fale conosco", tamanho="medio"),
        formulario(
            rotulo("Nome", para="nome"),
            entrada(tipo="text",  nome="nome",  placeholder="Seu nome completo", obrigatorio=True),
            rotulo("Email", para="email"),
            entrada(tipo="email", nome="email", placeholder="seu@email.com",      obrigatorio=True),
            rotulo("Assunto", para="assunto"),
            entrada(tipo="text",  nome="assunto", placeholder="Como podemos ajudar?"),
            rotulo("Mensagem", para="mensagem"),
            textarea(
                nome="mensagem",
                placeholder="Descreva sua dúvida ou sugestão...",
                linhas=6,
                obrigatorio=True,
            ),
            botao("Enviar mensagem", variante="primario", tipo="submit", classes="w-full"),
        ),
        enviar_formulario("form", "https://jsonplaceholder.typicode.com/posts"),
        classes="max-w-lg mx-auto",
    ),
    titulo_pagina="Contato",
    brython=True,
)
```

---

## Referência Rápida

| Parâmetro | Efeito |
|-----------|--------|
| `linhas=2` | Campo compacto |
| `linhas=4` | Altura padrão |
| `linhas=8` | Campo para textos longos |
| `classes="resize-none"` | Desabilita redimensionamento |
| `classes="font-mono"` | Fonte monospace (editor de código) |

---

← [rotulo-e-entrada](rotulo-e-entrada) · **textarea** · [formulario →](formulario)
