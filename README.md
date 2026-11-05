<div align="center">

# 📱 mobile-tests-appium

**Automação Mobile (Android)** &nbsp;·&nbsp; Appium &nbsp;·&nbsp; Python &nbsp;·&nbsp; UiAutomator2

[![Mobile Tests](https://github.com/MateusCerqueiraG/mobile-tests-appium/actions/workflows/mobile.yml/badge.svg)](https://github.com/MateusCerqueiraG/mobile-tests-appium/actions/workflows/mobile.yml)
&nbsp;
[![Relatório Allure](https://img.shields.io/badge/📊_Relatório-Allure_ao_vivo-5fd0e6?style=flat&labelColor=103a4e)](https://mateuscerqueirag.github.io/mobile-tests-appium/)

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

**3 testes &nbsp;·&nbsp; emulador Android real no CI &nbsp;·&nbsp; UiAutomator2**

</div>

## 🧰 Stack & práticas

- 📱 **Appium + UiAutomator2** — padrão de automação Android (mesma base do trabalho real em device farm)
- 🧩 **Page-ready** — capabilities centralizadas numa fixture `driver` (setup/teardown), fácil de escalar pra Page Objects
- 🤖 **Emulador real no CI** — `reactivecircus/android-emulator-runner` (KVM) sobe um Android de verdade a cada push
- 🔁 **Anti-flaky** — rerun automático (teste mobile é naturalmente mais sensível a timing)
- 📊 **Allure** — relatório publicado automaticamente

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

## 📊 Relatório Allure

### 👉 **[mateuscerqueirag.github.io/mobile-tests-appium](https://mateuscerqueirag.github.io/mobile-tests-appium/)**

---

<div align="center">
<sub>Projeto de portfólio · foco em automação mobile Android com Appium · alvo: app nativo de Configurações</sub>
</div>
