from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserAccount

class CustomUserAdmin(BaseUserAdmin):
    model = UserAccount
    list_display = ('id', 'email', 'username', 'phone', 'is_active', 'created_at' , 'is_staff', 'last_login')
    list_display_links = ('email',)
    list_filter = ('is_active',)
    search_fields = ('email', 'username', 'phone')
    ordering = ('id',)

    readonly_fields = ('created_at', 'updated_at', 'last_login')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions')}),
        ('Timestamps', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(UserAccount, CustomUserAdmin)
