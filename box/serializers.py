import datetime
from rest_framework import serializers
from django.db.models import Avg
from box.models import Box
from django.conf import settings

class BoxSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")
    last_updated = serializers.ReadOnlyField()

    class Meta:
        model = Box
        fields = (
            "id",
            "creator",
            "length",
            "breadth",
            "height",
            "area",
            "volume",
            "last_updated",
        )
        read_only_fields = (
            "area",
            "volume",
            "last_updated",
        )
        extra_kwargs = {
            "height": {"required": True},
            "breadth": {"required": True},
            "length": {"required": True},
        }

    def create(self, attr):
        if attr["length"] <= 0:
            raise serializers.ValidationError({"length": "Length must be greater than 0"})
        if attr["breadth"] <= 0:
            raise serializers.ValidationError({"breadth": "Breadth must be greater than 0"})
        if attr["height"] <= 0:
            raise serializers.ValidationError({"height": "Height must be greater than 0"})

        # condition 1
        avg_area = Box.objects.all().aggregate(Avg("area"))
        avg_area["average_area"] = 0 if avg_area is None else avg_area["average_area"]

        current_area = 2 * (
            attr["length"] * attr["breadth"]
            + attr["breadth"] * attr["height"]
            + attr["height"] * attr["length"]
        )
        avg_area["average_area"] = (avg_area["average_area"] + current_area) / 2
        if avg_area["average_area"] > settings.A1:
            raise serializers.ValidationError(
                {
                    "area_error": "Provided dimensions exceed the average area limit, try with smaller dimensions"
                }
            )

        # condition 2
        request = self.context.get("request", None)
        if request:
            avg_volume = Box.objects.filter(creator=request.user).aggregate(Avg("volume"))
            avg_volume["average_volume"] = 0 if avg_volume is None else avg_volume["average_volume"]
            current_volume = attr["length"] * attr["breadth"] * attr["height"]
            avg_volume["average_volume"] = (avg_volume["average_volume"] + current_volume) / 2
            if avg_volume["average_volume"] > settings.V1:
                raise serializers.ValidationError(
                    {
                        "Volume_error": "Provided dimensions exceed the average volume limit, try with smaller dimensions"
                    }
                )

        # condition 3
        past_week = datetime.date.today() - datetime.timedelta(days=7)
        total_boxes_last_week = Box.objects.filter(
            date_created__range=(past_week, datetime.datetime.now())
        ).count()
        if total_boxes_last_week >= settings.L1:
            raise serializers.ValidationError(
                {"error": "The total boxes added in the last 7 days exceed the limit"}
            )

        # condition 4
        total_boxes_last_week_user = Box.objects.filter(
            creator=request.user, date_created__range=(past_week, datetime.datetime.now())
        ).count()
        if total_boxes_last_week_user >= settings.L1:
            raise serializers.ValidationError(
                {"error": "The total boxes added by the user in the last 7 days exceed the limit"}
            )

        return super(BoxSerializer, self).create(attr)

    def update(self, instance, validated_data):
        if len(validated_data) == 0:
            raise serializers.ValidationError({"invalid_data": "Invalid data provided. Try again"})

        if validated_data.get("height", instance.height) <= 0:
            raise serializers.ValidationError({"height": "Height must be greater than 0."})
        if validated_data.get("length", instance.length) <= 0:
            raise serializers.ValidationError({"length": "Length must be greater than 0."})
        if validated_data.get("breadth", instance.breadth) <= 0:
            raise serializers.ValidationError({"breadth": "Breadth must be greater than 0."})

        return super(BoxSerializer, self).update(instance, validated_data)

    def __init__(self, *args, **kwargs):
        context = kwargs.get("context", None)
        user_is_staff = context.get("user_is_staff", None)
        if user_is_staff is not None:
            if not user_is_staff:
                remove_fields = ["last_updated", "creator"]
                for field_name in remove_fields:
                    self.fields.pop(field_name)
        super(BoxSerializer, self).__init__(*args, **kwargs)
