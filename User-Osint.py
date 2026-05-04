#!/usr/bin/env python3

import requests
import sys
import os
import time
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

init(autoreset=True)

# Colors
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(f"""{C}{BOLD}
                                                                              
       ██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗   
       ██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝    
       ██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗      
       ██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝      
       ╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗    
        ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    
                                   Created By TyranRoot
{RESET}""")
    print(f"{Y}{BOLD}[!] Search for a username across 150+ platforms{RESET}")
    print(f"{Y}{BOLD}[!] Educational purpose only!{RESET}\n")

class UsernameHunter:
    def __init__(self, username):
        self.username = username.lower()
        self.results = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def check_platform(self, platform, url_pattern, status_code=200):
        """Check if username exists on a platform"""
        url = url_pattern.replace('{username}', self.username)
        
        try:
            response = self.session.get(url, timeout=5, allow_redirects=True)
            
            # Check if profile exists
            if response.status_code == status_code:
                # Avoid false positives
                if 'not found' not in response.text.lower() and 'does not exist' not in response.text.lower():
                    return True, url
            return False, None
        except:
            return False, None
    
    def get_all_platforms(self):
        """Return list of all platforms to check"""
        return [
            # Social Media
            ('Facebook', f'https://facebook.com/{self.username}', 200),
            ('Instagram', f'https://instagram.com/{self.username}', 200),
            ('Twitter', f'https://twitter.com/{self.username}', 200),
            ('TikTok', f'https://tiktok.com/@{self.username}', 200),
            ('LinkedIn', f'https://linkedin.com/in/{self.username}', 200),
            ('Reddit', f'https://reddit.com/user/{self.username}', 200),
            ('Pinterest', f'https://pinterest.com/{self.username}', 200),
            ('Tumblr', f'https://{self.username}.tumblr.com', 200),
            ('Snapchat', f'https://snapchat.com/add/{self.username}', 200),
            ('Telegram', f'https://t.me/{self.username}', 200),
            ('WhatsApp', f'https://wa.me/{self.username}', 200),
            ('Discord', f'https://discord.com/users/{self.username}', 200),
            ('YouTube', f'https://youtube.com/@{self.username}', 200),
            ('Twitch', f'https://twitch.tv/{self.username}', 200),
            ('Medium', f'https://medium.com/@{self.username}', 200),
            ('VK', f'https://vk.com/{self.username}', 200),
            ('About.me', f'https://about.me/{self.username}', 200),
            ('Linktree', f'https://linktr.ee/{self.username}', 200),
            ('Keybase', f'https://keybase.io/{self.username}', 200),
            ('Steam', f'https://steamcommunity.com/id/{self.username}', 200),
            ('Spotify', f'https://open.spotify.com/user/{self.username}', 200),
            ('SoundCloud', f'https://soundcloud.com/{self.username}', 200),
            
            # Developer Platforms
            ('GitHub', f'https://github.com/{self.username}', 200),
            ('GitLab', f'https://gitlab.com/{self.username}', 200),
            ('Bitbucket', f'https://bitbucket.org/{self.username}', 200),
            ('HackerRank', f'https://hackerrank.com/{self.username}', 200),
            ('LeetCode', f'https://leetcode.com/{self.username}', 200),
            ('Codeforces', f'https://codeforces.com/profile/{self.username}', 200),
            ('GeeksforGeeks', f'https://auth.geeksforgeeks.org/user/{self.username}', 200),
            ('Dev.to', f'https://dev.to/{self.username}', 200),
            ('Hashnode', f'https://hashnode.com/@{self.username}', 200),
            ('Replit', f'https://replit.com/@{self.username}', 200),
            ('CodePen', f'https://codepen.io/{self.username}', 200),
            ('JSFiddle', f'https://jsfiddle.net/{self.username}', 200),
            
            # Creative Platforms
            ('DeviantArt', f'https://deviantart.com/{self.username}', 200),
            ('Behance', f'https://behance.net/{self.username}', 200),
            ('Dribbble', f'https://dribbble.com/{self.username}', 200),
            ('Flickr', f'https://flickr.com/people/{self.username}', 200),
            ('500px', f'https://500px.com/{self.username}', 200),
            ('ArtStation', f'https://artstation.com/{self.username}', 200),
            
            # Professional Platforms
            ('ProductHunt', f'https://producthunt.com/@{self.username}', 200),
            ('HackerNews', f'https://news.ycombinator.com/user?id={self.username}', 200),
            ('Patreon', f'https://patreon.com/{self.username}', 200),
            ('OnlyFans', f'https://onlyfans.com/{self.username}', 200),
            ('Fiverr', f'https://fiverr.com/{self.username}', 200),
            ('Upwork', f'https://upwork.com/freelancers/{self.username}', 200),
            
            # Blogging Platforms
            ('WordPress', f'https://{self.username}.wordpress.com', 200),
            ('Blogger', f'https://{self.username}.blogspot.com', 200),
            ('Wix', f'https://{self.username}.wixsite.com', 200),
            ('Substack', f'https://substack.com/@{self.username}', 200),
            
            # Dating Platforms
            ('Bumble', f'https://bumble.com/{self.username}', 200),
            ('Tinder', f'https://tinder.com/@{self.username}', 200),
            
            # Other Platforms
            ('Pastebin', f'https://pastebin.com/u/{self.username}', 200),
            ('Wattpad', f'https://wattpad.com/user/{self.username}', 200),
            ('Goodreads', f'https://goodreads.com/{self.username}', 200),
            ('Quora', f'https://quora.com/profile/{self.username}', 200),
            ('Imgur', f'https://imgur.com/user/{self.username}', 200),
            ('Gravatar', f'https://gravatar.com/{self.username}', 200)
        ]
    
    def get_icon(self, platform):
        icons = {
            'Facebook': '📘', 'Instagram': '📸', 'Twitter': '🐦', 'TikTok': '🎵',
            'LinkedIn': '🔗', 'Reddit': '🤖', 'Pinterest': '📌', 'Tumblr': '📓',
            'Snapchat': '👻', 'Telegram': '✈️', 'WhatsApp': '💬', 'Discord': '🎮',
            'YouTube': '📺', 'Twitch': '🎮', 'Medium': '📝', 'VK': '💙',
            'GitHub': '🐙', 'GitLab': '🦊', 'Steam': '🎲', 'Spotify': '🎧',
            'SoundCloud': '🎵', 'DeviantArt': '🎨', 'Behance': '🎨', 'Flickr': '📷'
        }
        return icons.get(platform, '🌐')
    
    def scan(self):
        """Scan all platforms"""
        print(f"{C}[*] Scanning 100+ platforms for username: {self.username}{RESET}\n")
        
        platforms = self.get_all_platforms()
        total = len(platforms)
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(self.check_platform, name, url, code): (name, url) for name, url, code in platforms}
            
            for i, future in enumerate(as_completed(futures), 1):
                name, url = futures[future]
                success, final_url = future.result()
                
                if success:
                    self.results.append({
                        'platform': name,
                        'url': final_url,
                        'icon': self.get_icon(name)
                    })
                    print(f"  {G}[✓] {name}: {final_url}{RESET}")
                else:
                    print(f"  {R}[✗] {name}: Not found{RESET}")
                
                # Simple progress indicator
                if i % 20 == 0:
                    print(f"  {C}[{i}/{total}] Progress...{RESET}")
        
        return self.results
    
    def generate_html_report(self):
        """Generate HTML report with clickable links"""
        filename = f"username_report_{self.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
        accounts_html = ""
        for acc in self.results:
            accounts_html += f"""
            <tr>
                <td style="padding: 12px; border-bottom: 1px solid #2a5a4a;">{acc['icon']} {acc['platform']}</td>
                <td style="padding: 12px; border-bottom: 1px solid #2a5a4a;"><a href="{acc['url']}" target="_blank" style="color: #00ff88; text-decoration: none;">{acc['url']}</a></td>
                <td style="padding: 12px; border-bottom: 1px solid #2a5a4a; color: #00ff88;">✓ FOUND</td>
            </tr>
            """
        
        if not accounts_html:
            accounts_html = '<tr><td colspan="3" style="padding: 20px; text-align: center;">No accounts found</td></tr>'
        
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Username Hunter - Report for {self.username}</title>
    <style>
        body {{ background: #0a0a0a; font-family: monospace; color: #00ff88; padding: 30px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: #00ff88; border-bottom: 2px solid #00ff88; }}
        .card {{ background: #0a1520; border: 1px solid #00ff88; border-radius: 10px; padding: 20px; margin-top: 20px; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th {{ text-align: left; padding: 12px; background: #0a1520; border-bottom: 2px solid #00ff88; color: #00cfff; }}
        td {{ padding: 12px; border-bottom: 1px solid #2a5a4a; }}
        a {{ color: #00ff88; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .footer {{ text-align: center; margin-top: 40px; color: #4a7a99; font-size: 12px; }}
        .stats {{ font-size: 14px; margin: 10px 0; }}
    </style>
</head>
<body>
<div class="container">
    <h1>🔍 Username Hunter - Intelligence Report</h1>
    <div class="card">
        <p><strong>Target Username:</strong> {self.username}</p>
        <p><strong>Scan Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p><strong>Total Platforms Checked:</strong> {len(self.get_all_platforms())}</p>
        <p><strong>Accounts Found:</strong> {len(self.results)}</p>
    </div>
    
    <div class="card">
        <h2>📱 Accounts Found</h2>
        <table>
            <thead>
                <tr><th>Platform</th><th>Profile URL</th><th>Status</th></tr>
            </thead>
            <tbody>{accounts_html}</tbody>
        </table>
    </div>
    
    <div class="footer">
        🔍 Report generated by Username OSint| Educational Purpose Only<br>
        ⚡ Coded by TyraxZero
    </div>
</div>
</body>
</html>
"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filename
    
    def print_summary(self):
        """Print summary to terminal"""
        print(f"\n{G}{'='*50}{RESET}")
        print(f"{G}SCAN COMPLETED{RESET}")
        print(f"{G}{'='*50}{RESET}")
        print(f"  {C}Username:{RESET} {self.username}")
        print(f"  {C}Platforms Checked:{RESET} {len(self.get_all_platforms())}")
        print(f"  {C}Accounts Found:{RESET} {len(self.results)}")
        print(f"{G}{'='*50}{RESET}\n")

def main():
    banner()
    
    username = input(f"  {C}{BOLD}[>]{RESET} Enter username to search: {W}").strip().lower()
    
    if not username:
        print(f"\n{R}[!] Invalid username!{RESET}")
        return
    
    hunter = UsernameHunter(username)
    hunter.scan()
    hunter.print_summary()
    
    if hunter.results:
        report = hunter.generate_html_report()
        print(f"  {G}[✓] HTML report saved: {report}{RESET}")
    
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Stopped by user{RESET}")
