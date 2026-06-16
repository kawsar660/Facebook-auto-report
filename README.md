# 🔥 Facebook Auto Reporter - EMON KHAN

একটি শক্তিশালী Python টুল যা Facebook-এ স্বয়ংক্রিয়ভাবে রিপোর্ট পাঠাতে পারে।

---

## 📋 ফিচার সমূহ

✅ Profile রিপোর্ট করুন  
✅ Post রিপোর্ট করুন  
✅ Page রিপোর্ট করুন  
✅ Comment রিপোর্ট করুন  
✅ একাধিক টার্গেট একসাথে রিপোর্ট করুন (Batch)  
✅ রিপোর্ট হিস্টরি দেখুন  
✅ ইন্টারেক্টিভ মেনু  

---

## 🚀 Redmi/Android-এ ইনস্টলেশন গাইড

### ধাপ ১: Termux ইনস্টল করুন

1. Google Play Store থেকে **Termux** ডাউনলোড করুন
2. অ্যাপটি খুলুন এবং permission দিন

### ধাপ ২: প্যাকেজ আপডেট করুন

```bash
pkg update
pkg upgrade
```

**Yes বলে এন্টার করুন যখন জিজ্ঞাসা করা হয়**

### ধাপ ৩: Python ইনস্টল করুন

```bash
pkg install python3
```

### ধাপ ৪: Git ইনস্টল করুন (অপশনাল কিন্তু সুপারিশকৃত)

```bash
pkg install git
```

### ধাপ ৫: রেপোজিটরি ক্লোন করুন

```bash
git clone https://github.com/kawsar660/Facebook-auto-report.git
cd Facebook-auto-report
```

**অথবা** ম্যানুয়াল ডাউনলোড:
- রেপোজিটরি থেকে সব ফাইল ডাউনলোড করুন
- Termux-এ যান এবং ফাইল রাখুন

### ধাপ ৬: Python প্যাকেজ ইনস্টল করুন

```bash
pip install -r requirements.txt
```

**অথবা সরাসরি:**
```bash
pip install requests
```

---

## 💻 ব্যবহার পদ্ধতি

### ইন্টারেক্টিভ মোড (সহজ)

```bash
python3 fb_reporter.py
```

অথবা:

```bash
python3 fb_reporter.py -i
```

এই কমান্ড একটি সুন্দর মেনু দেখাবে যেখানে আপনি সবকিছু করতে পারবেন।

---

### কমান্ড লাইন মোড (Advanced)

#### একটি Profile রিপোর্ট করুন:
```bash
python3 fb_reporter.py --profile <PROFILE_ID> --reason abuse --token <YOUR_TOKEN>
```

#### একটি Post রিপোর্ট করুন:
```bash
python3 fb_reporter.py --post <POST_URL> --reason spam --token <YOUR_TOKEN>
```

#### একটি Page রিপোর্ট করুন:
```bash
python3 fb_reporter.py --page <PAGE_ID> --reason scam --token <YOUR_TOKEN>
```

#### একটি Comment রিপোর্ট করুন:
```bash
python3 fb_reporter.py --comment <COMMENT_ID> --reason harassment --token <YOUR_TOKEN>
```

#### Batch রিপোর্ট (ফাইল থেকে):
```bash
python3 fb_reporter.py --batch targets.txt --type profile --reason abuse --delay 5 --token <YOUR_TOKEN>
```

#### রিপোর্ট রিজন লিস্ট দেখুন:
```bash
python3 fb_reporter.py --list
```

#### রিপোর্ট হিস্টরি দেখুন:
```bash
python3 fb_reporter.py --history --token <YOUR_TOKEN>
```

---

## 🔑 Facebook Access Token কীভাবে পাবেন?

1. Facebook Developers সাইটে যান: https://developers.facebook.com
2. একটি নতুন অ্যাপ তৈরি করুন
3. Graph API Explorer ব্যবহার করে Token জেনারেট করুন
4. অথবা আপনার ব্রাউজার কনসোল থেকে নিন

### সহজ পদ্ধতি (Browser Console):
```javascript
// Chrome/Firefox Developer Tools > Console
document.cookie.split(';').forEach(c => console.log(c))
// এখান থেকে access_token খুঁজে বের করুন
```

---

## 📝 Batch রিপোর্ট ফাইল তৈরি করুন

`targets.txt` ফাইল তৈরি করুন এবং এতে IDs/URLs রাখুন:

```
# Profile IDs (Profile টাইপের জন্য)
123456789
987654321
111111111

# অথবা URLs (Post টাইপের জন্য)
https://www.facebook.com/photo.php?fbid=123&set=a.456
https://www.facebook.com/photo.php?fbid=789&set=a.012
```

তারপর চালান:
```bash
python3 fb_reporter.py --batch targets.txt --type profile --reason abuse --delay 5 --token <YOUR_TOKEN>
```

---

## 📊 রিপোর্ট রিজন কোডস

### Profile Report রিজন:
1. General Abuse
2. Fake Account
3. Hate Speech
4. Violence/Threats
5. Harassment
6. Spam
7. Nudity
8. Terrorism
9. Suicide/Self-harm
10. Scam/Fraud
11. Impersonation
12. IP Violation

### Post Report রিজন:
1. Nudity
2. Hate Speech
3. Violence
4. Harassment
5. Fake News
6. Spam
7. Copyright
8. Scam

### Page Report রিজন:
1. Scam
2. Fake Page
3. Hate Speech
4. Violence
5. Impersonation
6. Spam

### Comment Report রিজন:
1. Harassment
2. Hate Speech
3. Violence
4. Spam
5. Bullying

---

## ⚙️ Environment Variable সেট করুন (Optional)

Access Token বার্বার দেওয়ার বদলে Environment Variable সেট করতে পারেন:

```bash
export FB_ACCESS_TOKEN="your_token_here"
```

তারপর টোকেন ছাড়াই চালান:
```bash
python3 fb_reporter.py -i
```

---

## 🛠️ ট্রাবলশুটিং

### সমস্যা: "requests module not found"
**সমাধান:**
```bash
pip install requests
```

### সমস্যা: "Permission denied"
**সমাধান:**
```bash
chmod +x fb_reporter.py
```

### সমস্যা: Token অবৈধ
- নিশ্চিত করুন টোকেন সঠিক এবং expired না হয়েছে
- নতুন টোকেন জেনারেট করুন
- টোকেন এ কোট মার্ক ছাড়াই পাস করুন

### সমস্যা: "Connection timeout"
- ডিভাইসের ইন্টারনেট চেক করুন
- Delay বাড়িয়ে দেখুন (`--delay 10`)
- VPN ব্যবহার করে দেখুন

---

## 📱 Redmi-তে দ্রুত অ্যাক্সেসের জন্য Shortcut তৈরি করুন

1. Termux-এ যান
2. কাজের ডাইরেক্টরিতে যান:
```bash
cd Facebook-auto-report
```

3. একটি শর্টকাট স্ক্রিপ্ট তৈরি করুন:
```bash
cat > run.sh << 'EOF'
#!/bin/bash
cd ~/Facebook-auto-report
python3 fb_reporter.py -i
EOF
```

4. এক্সিকিউটেবল করুন:
```bash
chmod +x run.sh
```

5. চালান:
```bash
./run.sh
```

---

## ⚠️ দায়িত্বের সাথে ব্যবহার করুন

এই টুলটি শুধুমাত্র আইনি এবং নৈতিক উদ্দেশ্যে ব্যবহার করুন। Facebook-এর Terms of Service মেনে চলুন।

---

## 👤 তৈরি করেছেন
- **EMON KHAN**
- **THE CYBER SECURITY FORCE**

---

## 📄 লাইসেন্স

এই প্রজেক্টটি শিক্ষামূলক উদ্দেশ্যে তৈরি।

---

## 🤝 সাহায্য এবং সমর্থন

কোন সমস্যা হলে GitHub Issues-এ রিপোর্ট করুন।

**Happy Reporting! 🔥**
