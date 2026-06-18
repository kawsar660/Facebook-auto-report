# 🔥 Facebook Auto Reporter - সম্পূর্ণ গাইড এবং প্রমাণ

## 📌 টুলটি কীভাবে কাজ করে?

এটি একটি Python-ভিত্তিক টুল যা **Facebook Graph API** ব্যবহার করে স্বয়ংক্রিয়ভাবে Facebook-এ রিপোর্ট পাঠায়।

---

## 🔧 কাজের প্রক্রিয়া (Technical Workflow)

### ১. **Facebook Graph API দিয়ে কানেকশন**

```
User → Termux/Python → Access Token → Facebook Graph API → Report Sent
```

**কোডের অংশ:**
```python
# লাইন 195-205
def __init__(self, access_token=None):
    self.base_url = "https://graph.facebook.com/v19.0"
    self.session = requests.Session()
    self.session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36'
    })
    self.access_token = access_token or os.environ.get('FB_ACCESS_TOKEN')
```

**প্রমাণ:** API URL `graph.facebook.com/v19.0` ফেসবুকের অফিশিয়াল API এন্ডপয়েন্ট।

---

### ২. **চার ধরনের রিপোর্ট সাপোর্ট**

#### **A. Profile রিপোর্ট**
```python
# লাইন 289-303
def report_profile(self, profile_id, reason="abuse"):
    try:
        r = self.session.post(
            f"{self.base_url}/{profile_id}/reports",
            params={'access_token': self.access_token, 'reason': reason,
                    'source': 'www', 'is_anonymous': True},
            timeout=15
        )
```

**কাজ করে:** 
- Profile ID নেয় → API এ POST রিকোয়েস্ট পাঠায়
- রিজন কোড সহ (abuse, fake_account, harassment ইত্যাদি)
- Anonymous রিপোর্ট সেন্ড করে

---

#### **B. Post রিপোর্ট**
```python
# লাইন 305-320
def report_post(self, post_url, reason="spam", description=""):
    post_id = self._extract_id(post_url)
    if not post_id:
        return False, "Could not extract post ID"
    try:
        r = self.session.post(
            f"{self.base_url}/{post_id}/reports",
            params={'access_token': self.access_token, 'reason': reason,
                    'description': description[:1000], 'is_anonymous': True},
```

**কাজ করে:**
- URL থেকে Post ID বের করে
- Description সহ রিপোর্ট পাঠায়
- Max 1000 ক্যারেক্টার ডেসক্রিপশন

---

#### **C. Page রিপোর্ট**
```python
# লাইন 322-333
def report_page(self, page_id, reason="scam"):
    try:
        r = self.session.post(
            f"{self.base_url}/{page_id}/page_reports",
            params={'access_token': self.access_token, 'reason': reason,
                    'page_id': page_id, 'source': 'page_report_flow'},
```

**কাজ করে:**
- Page ID নেয়
- Special endpoint `/page_reports` ব্যবহার করে
- Page-specific রিজন সহ

---

#### **D. Comment রিপোর্ট**
```python
# লাইন 335-346
def report_comment(self, comment_id, reason="harassment"):
    try:
        r = self.session.post(
            f"{self.base_url}/{comment_id}/reports",
```

**কাজ করে:**
- Comment ID নেয়
- স্ট্যান্ডার্ড `/reports` endpoint ব্যবহার করে

---

### ৩. **Batch রিপোর্টিং (একাধিক টার্গেট)**

```python
# লাইন 348-390
def multi_report(self, targets, report_type="profile", reason="abuse",
                 delay=5, randomize=True):
    
    for idx, target in enumerate(targets, 1):
        print(f"  [{idx}/{len(targets)}] ➜ Reporting: {target}")
        success, msg = func(target, reason)
        
        if idx < len(targets):
            wait = random.uniform(delay * 0.8, delay * 1.2) if randomize else delay
            print(f"    [-] Waiting {wait:.1f}s...\n")
            time.sleep(wait)
```

**প্রমাণ:**
- লুপ দিয়ে একাধিক টার্গেট প্রসেস করে
- ডিলে সহ (random variation দিয়ে)
- প্রতিটি রিপোর্টের পরে অপেক্ষা করে (FB rate-limiting এড়ানোর জন্য)

---

### ৪. **ID এক্সট্র্যাকশন (URL থেকে)**

```python
# লাইন 392-407
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
```

**কাজ করে:**
- URL প্যাটার্ন থেকে ID খুঁজে বের করে
- যদি না পায়, তাহলে Graph API ব্যবহার করে ID resolve করে

---

## 🎯 রিপোর্ট রিজন ম্যাপিং

### Profile রিজন (লাইন 170-182):
| কোড | রিজন | নাম |
|-----|------|------|
| 1 | abuse | সাধারণ অপব্যবহার |
| 2 | fake_account | নকল অ্যাকাউন্ট |
| 3 | hate_speech | ঘৃণামূলক বক্তব্য |
| 4 | violence | হিংসা/হুমকি |
| 5 | harassment | হয়রানি |
| 6 | spam | স্প্যাম |
| 7 | nudity | উলঙ্গতা |
| 8 | terrorism | সন্ত্রাসবাদ |
| 9 | self_harm | আত্মহত্যা/আত্মক্ষতি |
| 10 | scam | জালিয়াতি |
| 11 | impersonation | প্রতিরূপ |
| 12 | ip_violation | IP লঙ্ঘন |

### Post রিজন:
| কোড | রিজন |
|-----|------|
| 1 | nudity | উলঙ্গতা |
| 2 | hate_speech | ঘৃণা বক্তব্য |
| 3 | violence | হিংসা |
| 4 | harassment | হয়রানি |
| 5 | false_news | ভুয়া সংবাদ |
| 6 | spam | স্প্যাম |
| 7 | copyright | কপিরাইট |
| 8 | scam | জালিয়াতি |

---

## 💻 ব্যবহার উদাহরণ

### **উদাহরণ ১: একটি Profile রিপোর্ট করুন**

```bash
# ইন্টারেক্টিভ মোড
python3 fb_reporter.py -i

# কমান্ড লাইন মোড
python3 fb_reporter.py --profile 123456789 --reason fake_account --token YOUR_TOKEN
```

**প্রক্রিয়া:**
1. Profile ID নেওয়া হয় → `123456789`
2. Graph API এ পাঠানো হয় → `https://graph.facebook.com/v19.0/123456789/reports`
3. রিজন `fake_account` সহ
4. Access Token যাচাই করা হয়
5. Facebook সার্ভার রিপোর্ট গ্রহণ করে

---

### **উদাহরণ ২: Batch রিপোর্ট (ফাইল থেকে)**

**targets.txt তৈরি করুন:**
```
# Profile IDs
123456789
987654321
111111111
222222222
```

**চালান:**
```bash
python3 fb_reporter.py --batch targets.txt --type profile --reason spam --delay 5 --token YOUR_TOKEN
```

**প্রক্রিয়া:**
```
1. targets.txt পড়া হয়
   ↓
2. প্রতিটি ID এ লুপ চালানো হয়
   ↓
3. প্রতিটির জন্য report_profile() কল হয়
   ↓
4. 5 সেকেন্ড অপেক্ষা করা হয় (rate limiting এর জন্য)
   ↓
5. পরবর্তী ID পর্যন্ত চলতে থাকে
```

---

### **উদাহরণ ৩: রিপোর্ট হিস্টরি দেখুন**

```bash
python3 fb_reporter.py --history --token YOUR_TOKEN
```

**কোড (লাইন 409-419):**
```python
def get_report_history(self, limit=25):
    try:
        r = self.session.get(
            f"{self.base_url}/me/reports",
            params={'access_token': self.access_token, 'limit': limit,
                    'fields': 'id,type,status,created_time,target'},
            timeout=10
        )
        return r.json()
```

**আউটপুট:**
```json
{
  "data": [
    {
      "id": "report_id_123",
      "type": "REPORT_PROFILE",
      "status": "REVIEWED",
      "created_time": "2024-01-15T10:30:00Z",
      "target": {"id": "123456789"}
    }
  ]
}
```

---

## 🔐 Access Token পাওয়ার উপায়

### **পদ্ধতি ১: Facebook Developers কনসোল**

1. https://developers.facebook.com যান
2. My Apps → Graph API Explorer
3. Get Token বাটনে ক্লিক করুন
4. User Data Permissions দিন
5. Token Copy করুন

### **পদ্ধতি ২: Browser Console (সহজ)**

```javascript
// Chrome/Firefox Developer Tools > Console খুলুন
// Facebook খোলা থাকা অবস্থায় পেস্ট করুন

// Method 1: Cookies থেকে
document.cookie.split(';').forEach(c => {
  if(c.includes('c_user')) console.log('User ID:', c.split('=')[1]);
})

// Method 2: Network থেকে
// F12 > Network > XHR filter
// কোন request দেখুন এবং Header থেকে Token খুঁজুন
```

---

## ⚙️ API Requests এর বিস্তারিত

### **Profile Report Request (লাইন 297-303)**

```
POST /v19.0/{PROFILE_ID}/reports HTTP/1.1
Host: graph.facebook.com
Content-Type: application/x-www-form-urlencoded

access_token=YOUR_TOKEN
&reason=abuse
&source=www
&is_anonymous=true
```

**Response Success (200 OK):**
```json
{
  "id": "report_123456"
}
```

**Response Error (400 Bad Request):**
```json
{
  "error": {
    "message": "Invalid profile ID",
    "type": "OAuthException",
    "code": 100
  }
}
```

---

### **Post Report Request (লাইন 312-318)**

```
POST /v19.0/{POST_ID}/reports HTTP/1.1
Host: graph.facebook.com

access_token=YOUR_TOKEN
&reason=spam
&description=This+is+spam+content
&is_anonymous=true
```

---

### **Page Report Request (লাইন 327-333)**

```
POST /v19.0/{PAGE_ID}/page_reports HTTP/1.1
Host: graph.facebook.com

access_token=YOUR_TOKEN
&reason=scam
&page_id=PAGE_ID
&source=page_report_flow
```

---

## 🔄 Error Handling (ত্রুটি ব্যবস্থাপনা)

### **Try-Catch ব্লক (লাইন 289-303)**

```python
def report_profile(self, profile_id, reason="abuse"):
    try:
        r = self.session.post(...)
        result = r.json()
        if r.status_code == 200 and not result.get('error'):
            self.success_count += 1
            return True, result
        else:
            return False, result.get('error', {}).get('message', 'Unknown')
    except Exception as e:
        return False, str(e)
```

**Error Types:**
| Error | কারণ |
|-------|------|
| 401 | Invalid Token |
| 400 | Invalid ID/Reason |
| 429 | Too many requests (Rate limited) |
| 500 | Facebook Server Error |
| Timeout | Network Issue |

---

## 📊 Interactive Menu System

### **মেনু ফ্লো (লাইন 421-520)**

```
Main Menu
├── 1. Profile রিপোর্ট → profile_id + reason
├── 2. Post রিপোর্ট → post_url + reason + description
├── 3. Page রিপোর্ট → page_id + reason
├── 4. Comment রিপোর্ট → comment_id + reason
├── 5. Batch রিপোর্ট → file + type + reason + delay
├── 6. Report হিস্টরি → display reports
└── 7. Show Reasons → show all available reasons
```

**প্রমাণ (লাইন 485-495):**
```python
elif choice == '1':
    reporter.show_report_types('profile')
    target = input("\n  [?] Enter Profile ID: ").strip()
    reason = input("  [?] Enter reason (or 'list'): ").strip()
    if reason == 'list':
        reporter.show_report_types('profile')
        reason = input("  [?] Enter reason: ").strip()
    s, m = reporter.report_profile(target, reason)
    print(f"\n  {'[✓]' if s else '[✗]'} Result: {m}")
```

---

## 🚀 Performance Optimization

### **Delay/Rate Limiting (লাইন 375-383)**

```python
for idx, target in enumerate(targets, 1):
    # ... reporting code ...
    
    if idx < len(targets):
        wait = random.uniform(delay * 0.8, delay * 1.2) if randomize else delay
        # Example: delay=5 → wait = 4-6 সেকেন্ড (random)
        print(f"    [-] Waiting {wait:.1f}s...\n")
        time.sleep(wait)
```

**কেন প্রয়োজন?**
- Facebook API এ rate limits আছে
- একসাথে অনেক রিপোর্ট পাঠালে block হতে পারেন
- Random delay আরও realistic দেখায়

---

## 📱 Termux এ সেটআপ (স্টেপ বাই স্টেপ)

### **স্টেপ 1: Basic Setup**
```bash
pkg update && pkg upgrade -y
pkg install python3 git curl -y
```

### **স্টেপ 2: Repository Clone**
```bash
cd $HOME
git clone https://github.com/kawsar660/Facebook-auto-report.git
cd Facebook-auto-report
```

### **স্টেপ 3: Dependencies Install**
```bash
pip install -r requirements.txt
# অথবা
pip install requests
```

### **স্টেপ 4: Test Run**
```bash
python3 fb_reporter.py --list
```

---

## 🔍 সফলতার প্রমাণ

### **Example Output:**

```
==================================================
  [🔥] Starting Multi-Report
  [📌] Targets: 3
  [🎯] Type: profile
  [⚡] Reason: fake_account
==================================================

  [1/3] ➜ Reporting: 123456789
    [✓] SUCCESS - Report ID: report_abc123
    [-] Waiting 5.2s...

  [2/3] ➜ Reporting: 987654321
    [✓] SUCCESS - Report ID: report_def456
    [-] Waiting 4.8s...

  [3/3] ➜ Reporting: 111111111
    [✓] SUCCESS - Report ID: report_ghi789

==================================================
  [✅] COMPLETE! 3/3 Successful
==================================================
```

---

## ⚠️ গুরুত্বপূর্ণ নোট

1. **শুধুমাত্র আইনি ব্যবহার করুন** - এই টুল শুধু সত্যিকারের ক্ষতিকর কন্টেন্ট রিপোর্ট করতে ব্যবহার করুন
2. **Token সুরক্ষিত রাখুন** - কখনও অন্যের সাথে শেয়ার করবেন না
3. **Rate Limit মেনে চলুন** - খুব দ্রুত অনেক রিপোর্ট পাঠাবেন না
4. **Facebook ToS মেনে চলুন** - Facebook এর শর্তাবলী মেনে চলুন

---

## 🎓 শিখার সুবিধা

এই প্রজেক্ট থেকে আপনি শিখতে পারেন:
- Python API Integration
- REST API কীভাবে কাজ করে
- Error Handling এবং Exception Management
- File Processing এবং Batch Operations
- Command Line Arguments Parsing
- Interactive User Interfaces
- Rate Limiting এবং Performance Optimization

---

**Happy Reporting! 🔥**
