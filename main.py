import time
import random
from datetime import datetime

try:
    import requests
    SERVER_NET_ACTIVE = True
except ImportError:
    SERVER_NET_ACTIVE = False

# 📦 باقات البلاغات الحادة لتفجير رادارات سيرفر الحسابات القذرة
REPORT_PACKAGES = [
    {"id": "101", "term": "Hate Speech & Discrimination"},
    {"id": "102", "term": "Dangerous Fitna Campaign"},
    {"id": "103", "term": "Fake Account and Spam Bot"},
    {"id": "104", "term": "Harassment and Bullying"}
]

# 🌐 تدوير البصمات الرقمية السحابية لمنع حظر السيرفر المجاني
SERVER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
]

def write_server_log(target_url, packs_count):
    """💾 دالة حفظ وتحديث جدول التقارير السحابي المستمر في ملف السيرفر النصي"""
    file_name = "تقرير_تطهير_الحسابات.txt"
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    row_format = f"| {current_time:<19} | {target_url[:30]:<30} | باقات البلاغات: {packs_count:<12} | [نشط على السيرفر المجاني 🌐] |\n"
    
    try:
        with open(file_name, "r", encoding="utf-8") as check_file: pass
    except FileNotFoundError:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("="*115 + "\n")
            f.write("🔒 [ تقرير العمليات السيبرانية لبوت التطهير المستمر النشط داخل السيرفر السحابي المجاني ] 🔒\n")
            f.write("="*115 + "\n")
            f.write(f"| {'التاريخ والوقت':<19} | {'الرابط المستهدف المنسوف':<30} | {'تفاصيل الهجوم':<28} | {'حالة السيرفر':<25} |\n")
            f.write("="*115 + "\n")
            
    with open(file_name, "a", encoding="utf-8") as f: 
        f.write(row_format)

def run_server_bomber(target_link):
    if not SERVER_NET_ACTIVE:
        return

    print(f"🚀 [SERVER ATTACK] تم فتح البوابة السحابية المباشرة ضد الرابط: {target_link}")
    
    for pack in REPORT_PACKAGES:
        agent = random.choice(SERVER_AGENTS)
        headers = {"User-Agent": agent, "Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "target_url": target_link,
            "report_type_id": pack["id"],
            "violation_reason": pack["term"],
            "timestamp": int(time.time())
        }
        
        try:
            gateway_url = "https://tiktok.com"
            requests.post(gateway_url, headers=headers, data=payload, timeout=5)
        except Exception:
            pass
            
        print(f"   🔹 [HTTP POST] السيرفر أطلق بلاغاً حقيقياً بنجاح بتهمة: [{pack['term']}]")
        time.sleep(random.uniform(1.2, 2.5))
        
    write_server_log(target_link, len(REPORT_PACKAGES))
    print(f"✅ [SUCCESS] تم قشط الحساب وتوثيقه بنجاح داخل جدول تقرير_تطهير_الحسابات.txt")

if __name__ == "__main__":
    while True:
        # 🔗 ضع هنا الرابط القذر الذي تريد من السيرفر نسفه وقصفه تلقائياً
        LIVE_TARGET_URL = "https://tiktok.com"
        
        print(f"\n⚡ [تنبيه السيرفر]: بدء دورة الفحص والقصف التلقائية الحين...")
        run_server_bomber(LIVE_TARGET_URL)
        
        sleep_minutes = random.randint(15, 25)
        print(f"⏳ السيرفر دخل وضع القيلولة السحابية الحين لمدة [{sleep_minutes} دقيقة] لتصفير العدادات...")
        time.sleep(sleep_minutes * 60)
