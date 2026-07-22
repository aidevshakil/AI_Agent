# 🤖 AI Agent Chatbot - Streamlit App

A modern AI chatbot application powered by Groq API with support for multiple personalities, real-time conversations, and easy customization.

---

## ✨ Features

✅ **5 Built-in Personalities** - Math Teacher, Doctor, Travel Guide, Chef, Tech Support
✅ **Multi-Model Support** - Choose from Mixtral, Llama2, or Gemma
✅ **Real-time Chat** - Interactive chat interface with instant responses
✅ **Session Memory** - Maintains conversation context
✅ **Personality Enforcement** - Each AI stays within its domain boundaries
✅ **Easy Customization** - Add new personalities in seconds
✅ **Free Deployment** - Deploy to Streamlit Cloud at no cost

---

## 📁 Project Structure

```
AI_Agent/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration & constants
├── personalities.py      # Personality definitions
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── .streamlit/
│   ├── config.toml      # Streamlit config
│   └── secrets.toml     # API keys (local only)
└── README.md            # This file
```

---

## 🚀 Quick Start (5 Minutes)

### 1. Get Groq API Key
- Go to [console.groq.com](https://console.groq.com)
- Sign up (free)
- Create API Key

### 2. Setup Environment
```bash
cd AI_Agent
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Add API Key
Edit `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_api_key_here"
```

### 4. Run App

Open terminal and run:

```bash
streamlit run app.py
```

Your browser opens automatically at `http://localhost:8501`

**Keep the terminal open while using the app!**

---

## 📋 Complete Setup Guide

### Requirements
- Python 3.8+
- pip (Python package manager)
- GitHub account (for deployment)

### Step-by-Step Setup

#### For Windows
```bash
# 1. Navigate to project
cd C:\path\to\AI_Agent

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install packages
pip install -r requirements.txt

# 5. Add your API key
# Edit .streamlit/secrets.toml and add:
# GROQ_API_KEY = "your_key"

# 6. Run
streamlit run app.py
```

#### For macOS/Linux
```bash
# 1. Navigate to project
cd ~/path/to/AI_Agent

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install packages
pip install -r requirements.txt

# 5. Add your API key
# Edit .streamlit/secrets.toml and add:
# GROQ_API_KEY = "your_key"

# 6. Run
streamlit run app.py
```

### Verify Installation
Test with Math Teacher:
- Type: "Solve 2x + 5 = 9"
- You should get the solution ✓

---

## 🎭 Personalities

### Built-in Personalities

| Name | Scope | Example |
|------|-------|---------|
| **Math Teacher** | Mathematics only | "Explain calculus" |
| **Doctor** | Health & medical | "Symptoms of flu?" |
| **Travel Guide** | Travel & tourism | "Best time for Japan?" |
| **Chef** | Cooking & recipes | "How to make pasta?" |
| **Tech Support** | Technical issues | "Why is my PC slow?" |

### Add New Personality

Edit `personalities.py` and add:

```python
"Lawyer": {
    "description": "Legal advisor - legal information only",
    "system_prompt": """You are a Lawyer. Your role is to:
1. Answer ONLY legal questions
2. Explain laws and contracts
3. Encourage professional consultation
4. Politely refuse off-topic questions with: "I'm a Lawyer, so I can only help with legal questions!"

Remember: STRICTLY stick to legal topics."""
}
```

Save and restart. Your personality appears immediately! ✨

### More Example Personalities

**Fitness Coach:**
```python
"Fitness Coach": {
    "description": "Personal trainer - fitness advice only",
    "system_prompt": """You are a professional Fitness Coach. Your role is to:
1. Answer ONLY fitness and exercise questions
2. Provide workout routines and nutrition tips
3. Encourage safe practices
4. Politely refuse off-topic questions with: "I'm a Fitness Coach, so I can only help with fitness!"

Remember: STRICTLY stick to fitness topics."""
}
```

**Historian:**
```python
"Historian": {
    "description": "History expert - historical information only",
    "system_prompt": """You are a professional Historian. Your role is to:
1. Answer ONLY history questions
2. Provide historical context and information
3. Explain causes and effects
4. Politely refuse off-topic questions with: "I'm a Historian, so I can only help with history!"

Remember: STRICTLY stick to history topics."""
}
```

---

## ⚙️ Customize Settings

Edit `config.py` to change settings:

### API Parameters
```python
GROQ_CONFIG = {
    "temperature": 0.7,              # Creativity (0=deterministic, 2=creative)
    "max_tokens": 1000,              # Response length
    "message_history_limit": 10      # Context window
}
```

### Available Models
```python
AVAILABLE_MODELS = [
    "mixtral-8x7b-32768",   # Best quality (slower)
    "llama2-70b-4096",      # Balanced
    "gemma-7b-it"           # Fastest
]
```

### UI Configuration
```python
# Change colors in CSS section
CSS = """
<style>
    .personality-badge {
        background-color: #FF6B6B;  /* Change color here */
    }
</style>
"""
```

### Configuration Presets

**Fast Responses:**
```python
GROQ_CONFIG = {"temperature": 0.5, "max_tokens": 500, "message_history_limit": 5}
AVAILABLE_MODELS = ["gemma-7b-it"]
```

**Creative Responses:**
```python
GROQ_CONFIG = {"temperature": 1.5, "max_tokens": 2000, "message_history_limit": 20}
AVAILABLE_MODELS = ["mixtral-8x7b-32768"]
```

---

## 🌐 Deploy to Streamlit Cloud (Free)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: AI Agent Chatbot"
git remote add origin https://github.com/YOUR_USERNAME/AI-Agent-Chatbot.git
git branch -M main
git push -u origin main
```

### Step 2: Connect to Streamlit Cloud
1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Click **"New app"**
3. Select your repository, branch, and `app.py`
4. Click **Deploy!**

### Step 3: Add API Key
1. Click the **☰** menu (top right)
2. Go to **Settings** → **Secrets**
3. Add:
```
GROQ_API_KEY = "your_key_here"
```
4. Click **Save**

Your app is now live! 🎉

Access it at:
```
https://share.streamlit.io/YOUR_USERNAME/AI-Agent-Chatbot/main/app.py
```

---

## 🛠️ Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
# Activate virtual environment and reinstall
source venv/bin/activate
pip install -r requirements.txt
```

### "GROQ_API_KEY not found"
- Check `.streamlit/secrets.toml` exists
- Verify API key is there (no extra spaces)
- Restart Streamlit: `Ctrl+C` then `streamlit run app.py`

### Personality not appearing
- Check `personalities.py` syntax (colons, quotes)
- Restart Streamlit
- Clear cache: `Ctrl+C` then restart

### App very slow
- Try faster model: `gemma-7b-it`
- Reduce `max_tokens` in `config.py`
- Check internet connection

### Deployment fails
- Ensure GitHub repo is public
- Check `requirements.txt` syntax
- View logs: App menu → **View logs**

---

## 📚 File Descriptions

### `app.py`
Main Streamlit application with:
- Chat interface
- Message handling
- Personality selection
- Model selection
- Groq API integration

### `config.py`
Centralized configuration:
- Page settings
- API parameters
- Models list
- UI styling
- Error/success messages

### `personalities.py`
Personality definitions:
- System prompts
- Descriptions
- Helper functions

### `requirements.txt`
Python dependencies:
- streamlit 1.28.1
- groq 0.4.2
- python-dotenv 1.0.0

---

## 🔐 Security

✅ **Never hardcode API keys** - Use `.streamlit/secrets.toml`
✅ **Add to `.gitignore`** - Secrets won't be pushed to GitHub
✅ **For production** - Use Streamlit Cloud Secrets
✅ **Rotate keys regularly** - Regenerate API keys monthly

---

## 🚀 Advanced Customization

### Add Database Storage
```python
import sqlite3

def save_conversation(user_id, messages):
    conn = sqlite3.connect('chatbot.db')
    # Save logic here
    conn.close()
```

### Add User Authentication
```python
import streamlit_authenticator as stauth

authenticator = stauth.Authenticate(
    credentials, "session_name", "unsigned_keys"
)
```

### Add Conversation Export
```python
import json

def export_conversation():
    with open('conversation.json', 'w') as f:
        json.dump(st.session_state.messages, f)
```

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| Main file | 193 lines |
| Config file | 80 lines |
| Personalities | 5 built-in |
| Models | 3 available |
| Customizable | ✅ Yes |
| Deployable | ✅ Free |

---

## 🎯 Usage Examples

### Example 1: Math Solving
```
User: "A rectangle has perimeter 24cm and width 4cm. Find length."
Teacher: "Using formula P = 2(l + w)...
         l = 8 cm"
```

### Example 2: Health Advice
```
User: "I have headache and fever"
Doctor: "These suggest common cold or flu. 
         Rest, drink fluids, take paracetamol..."
```

### Example 3: Travel Planning
```
User: "Best time to visit Japan?"
Guide: "Spring (March-May) or Fall (Oct-Nov).
        Cherry blossoms in spring, leaves in fall..."
```

---

## 🔄 Update & Maintenance

### Check for Updates
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

### Backup Conversations
```bash
# Copy .streamlit/secrets.toml to safe location
# Keep git history for code recovery
```

### Monitor API Usage
- Check Groq Console for usage stats
- Set monthly budget limits
- Monitor response times

---

## ✅ Deployment Checklist

- [ ] Created Groq account and API key
- [ ] Installed Python packages
- [ ] Added API key to `.streamlit/secrets.toml`
- [ ] Tested locally: `streamlit run app.py`
- [ ] Tested all personalities
- [ ] Pushed to GitHub
- [ ] Deployed to Streamlit Cloud
- [ ] Added API key to Streamlit Cloud Secrets
- [ ] Verified live app works
- [ ] Shared with friends/colleagues

---

## 📖 Additional Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [Groq API Docs](https://console.groq.com/docs)
- [Python Docs](https://docs.python.org/3/)
- [Git Tutorial](https://git-scm.com/doc)

---

## 🎓 Learning Paths

### Beginner
1. Run locally
2. Test personalities
3. Customize settings in `config.py`

### Intermediate
1. Add new personalities to `personalities.py`
2. Customize system prompts
3. Deploy to Streamlit Cloud

### Advanced
1. Add database integration
2. Implement user authentication
3. Build conversation analytics
4. Create custom UI components

---

## 🤝 Contributing

Contributions welcome! You can:
- Add new personalities
- Improve system prompts
- Fix bugs
- Improve documentation
- Add new features

---

## 📝 License

MIT License - Feel free to use for personal or commercial projects.

---

## 🆘 Support

### Having Issues?
1. Check troubleshooting section above
2. Search GitHub issues
3. Check Streamlit/Groq documentation
4. Create a new GitHub issue

### Need Help?
- Ask in Streamlit community
- Check Groq API documentation
- Review code comments

---

## 🎉 Success!

You now have a fully functional AI Agent Chatbot! 

**Next steps:**
1. Customize personalities for your needs
2. Add more AI models
3. Deploy and share
4. Collect user feedback
5. Improve prompts

---

**Build amazing things with AI! 🚀**

Made with ❤️ using Streamlit & Groq API
