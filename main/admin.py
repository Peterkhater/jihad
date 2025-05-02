from django.contrib import admin
from  .models import Category,Project,Person, FamilyMember, EducationalQualification, WorkExperience, Goal

admin.site.register(Category)
admin.site.register(Project)

class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1

class EducationalQualificationInline(admin.TabularInline):
    model = EducationalQualification
    extra = 1

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1

class GoalInline(admin.TabularInline):
    model = Goal
    extra = 1

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'position', 'is_current_candidate')
    inlines = [EducationalQualificationInline, WorkExperienceInline, GoalInline,FamilyMemberInline]
    # filter_horizontal = ('family_members',)

# @admin.register(FamilyMember)
# class FamilyMemberAdmin(admin.ModelAdmin):
#     list_display = ('name', 'last_name', 'relation', 'occupation')