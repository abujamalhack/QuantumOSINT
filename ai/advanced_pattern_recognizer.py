#!/usr/bin/env python3
"""
متعرف الأنماط المتقدم
Advanced Pattern Recognizer
"""

import torch
import transformers
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import re
from typing import Dict, List, Any
import logging

class AdvancedPatternRecognizer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_deep_learning_models()
    
    def setup_deep_learning_models(self):
        """تهيئة نماذج التعلم العميق"""
        self.logger.info("🧠 تحميل نماذج التعلم العميق...")
        
        try:
            # نموذج تحليل المشاعر
            self.sentiment_analyzer = transformers.pipeline(
                "sentiment-analysis",
                model="cardiffnlp/twitter-roberta-base-sentiment-latest"
            )
            
            # نموذج التعرف على الكيانات المسماة
            self.ner_analyzer = transformers.pipeline(
                "ner",
                model="dslim/bert-base-NER",
                aggregation_strategy="simple"
            )
            
            self.logger.info("✅ تم تحميل النماذج بنجاح")
            
        except Exception as e:
            self.logger.error(f"❌ فشل تحميل النماذج: {e}")
    
    async def analyze_text_patterns(self, text_data: str) -> Dict[str, Any]:
        """تحليل أنماط النص"""
        analysis_results = {}
        
        try:
            # تحليل متعدد الأبعاد
            analyses = [
                self.semantic_analysis(text_data),
                self.entity_recognition(text_data),
                self.sentiment_analysis(text_data),
                self.behavioral_pattern_analysis(text_data)
            ]
            
            # تنفيذ التحليلات
            for analysis in analyses:
                analysis_results.update(analysis)
            
            self.logger.info("✅ اكتمل تحليل الأنماط")
            
        except Exception as e:
            self.logger.error(f"❌ فشل تحليل الأنماط: {e}")
            
        return analysis_results
    
    def semantic_analysis(self, text: str) -> Dict[str, Any]:
        """التحليل الدلالي"""
        semantic_insights = {}
        
        try:
            # استخدام النموذج للتحليل الدلالي
            if len(text) > 512:
                text = text[:512]  # تقليل النص للنموذج
            
            sentiment_result = self.sentiment_analyzer(text)
            semantic_insights['sentiment'] = sentiment_result[0]
            
            # تحليل الموضوعات
            topics = self.extract_topics(text)
            semantic_insights['topics'] = topics
            
        except Exception as e:
            self.logger.warning(f"التحليل الدلالي فشل: {e}")
            
        return semantic_insights
    
    def entity_recognition(self, text: str) -> Dict[str, Any]:
        """التعرف على الكيانات"""
        entities_data = {}
        
        try:
            # التعرف على الكيانات المسماة
            ner_results = self.ner_analyzer(text)
            
            entities_data['named_entities'] = {
                'persons': [ent for ent in ner_results if ent['entity_group'] == 'PER'],
                'organizations': [ent for ent in ner_results if ent['entity_group'] == 'ORG'],
                'locations': [ent for ent in ner_results if ent['entity_group'] == 'LOC'],
                'misc': [ent for ent in ner_results if ent['entity_group'] == 'MISC']
            }
            
            # استخراج جهات الاتصال
            entities_data['potential_contacts'] = self.extract_contacts_from_entities(ner_results)
            
        except Exception as e:
            self.logger.warning(f"التعرف على الكيانات فشل: {e}")
            
        return entities_data
    
    def extract_contacts_from_entities(self, entities: List[Dict]) -> Dict[str, List[str]]:
        """استخراج جهات الاتصال من الكيانات"""
        contacts = {
            'emails': [],
            'phones': [],
            'social_media': []
        }
        
        try:
            for entity in entities:
                entity_word = entity['word']
                
                # التحقق من الإيميلات
                if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', entity_word):
                    contacts['emails'].append(entity_word)
                
                # التحقق من الهواتف
                elif re.match(r'^\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$', entity_word):
                    contacts['phones'].append(entity_word)
                
                # التحقق من وسائل التواصل
                elif any(platform in entity_word.lower() for platform in ['facebook', 'twitter', 'instagram', 'linkedin']):
                    contacts['social_media'].append(entity_word)
                    
        except Exception as e:
            self.logger.warning(f"استخراج الجهات من الكيانات فشل: {e}")
            
        return contacts
    
    def extract_topics(self, text: str) -> List[str]:
        """استخراج الموضوعات من النص"""
        topics = []
        
        try:
            # كلمات مفتاحية شائعة
            keywords = {
                'technology': ['computer', 'software', 'programming', 'tech'],
                'business': ['company', 'work', 'job', 'business'],
                'education': ['school', 'university', 'study', 'learn'],
                'personal': ['family', 'friend', 'home', 'life']
            }
            
            text_lower = text.lower()
            for topic, words in keywords.items():
                if any(word in text_lower for word in words):
                    topics.append(topic)
            
        except Exception as e:
            self.logger.warning(f"استخراج الموضوعات فشل: {e}")
            
        return topics
