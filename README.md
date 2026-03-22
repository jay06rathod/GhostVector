# 👻 GhostVector

> **Recolor your SVGs. Don't haunt your presentation.**

GhostVector is a Streamlit web app that lets you batch-upload SVG icons, swap their colors with a hex picker, and export them as polished PNGs or recolored SVGs — all packed into a single ZIP download. Born in the chaos of a hackathon, shipped out of sheer stubbornness.

---

## 🧭 The Hackathon Side-Quest

Picture this: T-minus two hours to presentation time. The flowchart is built, the data preprocessing pipeline is documented, the slides look clean — except for one thing. The SVG icons I'd pulled together had hard-coded black fills, and our slide theme was decidedly *not* black. The presentation software? No SVG support whatsoever.

I could've edited them one by one in an SVG editor. I could've just used emoji. Instead, I opened a new terminal window, told myself *"this will only take 20 minutes"*, and built GhostVector.

It took longer than 20 minutes.

---

## ✨ Features

- 📁 **Batch SVG Upload** — drop as many icons as you need in one go
- 🎨 **Hex Color Picker** — instantly replace black outlines and fills with any custom color
- 🖼️ **PNG or SVG Output Toggle** — choose your export format depending on where you're headed
- 🔲 **Live Preview Grid** — see every recolored icon before you commit to downloading
- ⬇️ **Per-file Download Buttons** — grab just the one you need
- 🗜️ **"Download All" as ZIP** — batch export everything in one click, presentation-ready

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| App framework | [Streamlit](https://streamlit.io/) |
| SVG → PNG conversion | [CairoSVG](https://cairosvg.org/) |
| Color substitution | Python `re` (Regex) |
| Packaging | `zipfile`, `io` (stdlib) |

---

## 🚀 Running Locally

**1. Clone the repo**

```bash
git clone https://github.com/your-username/ghostvector.git
cd ghostvector
```

**2. Install dependencies**

```bash
pip install streamlit cairosvg
```

**3. Launch the app**

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

> **Note for Linux/Ubuntu users:** CairoSVG depends on system-level Cairo libraries. If you hit errors, install them via:
> ```bash
> sudo apt-get install libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf-2.0-0 shared-mime-info
> ```

---

## ☁️ Cloud Deployment (Streamlit Community Cloud)

CairoSVG needs a few system packages that aren't available on cloud environments by default. To fix this, create a `packages.txt` file in the root of your repo with the following:

```
libcairo2
libpango-1.0-0
libpangocairo-1.0-0
libgdk-pixbuf-2.0-0
shared-mime-info
```

Streamlit Community Cloud will pick this up automatically during the build and install the required system dependencies before launching your app.

---

## 📖 Usage

1. **Upload** one or more `.svg` files using the file uploader
2. **Pick a color** using the hex color picker (replaces black `#000000` fills/strokes)
3. **Choose your output format** — PNG for presentations, SVG if you need to keep them editable
4. **Preview** the recolored icons in the live grid
5. **Download** individual files or grab everything at once with **Download All as ZIP**

---

## 🤝 Contributing

Found a bug? Have a feature idea? PRs and issues are welcome. This started as a 20-minute hackathon fix — it can keep growing.

---

## 📄 License

MIT — use it, break it, ship it.

---

*GhostVector: because your icons shouldn't be invisible just because they're the wrong color.*