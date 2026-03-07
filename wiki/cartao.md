# `cartao()`

> Contêiner no estilo card — fundo branco, borda sutil e padding padrão para agrupar conteúdo relacionado.

`elementos.py` · `layout`

---

## Assinatura

```python
cartao(*conteudo: str, sombra: bool = True, classes: str | None = None) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `*conteudo` | `str` | — | Elementos filhos do card (obrigatório ao menos 1) |
| `sombra` | `bool` | `True` | Aplica `shadow-md` para elevação visual |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Card simples com título e parágrafo

```python
from pytohtml import cartao, titulo, paragrafo

cartao(
    titulo("Meu Card", tamanho="medio"),
    paragrafo("Conteúdo do card aqui."),
)
```

**HTML gerado:**

```html
<div class="bg-white rounded-2xl border border-gray-200 p-6 shadow-md">
  <h3 ...>Meu Card</h3>
  <p ...>Conteúdo do card aqui.</p>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Cards com e sem sombra em uma grade

```python
from pytohtml import grade, cartao, titulo, paragrafo, etiqueta

grade(
    cartao(
        etiqueta("Plano Free", cor="cinza"),
        titulo("R$ 0/mês", tamanho="grande"),
        paragrafo("Funcionalidades básicas para começar."),
    ),
    cartao(
        etiqueta("Plano Pro", cor="azul"),
        titulo("R$ 49/mês", tamanho="grande"),
        paragrafo("Tudo do Free + recursos avançados."),
        classes="border-blue-200 ring-2 ring-blue-500",
    ),
    cartao(
        etiqueta("Plano Enterprise", cor="roxo"),
        titulo("Sob consulta", tamanho="grande"),
        paragrafo("Soluções customizadas para grandes times."),
    ),
    colunas=3,
)
```

> 💡 **Dica:** Use `sombra=False` para cards dentro de outros cards ou em fundos já elevados, evitando sobreposição visual.

---

### 🟡 Nível 3 — Difícil

> Card de perfil com avatar, nome e etiquetas

```python
from pytohtml import cartao, coluna, linha, avatar, titulo, paragrafo, etiqueta

cartao(
    coluna(
        avatar(iniciais="GU", tamanho=16),
        titulo("Gabriel Uzeda", tamanho="medio"),
        paragrafo("Desenvolvedor Python", classes="text-gray-400 text-sm -mt-2"),
        linha(
            etiqueta("Python", cor="azul"),
            etiqueta("Tailwind", cor="roxo"),
            centralizado=True, distanciamento=2,
        ),
        centralizado=True, distanciamento=2,
    ),
    classes="max-w-xs mx-auto text-center",
)
```

---

### 🟣 Nível 4 — Profissional

> Card como container de formulário com cabeçalho destacado

```python
from pytohtml import cartao, titulo, paragrafo, divisor, formulario, rotulo, entrada, botao

cartao(
    titulo("Criar conta", tamanho="medio"),
    paragrafo("Preencha os dados para se cadastrar.", classes="text-gray-400 text-sm mt-1"),
    divisor(classes="my-4"),
    formulario(
        rotulo("Nome completo", para="nome"),
        entrada(tipo="text",  nome="nome",  placeholder="Seu nome"),
        rotulo("Email", para="email"),
        entrada(tipo="email", nome="email", placeholder="seu@email.com", obrigatorio=True),
        botao("Criar conta", variante="primario", tipo="submit", classes="w-full"),
        acao="/cadastro", metodo="post",
    ),
    classes="max-w-sm mx-auto",
)
```

---

## Referência Rápida

| Parâmetro / Classe | Efeito |
|--------------------|--------|
| `sombra=True` | Adiciona `shadow-md` (padrão) |
| `sombra=False` | Remove a sombra |
| `classes="max-w-sm"` | Limita a largura do card |
| `classes="mx-auto"` | Centraliza horizontalmente |
| `classes="ring-2 ring-blue-500"` | Borda de destaque (card selecionado) |
| `classes="hover:shadow-lg transition-shadow"` | Sombra maior no hover |

---

← [aviso-estatico](aviso-estatico) · **cartao** · [lista →](lista)
