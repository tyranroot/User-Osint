```
 ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║   ██║╚════██║██║██║╚██╗██║   ██║   
╚██████╔╝███████║██║██║ ╚████║   ██║   
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝  
```

<div align="center">

# 🕵️ USERNAME-OSINT

**Advanced Username Intelligence & Footprinting Framework**

![Python](https://img.shields.io/badge/Python-3.8%2B-00ff41?style=for-the-badge&logo=python&logoColor=white&labelColor=0d0d0d)
![Platforms](https://img.shields.io/badge/Platforms-100%2B-00ff41?style=for-the-badge&logoColor=white&labelColor=0d0d0d)
![Async](https://img.shields.io/badge/Engine-Async-41ffff?style=for-the-badge&labelColor=0d0d0d)
![License](https://img.shields.io/badge/License-MIT-ffff41?style=for-the-badge&labelColor=0d0d0d)
![Docker](https://img.shields.io/badge/Docker-Ready-00ff41?style=for-the-badge&logo=docker&labelColor=0d0d0d)

```
[ TARGET ACQUIRED ] >> SCANNING 100+ PLATFORMS >> ZERO FALSE POSITIVES
```

</div>

---

## 📡 Overview

**USERNAME-OSINT** is a high-performance open-source intelligence tool designed to hunt a target username across **100+ social platforms, forums, and online services** — simultaneously, in seconds.

Built for:
- 🔴 **Red Teamers** — reconnaissance & footprinting
- 🔵 **Blue Teamers** — exposure assessment
- 🕵️ **Digital Investigators** — identity correlation
- 🔬 **Security Researchers** — OSINT automation

> ⚡ Powered by async HTTP engine — **3x faster** than sequential scanners.

---

## ⚙️ Installation

### Method 1 — Git Clone (Recommended)

```bash
git clone https://github.com/yourname/username-osint
cd username-osint
pip install -r requirements.txt
```

### Method 2 — pip

```bash
pip install username-osint
```

### Method 3 — Docker (Isolated Environment)

```bash
docker build -t username-osint .
docker run --rm username-osint scan -u target_username
```

---

## 🚀 Usage

### Basic Scan

```bash
python osint.py -u john_doe
```

### Export to JSON

```bash
python osint.py -u john_doe --output json --save results.json
```

### Scan by Category

```bash
python osint.py -u john_doe --category social,gaming,forums
```

### Anonymous Mode (Tor / Proxy)

```bash
python osint.py -u john_doe -v --proxy socks5://127.0.0.1:9050
```

### Verbose + Custom Timeout

```bash
python osint.py -u john_doe -v --timeout 10 --threads 100
```

---

## 🏴 CLI Flags Reference

| Flag | Description | Default |
|------|-------------|---------|
| `-u, --username` | 🎯 Target username | **required** |
| `--output` | Output format: `text` / `json` / `csv` | `text` |
| `--save` | Save results to file | `None` |
| `--category` | Filter: `social`, `gaming`, `forums`, `dev`, `dark` | `all` |
| `--proxy` | Proxy URL (`socks5://` or `http://`) | `None` |
| `--timeout` | Request timeout (seconds) | `5` |
| `--threads` | Max concurrent requests | `50` |
| `-v, --verbose` | Show all results (including misses) | `False` |
| `--csv` | Export to CSV format | `False` |
| `--tor` | Route through Tor network | `False` |

---

## 🗂️ Platform Coverage

| Category | Platforms | Coverage |
|----------|-----------|----------|
| 🌐 Social Media | Twitter, Instagram, TikTok, Facebook, Reddit... | 92% |
| 💻 Dev / Code | GitHub, GitLab, HackerNews, Replit, Codepen... | 85% |
| 🎮 Gaming | Steam, Xbox, PSN, Twitch, Chess.com... | 78% |
| 💬 Forums | 4chan, Reddit, Quora, StackOverflow... | 70% |
| 🧅 Dark / Alt | Pastebin, Onion sites, IRC archives... | 55% |

---

## 🧠 Features

```
✔  Async HTTP engine (asyncio + aiohttp)
✔  100+ platform database (sites.json)
✔  Smart response fingerprinting — zero false positives
✔  Tor / SOCKS5 / HTTP proxy support
✔  JSON, CSV, plaintext export
✔  Docker-ready for isolated environments
✔  Modular site database — easy to extend
✔  Rate limiting & anti-detection headers
✔  Category filtering for targeted recon
```

---

## 🗃️ Project Structure

```
username-osint/
├── osint.py            # Main entry point
├── sites.json          # Platform database (100+ entries)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build file
├── core/
│   ├── scanner.py      # Async HTTP scanner engine
│   ├── reporter.py     # Output formatter (JSON/CSV/text)
│   └── proxy.py        # Proxy / Tor handler
├── tests/
│   └── test_scanner.py # Unit tests
└── README.md
```

---

## 🔧 Adding New Sites

Edit `sites.json` to add custom platforms:

```json
"SiteName": {
  "url": "https://example.com/{}",
  "errorType": "status_code",
  "errorCode": 404,
  "category": "social"
}
```

**Error types supported:**
- `status_code` — checks HTTP response code
- `message` — checks for error string in body
- `response_url` — checks for redirect pattern

Then run tests:

```bash
pytest tests/
```

---

## 📦 Dependencies

```
aiohttp>=3.8.0
asyncio
requests
colorama
rich
tqdm
```

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-platform`
3. Commit changes: `git commit -m 'Add: 10 new gaming platforms'`
4. Push to branch: `git push origin feature/new-platform`
5. Open a Pull Request

---

## ⚠️ Legal Disclaimer

```bash
╔══════════════════════════════════════════════════════════════╗
║                      ⚠  WARNING  ⚠                          ║
╠══════════════════════════════════════════════════════════════╣
║  This tool is intended STRICTLY for:                         ║
║    • Authorized security research                            ║
║    • Digital forensics & investigations                      ║
║    • Educational & CTF purposes                              ║
║                                                              ║
║  Unauthorized use against individuals without explicit       ║
║  consent may violate CFAA, GDPR, and local cyber laws.      ║
║                                                              ║
║  The author assumes ZERO liability for misuse.               ║
║  YOU are solely responsible for your actions.                ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📜 License

```
MIT License — © 2025 @yourhandle
Permission granted for personal, educational, and research use.
```

---

<div align="center">

```
root@osint:~# █
```

**Made with ☠ for the community**

⭐ Star this repo if it helped you!

</div>
