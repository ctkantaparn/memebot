# Discord Meme Bot 😄

A simple and lightweight Discord bot that fetches memes from Reddit using the [meme-api.com](https://meme-api.com) and posts them into your Discord server.

## ✨ Features

- Fetch memes from any subreddit
- Request 1–10 memes at a time
- Lightweight and easy to deploy

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A Discord bot token
- `pip` installed packages:
  - `discord.py`
  - `requests`

### Installation

1. Clone the repository or copy the bot script.
2. Install required packages:

```bash
pip install discord.py requests
```

3. Replace `'Token'` in the last line with your actual Discord bot token.
4. Run the bot:
```bash
python bot.py
```

## 💡 Commands

| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `$help`                  | Displays the list of available commands          |
| `$meme`                  | Sends 1 random meme from r/memes                 |
| `$meme [subreddit]`      | Sends 1 meme from the specified subreddit        |
| `$meme [subreddit] [n]`  | Sends `n` memes (1 ≤ n ≤ 10) from subreddit      |

### 🛠 Customization
You can modify the default subreddit or maximum meme count by editing the get_meme() function and validation logic in the bot code.

### 🧾 License
[MIT License](./LICENSE)
