```markdown
# 🌐 Web URL Config Loader

This project is a simple template for loading a user-defined website URL from a configuration file. It can be used as a base for scripts or tools that interact with a specific website.

---

## 📁 Project Structure

```
your-project/
├── main.py
├── config.json
├── config.py
└── README.md
```

---

## 🔧 Configuration

Before running the code, you need to create a file named `config.json` in the root directory of the project.

### ✅ `config.json` Format

```json
{
  "config_path": {
    "web_url": "https://your-custom-url.com/"
  }
}
```

### 📌 Notes:
- Replace `"https://your-custom-url.com/"` with the URL of the website you want the script to work with.
- Make sure the JSON is valid and correctly formatted.

### 📍 Example

```json
{
  "config_path": {
    "web_url": "https://google.com/"
  }
}
```

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Add a `config.json` file in the project root as described above.

3. Run the script:
   ```bash
   python main.py
   ```

---


## 📦 Dependencies

To run this project, make sure you have the following Python libraries installed:

- `beautifulsoup4`
- (Standard libraries used: `json`, `typing`, `urllib.request` — no need to install separately)

Install dependencies using the following command:

```bash
pip install -r requirements.txt

---

## 📄 License

[MIT License](LICENSE)

---

## 🙋‍♂️ Author

Created by [Parnian](https://github.com/ParnianKhaleghi)
```
