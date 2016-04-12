import datetime
from haystack import indexes
from shoppersapp.models import ScraperItem

class ScraperItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    category = indexes.CharField(model_attr='category')
    price = indexes.CharField(model_attr='price')

    def get_model(self):
        return ScraperItem

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
