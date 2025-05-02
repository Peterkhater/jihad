from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True, verbose_name="وصف الفئة")
    icon = models.CharField(max_length=50, blank=True, help_text="اسم أيقونة Font Awesome")
    
    class Meta:
        verbose_name = "فئة المشروع"
        verbose_name_plural = "فئات المشاريع"
    
    def __str__(self):
        return self.name

class Project(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="عنوان المشروع")
    description = models.TextField(verbose_name="وصف المشروع")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, 
                               null=True, verbose_name="الفئة")
    image = models.ImageField(upload_to='projects/', verbose_name="صورة المشروع")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[self.id])

    class Meta:
        verbose_name = "مشروع"
        verbose_name_plural = "المشاريع"
    
    def __str__(self):
        return self.title
    



    

class Person(models.Model):
    # Existing fields (remain unchanged)
    name = models.CharField(max_length=200, verbose_name="اسم المرشح")
    last_name = models.CharField(max_length=200, verbose_name="شهرة المرشح")
    position = models.CharField(max_length=100, verbose_name="المنصب")
    profile_picture = models.ImageField(upload_to='profiles/', verbose_name="صورة المرشح", blank=True, null=True)
    age = models.PositiveIntegerField(verbose_name="العمر")
    phone = models.CharField(blank=True, null=True,verbose_name="رقم الهاتف",default='+961', max_length=100)
    note = models.TextField(verbose_name="ملاحظات", blank=True)
    election_program = models.TextField(verbose_name="البرنامج الانتخابي", blank=True)
    is_current_candidate = models.BooleanField(verbose_name="مرشح حاليا", default=True)
    vision = models.TextField(verbose_name="الرؤية", blank=True)
    twitter = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse('person', args=[self.id])

    class Meta:
        verbose_name = "مرشح"
        verbose_name_plural = "المرشحين"
        ordering = ['position', 'last_name']
    
    def __str__(self):
        return f"{self.name} {self.last_name}"

class FamilyMember(models.Model): 
    RELATION_CHOICES = [
        ('father', 'أب'),
        ('mother', 'أم'),
        ('spouse', 'زوج/زوجة'),
        ('son', 'ابن'),
        ('daughter', 'ابنة'),
        ('brother', 'أخ'),
        ('sister', 'أخت'),
        ('other', 'أخرى'),
    ]
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='famMember', verbose_name="المرشح")
    name = models.CharField(max_length=200, verbose_name="الاسم")
    last_name = models.CharField(max_length=200, verbose_name="الشهرة")
    age = models.PositiveIntegerField(verbose_name="العمر")  # Changed from IntegerChoices
    relation = models.CharField(
        max_length=15,
        choices=RELATION_CHOICES,
        verbose_name="صلة القرابة",
        default='other'
    )
    occupation = models.CharField(max_length=200, verbose_name="المهنة", blank=True)
    note = models.TextField(verbose_name="ملاحظات", blank=True)

    class Meta:
        verbose_name = "عضو الأسرة"
        verbose_name_plural = " أعضاء أسرة ألمرشح" 
    def __str__(self):
        return f"{self.name} {self.last_name}"

class EducationalQualification(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='qualifications', verbose_name="المرشح")
    title = models.CharField(max_length=200, verbose_name="المؤهل العلمي")
    institution = models.CharField(max_length=200, verbose_name="المؤسسة التعليمية")
    year = models.PositiveIntegerField(verbose_name="سنة الحصول")

    class Meta:
        verbose_name = "المؤهل العلمي"
        verbose_name_plural = "المؤهلات العلمية"

    def __str__(self):
        return f"{self.title} - {self.institution}"

class WorkExperience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='experiences', verbose_name="المرشح")
    position = models.CharField(max_length=200, verbose_name="المنصب")
    organization = models.CharField(max_length=200, verbose_name="المؤسسة")
    start_year = models.PositiveIntegerField(verbose_name="سنة البدء")
    end_year = models.PositiveIntegerField(verbose_name="سنة الانتهاء", null=True, blank=True)

    class Meta:
        verbose_name = "الخبرة العملية"
        verbose_name_plural = "الخبرات العملية"

    def __str__(self):
        return f"{self.position} في {self.organization}"

class Goal(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='goals', verbose_name="المرشح")
    title = models.CharField(max_length=200, verbose_name="الهدف")
    description = models.TextField(verbose_name="تفاصيل الهدف")

    class Meta:
        verbose_name = "الهدف"
        verbose_name_plural = "الأهداف"

    def __str__(self):
        return self.title