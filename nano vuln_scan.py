import requests
from bs4 import BeautifulSoup

url = input("أدخل رابط الموقع (مثال: http://example.com): ").strip()

def check_headers():
    print("\n[+] فحص الهيدر...")
    r = requests.get(url)
    headers = r.headers
    if 'X-Frame-Options' not in headers:
        print("[-] X-Frame-Options غير موجود! ممكن عرض الموقع داخل iFrame")
    if 'Content-Security-Policy' not in headers:
        print("[-] Content-Security-Policy مفقود! ممكن ثغرات XSS")
    print("[+] تم فحص الهيدر.")

def xss_test():
    print("\n[+] اختبار XSS...")
    test = "<script>alert(1)</script>"
    test_url = f"{url}?q={test}"
    r = requests.get(test_url)
    if test in r.text:
        print("[!] ممكن وجود XSS في المتغير 'q'")
    else:
        print("[+] لا توجد علامات واضحة لـ XSS.")

def sql_test():
    print("\n[+] اختبار SQL Injection...")
    payload = "' OR '1'='1"
    test_url = f"{url}?id={payload}"
    r = requests.get(test_url)
    errors = ["sql syntax", "mysql", "error in your SQL"]
    if any(e in r.text.lower() for e in errors):
        print("[!] قد يكون الموقع معرض لـ SQL Injection في المتغير 'id'")
    else:
        print("[+] لا توجد علامات واضحة لـ SQLi.")

def dir_scan():
    print("\n[+] فحص الصفحات المخفية...")
    paths = ['admin', 'login', 'uploads', 'config', 'phpmyadmin']
    for path in paths:
        test_url = f"{url}/{path}"
        r = requests.get(test_url)
        if r.status_code == 200:
            print(f"[!] تم العثور على صفحة: {test_url}")

# تشغيل الوظائف
check_headers()
xss_test()
sql_test()
dir_scan()
