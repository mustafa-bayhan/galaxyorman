from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

CHOICES2 = (
    ('completed', 'completed'),
    ('draft', 'draft'),
)

aylar = {
    '1': 'Ocak',
    '2': 'Şubat',
    '3': 'Mart',
    '4': 'Nisan',
    '5': 'Mayıs',
    '6': 'Haziran',
    '7': 'Temmuz',
    '8': 'Ağustos',
    '9': 'Eylül',
    '10': 'Ekim',
    '11': 'Kasım',
    '12': 'Aralık'
}





class Reference(models.Model):
    
    reference_name = models.CharField(max_length=100, null= True, blank=False, verbose_name = 'Reference Name')
    reference_image = models.ImageField(null=True, upload_to='image/references/', verbose_name = 'Reference Image')
    
    def __str__(self):
        return self.reference_name
    
    
    
    
class News_Category(models.Model):
    
    name = models.CharField(max_length=100, null= True, blank=False, verbose_name = 'Category Name')
    
    def __str__(self):
        return self.name
    
    
class News (models.Model):
    title=models.CharField(null= True, max_length=200)
    image = models.ImageField(null=True, upload_to='image/')
    category = models.ForeignKey(News_Category, on_delete= models.PROTECT, related_name='Category',null= True)
    publishing_date =models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    completed=models.CharField(choices=CHOICES2,default='completed',max_length=200)
    author=models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, null= True, blank=False,
    )
    summary=models.CharField(null= True, max_length=500)
    content=RichTextField(null= True)
    slug = models.SlugField(editable=False, unique=True, null= True, blank=False)
    date = models.CharField( editable=False, max_length=200, default = aylar[str(datetime.now().month)] + ' ' + str(datetime.now().year))
    date_for_news = models.CharField( editable=False, max_length=200, default = str(datetime.now().day)+ ' ' +aylar[str(datetime.now().month)] + ' ' + str(datetime.now().year))
    def get_unique_slug(self):
        if not self.pk:
            slug = slugify(self.title.replace('ı', 'i'))
            unique_slug = slug
        
            counter = 1
            while News.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(slug, counter)
                counter += 1
        
        else:
            unique_slug=self.slug
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(News, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_single', kwargs={"slug":self.slug})




class Connection(models.Model):
    
    Name = models.CharField(max_length=200,null= True, blank=False)
    Subject = models.CharField(max_length=200,null= True, blank=False)
    Content = models.TextField(max_length=2500, verbose_name='Content',null= True, blank=False)
    mail= models.EmailField(max_length=100, null= True, blank=False)
    tel = models.CharField(max_length=12, verbose_name='telefon',null= True, blank=False)
    

    def __str__(self):
        return 'Name:      ' + self.Name + '           Subject:        ' + self.Subject
    
    
    
class About(models.Model):
    
    about_image = models.ImageField(null=True, upload_to='image/')
    about_text = RichTextField(null= True)
    detail_image = models.ImageField(null=True, upload_to='image/')
    detail_text_1 = models.CharField(max_length=700,null= True, blank=False)
    detail_text_2 = models.CharField(max_length=700,null= True, blank=False)
    detail_text_3 = models.CharField(max_length=700,null= True, blank=False)
    detail_text_4 = models.CharField(max_length=700,null= True, blank=False)
    

    def __str__(self):
        return "About content"
    
    
    
    
class Team_Member(models.Model):
    
    image = models.ImageField(null=True, upload_to='image/')
    name = models.CharField(max_length=100, null= True, blank=False, verbose_name = 'Member Name')
    position = models.CharField(max_length=100, null= True, blank=False, verbose_name = 'Member Position')
    facebook_link = models.CharField(max_length=150, null= True, blank=True)
    instagram_link = models.CharField(max_length=150, null= True, blank=True)
    twitter_link = models.CharField(max_length=150, null= True, blank=True)
   
    

    def __str__(self):
        return self.name + ' - ' +  self.position
    
    
    
class Product(models.Model):
    
    image = models.ImageField(null=True, upload_to='image/products/')
    name = models.CharField(max_length=100, null= True, blank=False)
    amount = models.CharField(max_length=100, null= True, blank=False)
    price = models.PositiveIntegerField(null= True, blank=False)
    description = RichTextField(null= True)
    category = models.CharField(max_length=100, null= True, blank=False, default = "Nargile kömürü")
    slug = models.SlugField(editable=False, unique=True, null= True, blank=False)
    publishing_date =models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    
    def get_unique_slug(self):
        if not self.pk:
            slug = slugify(self.name.replace('ı', 'i'))
            unique_slug = slug
        
            counter = 1
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(slug, counter)
                counter += 1
        
        else:
            unique_slug=self.slug
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Product, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('single-product', kwargs={"slug":self.slug})

    def __str__(self):
        return self.name
    
    
    
class Comments(models.Model):
    post = models.ForeignKey(News, on_delete= models.CASCADE, related_name='comments',null= True)
    name = models.CharField(max_length=100, verbose_name='Name - Surname',null= True)
    email = models.CharField(max_length=150, verbose_name='Email',null= True)
    content = models.TextField(max_length=500, verbose_name='Comment',null= True)
    publishing_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True, null= True )
    date_for_news = models.CharField( editable=False, max_length=200, default = str(datetime.now().day)+ '.' + str(datetime.now().month) + '.' + str(datetime.now().year))
  
    def __str__(self):
        return self.name

    class Meta:
        ordering  = ['-publishing_date', 'id']
    
    
    
    
    
    
class Cover_image(models.Model):
    image1 = models.ImageField(null=True, upload_to='image/cover/')
    image2 = models.ImageField(null=True, upload_to='image/cover/')
    image3 = models.ImageField(null=True, upload_to='image/cover/')
    
    def __str__(self):
        return 'Cover Images'

    
    
class Discount_Product(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='Product',null= True)
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],null= True)
    due_date = models.DateTimeField(auto_now_add=False, null= True )
    def __str__(self):
        return self.product.name + '  -  %' + str(self.discount)
    
    
    
class Bulk_Order_Product(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='The_Product',null= True)
    
    def __str__(self):
        return 'Bulk Order Product'

    
       