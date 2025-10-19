#!/usr/bin/env python3
"""
ملف التشغيل الرئيسي للنظام
Main System Runner
"""

import asyncio
import logging
from core.advanced_engine import QuantumOSINTEngine
from utils.logger import setup_logging

async def main():
    """الدالة الرئيسية"""
    print("🚀 نظام OSINT المتقدم - الإصدار الكمي")
    print("=" * 50)
    
    # إعداد التسجيل
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # تهيئة المحرك
        logger.info("تهيئة نظام OSINT المتقدم...")
        engine = QuantumOSINTEngine()
        
        # أهداف الاختبار
        test_targets = [
            "example_target"
        ]
        
        # تنفيذ المسح
        logger.info("بدء المسح المتقدم...")
        results = await engine.comprehensive_scan(test_targets)
        
        # عرض النتائج
        print("\n🎉 اكتمل المسح بنجاح!")
        print(f"📊 عدد الأهداف: {len(test_targets)}")
        print(f"⏱️  وقت التنفيذ: {engine.operation_start}")
        
        # حفظ النتائج
        await save_results(results)
        
    except Exception as e:
        logger.error(f"فشل التشغيل: {e}")
        return 1
    
    return 0

async def save_results(results):
    """حفظ النتائج"""
    try:
        import json
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"osint_results_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"💾 تم حفظ النتائج في: {filename}")
        
    except Exception as e:
        print(f"❌ فشل حفظ النتائج: {e}")

if __name__ == "__main__":
    # تشغيل النظام
    exit_code = asyncio.run(main())
    exit(exit_code)
