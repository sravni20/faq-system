from django.db import models
from django.core.cache import cache
from django_ckeditor_5.fields import CKEditor5Field
from translate import Translator

class FAQ(models.Model):
    # Base fields
    question = models.TextField()
    answer = CKEditor5Field()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Translation fields
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = CKEditor5Field(blank=True, null=True)
    answer_bn = CKEditor5Field(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question[:50]

    def get_translated_field(self, field_name, lang):
        """Get translated text with caching support"""
        if lang == 'en':
            return getattr(self, field_name)
            
        translated_field = f'{field_name}_{lang}'
        if hasattr(self, translated_field):
            translated_text = getattr(self, translated_field)
            if translated_text:
                return translated_text

        try:
            translator = Translator(to_lang=lang)
            original_text = getattr(self, field_name)
            translated_text = translator.translate(original_text)
            
            # Store the translation
            setattr(self, translated_field, translated_text)
            self.save(update_fields=[translated_field])
            
            return translated_text
        except Exception as e:
            # Fallback to original text if translation fails
            return getattr(self, field_name)

    def save(self, *args, **kwargs):
        """Override save to auto-translate on creation"""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            self.translate_all_fields()

    def translate_all_fields(self):
        """Translate all fields to supported languages"""
        try:
            supported_langs = ['hi', 'bn']
            fields_to_translate = ['question', 'answer']
            
            for lang in supported_langs:
                for field in fields_to_translate:
                    self.get_translated_field(field, lang)
        except Exception as e:
            # Log the error but don't stop the save process
            print(f"Translation error: {str(e)}")
