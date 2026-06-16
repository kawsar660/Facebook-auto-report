#!/usr/bin/env python3
"""
███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
█████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝
██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗
██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

███████╗███╗   ███╗ ██████╗ ███╗   ██╗    ██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗
██╔════╝████╗ ████║██╔═══██╗████╗  ██║    ██║ ██╔╝██║  ██║██╔══██╗████╗  ██║
█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║    █████╔╝ ███████║███████║██╔██╗ ██║
██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║    ██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║
███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    ██║  ██╗██║  ██║██║  ██║██║ ╚████║
╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

                    ╔══════════════════════════════════════╗
                    ║      THE CYBER SECURITY FORCE        ║
                    ║    🔥 FACEBOOK AUTO REPORTER 🔥      ║
                    ╚══════════════════════════════════════╝

                    ╔══════════════════════════════════════╗
                    ║       CREATED BY: EMON KHAN          ║
                    ║     🛡️  PENTESTING TOOL v2.0 🛡️        ║
                    ╚══════════════════════════════════════╝

============================================================
           🔥 TERMUX FULL SCREEN MODE ACTIVATED 🔥
============================================================
"""

import requests
import json
import time
import random
import sys
import argparse
import os
from urllib.parse import urlparse, quote

# ============================================
# ═══ TEAM & CREATOR INFORMATION ═══
# ============================================
CREATOR = "EMON KHAN"
TEAM_NAME = "THE CYBER SECURITY FORCE"
TOOL_NAME = "FACEBOOK AUTO REPORTER"

# ═══ FULL SCREEN BANNER ═══
def clear_screen():
    """Termux স্ক্রিন ক্লিয়ার করা"""
    os.system('clear' if os.name == 'posix' else 'cls')

def show_fullscreen_banner():
    """পুরো ফোন জুড়ে বড় ব্যানার দেখানো"""
    clear_screen()

    banner = f"""
{'='*70}

{' '*30}███████╗███╗   ███╗ ██████╗ ███╗   ██╗
{' '*30}██╔════╝████╗ ████║██╔═══██╗████╗  ██║
{' '*30}█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
{' '*30}██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
{' '*30}███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
{' '*30}╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

{'='*70}

{' '*10}██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗
{' '*10}██║ ██╔╝██║  ██║██╔══██╗████╗  ██║
{' '*10}█████╔╝ ███████║███████║██╔██╗ ██║
{' '*10}██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║
{' '*10}██║  ██╗██║  ██║██║  ██║██║ ╚████║
{' '*10}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

{'='*70}

{' '*15}[{'='*38}]
{' '*15}[{' '*38}]
{' '*15}    🔥  EMON KHAN  🔥
{' '*15}    📌  FACEBOOK
{' '*15}[{' '*38}]
{' '*15}[{'='*38}]

{'='*70}
"""
    print(banner)
    input("     [⚠️] Press ENTER to continue...")
    clear_screen()

# ═══ ফুল-স্ক্রিন লোডিং এনিমেশন ═══
def loading_animation(seconds=2):
    """Termux-এ বড় লোডিং বার দেখা"""
    for i in range(seconds * 5):
        bar = '█' * i + '░' * (seconds * 5 - i)
        sys.stdout.write(f"\r{' '*10}[{bar}] LOADING... {int((i/(seconds*5))*100)}%")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n" + " "*10 + "[LOADING COMPLETE!]" + "\n")


class FacebookAutoReporter:
    """Facebook Auto Reporter - All Report Types"""

    # Complete report reason mappings
    REASONS_PROFILE = {
        1: ('abuse', 'General Abuse'),
        2: ('fake_account', 'Fake Account'),
        3: ('hate_speech', 'Hate Speech'),
        4: ('violence', 'Violence/Threats'),
        5: ('harassment', 'Harassment'),
        6: ('spam', 'Spam'),
        7: ('nudity', 'Nudity'),
        8: ('terrorism', 'Terrorism'),
        9: ('self_harm', 'Suicide/Self-harm'),
        10: ('scam', 'Scam/Fraud'),
        11: ('impersonation', 'Impersonation'),
        12: ('ip_violation', 'IP Violation'),
    }

    REASONS_POST = {
        1: ('nudity', 'Nudity'),
        2: ('hate_speech', 'Hate Speech'),
        3: ('violence', 'Violence'),
        4: ('harassment', 'Harassment'),
        5: ('false_news', 'Fake News'),
        6: ('spam', 'Spam'),
        7: ('copyright', 'Copyright'),
        8: ('scam', 'Scam'),
    }

    REASONS_PAGE = {
        1: ('scam', 'Scam'),
        2: ('fake_page', 'Fake Page'),
        3: ('hate_speech', 'Hate Speech'),
        4: ('violence', 'Violence'),
        5: ('impersonation', 'Impersonation'),
        6: ('spam', 'Spam'),
    }

    REASONS_COMMENT = {
        1: ('harassment', 'Harassment'),
        2: ('hate_speech', 'Hate Speech'),
        3: ('violence', 'Violence'),
        4: ('spam', 'Spam'),
        5: ('bullying', 'Bullying'),
    }

    def __init__(self, access_token=None):
        self.base_url = "https://graph.facebook.com/v19.0"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36'
        })
        self.access_token = access_token or os.environ.get('FB_ACCESS_TOKEN')
        if not self.access_token:
            print("\n")
            print("╔" + "═"*50 + "╗")
            print("║" + " "*50 + "║")
            print("║     🔑 FACEBOOK ACCESS TOKEN REQUIRED          ║")
            print("║" + " "*50 + "║")
            print("╚" + "═"*50 + "╝")
            self.access_token = input("\n[+] Enter Facebook Access Token: ").strip()
        self.report_count = 0
        self.success_count = 0

    def show_report_types(self, target_type='all'):
        """Display available report reasons"""
        categories = {
            'profile': self.REASONS_PROFILE,
            'post': self.REASONS_POST,
            'page': self.REASONS_PAGE,
            'comment': self.REASONS_COMMENT,
        }

        if target_type == 'all':
            for cat, reasons in categories.items():
                print(f"\n{'='*50}")
                print(f"  [{cat.upper()}] - Report Reasons:")
                print('='*50)
                for num, (reason, desc) in reasons.items():
                    print(f"    {num:2d}. {desc:35s} -> ({reason})")
        elif target_type in categories:
            print(f"\n{'='*50}")
            print(f"  [{target_type.upper()}] - Report Reasons:")
            print('='*50)
            for num, (reason, desc) in categories[target_type].items():
                print(f"    {num:2d}. {desc:35s} -> ({reason})")

    def report_profile(self, profile_id, reason="abuse"):
        try:
            r = self.session.post(
                f"{self.base_url}/{profile_id}/reports",
                params={'access_token': self.access_token, 'reason': reason,
                        'source': 'www', 'is_anonymous': True},
                timeout=15
            )
            result = r.json()
            if r.status_code == 200 and not result.get('error'):
                self.success_count += 1
                return True, result
            else:
                return False, result.get('error', {}).get('message', 'Unknown')
        except Exception as e:
            return False, str(e)

    def report_post(self, post_url, reason="spam", description=""):
        post_id = self._extract_id(post_url)
        if not post_id:
            return False, "Could not extract post ID"
        try:
            r = self.session.post(
                f"{self.base_url}/{post_id}/reports",
                params={'access_token': self.access_token, 'reason': reason,
                        'description': description[:1000], 'is_anonymous': True},
                timeout=15
            )
            result = r.json()
            if r.status_code == 200:
                self.success_count += 1
                return True, result
            else:
                return False, result.get('error', {}).get('message', 'Unknown')
        except Exception as e:
            return False, str(e)

    def report_page(self, page_id, reason="scam"):
        try:
            r = self.session.post(
                f"{self.base_url}/{page_id}/page_reports",
                params={'access_token': self.access_token, 'reason': reason,
                        'page_id': page_id, 'source': 'page_report_flow'},
                timeout=15
            )
            result = r.json()
            if r.status_code == 200:
                self.success_count += 1
                return True, result
            else:
                return False, result.get('error', {}).get('message', 'Unknown')
        except Exception as e:
            return False, str(e)

    def report_comment(self, comment_id, reason="harassment"):
        try:
            r = self.session.post(
                f"{self.base_url}/{comment_id}/reports",
                params={'access_token': self.access_token, 'reason': reason,
                        'is_anonymous': True},
                timeout=15
            )
            result = r.json()
            if r.status_code == 200:
                self.success_count += 1
                return True, result
            else:
                return False, result.get('error', {}).get('message', 'Unknown')
        except Exception as e:
            return False, str(e)

    def multi_report(self, targets, report_type="profile", reason="abuse",
                     delay=5, randomize=True):
        print(f"\n{'='*50}")
        print(f"  [🔥] Starting Multi-Report")
        print(f"  [📌] Targets: {len(targets)}")
        print(f"  [🎯] Type: {report_type}")
        print(f"  [⚡] Reason: {reason}")
        print(f"{'='*50}\n")

        report_functions = {
            'profile': self.report_profile,
            'post': self.report_post,
            'page': self.report_page,
            'comment': self.report_comment,
        }

        func = report_functions.get(report_type)
        if not func:
            print(f"[✗] Unknown type: {report_type}")
            return

        for idx, target in enumerate(targets, 1):
            print(f"  [{idx}/{len(targets)}] ➜ Reporting: {target}")
            success, msg = func(target, reason)
            if success:
                print(f"    [✓] SUCCESS - Report ID: {msg.get('id', 'N/A')}")
            else:
                print(f"    [✗] FAILED - {msg}")
            self.report_count += 1

            if idx < len(targets):
                wait = random.uniform(delay * 0.8, delay * 1.2) if randomize else delay
                print(f"    [-] Waiting {wait:.1f}s...\n")
                time.sleep(wait)

        print(f"\n{'='*50}")
        print(f"  [✅] COMPLETE! {self.success_count}/{self.report_count} Successful")
        print(f"{'='*50}")

    def _extract_id(self, url):
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        parts = path.split('/')
        for part in parts:
            if '_' in part and part.replace('_', '').isdigit():
                return part
        try:
            r = self.session.get(
                f"{self.base_url}/?id={quote(url)}&access_token={self.access_token}",
                timeout=10
            )
            data = r.json()
            return data.get('id')
        except:
            return None

    def get_report_history(self, limit=25):
        try:
            r = self.session.get(
                f"{self.base_url}/me/reports",
                params={'access_token': self.access_token, 'limit': limit,
                        'fields': 'id,type,status,created_time,target'},
                timeout=10
            )
            return r.json()
        except:
            return {'error': 'Failed to fetch history'}


def interactive_mode(reporter):
    """Full Screen Interactive Menu"""
    while True:
        clear_screen()

        # Main Menu Header
        print(f"""
{'='*60}
{' '*20}███████╗ █████╗  ██████╗███████╗
{' '*20}██╔════╝██╔══██╗██╔════╝██╔════╝
{' '*20}█████╗  ███████║██║     █████╗
{' '*20}██╔══╝  ██╔══██║██║     ██╔══╝
{' '*20}██║     ██║  ██║╚██████╗███████╗
{' '*20}╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
{'='*60}
{' '*15}[ {TEAM_NAME} - {TOOL_NAME} ]
{' '*15}[ 👤 CREATED BY: {CREATOR} ]
{'='*60}
""")

        print("  ╔══════════════════════════════════════════╗")
        print("  ║         🔥 MAIN MENU                    ║")
        print("  ╠══════════════════════════════════════════╣")
        print("  ║  1. 📋 Report Profile                   ║")
        print("  ║  2. 📝 Report Post                      ║")
        print("  ║  3. 📄 Report Page                      ║")
        print("  ║  4. 💬 Report Comment                   ║")
        print("  ║  5. 📦 Batch Report (from file)         ║")
        print("  ║  6. 📜 View Report History              ║")
        print("  ║  7. 📚 Show All Report Reasons          ║")
        print("  ║  0. 🚪 Exit                             ║")
        print("  ╚══════════════════════════════════════════╝")

        choice = input("\n  [?] Select option: ").strip()

        if choice == '0':
            print(f"\n  [👋] Thank you for using {TOOL_NAME}")
            print(f"  [👤] Created by {CREATOR}\n")
            break

        elif choice == '1':
            reporter.show_report_types('profile')
            target = input("\n  [?] Enter Profile ID: ").strip()
            reason = input("  [?] Enter reason (or 'list'): ").strip()
            if reason == 'list':
                reporter.show_report_types('profile')
                reason = input("  [?] Enter reason: ").strip()
            s, m = reporter.report_profile(target, reason)
            print(f"\n  {'[✓]' if s else '[✗]'} Result: {m}")
            input("\n  [Press ENTER to continue...]")

        elif choice == '2':
            reporter.show_report_types('post')
            target = input("\n  [?] Enter Post URL: ").strip()
            reason = input("  [?] Enter reason (or 'list'): ").strip()
            if reason == 'list':
                reporter.show_report_types('post')
                reason = input("  [?] Enter reason: ").strip()
            desc = input("  [?] Description (optional): ").strip()
            s, m = reporter.report_post(target, reason, desc)
            print(f"\n  {'[✓]' if s else '[✗]'} Result: {m}")
            input("\n  [Press ENTER to continue...]")

        elif choice == '3':
            reporter.show_report_types('page')
            target = input("\n  [?] Enter Page ID/Name: ").strip()
            reason = input("  [?] Enter reason (or 'list'): ").strip()
            if reason == 'list':
                reporter.show_report_types('page')
                reason = input("  [?] Enter reason: ").strip()
            s, m = reporter.report_page(target, reason)
            print(f"\n  {'[✓]' if s else '[✗]'} Result: {m}")
            input("\n  [Press ENTER to continue...]")

        elif choice == '4':
            reporter.show_report_types('comment')
            target = input("\n  [?] Enter Comment ID: ").strip()
            reason = input("  [?] Enter reason (or 'list'): ").strip()
            if reason == 'list':
                reporter.show_report_types('comment')
                reason = input("  [?] Enter reason: ").strip()
            s, m = reporter.report_comment(target, reason)
            print(f"\n  {'[✓]' if s else '[✗]'} Result: {m}")
            input("\n  [Press ENTER to continue...]")

        elif choice == '5':
            filepath = input("\n  [?] Path to target file: ").strip()
            print("\n  Target types:")
            print("    1. Profile  2. Post  3. Page  4. Comment")
            ttype_choice = input("  [?] Select target type (1-4): ").strip()
            type_map = {'1': 'profile', '2': 'post', '3': 'page', '4': 'comment'}
            ttype = type_map.get(ttype_choice, 'profile')
            reason = input("  [?] Reason: ").strip()
            try:
                delay = float(input("  [?] Delay in seconds (default 5): ").strip() or '5')
            except:
                delay = 5
            try:
                with open(filepath) as f:
                    targets = [l.strip() for l in f if l.strip() and not l.startswith('#')]
                reporter.multi_report(targets, ttype, reason, delay)
            except Exception as e:
                print(f"\n  [✗] Error: {e}")
            input("\n  [Press ENTER to continue...]")

        elif choice == '6':
            result = reporter.get_report_history()
            print(f"\n{'='*50}")
            print("  📜 REPORT HISTORY")
            print('='*50)
            if 'data' in result:
                for item in result['data']:
                    print(f"  ID: {item.get('id')}")
                    print(f"  Status: {item.get('status')}")
                    print(f"  Time: {item.get('created_time')}")
                    print(f"  Target: {item.get('target', {}).get('id', 'N/A')}")
                    print("-"*40)
            else:
                print(f"  {json.dumps(result, indent=2)}")
            input("\n  [Press ENTER to continue...]")

        elif choice == '7':
            reporter.show_report_types('all')
            input("\n  [Press ENTER to continue...]")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} - {CREATOR}")
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    parser.add_argument('--profile', help='Report profile by ID')
    parser.add_argument('--post', help='Report post by URL')
    parser.add_argument('--page', help='Report page by ID')
    parser.add_argument('--comment', help='Report comment by ID')
    parser.add_argument('--reason', default='abuse', help='Report reason')
    parser.add_argument('--token', help='Facebook Access Token')
    parser.add_argument('--history', action='store_true', help='View report history')
    parser.add_argument('--list', action='store_true', help='List all report reasons')
    parser.add_argument('--batch', help='File with targets')
    parser.add_argument('--type', default='profile', help='Target type for batch')
    parser.add_argument('--delay', type=float, default=5.0, help='Delay between reports')

    args = parser.parse_args()

    # Show full screen banner first
    show_fullscreen_banner()
    loading_animation(2)

    reporter = FacebookAutoReporter(args.token)

    if args.interactive or len(sys.argv) == 1:
        interactive_mode(reporter)
        return

    if args.list:
        reporter.show_report_types('all')
        return

    if args.history:
        print(json.dumps(reporter.get_report_history(), indent=2))
        return

    if args.profile:
        s, m = reporter.report_profile(args.profile, args.reason)
        print(f"{'[✓]' if s else '[✗]'} Profile: {m}")
    if args.post:
        s, m = reporter.report_post(args.post, args.reason)
        print(f"{'[✓]' if s else '[✗]'} Post: {m}")
    if args.page:
        s, m = reporter.report_page(args.page, args.reason)
        print(f"{'[✓]' if s else '[✗]'} Page: {m}")
    if args.comment:
        s, m = reporter.report_comment(args.comment, args.reason)
        print(f"{'[✓]' if s else '[✗]'} Comment: {m}")
    if args.batch:
        targets = [l.strip() for l in open(args.batch)
                  if l.strip() and not l.startswith('#')]
        reporter.multi_report(targets, args.type, args.reason, args.delay)


if __name__ == '__main__':
    main()
