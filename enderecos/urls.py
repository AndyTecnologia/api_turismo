from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Ponto Turistico",
        default_version='v1',
        description="Test description",
        terms_of_service="https://andy-api.herokuapp.com/policies/terms/",
        contact=openapi.Contact(email="andersonfs.2608@gmail.com"),
        license=openapi.License(name="testLicense"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [



]
