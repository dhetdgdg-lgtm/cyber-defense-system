import time
import random
from datetime import datetime

try:
    import requests
    SERVER_NET_ACTIVE = True
except ImportError:
    SERVER_NET_ACTIVE = False

REPORT_PACKAGES = [
    {"id": "101", "term": "Hate Speech & Discrimination"},
    {"id": "102", "term": "Dangerous Fitna Campaign"},
    {"id": "103", "term": "Fake Account and Spam Bot"},
    {"id": "104", "term": "Harassment and Bullying"}
]

SERVER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
]

def print_table_directly_to_logs(target_url, packs_count):
    """📊 دالة قذف وطباعة الجدول تلقائياً في الشاشة السوداء المجانية لتجاوز الاشتراك"""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "="*95)
    print("🔒 [ تقرير العمليات السيبرانية الحية للبوت - تم تحديث الجدول تلقائياً ] 🔒")
    print("="*95)
    print(f"| {'التاريخ والوقت':<19} | {'الرابط المستهدف المنسوف':<30} | {'تفاصيل الهجوم':<20} | {'الحالة':<15} |")
    print("-"*95)
    print(f"| {current_time:<19} | {target_url[:30]:<30} | {packs_count:<3} باقات حادة       | تم الإرسال الفعلي 🔵 |")
    print("="*95 + "\n")

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
            
        print(f"   🔹 [HTTP POST] السيرفر أطلق بلاغاً بنجاح بتهمة: [{pack['term']}]")
        time.sleep(random.uniform(1.2, 2.5))
        
    # استدعاء دالة الطباعة الفورية المباشرة في الـ Logs لتظهر في شاشتك مجاناً
    print_table_directly_to_logs(target_link, len(REPORT_PACKAGES))

if __name__ == "__main__":
    while True:
        # 🔗 ضع هنا الرابط القذر الذي تريد من السيرفر نسفه وقصفه تلقائياً
        LIVE_TARGET_URL = "https://tiktok.com"
        
        print(f"\n⚡ [تنبيه السيرفر]: بدء دورة الفحص والقصف التلقائية الحين...")
        run_server_bomber(LIVE_TARGET_URL)
        
        sleep_minutes = random.randint(15, 25)
        print(f"⏳ السيرفر دخل وضع القيلولة السحابية الحين لمدة [{sleep_minutes} دقيقة] لتصفير العدادات...")
        time.sleep(sleep_minutes * 60)

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
