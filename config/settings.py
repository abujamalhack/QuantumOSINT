#!/usr/bin/env python3
"""
إعدادات النظام
System Settings
"""

import os
from typing import Dict, Any

class Settings:
    """فئة الإعدادات"""
    
    # إعدادات النظام
    APP_NAME = "نظام OSINT المتقدم"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # إعدادات الأمان
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "your-encryption-key-here")
    
    # إعدادات قاعدة البيانات
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./osint.db")
    
    # إعدادات API
    MAX_CONCURRENT_REQUESTS = int(os.getenv("MAX_CONCURRENT_REQUESTS", "50"))
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))
    
    # إعدادات المنصات
    PLATFORMS = {
        'facebook': {
            'enabled': True,
            'depth': 'deep',
            'rate_limit': 10
        },
        'instagram': {
            'enabled': True,
            'depth': 'deep',
            'rate_limit': 10
        },
        'twitter': {
            'enabled': True,
            'depth': 'extreme',
            'rate_limit': 15
        }
    }
    
    # إعدادات التحليل
    ANALYSIS = {
        'network_analysis': True,
        'behavioral_analysis': True,
        'temporal_analysis': True,
        'threat_analysis': True
    }
    
    @classmethod
    def get_all_settings(cls) -> Dict[str, Any]:
        """الحصول على جميع الإعدادات"""
        return {
            key: value for key, value in cls.__dict__.items() 
            if not key.startswith('_') and not callable(value)
        }

# إنشاء كائن الإعدادات
settings = Settings()
