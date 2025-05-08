# from django.contrib import admin
# from  .models import Category,Project,Person, FamilyMember, EducationalQualification, WorkExperience, Goal,Gallery,MySetting

# admin.site.register(Category)
# admin.site.register(Project)

# class FamilyMemberInline(admin.TabularInline):
#     model = FamilyMember
#     extra = 1

# class EducationalQualificationInline(admin.TabularInline):
#     model = EducationalQualification
#     extra = 1

# class WorkExperienceInline(admin.TabularInline):
#     model = WorkExperience
#     extra = 1

# class GoalInline(admin.TabularInline):
#     model = Goal
#     extra = 1

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'last_name', 'position', 'is_current_candidate')
#     inlines = [EducationalQualificationInline, WorkExperienceInline, GoalInline,FamilyMemberInline]
    
# admin.site.register(Gallery)
# admin.site.register(MySetting)


from django.contrib import admin
from .models import Category, Project, Person, FamilyMember, EducationalQualification, WorkExperience, Goal, Gallery, MySetting

class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1
    verbose_name = "عضو الأسرة"
    verbose_name_plural = "أعضاء الأسرة"

class EducationalQualificationInline(admin.TabularInline):
    model = EducationalQualification
    extra = 1
    verbose_name = "المؤهل العلمي"
    verbose_name_plural = "المؤهلات العلمية"

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1
    verbose_name = "الخبرة العملية"
    verbose_name_plural = "الخبرات العملية"

class GoalInline(admin.TabularInline):
    model = Goal
    extra = 1
    verbose_name = "الهدف"
    verbose_name_plural = "الأهداف"

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'position', 'is_current_candidate', 'display_categories')
    list_filter = ('target_categories', 'is_current_candidate', 'position')
    filter_horizontal = ('target_categories',)
    search_fields = ('name', 'last_name', 'position')
    inlines = [EducationalQualificationInline, WorkExperienceInline, GoalInline, FamilyMemberInline]
    
    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.target_categories.all()])
    display_categories.short_description = "الفئات المستهدفة"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(MySetting)
class MySettingAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'phone', 'email')