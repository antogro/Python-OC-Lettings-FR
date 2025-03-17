from django.db import migrations


def migrate_lettings(apps, schema_editor):
    OldAddress = apps.get_model("lettings", "Address")
    # OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("lettings", "Letting")
    # OldLetting = apps.get_model("oc_lettings_site", "Letting")
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

    for old_letting in OldLetting.objects.all():
        NewLetting.objects.create(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address.id,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(migrate_lettings),
    ]
