from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description', ]

# class BookSerializer(serializers.Serializer):
#     bid = serializers.IntegerField()
#     title = serializers.CharField(max_length=50)
#     author = serializers.CharField(max_length=50)
#     category = serializers.CharField(max_length=50)
#     pages = serializers.IntegerField()
#     price = serializers.IntegerField()
#     published_date = serializers.DateField()
#     description = serializers.TextField()

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.bid = validated_data.get('bid', instance.bid)
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.category = validated_data.get('category', instance.category)
#         instance.pages = validated_data.get('pages', instance.pages)
#         instance.price = validated_data.get('price', instance.price)
#         instance.published_date = validated_data.get('published_date', instance.published_date)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()

#         return instance
{
    "bid": 1,
    "title": "책",
    "author": "저자",
    "category": "카테고리",
    "pages": "308",
    "price": 20000,
    "published_date": "2021-01-30",
    "description": "인공지능",
}
