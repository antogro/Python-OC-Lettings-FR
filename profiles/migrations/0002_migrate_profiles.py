from django.db import migrations


def migrate_profiles(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            user_id=old_profile.user.id,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(migrate_profiles),
    ]
