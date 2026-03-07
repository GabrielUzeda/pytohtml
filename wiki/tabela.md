# `tabela()`

> Gera uma tabela HTML estilizada a partir de uma lista de listas Python.

`elementos.py` · `dados`

---

## Assinatura

```python
tabela(dados: list[list[Any]], cabecalho: bool = True, classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `dados` | `list[list[Any]]` | — | Lista de linhas; cada linha é uma lista de células (obrigatório) |
| `cabecalho` | `bool` | `True` | Trata a primeira linha como cabeçalho `<thead>` |
| `classes` | `str \| None` | `None` | Classes Tailwind extras para a `<table>` |
| `escapar` | `bool` | `True` | Escapa HTML das células para prevenir XSS |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Tabela simples com cabeçalho automático

```python
from pytohtml import tabela

tabela([
    ["Nome", "Idade", "Cidade"],
    ["Ana",  28,      "São Paulo"],
    ["João", 34,      "Rio de Janeiro"],
    ["Maria", 22,     "Belo Horizonte"],
])
```

**HTML gerado (estrutura):**

```html
<div class="overflow-x-auto rounded-xl border border-gray-200 shadow-sm">
  <table class="w-full border-collapse text-sm">
    <thead>
      <tr>
        <th class="bg-gray-100 ...">Nome</th>
        <th class="bg-gray-100 ...">Idade</th>
        <th class="bg-gray-100 ...">Cidade</th>
      </tr>
    </thead>
    <tbody>
      <tr><td class="bg-white ...">Ana</td>...</tr>
      <tr><td class="bg-gray-50 ...">João</td>...</tr>
    </tbody>
  </table>
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Tabela sem cabeçalho e tabela de documentação

```python
# Sem cabeçalho — todas as linhas são dados
tabela([
    ["Python", "3.10+"],
    ["Tailwind CSS", "via CDN"],
    ["SweetAlert2", "v11"],
], cabecalho=False)

# Tabela de parâmetros de função
tabela([
    ["Parâmetro", "Tipo",   "Padrão",   "Descrição"],
    ["texto",     "str",    "—",        "Texto do botão"],
    ["variante",  "str",    '"primario"', "Estilo visual"],
    ["tipo",      "str",    '"button"',  "Atributo type HTML"],
], cabecalho=True)
```

> 💡 **Dica:** As linhas do `<tbody>` têm zebra striping automático — linhas pares ficam brancas (`bg-white`) e linhas ímpares ficam cinza claro (`bg-gray-50`).

---

### 🟡 Nível 3 — Difícil

> Tabela gerada dinamicamente a partir de dados Python

```python
from pytohtml import cartao, titulo, tabela

# Dados vindos de uma API ou banco de dados
usuarios = [
    {"nome": "Ana Silva",  "plano": "Pro",    "status": "Ativo"},
    {"nome": "João Costa", "plano": "Free",   "status": "Ativo"},
    {"nome": "Maria Lima", "plano": "Pro",    "status": "Inativo"},
]

linhas = [["Nome", "Plano", "Status"]]
for u in usuarios:
    linhas.append([u["nome"], u["plano"], u["status"]])

cartao(
    titulo("Usuários cadastrados", tamanho="medio"),
    tabela(linhas),
)
```

---

### 🟣 Nível 4 — Profissional

> Tabela com HTML nas células via `escapar=False`

```python
from pytohtml import tabela, etiqueta, botao

# Cria tabela com badges e botões nas células
linhas = [
    ["Produto", "Status", "Ação"],
    [
        "pytohtml v1.0",
        etiqueta("Publicado", cor="verde"),
        botao("Ver", variante="fantasma", classes="text-xs py-1 px-3"),
    ],
    [
        "pytohtml v2.0",
        etiqueta("Em desenvolvimento", cor="amarelo"),
        botao("Ver", variante="fantasma", classes="text-xs py-1 px-3"),
    ],
]

tabela(linhas, escapar=False)
```

> ⚠️ **Atenção:** Com `escapar=False`, os dados das células são inseridos como HTML bruto. Use apenas com dados confiáveis gerados pela própria lib (como `etiqueta()`, `botao()`), nunca com input do usuário.

---

## Referência Rápida

| Parâmetro | Efeito |
|-----------|--------|
| `cabecalho=True` | Primeira linha vira `<thead>` com fundo cinza (padrão) |
| `cabecalho=False` | Todas as linhas ficam no `<tbody>` |
| `escapar=True` | Escapa HTML nas células (padrão, seguro) |
| `escapar=False` | Permite HTML nas células (para badges, botões) |

---

← [lista](lista) · **tabela** · [imagem →](imagem)
