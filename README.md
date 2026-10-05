# 🤖 Chatbot CLI (V1)

Chatbot en ligne de commande qui tourne **100 % en local**, grâce à un modèle de langage chargé dans LM Studio et orchestré avec LangChain. Pas de clé API, pas de cloud : tout reste sur ma machine.

> Première version d'un projet en plusieurs étapes : CLI → application web Django → assistant RAG sur documents → pipeline vocal.

## ✨ Fonctionnalités

- Discussion avec un LLM local directement dans le terminal
- Utilisation de LangChain pour communiquer avec le modèle
- Fonctionne hors ligne une fois le modèle téléchargé
-  prompt système
## 🛠️ Stack technique

| Outil | Rôle |
|-------|------|
| Python 3 | Langage principal |
| LangChain | Orchestration des appels au modèle |
| LM Studio | Serveur local pour faire tourner le LLM |

### 4. Préparer LM Studio

1. Installer [LM Studio](https://lmstudio.ai/)
2. Télécharger un modèle de ton choix
3. Charger le modèle et **démarrer le serveur local** (onglet Developer)

## ▶️ Lancer le chatbot

```bash
python main.py
```

Tape ton message et appuie sur Entrée pour discuter avec le modèle.


## 🗺️ Roadmap

- [x] **V1** : chatbot CLI (LangChain + LM Studio)
- [ ] **V2** : application web Django avec streaming
- [ ] **V3** : assistant RAG sur documents
- [ ] **V4** : pipeline vocal (STT / TTS)

## 👤 Auteur

**Louay** 

- GitHub : [@TON-PSEUDO](https://github.com/toutalouay07-source)
