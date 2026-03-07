# `rotulo()` e `entrada()`

> `rotulo()` gera um `<label>` semântico. `entrada()` gera um `<input>` estilizado. Usados em conjunto para criar campos de formulário acessíveis.

`elementos.py` · `formulários`

---

## Assinaturas

```python
rotulo(texto: str, para: str | None = None, classes: str | None = None) → str

entrada(
    tipo: str = "text",
    nome: str = "",
    placeholder: str = "",
    valor: str = "",
    obrigatorio: bool = False,
    classes: str | None = None,
) → str
```

## Parâmetros — `rotulo()`

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Texto do rótulo (obrigatório) |
| `para` | `str \| None` | `None` | ID do `<input>` associado (atributo `for`) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

## Parâmetros — `entrada()`

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `tipo` | `str` | `"text"` | Tipo HTML: `"text"`, `"email"`, `"password"`, `"number"`, `"tel"`, etc. |
| `nome` | `str` | `""` | Atributo `name` e `id` do campo |
| `placeholder` | `str` | `""` | Texto de dica exibido quando vazio |
| `valor` | `str` | `""` | Valor inicial pré-preenchido |
| `obrigatorio` | `bool` | `False` | Impede o envio do form se vazio (atributo `required`) |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Campo de texto simples com rótulo

```python
from pytohtml import rotulo, entrada

rotulo("Nome completo", para="nome")
entrada(nome="nome", placeholder="Digite seu nome")
```

**HTML gerado:**

```html
<label for="nome" class="block text-sm font-medium text-gray-700 mb-1">Nome completo</label>
<input type="text" name="nome" id="nome" placeholder="Digite seu nome"
       class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
```

---

### 🔵 Nível 2 — Intermediário

> Diferentes tipos de entrada

```python
from pytohtml import coluna, rotulo, entrada

coluna(
    rotulo("Email",  para="email"),
    entrada(tipo="email",    nome="email",    placeholder="seu@email.com", obrigatorio=True),

    rotulo("Senha",  para="senha"),
    entrada(tipo="password", nome="senha",    placeholder="Mínimo 8 caracteres"),

    rotulo("Idade",  para="idade"),
    entrada(tipo="number",   nome="idade",    placeholder="25", valor="18"),

    rotulo("Telefone", para="tel"),
    entrada(tipo="tel",      nome="tel",      placeholder="(11) 99999-9999"),

    centralizado=False, distanciamento=2,
)
```

> 💡 **Dica:** O atributo `id` e `name` são preenchidos com o mesmo valor do parâmetro `nome`. Isso vincula automaticamente o `rotulo(para=...)` ao `entrada(nome=...)`, melhorando a acessibilidade.

---

### 🟡 Nível 3 — Difícil

> Campo de busca com estilo customizado

```python
from pytohtml import linha, entrada, botao

linha(
    entrada(
        tipo="search",
        nome="q",
        placeholder="Buscar documentação...",
        classes="rounded-r-none border-r-0 flex-1"
    ),
    botao("Buscar", variante="primario", classes="rounded-l-none"),
    centralizado=False, distanciamento=0,
)
```

---

### 🟣 Nível 4 — Profissional

> Campos com validação e pré-preenchimento

```python
from pytohtml import formulario, rotulo, entrada, botao

# Simula um formulário de edição com dados existentes
usuario = {"nome": "Gabriel Uzeda", "email": "gabriel@exemplo.com"}

formulario(
    rotulo("Nome", para="nome"),
    entrada(
        tipo="text",
        nome="nome",
        valor=usuario["nome"],
        obrigatorio=True,
        classes="bg-blue-50",
    ),
    rotulo("Email", para="email"),
    entrada(
        tipo="email",
        nome="email",
        valor=usuario["email"],
        obrigatorio=True,
    ),
    rotulo("Nova senha (opcional)", para="senha"),
    entrada(
        tipo="password",
        nome="senha",
        placeholder="Deixe vazio para manter a atual",
    ),
    botao("Salvar alterações", variante="primario", tipo="submit", classes="w-full"),
    acao="/usuario/editar",
    metodo="post",
)
```

---

## Referência Rápida — `entrada(tipo=...)`

| `tipo=` | Uso |
|---------|-----|
| `"text"` | Texto livre (padrão) |
| `"email"` | Email com validação nativa |
| `"password"` | Senha (texto ocultado) |
| `"number"` | Número com controles +/- |
| `"tel"` | Telefone (teclado numérico no mobile) |
| `"search"` | Campo de busca (com ícone no browser) |
| `"date"` | Seletor de data |
| `"file"` | Upload de arquivo |
| `"hidden"` | Campo oculto (não visível) |

---

← [accordion](accordion) · **rotulo e entrada** · [textarea →](textarea)
