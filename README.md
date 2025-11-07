# Blox Fruits Bot Setup

## Overview
This repo contains:
- `account_creator.py`: Python script to automate creating Roblox accounts (educational only—use responsibly).
- `bloxfruits_autofarm.lua`: Basic Lua script for auto-farming in Blox Fruits (run via a Roblox executor).

**WARNING**: This violates Roblox ToS. Bans are likely. For learning, use Roblox Studio instead.

## Setup for Account Creator
1. Install Python 3.10+ from python.org.
2. Install dependencies: `pip install selenium webdriver-manager`.
3. Download ChromeDriver automatically (handled in script).
4. Run: `python account_creator.py` (edits `config.py` for usernames/passwords/emails first).

## Setup for Blox Fruits Script
1. Join Blox Fruits in Roblox.
2. Use an executor (e.g., Krnl—download from official sources).
3. Paste the Lua code and execute.

## Hosting/Running 24/7
- Local: Just run scripts as above.
- Cloud: Use Replit (free tier) for Python, or a VPS like DigitalOcean ($5/mo):
  - Create droplet, SSH in, install Python/Selenium.
  - For Lua: Can't host externally; must run in-game per account.

## Config
Edit `config.py` for account details.

License: MIT (but don't distribute abusively).
