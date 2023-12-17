from django_filters import rest_framework as filters
from box.models import Box
class BoxFilter(filters.FilterSet):
    length_more_than = filters.NumberFilter(field_name="length", lookup_expr="gt")
    length_less_than = filters.NumberFilter(field_name="length", lookup_expr="lt")

    breadth_more_than = filters.NumberFilter(field_name="breadth", lookup_expr="gt")
    breadth_less_than = filters.NumberFilter(field_name="breadth", lookup_expr="lt")

    height_more_than = filters.NumberFilter(field_name="height", lookup_expr="gt")
    height_less_than = filters.NumberFilter(field_name="height", lookup_expr="lt")

    area_more_than = filters.NumberFilter(field_name="area", lookup_expr="gt")
    area_less_than = filters.NumberFilter(field_name="area", lookup_expr="lt")

    volume_more_than = filters.NumberFilter(field_name="volume", lookup_expr="gt")
    volume_less_than = filters.NumberFilter(field_name="volume", lookup_expr="lt")

    class Meta:
        model = Box
        fields = [
            "length_more_than",
            "length_less_than",
            "breadth_more_than",
            "breadth_less_than",
            "height_more_than",
            "height_less_than",
            "area_more_than",
            "area_less_than",
            "volume_more_than",
            "volume_less_than",
        ]


class BoxUsernameDateFilter(filters.FilterSet):

    length_more_than = filters.NumberFilter(field_name="length", lookup_expr="gt")
    length_less_than = filters.NumberFilter(field_name="length", lookup_expr="lt")

    breadth_more_than = filters.NumberFilter(field_name="breadth", lookup_expr="gt")
    breadth_less_than = filters.NumberFilter(field_name="breadth", lookup_expr="lt")

    height_more_than = filters.NumberFilter(field_name="height", lookup_expr="gt")
    height_less_than = filters.NumberFilter(field_name="height", lookup_expr="lt")

    area_more_than = filters.NumberFilter(field_name="area", lookup_expr="gt")
    area_less_than = filters.NumberFilter(field_name="area", lookup_expr="lt")

    volume_more_than = filters.NumberFilter(field_name="volume", lookup_expr="gt")
    volume_less_than = filters.NumberFilter(field_name="volume", lookup_expr="lt")

    created_after = filters.DateFilter(field_name="date_created", lookup_expr="gt")
    created_before = filters.DateFilter(field_name="date_created", lookup_expr="lt")

    username = filters.CharFilter(
        field_name="creator__username", lookup_expr="icontains"
    )

    class Meta:
        model = Box
        fields = [
            "length_more_than",
            "length_less_than",
            "breadth_more_than",
            "breadth_less_than",
            "height_more_than",
            "height_less_than",
            "area_more_than",
            "area_less_than",
            "volume_more_than",
            "volume_less_than",
            "created_after",
            "created_before",
            "username",
        ]
