# `alerta()` e variantes

> Exibem popups elegantes via SweetAlert2. Não requerem Brython — funcionam com JavaScript puro.

`interatividade.py` · `sweetalert2` · **Não requer `brython=True`**

---

## Assinaturas

```python
# Popup flexível
alerta(titulo: str, texto: str = "", icone: str = "info") → str

# Variantes por tipo
alerta_sucesso(titulo: str = "Sucesso!", texto: str = "") → str
alerta_erro(titulo: str = "Erro!",       texto: str = "") → str
alerta_aviso(titulo: str = "Atenção!",   texto: str = "") → str
alerta_info(titulo: str = "Info",        texto: str = "") → str
```

## Parâmetros — `alerta()`

| Nome | Tipo | Padrão | Descrição |
|------|------|--------|-----------|
| `titulo` | `str` | — | Título do popup (obrigatório) |
| `texto` | `str` | `""` | Mensagem descritiva |
| `icone` | `str` | `"info"` | Ícone: `"success"`, `"error"`, `"warning"`, `"info"`, `"question"` |

---

## Exemplos

### 🟢 Nível 1 — Iniciante

> Popup de sucesso ao carregar a página

```python
from pytohtml import html, alerta_sucesso

pagina = html(
    alerta_sucesso("Operação concluída!", "Seus dados foram salvos com sucesso."),
    titulo_pagina="Sucesso",
)
```

**Script gerado:**

```html
<script>Swal.fire({icon: 'success', title: 'Operação concluída!', text: 'Seus dados foram salvos com sucesso.', confirmButtonColor: '#16a34a'})</script>
```

> ⚠️ **Atenção:** Os alertas são disparados **imediatamente ao carregar a página**. Para alertas acionados por eventos (clique, submit), use `alerta_ao_clicar()` ou `alerta_ao_enviar()`.

---

### 🔵 Nível 2 — Intermediário

> Todos os tipos de alerta

```python
# Sucesso — verde
alerta_sucesso("Salvo!",         "Alterações gravadas com sucesso.")

# Erro — vermelho
alerta_erro("Falha!",            "Não foi possível conectar ao servidor.")

# Aviso — amarelo
alerta_aviso("Atenção!",         "Esta ação não pode ser desfeita.")

# Info — azul
alerta_info("Informação",        "Sua sessão expira em 10 minutos.")

# Pergunta — com ícone de "?"
alerta("Tem certeza?",           "Você deseja excluir este item?", icone="question")
```

> 💡 **Dica:** Para popups de confirmação com botão Sim/Não, prefira `pedir_confirmacao()` que tem mais controle sobre os callbacks.

---

### 🟡 Nível 3 — Difícil

> Alerta condicional baseado em lógica Python

```python
from pytohtml import html, alerta_sucesso, alerta_erro

# Simula resultado de uma operação no servidor
operacao_ok = True
mensagem = "Usuário cadastrado com sucesso!" if operacao_ok else "Email já cadastrado."

popup = alerta_sucesso(mensagem) if operacao_ok else alerta_erro("Erro no cadastro", mensagem)

pagina = html(popup, titulo_pagina="Resultado")
```

---

### 🟣 Nível 4 — Profissional

> Redirect após popup de sucesso (com timer)

```python
from pytohtml import html

# HTML puro para popup com timer e redirect automático
popup_redirect = '''
<script>
Swal.fire({
    icon: "success",
    title: "Cadastro concluído!",
    text: "Você será redirecionado em instantes.",
    timer: 3000,
    timerProgressBar: true,
    showConfirmButton: false,
}).then(() => {
    window.location.href = "/dashboard";
});
</script>
'''

pagina = html(popup_redirect, titulo_pagina="Cadastro OK")
```

---

## Referência Rápida

| Função | Ícone | Cor do botão | Trigger |
|--------|-------|-------------|---------|
| `alerta_sucesso()` | ✅ | Verde | Ao carregar |
| `alerta_erro()` | ❌ | Vermelho | Ao carregar |
| `alerta_aviso()` | ⚠️ | Amarelo | Ao carregar |
| `alerta_info()` | ℹ️ | Azul | Ao carregar |
| `alerta("...", icone="question")` | ❓ | Azul | Ao carregar |
| `alerta_ao_clicar()` | Qualquer | — | Ao clicar |
| `alerta_ao_enviar()` | ✅ | Verde | Ao submeter form |

---

← [enviar-formulario](enviar-formulario) · **alerta** · [notificacao-rapida →](notificacao-rapida)
