from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super(UserEditForm, self).__init__(*args, **kwargs)
            self.fields['username'].disabled = True
            self.fields['id'].disabled = True
            self.fields['created_datetime'].disabled = True