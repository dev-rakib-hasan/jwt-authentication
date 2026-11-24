from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

def generate_unique_slug(instance, value):
    base_slug = slugify(value)
    
    if not base_slug:
        base_slug = instance._meta.model_name
    slug = base_slug
    counter = 1
    
    queryset = instance.__class__.objects.all()
    
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)
        
    while queryset.filter(slug=slug).exists():
        slug = f'{base_slug}-{counter}'
        counter+=1
        
    return slug


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
class Blog(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=155)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)
   
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title