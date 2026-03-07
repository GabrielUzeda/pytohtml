# `aviso_estatico()`

> Gera um banner estático colorido para exibir mensagens de informação, sucesso, aviso ou erro.

`elementos.py` · `feedback`

---

## Assinatura

```python
aviso_estatico(texto: str, tipo: str = "info", classes: str | None = None, escapar: bool = True) → str
```

## Parâmetros

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `texto` | `str` | — | Conteúdo da mensagem (obrigatório) |
| `tipo` | `str` | `"info"` | Estilo visual — `"info"`, `"sucesso"`, `"aviso"`, `"perigo"` |
| `classes` | `str \| None` | `None` | Classes Tailwind extras |
| `escapar` | `bool` | `True` | Escapa HTML para prevenir XSS |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Aviso informativo padrão

```python
from pytohtml import aviso_estatico

aviso_estatico("Sua conta foi criada com sucesso.")
```

**HTML gerado:**

```html
<div role="alert" class="border rounded-lg px-4 py-3 my-2 text-sm bg-blue-50 border-blue-200 text-blue-800">
  Sua conta foi criada com sucesso.
</div>
```

---

### 🔵 Nível 2 — Intermediário

> Todos os tipos de aviso

```python
aviso_estatico("Operação concluída com sucesso!",    tipo="sucesso")
aviso_estatico("Você tem mensagens não lidas.",       tipo="info")
aviso_estatico("Atenção: essa ação não pode ser desfeita.", tipo="aviso")
aviso_estatico("Erro ao salvar. Tente novamente.",   tipo="perigo")
```

> 💡 **Dica:** Diferente de `alerta_sucesso()` e similares (que usam SweetAlert2 com popup), `aviso_estatico()` é um elemento fixo na página — ideal para mensagens persistentes que o usuário não deve precisar fechar.

---

### 🟡 Nível 3 — Difícil

> Aviso com HTML inline para links e formatação

```python
aviso_estatico(
    'Sua sessão expira em 5 minutos. <a href="/renovar" class="underline font-semibold">Renovar agora</a>',
    tipo="aviso",
    escapar=False,
)
```

---

### 🟣 Nível 4 — Profissional

> Avisos condicionais baseados em lógica Python

```python
from pytohtml import html, aviso_estatico, container, titulo

# Simula resultado de uma operação
status = "sucesso"
mensagem = "Formulário enviado com sucesso!"

if status == "sucesso":
    banner = aviso_estatico(mensagem, tipo="sucesso")
elif status == "erro":
    banner = aviso_estatico(mensagem, tipo="perigo")
else:
    banner = aviso_estatico(mensagem, tipo="info")

pagina = html(
    container(
        titulo("Resultado", tamanho="medio"),
        banner,
    ),
    titulo_pagina="Status"
)
```

---

## Referência Rápida

| `tipo=` | Fundo | Borda | Texto | Uso típico |
|---------|-------|-------|-------|------------|
| `"info"` | azul claro | azul | azul escuro | Informações neutras |
| `"sucesso"` | verde claro | verde | verde escuro | Confirmações |
| `"aviso"` | amarelo claro | amarelo | âmbar | Alertas não críticos |
| `"perigo"` | vermelho claro | vermelho | vermelho escuro | Erros críticos |

---

← [divisor](divisor) · **aviso-estatico** · [cartao →](cartao)
