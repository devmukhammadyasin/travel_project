from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Direction, News


class DirectionTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

translator.register(Direction, DirectionTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

translator.register(News, NewsTranslationOptions)