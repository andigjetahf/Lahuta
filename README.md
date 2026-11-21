# 🦅 Lahuta

<p align="center">
  <strong>Ndërfaqe e Avancuar dhe Gjithëpërfshirëse e Inteligjencës Artificiale në Gjuhën Shqipe</strong>
</p>

<p align="center">
  <img src="./banner.png" alt="Lahuta Banner" width="100%" />
</p>

---

**Lahuta** është një platformë e inteligjencës artificiale (AI) e vetë-strehuar (*self-hosted*), e pasur me veçori, e fuqishme dhe e krijuar me fokus të veçantë në **gjuhën shqipe**. Ajo mbështet modele të ndryshme gjuhësore (LLM) duke përfshirë **Ollama**, **OpenAI**, **Anthropic Claude**, **Google Gemini** dhe çdo API të përputhshme me formatin e OpenAI.

Me motor të integruar për **RAG (Retrieval Augmented Generation)**, kërkim në ueb, biseda me zë dhe video, si dhe ekzekutim të funksioneve Python, **Lahuta** ofron një përvojë të plotë dhe të sigurt për përdoruesit individualë dhe organizatat.

<p align="center">
  <img src="./demo.png" alt="Lahuta Demo" width="100%" />
</p>

---

## ✨ Veçoritë Kryesore të Lahuta

- 🇦🇱 **Lokalizim 100% në Gjuhën Shqipe**: E gjithë ndërfaqja, menutë, njoftimet dhe cilësimet janë të parazgjedhura në shqip (`sq-AL`), me përshtatje gjuhësore me cilësi të lartë.
- 🚀 **Instalim i Thjeshtë me Docker**: Nisje e menjëhershme përmes Docker ose Docker Compose me mbështetje për GPU (Nvidia CUDA) dhe CPU.
- 🤝 **Integrim i Gjithanshëm me Modelet LLM**: Lidhuni lehtësisht me serverin lokal të **Ollama**, ose integroni shërbime si **OpenAI**, **Anthropic**, **Gemini**, **Groq**, **Mistral**, **OpenRouter**, **LMStudio** dhe të tjera.
- 📚 **RAG Lokal i Avancuar**: Ngarkoni dokumente (PDF, Word, Excel, tekst) drejtpërdrejt në bisedë me komandën `#`. Mbështet 9 baza të dhënash vektoriale (ChromaDB, PGVector, Qdrant, Milvus, Elasticsearch, etj.).
- 🔍 **Kërkim në Ueb për RAG**: Merrni të dhëna në kohë reale nga interneti duke përdorur SearXNG, Google PSE, Brave Search, DuckDuckGo, Tavily dhe ofrues të tjerë.
- 🌐 **Shfletim Uebi në Bisedë**: Përfshini përmbajtje nga faqet e internetit direkt në diskutim duke vendosur `#` e ndjekur nga një lidhje uebi (URL).
- 🎨 **Gjenerim & Redaktim Imazhesh**: Krijoni imazhe me DALL-E, Google Imagen, ComfyUI ose Stable Diffusion (AUTOMATIC1111).
- 🎤📹 **Biseda me Zë dhe Video (Hands-Free)**: Komunikoni me zë në kohë reale me anë të njohjes së zërit (Whisper lokal, OpenAI) dhe sintezës së zërit (TTS).
- 🐍 **Mjete & Funksione Python**: Shtoni logjikë të personalizuar përmes editorit të kodit Python të integruar (BYOF - Bring Your Own Function).
- 🛡️ **Kontroll i Qasjes me Role (RBAC)**: Menaxhoni lejet, rolet dhe grupet e përdoruesve në mënyrë të detajuar për mjedise arsimore dhe korporative.
- 📱 **Dizajn i Përshtatshëm (Responsive) & PWA**: Funksionon shkëlqyeshëm në desktop, tablet dhe celularë (si Progressive Web App).
- 🔐 **Siguri & Privatësi**: Të gjitha të dhënat mbeten nën kontrollin tuaj lokal; asnjë mesazh apo dokument nuk ndahet pa miratimin tuaj.

---

## 🚀 Si të Instaloni Lahuta

### Opsioni 1: Me Docker Compose (E Rekanduar)

Kloni depon dhe nisni shërbimet me Docker Compose:

```bash
git clone https://github.com/andigjetahf/Lahuta.git
cd Lahuta
docker compose up -d
```

Pasi shërbimet të nisen, hapni shfletuesin tuaj në:
👉 **[http://localhost:3000](http://localhost:3000)**

### Opsioni 2: Me Docker CLI

Nëse keni tashmë Ollama të instaluar në kompjuterin tuaj:

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v lahuta-data:/app/backend/data \
  --name lahuta \
  --restart always \
  sghtf/lahuta-ui
```

Për të aktivizuar mbështetjen e GPU-së (Nvidia CUDA):

```bash
docker run -d -p 3000:8080 --gpus all \
  --add-host=host.docker.internal:host-gateway \
  -v lahuta-data:/app/backend/data \
  --name lahuta \
  --restart always \
  sghtf/lahuta-ui
```

### Opsioni 3: Zhvillim Lokal (Development)

#### Kërkesat Paraprake:
- **Node.js** >= 18.13.0
- **Python** 3.11 ose 3.12

#### 1. Nisja e Backend-it:
```bash
cd backend
python -m venv venv
# Në Windows:
.\venv\Scripts\activate
# Në Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
python -m open_webui.main
```

#### 2. Nisja e Frontend-it:
```bash
npm install
npm run dev
```

Ndërfaqja do të jetë e disponueshme në: **http://localhost:5173**

---

## ⚙️ Variablat Kryesore të Mjedisit

| Variabla | Përshkrimi | Vlera e Parazgjedhur |
| :--- | :--- | :--- |
| `WEBUI_NAME` | Emri i aplikacionit në ndërfaqe | `"Lahuta"` |
| `DEFAULT_LOCALE` | Gjuha kryesore e ndërfaqes | `"sq-AL"` (Shqip) |
| `OLLAMA_BASE_URL` | URL-ja e serverit Ollama | `http://localhost:11434` |
| `OPENAI_API_BASE_URL` | URL-ja e pikës fundore të OpenAI | `https://api.openai.com/v1` |
| `OPENAI_API_KEY` | Çelësi i API-së së OpenAI | Bosh |
| `WEBUI_SECRET_KEY` | Çelësi i sigurisë për sesionet | Gjenerohet automatikisht |

---

## 🇦🇱 Ekipi dhe Kontributet

**Lahuta** është ndërtuar për komunitetin shqipfolës me synimin për të sjellë mjetet më të avancuara të inteligjencës artificiale në mënyrë të thjeshtë, të sigurt dhe të plotë në gjuhën shqipe.

Nëse dëshironi të kontribuoni me ide, përmirësime ose shtesa:
1. Bëni **Fork** projektin
2. Krijoni një degë të re (`git checkout -b permiresim-i-ri`)
3. Bëni **Commit** ndryshimet (`git commit -m 'Shto veçori të re'`)
4. Bëni **Push** në degë (`git push origin permiresim-i-ri`)
5. Hapni një **Pull Request**

---

## 📜 Licenca

Ky projekt bazohet në kod me burim të hapur dhe licencohet sipas kushteve të përcaktuara në skedarin [LICENSE](./LICENSE).
