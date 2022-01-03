# Generated by Django 4.0 on 2022-01-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accesstoken",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("createdat", models.DateTimeField(db_column="createdAt")),
                ("updatedat", models.DateTimeField(db_column="updatedAt")),
                ("token", models.TextField(unique=True)),
                ("isrevoked", models.BooleanField(db_column="isRevoked")),
                (
                    "lastused",
                    models.DateTimeField(blank=True, db_column="lastUsed", null=True),
                ),
            ],
            options={
                "db_table": "AccessToken",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Anonymouscompany",
            fields=[
                ("id", models.TextField(primary_key=True, serialize=False)),
                ("siret", models.TextField(unique=True)),
                ("name", models.TextField()),
                ("address", models.TextField()),
                ("codenaf", models.TextField(db_column="codeNaf")),
                ("libellenaf", models.TextField(db_column="libelleNaf")),
                ("codecommune", models.TextField(db_column="codeCommune")),
            ],
            options={
                "db_table": "AnonymousCompany",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("createdat", models.DateTimeField(db_column="createdAt")),
                ("updatedat", models.DateTimeField(db_column="updatedAt")),
                ("clientsecret", models.TextField(db_column="clientSecret")),
                ("name", models.TextField()),
                (
                    "logourl",
                    models.TextField(blank=True, db_column="logoUrl", null=True),
                ),
                (
                    "redirecturis",
                    models.TextField(blank=True, db_column="redirectUris", null=True),
                ),
            ],
            options={
                "db_table": "Application",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Brokerreceipt",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("receiptnumber", models.TextField(db_column="receiptNumber")),
                ("validitylimit", models.DateTimeField(db_column="validityLimit")),
                ("department", models.TextField()),
            ],
            options={
                "db_table": "BrokerReceipt",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Bsdasri",
            fields=[
                ("id", models.TextField(primary_key=True, serialize=False)),
                ("status", models.TextField()),
                ("createdat", models.DateTimeField(db_column="createdAt")),
                ("updatedat", models.DateTimeField(db_column="updatedAt")),
                (
                    "isdeleted",
                    models.BooleanField(blank=True, db_column="isDeleted", null=True),
                ),
                (
                    "isdraft",
                    models.BooleanField(blank=True, db_column="isDraft", null=True),
                ),
                (
                    "emittercompanyname",
                    models.TextField(
                        blank=True, db_column="emitterCompanyName", null=True
                    ),
                ),
                (
                    "emittercompanysiret",
                    models.TextField(
                        blank=True, db_column="emitterCompanySiret", null=True
                    ),
                ),
                (
                    "emittercompanyaddress",
                    models.TextField(
                        blank=True, db_column="emitterCompanyAddress", null=True
                    ),
                ),
                (
                    "emittercompanycontact",
                    models.TextField(
                        blank=True, db_column="emitterCompanyContact", null=True
                    ),
                ),
                (
                    "emittercompanyphone",
                    models.TextField(
                        blank=True, db_column="emitterCompanyPhone", null=True
                    ),
                ),
                (
                    "emittercompanymail",
                    models.TextField(
                        blank=True, db_column="emitterCompanyMail", null=True
                    ),
                ),
                (
                    "emitterpickupsitename",
                    models.TextField(
                        blank=True, db_column="emitterPickupSiteName", null=True
                    ),
                ),
                (
                    "emitterpickupsiteaddress",
                    models.TextField(
                        blank=True, db_column="emitterPickupSiteAddress", null=True
                    ),
                ),
                (
                    "emitterpickupsitecity",
                    models.TextField(
                        blank=True, db_column="emitterPickupSiteCity", null=True
                    ),
                ),
                (
                    "emitterpickupsitepostalcode",
                    models.TextField(
                        blank=True, db_column="emitterPickupSitePostalCode", null=True
                    ),
                ),
                (
                    "emitterpickupsiteinfos",
                    models.TextField(
                        blank=True, db_column="emitterPickupSiteInfos", null=True
                    ),
                ),
                (
                    "wastecode",
                    models.TextField(blank=True, db_column="wasteCode", null=True),
                ),
                (
                    "wasteadr",
                    models.TextField(blank=True, db_column="wasteAdr", null=True),
                ),
                (
                    "emitterwasteweightvalue",
                    models.DecimalField(
                        blank=True,
                        db_column="emitterWasteWeightValue",
                        decimal_places=30,
                        max_digits=65,
                        null=True,
                    ),
                ),
                (
                    "emitterwastevolume",
                    models.IntegerField(
                        blank=True, db_column="emitterWasteVolume", null=True
                    ),
                ),
                (
                    "emitterwastepackagings",
                    models.JSONField(db_column="emitterWastePackagings"),
                ),
                (
                    "emittercustominfo",
                    models.TextField(
                        blank=True, db_column="emitterCustomInfo", null=True
                    ),
                ),
                (
                    "emitteremissionsignatureauthor",
                    models.TextField(
                        blank=True,
                        db_column="emitterEmissionSignatureAuthor",
                        null=True,
                    ),
                ),
                (
                    "emitteremissionsignaturedate",
                    models.DateTimeField(
                        blank=True, db_column="emitterEmissionSignatureDate", null=True
                    ),
                ),
                (
                    "isemissiondirecttakenover",
                    models.BooleanField(
                        blank=True, db_column="isEmissionDirectTakenOver", null=True
                    ),
                ),
                (
                    "isemissiontakenoverwithsecretcode",
                    models.BooleanField(
                        blank=True,
                        db_column="isEmissionTakenOverWithSecretCode",
                        null=True,
                    ),
                ),
                (
                    "transportercompanyname",
                    models.TextField(
                        blank=True, db_column="transporterCompanyName", null=True
                    ),
                ),
                (
                    "transportercompanysiret",
                    models.TextField(
                        blank=True, db_column="transporterCompanySiret", null=True
                    ),
                ),
                (
                    "transportercompanyaddress",
                    models.TextField(
                        blank=True, db_column="transporterCompanyAddress", null=True
                    ),
                ),
                (
                    "transportercompanyphone",
                    models.TextField(
                        blank=True, db_column="transporterCompanyPhone", null=True
                    ),
                ),
                (
                    "transportercompanycontact",
                    models.TextField(
                        blank=True, db_column="transporterCompanyContact", null=True
                    ),
                ),
                (
                    "transportercompanymail",
                    models.TextField(
                        blank=True, db_column="transporterCompanyMail", null=True
                    ),
                ),
                (
                    "transporterrecepissenumber",
                    models.TextField(
                        blank=True, db_column="transporterRecepisseNumber", null=True
                    ),
                ),
                (
                    "transporterrecepissedepartment",
                    models.TextField(
                        blank=True,
                        db_column="transporterRecepisseDepartment",
                        null=True,
                    ),
                ),
                (
                    "transporterrecepissevaliditylimit",
                    models.DateTimeField(
                        blank=True,
                        db_column="transporterRecepisseValidityLimit",
                        null=True,
                    ),
                ),
                (
                    "transporteracceptationstatus",
                    models.TextField(
                        blank=True, db_column="transporterAcceptationStatus", null=True
                    ),
                ),
                (
                    "transporterwasterefusalreason",
                    models.TextField(
                        blank=True, db_column="transporterWasteRefusalReason", null=True
                    ),
                ),
                (
                    "transporterwasterefusedweightvalue",
                    models.DecimalField(
                        blank=True,
                        db_column="transporterWasteRefusedWeightValue",
                        decimal_places=30,
                        max_digits=65,
                        null=True,
                    ),
                ),
                (
                    "transportertakenoverat",
                    models.DateTimeField(
                        blank=True, db_column="transporterTakenOverAt", null=True
                    ),
                ),
                (
                    "transporterwastepackagings",
                    models.JSONField(db_column="transporterWastePackagings"),
                ),
                (
                    "transporterwasteweightvalue",
                    models.DecimalField(
                        blank=True,
                        db_column="transporterWasteWeightValue",
                        decimal_places=30,
                        max_digits=65,
                        null=True,
                    ),
                ),
                (
                    "transporterwastevolume",
                    models.IntegerField(
                        blank=True, db_column="transporterWasteVolume", null=True
                    ),
                ),
                (
                    "transportercustominfo",
                    models.TextField(
                        blank=True, db_column="transporterCustomInfo", null=True
                    ),
                ),
                (
                    "handedovertorecipientat",
                    models.DateTimeField(
                        blank=True, db_column="handedOverToRecipientAt", null=True
                    ),
                ),
                (
                    "transportertransportsignatureauthor",
                    models.TextField(
                        blank=True,
                        db_column="transporterTransportSignatureAuthor",
                        null=True,
                    ),
                ),
                (
                    "transportertransportsignaturedate",
                    models.DateTimeField(
                        blank=True,
                        db_column="transporterTransportSignatureDate",
                        null=True,
                    ),
                ),
                (
                    "destinationcompanyname",
                    models.TextField(
                        blank=True, db_column="destinationCompanyName", null=True
                    ),
                ),
                (
                    "destinationcompanysiret",
                    models.TextField(
                        blank=True, db_column="destinationCompanySiret", null=True
                    ),
                ),
                (
                    "destinationcompanyaddress",
                    models.TextField(
                        blank=True, db_column="destinationCompanyAddress", null=True
                    ),
                ),
                (
                    "destinationcompanycontact",
                    models.TextField(
                        blank=True, db_column="destinationCompanyContact", null=True
                    ),
                ),
                (
                    "destinationcompanyphone",
                    models.TextField(
                        blank=True, db_column="destinationCompanyPhone", null=True
                    ),
                ),
                (
                    "destinationcompanymail",
                    models.TextField(
                        blank=True, db_column="destinationCompanyMail", null=True
                    ),
                ),
                (
                    "destinationwastepackagings",
                    models.JSONField(db_column="destinationWastePackagings"),
                ),
                (
                    "destinationreceptionacceptationstatus",
                    models.TextField(
                        blank=True,
                        db_column="destinationReceptionAcceptationStatus",
                        null=True,
                    ),
                ),
                (
                    "destinationreceptionwasterefusalreason",
                    models.TextField(
                        blank=True,
                        db_column="destinationReceptionWasteRefusalReason",
                        null=True,
                    ),
                ),
                (
                    "destinationreceptionwasterefusedweightvalue",
                    models.DecimalField(
                        blank=True,
                        db_column="destinationReceptionWasteRefusedWeightValue",
                        decimal_places=30,
                        max_digits=65,
                        null=True,
                    ),
                ),
                (
                    "destinationreceptionwasteweightvalue",
                    models.DecimalField(
                        blank=True,
                        db_column="destinationReceptionWasteWeightValue",
                        decimal_places=30,
                        max_digits=65,
                        null=True,
                    ),
                ),
                (
                    "destinationreceptionwastevolume",
                    models.IntegerField(
                        blank=True,
                        db_column="destinationReceptionWasteVolume",
                        null=True,
                    ),
                ),
                (
                    "destinationcustominfo",
                    models.TextField(
                        blank=True, db_column="destinationCustomInfo", null=True
                    ),
                ),
                (
                    "destinationreceptiondate",
                    models.DateTimeField(
                        blank=True, db_column="destinationReceptionDate", null=True
                    ),
                ),
                (
                    "destinationoperationcode",
                    models.TextField(
                        blank=True, db_column="destinationOperationCode", null=True
                    ),
                ),
                (
                    "destinationoperationdate",
                    models.DateTimeField(
                        blank=True, db_column="destinationOperationDate", null=True
                    ),
                ),
                (
                    "destinationreceptionsignatureauthor",
                    models.TextField(
                        blank=True,
                        db_column="destinationReceptionSignatureAuthor",
                        null=True,
                    ),
                ),
                (
                    "destinationreceptionsignaturedate",
                    models.DateTimeField(
                        blank=True,
                        db_column="destinationReceptionSignatureDate",
                        null=True,
                    ),
                ),
                (
                    "destinationoperationsignaturedate",
                    models.DateTimeField(
                        blank=True,
                        db_column="destinationOperationSignatureDate",
                        null=True,
                    ),
                ),
                (
                    "destinationoperationsignatureauthor",
                    models.TextField(
                        blank=True,
                        db_column="destinationOperationSignatureAuthor",
                        null=True,
                    ),
                ),
                (
                    "transportertransportmode",
                    models.TextField(db_column="transporterTransportMode"),
                ),
                ("type", models.TextField()),
                (
                    "emitterwasteweightisestimate",
                    models.BooleanField(
                        blank=True, db_column="emitterWasteWeightIsEstimate", null=True
                    ),
                ),
                (
                    "transporterwasteweightisestimate",
                    models.BooleanField(
                        blank=True,
                        db_column="transporterWasteWeightIsEstimate",
                        null=True,
                    ),
                ),
                (
                    "ecoorganismename",
                    models.TextField(
                        blank=True, db_column="ecoOrganismeName", null=True
                    ),
                ),
                (
                    "ecoorganismesiret",
                    models.TextField(
                        blank=True, db_column="ecoOrganismeSiret", null=True
                    ),
                ),
                (
                    "transportertransportplates",
                    models.TextField(
                        blank=True, db_column="transporterTransportPlates", null=True
                    ),
                ),
                (
                    "identificationnumbers",
                    models.TextField(
                        blank=True, db_column="identificationNumbers", null=True
                    ),
                ),
            ],
            options={
                "db_table": "Bsdasri",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("siret", models.TextField(unique=True)),
                ("updatedat", models.DateTimeField(db_column="updatedAt")),
                ("createdat", models.DateTimeField(db_column="createdAt")),
                ("securitycode", models.IntegerField(db_column="securityCode")),
                ("name", models.TextField(blank=True, null=True)),
                (
                    "gerepid",
                    models.TextField(blank=True, db_column="gerepId", null=True),
                ),
                (
                    "codenaf",
                    models.TextField(blank=True, db_column="codeNaf", null=True),
                ),
                (
                    "contactemail",
                    models.TextField(blank=True, db_column="contactEmail", null=True),
                ),
                (
                    "contactphone",
                    models.TextField(blank=True, db_column="contactPhone", null=True),
                ),
                ("website", models.TextField(blank=True, null=True)),
                (
                    "givenname",
                    models.TextField(blank=True, db_column="givenName", null=True),
                ),
                (
                    "ecoorganismeagreements",
                    models.TextField(
                        blank=True, db_column="ecoOrganismeAgreements", null=True
                    ),
                ),
                (
                    "companytypes",
                    models.TextField(blank=True, db_column="companyTypes", null=True),
                ),
                ("address", models.TextField(blank=True, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("verificationcode", models.TextField(db_column="verificationCode")),
                (
                    "verificationstatus",
                    models.TextField(db_column="verificationStatus"),
                ),
                (
                    "verificationmode",
                    models.TextField(
                        blank=True, db_column="verificationMode", null=True
                    ),
                ),
                (
                    "verificationcomment",
                    models.TextField(
                        blank=True, db_column="verificationComment", null=True
                    ),
                ),
                (
                    "verifiedat",
                    models.DateTimeField(blank=True, db_column="verifiedAt", null=True),
                ),
                (
                    "allowbsdasritakeoverwithoutsignature",
                    models.BooleanField(
                        blank=True,
                        db_column="allowBsdasriTakeOverWithoutSignature",
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "Company",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Companyassociation",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("role", models.TextField()),
            ],
            options={
                "db_table": "CompanyAssociation",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Traderreceipt",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("receiptnumber", models.TextField(db_column="receiptNumber")),
                ("validitylimit", models.DateTimeField(db_column="validityLimit")),
                ("department", models.TextField()),
            ],
            options={
                "db_table": "TraderReceipt",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Transporterreceipt",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("receiptnumber", models.TextField(db_column="receiptNumber")),
                ("validitylimit", models.DateTimeField(db_column="validityLimit")),
                ("department", models.TextField()),
            ],
            options={
                "db_table": "TransporterReceipt",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("email", models.TextField(unique=True)),
                ("password", models.TextField()),
                ("name", models.TextField(blank=True, null=True)),
                ("phone", models.TextField(blank=True, null=True)),
                ("createdat", models.DateTimeField(db_column="createdAt")),
                ("updatedat", models.DateTimeField(db_column="updatedAt")),
                (
                    "isactive",
                    models.BooleanField(blank=True, db_column="isActive", null=True),
                ),
                (
                    "applicationid",
                    models.CharField(
                        blank=True, db_column="applicationId", max_length=30, null=True
                    ),
                ),
                (
                    "activatedat",
                    models.DateTimeField(
                        blank=True, db_column="activatedAt", null=True
                    ),
                ),
                (
                    "firstassociationdate",
                    models.DateTimeField(
                        blank=True, db_column="firstAssociationDate", null=True
                    ),
                ),
                ("isadmin", models.BooleanField(db_column="isAdmin")),
            ],
            options={
                "db_table": "User",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Useraccounthash",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("email", models.TextField()),
                (
                    "companysiret",
                    models.CharField(db_column="companySiret", max_length=25),
                ),
                ("hash", models.TextField(unique=True)),
                ("updatedat", models.DateTimeField(db_column="updatedAt")),
                ("createdat", models.DateTimeField(db_column="createdAt")),
                ("role", models.TextField()),
                (
                    "acceptedat",
                    models.DateTimeField(blank=True, db_column="acceptedAt", null=True),
                ),
            ],
            options={
                "db_table": "UserAccountHash",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Useractivationhash",
            fields=[
                (
                    "id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("hash", models.TextField(unique=True)),
                ("updatedat", models.DateTimeField(db_column="updatedAt")),
                ("createdat", models.DateTimeField(db_column="createdAt")),
                ("userid", models.CharField(db_column="userId", max_length=30)),
            ],
            options={
                "db_table": "UserActivationHash",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Vhuagrement",
            fields=[
                (
                    "id",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                (
                    "agrementnumber",
                    models.CharField(db_column="agrementNumber", max_length=50),
                ),
                ("department", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "VhuAgrement",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CompanyProxy",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("trackdechets.company",),
        ),
    ]