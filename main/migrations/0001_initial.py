# Generated by Django 3.0.7 on 2020-07-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField(default='2020-06-02')),
                ('weight', models.IntegerField(default='50')),
                ('height_feet', models.IntegerField(blank=True, default=0, null=True)),
                ('height_inches', models.IntegerField(blank=True, default=0, null=True)),
                ('waist', models.IntegerField(default='28')),
                ('hip', models.IntegerField(default='30')),
                ('purpose', models.CharField(choices=[('GW', 'I want to know why I might have gained weight'), ('FR', 'I am more concerned about future risks from this weight gain '), ('BC', 'Want to prepare my body for conception'), ('PR', 'Need to get my prescription renewed'), ('SO', 'Need to get a second opinion'), ('PC', 'Follow up for previous consultation'), ('other', 'Other')], default='None', max_length=100)),
                ('have_baby', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='n', max_length=100)),
                ('hyperprolactinemia', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('pcos_pcod', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('hypothyroidism', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('other', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('hyperprolactinemia_days', models.IntegerField(blank=True, default=0, null=True)),
                ('pcos_pcod_days', models.IntegerField(blank=True, default=0, null=True)),
                ('hypothyroidism_days', models.IntegerField(blank=True, default=0, null=True)),
                ('other_days', models.IntegerField(blank=True, default=0, null=True)),
                ('symptoms7', models.CharField(default='none', max_length=100)),
                ('month8', models.CharField(choices=[('JAN', 'JAN'), ('FEB', 'FEB'), ('MAR', 'MAR'), ('APR', 'APR'), ('MAY', 'MAY'), ('JUN', 'JUN'), ('JUL', 'JUL'), ('AUG', 'AUG'), ('SEP', 'SEP'), ('OCT', 'OCT'), ('NOV', 'NOV'), ('DEC', 'DEC')], default='JAN', max_length=100)),
                ('year8', models.CharField(choices=[('2019', '2019'), ('2020', '2020')], default='2019', max_length=100)),
                ('weight9', models.IntegerField(blank=True, default=None, null=True)),
                ('time9', models.IntegerField(blank=True, default=None, null=True)),
                ('time9_d', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('stoppedPeriods', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('lessThanSixCycles', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('moreThanSixCycles', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('countinuosFlow', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('lastPeriodTimeMonth', models.CharField(choices=[('JAN', 'JAN'), ('FEB', 'FEB'), ('MAR', 'MAR'), ('APR', 'APR'), ('MAY', 'MAY'), ('JUN', 'JUN'), ('JUL', 'JUL'), ('AUG', 'AUG'), ('SEP', 'SEP'), ('OCT', 'OCT'), ('NOV', 'NOV'), ('DEC', 'DEC')], default='JAN', max_length=100)),
                ('lastPeriodTimeYear', models.CharField(choices=[('2019', '2019'), ('2020', '2020')], default='2019', max_length=100)),
                ('currentlyNotUnderAnyMedication', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('diabestes', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('migrane', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('medicationHighBloodPressure', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('medicationMentalHealthDisorder', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('steroidTherapy', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('hormonalContraception', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('seizure', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('proteinSupplements', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('Opioids', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('antiHistamines', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('currentlyNotUnderAnyMedicationDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('diabestesDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('migraneDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('medicationHighBloodPressureDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('medicationMentalHealthDisorderDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('steroidTherapyDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('hormonalContraceptionDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('seizureDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('proteinSupplementsDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('OpioidsDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('antiHistaminesDuration', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('currentlyNotUnderAnyMedicationDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('diabestesDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('migraneDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('medicationHighBloodPressureDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('medicationMentalHealthDisorderDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('steroidTherapyDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('hormonalContraceptionDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('seizureDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('proteinSupplementsDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('OpioidsDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('antiHistaminesDurationType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('medicalAllergies', models.CharField(blank=True, default='none', max_length=100, null=True)),
                ('undergoneSurgery', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('physicallyImmobile', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('viralFever', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('workoutValue', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='n', max_length=100)),
                ('eatFoodValue', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='n', max_length=100)),
                ('sleepValue', models.CharField(blank=True, default='none', max_length=100, null=True)),
                ('sleepValueType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('highBloodPressure', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('highCholesterol', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('familyHypothyroidism', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('diabetes', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('pcos', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('reportFirst', models.FileField(default='none', upload_to='')),
                ('reportSecond', models.FileField(default='none', upload_to='')),
                ('otherExtraDetailForDoctor', models.CharField(blank=True, default='none', max_length=100, null=True)),
                ('nutritionExpert', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('yogaTherapist', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('dermatologist', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('psychiatrist', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('hairLoss', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('hairLossRange', models.IntegerField(blank=True, default=None, null=True)),
                ('hairLossTime', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('hairLossTimeType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('acneLoss', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('acneLossRange', models.IntegerField(blank=True, default=None, null=True)),
                ('acneLossTime', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('acneLossTimeType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('missedPeriod', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('missedPeriodTime', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('missedPeriodTimeType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('extraHair', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('extraHairRange', models.IntegerField(blank=True, default=None, null=True)),
                ('extraHairTime', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('extraHairTimeType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('constipation', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('skinPigmentation', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('slowHeartbeat', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('headache', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('headacheRange', models.IntegerField(blank=True, default=None, null=True)),
                ('headacheTime', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('headacheTimeType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
                ('dischargeNipple', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('moodSwings', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('others', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('othersRange', models.IntegerField(blank=True, default=None, null=True)),
                ('othersTime', models.CharField(blank=True, default='false', max_length=100, null=True)),
                ('othersTimeType', models.CharField(choices=[('d', 'days'), ('m', 'months'), ('y', 'years')], default='m', max_length=100)),
            ],
        ),
    ]
