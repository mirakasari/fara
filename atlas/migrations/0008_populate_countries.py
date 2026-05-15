from django.db import migrations


def forwards(apps, schema_editor):
    Atlas = apps.get_model('atlas', 'Atlas')
    Country = apps.get_model('atlas', 'Country')

    # create Country rows for each distinct existing country string
    countries = set(Atlas.objects.values_list('country', flat=True))
    created = {}
    for name in countries:
        if name is None or name == '':
            continue
        obj, _ = Country.objects.get_or_create(name=name, defaults={'slug': name.replace(' ', '-').lower()})
        created[name] = obj

    # assign country_obj FK on Atlas rows
    for atlas in Atlas.objects.all():
        name = atlas.country
        if name in created:
            atlas.country_obj = created[name]
            atlas.save(update_fields=['country_obj'])


def backwards(apps, schema_editor):
    Atlas = apps.get_model('atlas', 'Atlas')
    # simply unset country_obj
    for atlas in Atlas.objects.all():
        atlas.country_obj = None
        atlas.save(update_fields=['country_obj'])


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0007_country_atlas_country_obj'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
