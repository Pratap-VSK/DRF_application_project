from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    Comments = CommentSerializer(many=True, read_only = True)
    class meta:
        model = Blog
        fields = '__all__'
