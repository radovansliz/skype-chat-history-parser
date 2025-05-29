# Skype Chat Export Parser

This script converts an exported Skype message history JSON into a readable text format, grouped by date.

> ⚠️ Since Skype is discontinued, the only available option is to export your chat history via the official Microsoft export tool. This script processes that export.

---

## 🛠 Features

- Parses all conversations from Skype JSON chat export
- Skips calls, events, and URI-based messages
- Groups messages by date
- Outputs a clean, readable `.txt` file

---

## How to Use

### 1. Download Your Skype Export

Go to [https://privacy.microsoft.com/en-us](https://privacy.microsoft.com/en-us), request your data export, and download the `.tar` or `.zip` archive. Inside, locate the `messages.json` file.

### 2. Run the Script

#### Basic usage:

```bash
python parse_skype_export.py -i messages.json
```

Optional: specify output file name

```bash
python parse_skype_export.py -i messages.json -o my_chats.txt
```

---

### This is an open-source tool – feel free to improve it or add new features via pull request. If you'd like to support my work, you can do so here:

<a href="https://www.buymeacoffee.com/slizradovas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
