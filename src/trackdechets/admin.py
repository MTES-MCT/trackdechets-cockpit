from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.html import format_html

from .forms import (
    AnonymousCompanyForm,
    ApplicationForm,
    BsdasriForm,
    CompanyForm,
    UserForm,
)
from .models import (
    Anonymouscompany,
    Application,
    Bsdasri,
    Company,
    Companyassociation,
    User,
)


@admin.register(Anonymouscompany)
class AnonymouscompanyAdmin(admin.ModelAdmin):
    list_display = [
        "siret",
        "name",
        "id",
    ]
    search_fields = ["siret", "name"]
    form = AnonymousCompanyForm


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "createdat"]
    form = ApplicationForm


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "siret",
        "name",
        "verificationstatus",
        "verificationmode",
        "createdat",
        "id",
        "view_members",
    ]
    form = CompanyForm
    search_fields = ["siret", "name", "id"]
    list_filter = ["verificationstatus", "createdat"]

    def view_members(self, obj):
        url = reverse("admin:company_members", args=[obj.pk])
        return format_html(f'<a href="{url}">View</a>')

    view_members.short_description = "Members"

    def get_urls(self):
        urls = super(CompanyAdmin, self).get_urls()

        members_url = [
            path("members/<str:company_id>/", self.members_view, name="company_members")
        ]

        return members_url + urls

    def members_view(self, request, company_id):
        company = Company.objects.get(id=company_id)

        associations = Companyassociation.objects.filter(
            companyid=company.id
        ).select_related("userid")

        context = dict(
            self.admin_site.each_context(request),
            company=company,
            associations=associations,
        )
        return TemplateResponse(request, "trackdechets/members.html", context)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ["isactive", "createdat", "activatedat"]
    search_fields = ["email", "name", "id"]
    list_display = [
        "email",
        "name",
        "isactive",
        "createdat",
        "isadmin",
        "id",
        "view_companies",
    ]
    readonly_fields = ["id", "isadmin", "password"]
    form = UserForm

    def view_companies(self, obj):
        url = reverse("admin:user_companies", args=[obj.pk])
        return format_html(f'<a href="{url}">View</a>')

    view_companies.short_description = "Companies"

    def get_urls(self):
        urls = super(UserAdmin, self).get_urls()

        members_url = [
            path(
                "companies/<str:user_id>/",
                self.user_companies_views,
                name="user_companies",
            )
        ]

        return members_url + urls

    def user_companies_views(self, request, user_id):
        user = User.objects.get(id=user_id)

        associations = Companyassociation.objects.filter(userid=user_id).select_related(
            "companyid"
        )

        context = dict(
            self.admin_site.each_context(request), user=user, associations=associations
        )
        return TemplateResponse(request, "trackdechets/user_companies.html", context)


@admin.register(Bsdasri)
class BsdasriAdmin(admin.ModelAdmin):
    list_filter = ["status", "isdraft", "type"]
    search_fields = [
        "id",
        "emittercompanysiret",
        "transportercompanysiret",
        "destinationcompanysiret",
    ]
    list_display = [
        "id",
        "status",
        "emittercompanysiret",
        "transportercompanysiret",
        "destinationcompanysiret",
        "type",
    ]
    form = BsdasriForm
    raw_id_fields = ("emissionsignatoryid", "groupedinid")
