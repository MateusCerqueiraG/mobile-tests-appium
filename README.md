<div align="center">

# 📱 mobile-tests-appium

**Automação Mobile (Android)** &nbsp;·&nbsp; Appium &nbsp;·&nbsp; Python &nbsp;·&nbsp; UiAutomator2

[![Mobile Tests](https://github.com/MateusCerqueiraG/mobile-tests-appium/actions/workflows/mobile.yml/badge.svg)](https://github.com/MateusCerqueiraG/mobile-tests-appium/actions/workflows/mobile.yml)
&nbsp;
[![Relatório](https://img.shields.io/badge/📊_Relatório-execução_em_emulador-5fd0e6?style=flat&labelColor=103a4e)](https://mateuscerqueirag.github.io/mobile-tests-appium/)

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-662D91?logo=appium&logoColor=white)
![Android](https://img.shields.io/badge/Android-UiAutomator2-3DDC84?logo=android&logoColor=white)

</div>

---

Automação de **testes E2E mobile** no **Android** com **Appium** (driver UiAutomator2) e **pytest** — abrindo um app real no dispositivo, interagindo com a tela (toques, scroll) e validando o comportamento. Roda em **CI** sobre um **emulador Android de verdade** (via `android-emulator-runner`), com relatório **Allure**.

> 🎯 **Alvo sob teste:** o app **Configurações do Android** (`com.android.settings`) — um app **nativo que existe em todo dispositivo/emulador**, então a suíte roda **sem depender de nenhum APK externo**. As mesmas técnicas valem para qualquer `.apk` (basta trocar o `app_package`/`app_activity` ou apontar o `app` para o arquivo).

## ✅ O que a suíte verifica

| Teste | O que faz |
|:--|:--|
| 📲 **App abre** | o app Configurações sobe e fica em primeiro plano |
| 📋 **Conteúdo carrega** | a tela lista itens de menu (elementos nativos encontrados) |
| 👆 **Interação (scroll)** | executa um gesto de rolagem e confirma o estado da tela |

<div align="center">

**3 testes &nbsp;·&nbsp; validados em emulador Android real &nbsp;·&nbsp; UiAutomator2**

</div>

## ⚙️ Como roda (CI honesto)

Teste mobile precisa de um **dispositivo/emulador**, e o runner grátis do GitHub é lento/instável pra bootar um Android. Então o CI é dividido em dois:

| Job | Quando | O quê |
|:--|:--|:--|
| ✅ **Validação** | todo push | instala tudo, sobe o Appium e roda `pytest --collect-only` (garante que o código importa e coleta sem erro). **É o que o badge reflete.** |
| 📱 **Emulador (best-effort)** | sob demanda (`workflow_dispatch`) | tenta a suíte num emulador Android real; é *falha permitida* com timeout, pra não travar o badge |

> **Prova de execução real:** os 3 testes foram **validados contra um emulador Android de verdade** (3/3 verde) — [**relatório dessa execução**](https://mateuscerqueirag.github.io/mobile-tests-appium/). Em ambiente profissional, suíte mobile costuma rodar em **device farm** (AWS Device Farm / BrowserStack) — bem mais confiável que emulador no CI grátis. É assim, por exemplo, no projeto real da SEA (`sesc-mobile-tests`, AWS Device Farm).

## 🧰 Stack & práticas

- 📱 **Appium + UiAutomator2** — padrão de automação Android (mesma base de device farm)
- 🧩 **Page-ready** — capabilities centralizadas numa fixture `driver` (setup/teardown), fácil de escalar pra Page Objects
- 🔁 **Anti-flaky** — rerun automático (teste mobile é naturalmente mais sensível a timing)

## 📁 Estrutura

```
conftest.py                 # fixture 'driver' com as capabilities (UiAutomator2)
tests/
└── test_settings_app.py    # abre o app, valida conteúdo e interage (scroll)
.github/workflows/mobile.yml
requirements.txt
```

## ▶️ Como rodar localmente

Pré-requisitos: Android SDK + um emulador/AVD + Appium (`npm i -g appium` e `appium driver install uiautomator2`).

```bash
# 1) sobe um emulador
emulator -avd <seu_avd> -no-window &
adb wait-for-device

# 2) sobe o Appium
appium &

# 3) instala e roda
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## 📱 Rodar a suíte completa no emulador

Localmente (com um emulador/AVD de pé) ou disparando o job sob demanda em **Actions → Mobile Tests → Run workflow**:
```bash
pytest   # contra o emulador conectado via Appium
```

---

<div align="center">
<sub>Projeto de portfólio · foco em automação mobile Android com Appium · alvo: app nativo de Configurações</sub>
</div>
