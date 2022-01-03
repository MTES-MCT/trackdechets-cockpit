# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Accesstoken(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.
    token = models.TextField(unique=True)
    isrevoked = models.BooleanField(db_column="isRevoked")  # Field name made lowercase.
    lastused = models.DateTimeField(
        db_column="lastUsed", blank=True, null=True
    )  # Field name made lowercase.
    userid = models.ForeignKey(
        "User", models.DO_NOTHING, db_column="userId"
    )  # Field name made lowercase.
    applicationid = models.ForeignKey(
        "Application",
        models.DO_NOTHING,
        db_column="applicationId",
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AccessToken"


class Anonymouscompany(models.Model):
    id = models.TextField(primary_key=True)
    siret = models.TextField(unique=True)
    name = models.TextField()
    address = models.TextField()
    codenaf = models.TextField(db_column="codeNaf")  # Field name made lowercase.
    libellenaf = models.TextField(db_column="libelleNaf")  # Field name made lowercase.
    codecommune = models.TextField(
        db_column="codeCommune"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "AnonymousCompany"


class Application(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.
    clientsecret = models.TextField(
        db_column="clientSecret"
    )  # Field name made lowercase.
    name = models.TextField()
    logourl = models.TextField(
        db_column="logoUrl", blank=True, null=True
    )  # Field name made lowercase.
    redirecturis = models.TextField(
        db_column="redirectUris", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = "Application"


class Brokerreceipt(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    receiptnumber = models.TextField(
        db_column="receiptNumber"
    )  # Field name made lowercase.
    validitylimit = models.DateTimeField(
        db_column="validityLimit"
    )  # Field name made lowercase.
    department = models.TextField()

    class Meta:
        managed = False
        db_table = "BrokerReceipt"


#
# class Bsda(models.Model):
#     id = models.TextField(primary_key=True)
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     isdraft = models.BooleanField(db_column='isDraft')  # Field name made lowercase.
#     isdeleted = models.BooleanField(db_column='isDeleted')  # Field name made lowercase.
#     status = models.TextField()  # This field type is a guess.
#     type = models.TextField()  # This field type is a guess.
#     emitterisprivateindividual = models.BooleanField(db_column='emitterIsPrivateIndividual', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyname = models.TextField(db_column='emitterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     emittercompanysiret = models.TextField(db_column='emitterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyaddress = models.TextField(db_column='emitterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     emittercompanycontact = models.TextField(db_column='emitterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyphone = models.TextField(db_column='emitterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     emittercompanymail = models.TextField(db_column='emitterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     emitterpickupsitename = models.TextField(db_column='emitterPickupSiteName', blank=True, null=True)  # Field name made lowercase.
#     emitterpickupsiteaddress = models.TextField(db_column='emitterPickupSiteAddress', blank=True, null=True)  # Field name made lowercase.
#     emitterpickupsitecity = models.TextField(db_column='emitterPickupSiteCity', blank=True, null=True)  # Field name made lowercase.
#     emitterpickupsitepostalcode = models.TextField(db_column='emitterPickupSitePostalCode', blank=True, null=True)  # Field name made lowercase.
#     emitterpickupsiteinfos = models.TextField(db_column='emitterPickupSiteInfos', blank=True, null=True)  # Field name made lowercase.
#     emitteremissionsignatureauthor = models.TextField(db_column='emitterEmissionSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     emitteremissionsignaturedate = models.DateTimeField(db_column='emitterEmissionSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     wastecode = models.TextField(db_column='wasteCode', blank=True, null=True)  # Field name made lowercase.
#     wastename = models.TextField(db_column='wasteName', blank=True, null=True)  # Field name made lowercase.
#     wastefamilycode = models.TextField(db_column='wasteFamilyCode', blank=True, null=True)  # Field name made lowercase.
#     wastematerialname = models.TextField(db_column='wasteMaterialName', blank=True, null=True)  # Field name made lowercase.
#     wasteconsistence = models.TextField(db_column='wasteConsistence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     wastesealnumbers = models.TextField(db_column='wasteSealNumbers', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     wasteadr = models.TextField(db_column='wasteAdr', blank=True, null=True)  # Field name made lowercase.
#     packagings = models.JSONField()
#     quantitytype = models.TextField(db_column='quantityType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     weightvalue = models.DecimalField(db_column='weightValue', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyname = models.TextField(db_column='destinationCompanyName', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanysiret = models.TextField(db_column='destinationCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyaddress = models.TextField(db_column='destinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanycontact = models.TextField(db_column='destinationCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyphone = models.TextField(db_column='destinationCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanymail = models.TextField(db_column='destinationCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     destinationcap = models.TextField(db_column='destinationCap', blank=True, null=True)  # Field name made lowercase.
#     destinationplannedoperationcode = models.TextField(db_column='destinationPlannedOperationCode', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptiondate = models.DateTimeField(db_column='destinationReceptionDate', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionweight = models.DecimalField(db_column='destinationReceptionWeight', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionacceptationstatus = models.TextField(db_column='destinationReceptionAcceptationStatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destinationreceptionrefusalreason = models.TextField(db_column='destinationReceptionRefusalReason', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationcode = models.TextField(db_column='destinationOperationCode', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationdate = models.DateTimeField(db_column='destinationOperationDate', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationsignatureauthor = models.TextField(db_column='destinationOperationSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationsignaturedate = models.DateTimeField(db_column='destinationOperationSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyname = models.TextField(db_column='transporterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     transportercompanysiret = models.TextField(db_column='transporterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyaddress = models.TextField(db_column='transporterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     transportercompanycontact = models.TextField(db_column='transporterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyphone = models.TextField(db_column='transporterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     transportercompanymail = models.TextField(db_column='transporterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyvatnumber = models.TextField(db_column='transporterCompanyVatNumber', blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissenumber = models.TextField(db_column='transporterRecepisseNumber', blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissedepartment = models.TextField(db_column='transporterRecepisseDepartment', blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissevaliditylimit = models.DateTimeField(db_column='transporterRecepisseValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     transportertransportsignatureauthor = models.TextField(db_column='transporterTransportSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     transportertransportsignaturedate = models.DateTimeField(db_column='transporterTransportSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     workercompanyname = models.TextField(db_column='workerCompanyName', blank=True, null=True)  # Field name made lowercase.
#     workercompanysiret = models.TextField(db_column='workerCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     workercompanyaddress = models.TextField(db_column='workerCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     workercompanycontact = models.TextField(db_column='workerCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     workercompanyphone = models.TextField(db_column='workerCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     workercompanymail = models.TextField(db_column='workerCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     workerworkhasemitterpapersignature = models.BooleanField(db_column='workerWorkHasEmitterPaperSignature', blank=True, null=True)  # Field name made lowercase.
#     workerworksignatureauthor = models.TextField(db_column='workerWorkSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     workerworksignaturedate = models.DateTimeField(db_column='workerWorkSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     childbsdaid = models.ForeignKey('self', models.DO_NOTHING, db_column='childBsdaId', blank=True, null=True)  # Field name made lowercase.
#     brokercompanyname = models.TextField(db_column='brokerCompanyName', blank=True, null=True)  # Field name made lowercase.
#     brokercompanysiret = models.TextField(db_column='brokerCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     brokercompanyaddress = models.TextField(db_column='brokerCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     brokercompanycontact = models.TextField(db_column='brokerCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     brokercompanyphone = models.TextField(db_column='brokerCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     brokercompanymail = models.TextField(db_column='brokerCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     brokerrecepissenumber = models.TextField(db_column='brokerRecepisseNumber', blank=True, null=True)  # Field name made lowercase.
#     brokerrecepissedepartment = models.TextField(db_column='brokerRecepisseDepartment', blank=True, null=True)  # Field name made lowercase.
#     brokerrecepissevaliditylimit = models.DateTimeField(db_column='brokerRecepisseValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyname = models.TextField(db_column='destinationOperationNextDestinationCompanyName', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanysiret = models.TextField(db_column='destinationOperationNextDestinationCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyvatnumber = models.TextField(db_column='destinationOperationNextDestinationCompanyVatNumber', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyaddress = models.TextField(db_column='destinationOperationNextDestinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanycontact = models.TextField(db_column='destinationOperationNextDestinationCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyphone = models.TextField(db_column='destinationOperationNextDestinationCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanymail = models.TextField(db_column='destinationOperationNextDestinationCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcap = models.TextField(db_column='destinationOperationNextDestinationCap', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationplannedoperationcode = models.TextField(db_column='destinationOperationNextDestinationPlannedOperationCode', blank=True, null=True)  # Field name made lowercase.
#     transporterrecepisseisexempted = models.BooleanField(db_column='transporterRecepisseIsExempted', blank=True, null=True)  # Field name made lowercase.
#     transportertransportmode = models.TextField(db_column='transporterTransportMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     transportertransportplates = models.TextField(db_column='transporterTransportPlates', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     transportertransporttakenoverat = models.DateTimeField(db_column='transporterTransportTakenOverAt', blank=True, null=True)  # Field name made lowercase.
#     weightisestimate = models.BooleanField(db_column='weightIsEstimate', blank=True, null=True)  # Field name made lowercase.
#     emittercustominfo = models.TextField(db_column='emitterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     destinationcustominfo = models.TextField(db_column='destinationCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     transportercustominfo = models.TextField(db_column='transporterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     repackagedinid = models.TextField(db_column='repackagedInId', blank=True, null=True)  # Field name made lowercase.
#     ecoorganismename = models.TextField(db_column='ecoOrganismeName', blank=True, null=True)  # Field name made lowercase.
#     ecoorganismesiret = models.TextField(db_column='ecoOrganismeSiret', blank=True, null=True)  # Field name made lowercase.
#     forwardingid = models.OneToOneField('self', models.DO_NOTHING, db_column='forwardingId', blank=True, null=True)  # Field name made lowercase.
#     groupedinid = models.ForeignKey('self', models.DO_NOTHING, db_column='groupedInId', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Bsda'
#
#


class Bsdasri(models.Model):
    id = models.TextField(primary_key=True)
    status = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.
    isdeleted = models.BooleanField(
        db_column="isDeleted", blank=True, null=True
    )  # Field name made lowercase.
    isdraft = models.BooleanField(
        db_column="isDraft", blank=True, null=True
    )  # Field name made lowercase.
    emittercompanyname = models.TextField(
        db_column="emitterCompanyName", blank=True, null=True
    )  # Field name made lowercase.
    emittercompanysiret = models.TextField(
        db_column="emitterCompanySiret", blank=True, null=True
    )  # Field name made lowercase.
    emittercompanyaddress = models.TextField(
        db_column="emitterCompanyAddress", blank=True, null=True
    )  # Field name made lowercase.
    emittercompanycontact = models.TextField(
        db_column="emitterCompanyContact", blank=True, null=True
    )  # Field name made lowercase.
    emittercompanyphone = models.TextField(
        db_column="emitterCompanyPhone", blank=True, null=True
    )  # Field name made lowercase.
    emittercompanymail = models.TextField(
        db_column="emitterCompanyMail", blank=True, null=True
    )  # Field name made lowercase.
    emitterpickupsitename = models.TextField(
        db_column="emitterPickupSiteName", blank=True, null=True
    )  # Field name made lowercase.
    emitterpickupsiteaddress = models.TextField(
        db_column="emitterPickupSiteAddress", blank=True, null=True
    )  # Field name made lowercase.
    emitterpickupsitecity = models.TextField(
        db_column="emitterPickupSiteCity", blank=True, null=True
    )  # Field name made lowercase.
    emitterpickupsitepostalcode = models.TextField(
        db_column="emitterPickupSitePostalCode", blank=True, null=True
    )  # Field name made lowercase.
    emitterpickupsiteinfos = models.TextField(
        db_column="emitterPickupSiteInfos", blank=True, null=True
    )  # Field name made lowercase.
    wastecode = models.TextField(
        db_column="wasteCode", blank=True, null=True
    )  # Field name made lowercase.
    wasteadr = models.TextField(
        db_column="wasteAdr", blank=True, null=True
    )  # Field name made lowercase.
    emitterwasteweightvalue = models.DecimalField(
        db_column="emitterWasteWeightValue",
        max_digits=65,
        decimal_places=30,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    emitterwastevolume = models.IntegerField(
        db_column="emitterWasteVolume", blank=True, null=True
    )  # Field name made lowercase.
    emitterwastepackagings = models.JSONField(
        db_column="emitterWastePackagings"
    )  # Field name made lowercase.
    emittercustominfo = models.TextField(
        db_column="emitterCustomInfo", blank=True, null=True
    )  # Field name made lowercase.
    emitteremissionsignatureauthor = models.TextField(
        db_column="emitterEmissionSignatureAuthor", blank=True, null=True
    )  # Field name made lowercase.
    emitteremissionsignaturedate = models.DateTimeField(
        db_column="emitterEmissionSignatureDate", blank=True, null=True
    )  # Field name made lowercase.
    isemissiondirecttakenover = models.BooleanField(
        db_column="isEmissionDirectTakenOver", blank=True, null=True
    )  # Field name made lowercase.
    isemissiontakenoverwithsecretcode = models.BooleanField(
        db_column="isEmissionTakenOverWithSecretCode", blank=True, null=True
    )  # Field name made lowercase.
    transportercompanyname = models.TextField(
        db_column="transporterCompanyName", blank=True, null=True
    )  # Field name made lowercase.
    transportercompanysiret = models.TextField(
        db_column="transporterCompanySiret", blank=True, null=True
    )  # Field name made lowercase.
    transportercompanyaddress = models.TextField(
        db_column="transporterCompanyAddress", blank=True, null=True
    )  # Field name made lowercase.
    transportercompanyphone = models.TextField(
        db_column="transporterCompanyPhone", blank=True, null=True
    )  # Field name made lowercase.
    transportercompanycontact = models.TextField(
        db_column="transporterCompanyContact", blank=True, null=True
    )  # Field name made lowercase.
    transportercompanymail = models.TextField(
        db_column="transporterCompanyMail", blank=True, null=True
    )  # Field name made lowercase.
    transporterrecepissenumber = models.TextField(
        db_column="transporterRecepisseNumber", blank=True, null=True
    )  # Field name made lowercase.
    transporterrecepissedepartment = models.TextField(
        db_column="transporterRecepisseDepartment", blank=True, null=True
    )  # Field name made lowercase.
    transporterrecepissevaliditylimit = models.DateTimeField(
        db_column="transporterRecepisseValidityLimit", blank=True, null=True
    )  # Field name made lowercase.
    transporteracceptationstatus = models.TextField(
        db_column="transporterAcceptationStatus", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    transporterwasterefusalreason = models.TextField(
        db_column="transporterWasteRefusalReason", blank=True, null=True
    )  # Field name made lowercase.
    transporterwasterefusedweightvalue = models.DecimalField(
        db_column="transporterWasteRefusedWeightValue",
        max_digits=65,
        decimal_places=30,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    transportertakenoverat = models.DateTimeField(
        db_column="transporterTakenOverAt", blank=True, null=True
    )  # Field name made lowercase.
    transporterwastepackagings = models.JSONField(
        db_column="transporterWastePackagings"
    )  # Field name made lowercase.
    transporterwasteweightvalue = models.DecimalField(
        db_column="transporterWasteWeightValue",
        max_digits=65,
        decimal_places=30,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    transporterwastevolume = models.IntegerField(
        db_column="transporterWasteVolume", blank=True, null=True
    )  # Field name made lowercase.
    transportercustominfo = models.TextField(
        db_column="transporterCustomInfo", blank=True, null=True
    )  # Field name made lowercase.
    handedovertorecipientat = models.DateTimeField(
        db_column="handedOverToRecipientAt", blank=True, null=True
    )  # Field name made lowercase.
    transportertransportsignatureauthor = models.TextField(
        db_column="transporterTransportSignatureAuthor", blank=True, null=True
    )  # Field name made lowercase.
    transportertransportsignaturedate = models.DateTimeField(
        db_column="transporterTransportSignatureDate", blank=True, null=True
    )  # Field name made lowercase.
    destinationcompanyname = models.TextField(
        db_column="destinationCompanyName", blank=True, null=True
    )  # Field name made lowercase.
    destinationcompanysiret = models.TextField(
        db_column="destinationCompanySiret", blank=True, null=True
    )  # Field name made lowercase.
    destinationcompanyaddress = models.TextField(
        db_column="destinationCompanyAddress", blank=True, null=True
    )  # Field name made lowercase.
    destinationcompanycontact = models.TextField(
        db_column="destinationCompanyContact", blank=True, null=True
    )  # Field name made lowercase.
    destinationcompanyphone = models.TextField(
        db_column="destinationCompanyPhone", blank=True, null=True
    )  # Field name made lowercase.
    destinationcompanymail = models.TextField(
        db_column="destinationCompanyMail", blank=True, null=True
    )  # Field name made lowercase.
    destinationwastepackagings = models.JSONField(
        db_column="destinationWastePackagings"
    )  # Field name made lowercase.
    destinationreceptionacceptationstatus = models.TextField(
        db_column="destinationReceptionAcceptationStatus", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    destinationreceptionwasterefusalreason = models.TextField(
        db_column="destinationReceptionWasteRefusalReason", blank=True, null=True
    )  # Field name made lowercase.
    destinationreceptionwasterefusedweightvalue = models.DecimalField(
        db_column="destinationReceptionWasteRefusedWeightValue",
        max_digits=65,
        decimal_places=30,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    destinationreceptionwasteweightvalue = models.DecimalField(
        db_column="destinationReceptionWasteWeightValue",
        max_digits=65,
        decimal_places=30,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    destinationreceptionwastevolume = models.IntegerField(
        db_column="destinationReceptionWasteVolume", blank=True, null=True
    )  # Field name made lowercase.
    destinationcustominfo = models.TextField(
        db_column="destinationCustomInfo", blank=True, null=True
    )  # Field name made lowercase.
    destinationreceptiondate = models.DateTimeField(
        db_column="destinationReceptionDate", blank=True, null=True
    )  # Field name made lowercase.
    destinationoperationcode = models.TextField(
        db_column="destinationOperationCode", blank=True, null=True
    )  # Field name made lowercase.
    destinationoperationdate = models.DateTimeField(
        db_column="destinationOperationDate", blank=True, null=True
    )  # Field name made lowercase.
    destinationreceptionsignatureauthor = models.TextField(
        db_column="destinationReceptionSignatureAuthor", blank=True, null=True
    )  # Field name made lowercase.
    destinationreceptionsignaturedate = models.DateTimeField(
        db_column="destinationReceptionSignatureDate", blank=True, null=True
    )  # Field name made lowercase.
    destinationoperationsignaturedate = models.DateTimeField(
        db_column="destinationOperationSignatureDate", blank=True, null=True
    )  # Field name made lowercase.
    destinationoperationsignatureauthor = models.TextField(
        db_column="destinationOperationSignatureAuthor", blank=True, null=True
    )  # Field name made lowercase.
    emissionsignatoryid = models.ForeignKey(
        "User",
        models.DO_NOTHING,
        db_column="emissionSignatoryId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    # transportsignatoryid = models.ForeignKey('User', models.DO_NOTHING, db_column='transportSignatoryId', blank=True, null=True)  # Field name made lowercase.
    # receptionsignatoryid = models.ForeignKey('User', models.DO_NOTHING, db_column='receptionSignatoryId', blank=True, null=True)  # Field name made lowercase.
    # operationsignatoryid = models.ForeignKey('User', models.DO_NOTHING, db_column='operationSignatoryId', blank=True, null=True)  # Field name made lowercase.
    groupedinid = models.ForeignKey(
        "self", models.DO_NOTHING, db_column="groupedInId", blank=True, null=True
    )  # Field name made lowercase.
    transportertransportmode = models.TextField(
        db_column="transporterTransportMode"
    )  # Field name made lowercase. This field type is a guess.
    type = models.TextField()  # This field type is a guess.
    emitterwasteweightisestimate = models.BooleanField(
        db_column="emitterWasteWeightIsEstimate", blank=True, null=True
    )  # Field name made lowercase.
    transporterwasteweightisestimate = models.BooleanField(
        db_column="transporterWasteWeightIsEstimate", blank=True, null=True
    )  # Field name made lowercase.
    ecoorganismename = models.TextField(
        db_column="ecoOrganismeName", blank=True, null=True
    )  # Field name made lowercase.
    ecoorganismesiret = models.TextField(
        db_column="ecoOrganismeSiret", blank=True, null=True
    )  # Field name made lowercase.

    transportertransportplates = ArrayField(
        models.TextField(),
        db_column="transporterTransportPlates",
        blank=True,
        null=True,
    )  # Field name made lowercase. Manually edited.

    identificationnumbers = ArrayField(
        models.TextField(), db_column="identificationNumbers", blank=True, null=True
    )  # Field name made lowercase. Manually edited.

    class Meta:
        managed = False
        db_table = "Bsdasri"


#
#
# class Bsff(models.Model):
#     id = models.TextField(primary_key=True)
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     isdeleted = models.BooleanField(db_column='isDeleted')  # Field name made lowercase.
#     emittercompanyname = models.TextField(db_column='emitterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     emittercompanysiret = models.TextField(db_column='emitterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyaddress = models.TextField(db_column='emitterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     emittercompanycontact = models.TextField(db_column='emitterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyphone = models.TextField(db_column='emitterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     emittercompanymail = models.TextField(db_column='emitterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     emitteremissionsignatureauthor = models.TextField(db_column='emitterEmissionSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     emitteremissionsignaturedate = models.DateTimeField(db_column='emitterEmissionSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     packagings = models.JSONField()
#     wastecode = models.TextField(db_column='wasteCode', blank=True, null=True)  # Field name made lowercase.
#     wasteadr = models.TextField(db_column='wasteAdr', blank=True, null=True)  # Field name made lowercase.
#     weightvalue = models.DecimalField(db_column='weightValue', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     weightisestimate = models.BooleanField(db_column='weightIsEstimate', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyname = models.TextField(db_column='transporterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     transportercompanysiret = models.TextField(db_column='transporterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyaddress = models.TextField(db_column='transporterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     transportercompanycontact = models.TextField(db_column='transporterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyphone = models.TextField(db_column='transporterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     transportercompanymail = models.TextField(db_column='transporterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissenumber = models.TextField(db_column='transporterRecepisseNumber', blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissedepartment = models.TextField(db_column='transporterRecepisseDepartment', blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissevaliditylimit = models.DateTimeField(db_column='transporterRecepisseValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     transportertransportmode = models.TextField(db_column='transporterTransportMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     transportertransportsignatureauthor = models.TextField(db_column='transporterTransportSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     transportertransportsignaturedate = models.DateTimeField(db_column='transporterTransportSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyname = models.TextField(db_column='destinationCompanyName', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanysiret = models.TextField(db_column='destinationCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyaddress = models.TextField(db_column='destinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanycontact = models.TextField(db_column='destinationCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyphone = models.TextField(db_column='destinationCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanymail = models.TextField(db_column='destinationCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptiondate = models.DateTimeField(db_column='destinationReceptionDate', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionweight = models.DecimalField(db_column='destinationReceptionWeight', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionrefusalreason = models.TextField(db_column='destinationReceptionRefusalReason', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionsignatureauthor = models.TextField(db_column='destinationReceptionSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionsignaturedate = models.DateTimeField(db_column='destinationReceptionSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     destinationplannedoperationcode = models.TextField(db_column='destinationPlannedOperationCode', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationcode = models.TextField(db_column='destinationOperationCode', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationsignatureauthor = models.TextField(db_column='destinationOperationSignatureAuthor', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationsignaturedate = models.DateTimeField(db_column='destinationOperationSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     destinationcap = models.TextField(db_column='destinationCap', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyvatnumber = models.TextField(db_column='transporterCompanyVatNumber', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyname = models.TextField(db_column='destinationOperationNextDestinationCompanyName', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanysiret = models.TextField(db_column='destinationOperationNextDestinationCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyvatnumber = models.TextField(db_column='destinationOperationNextDestinationCompanyVatNumber', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyaddress = models.TextField(db_column='destinationOperationNextDestinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanycontact = models.TextField(db_column='destinationOperationNextDestinationCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyphone = models.TextField(db_column='destinationOperationNextDestinationCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanymail = models.TextField(db_column='destinationOperationNextDestinationCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     status = models.TextField()  # This field type is a guess.
#     wastedescription = models.TextField(db_column='wasteDescription', blank=True, null=True)  # Field name made lowercase.
#     nextbsffid = models.ForeignKey('self', models.DO_NOTHING, db_column='nextBsffId', blank=True, null=True)  # Field name made lowercase.
#     isdraft = models.BooleanField(db_column='isDraft')  # Field name made lowercase.
#     type = models.TextField()  # This field type is a guess.
#     destinationcustominfo = models.TextField(db_column='destinationCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionacceptationstatus = models.TextField(db_column='destinationReceptionAcceptationStatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     emittercustominfo = models.TextField(db_column='emitterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     transportercustominfo = models.TextField(db_column='transporterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     repackagedinid = models.ForeignKey('self', models.DO_NOTHING, db_column='repackagedInId', blank=True, null=True)  # Field name made lowercase.
#     groupedinid = models.ForeignKey('self', models.DO_NOTHING, db_column='groupedInId', blank=True, null=True)  # Field name made lowercase.
#     forwardingid = models.OneToOneField('self', models.DO_NOTHING, db_column='forwardingId', blank=True, null=True)  # Field name made lowercase.
#     transportertransporttakenoverat = models.DateTimeField(db_column='transporterTransportTakenOverAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Bsff'
#
#
# class Bsffficheintervention(models.Model):
#     id = models.TextField(primary_key=True)
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     numero = models.TextField()
#     weight = models.DecimalField(max_digits=65, decimal_places=30)
#     postalcode = models.TextField(db_column='postalCode')  # Field name made lowercase.
#     bsffid = models.TextField(db_column='bsffId', blank=True, null=True)  # Field name made lowercase.
#     detenteurcompanyname = models.TextField(db_column='detenteurCompanyName')  # Field name made lowercase.
#     detenteurcompanysiret = models.TextField(db_column='detenteurCompanySiret')  # Field name made lowercase.
#     detenteurcompanyaddress = models.TextField(db_column='detenteurCompanyAddress')  # Field name made lowercase.
#     detenteurcompanycontact = models.TextField(db_column='detenteurCompanyContact')  # Field name made lowercase.
#     detenteurcompanyphone = models.TextField(db_column='detenteurCompanyPhone')  # Field name made lowercase.
#     detenteurcompanymail = models.TextField(db_column='detenteurCompanyMail')  # Field name made lowercase.
#     operateurcompanyname = models.TextField(db_column='operateurCompanyName')  # Field name made lowercase.
#     operateurcompanysiret = models.TextField(db_column='operateurCompanySiret')  # Field name made lowercase.
#     operateurcompanyaddress = models.TextField(db_column='operateurCompanyAddress')  # Field name made lowercase.
#     operateurcompanycontact = models.TextField(db_column='operateurCompanyContact')  # Field name made lowercase.
#     operateurcompanyphone = models.TextField(db_column='operateurCompanyPhone')  # Field name made lowercase.
#     operateurcompanymail = models.TextField(db_column='operateurCompanyMail')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'BsffFicheIntervention'
#
#
# class Bsvhu(models.Model):
#     id = models.CharField(primary_key=True, max_length=40)
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     isdraft = models.BooleanField(db_column='isDraft')  # Field name made lowercase.
#     isdeleted = models.BooleanField(db_column='isDeleted')  # Field name made lowercase.
#     status = models.TextField()  # This field type is a guess.
#     emitteragrementnumber = models.CharField(db_column='emitterAgrementNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     emittercompanyname = models.CharField(db_column='emitterCompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     emittercompanysiret = models.CharField(db_column='emitterCompanySiret', max_length=17, blank=True, null=True)  # Field name made lowercase.
#     emittercompanyaddress = models.TextField(db_column='emitterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     emittercompanycontact = models.CharField(db_column='emitterCompanyContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     emittercompanyphone = models.CharField(db_column='emitterCompanyPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     emittercompanymail = models.CharField(db_column='emitterCompanyMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     destinationtype = models.TextField(db_column='destinationType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destinationplannedoperationcode = models.CharField(db_column='destinationPlannedOperationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     destinationagrementnumber = models.CharField(db_column='destinationAgrementNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyname = models.CharField(db_column='destinationCompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     destinationcompanysiret = models.CharField(db_column='destinationCompanySiret', max_length=17, blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyaddress = models.TextField(db_column='destinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanycontact = models.CharField(db_column='destinationCompanyContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyphone = models.CharField(db_column='destinationCompanyPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     destinationcompanymail = models.CharField(db_column='destinationCompanyMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     wastecode = models.CharField(db_column='wasteCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     packaging = models.TextField(blank=True, null=True)  # This field type is a guess.
#     identificationnumbers = models.TextField(db_column='identificationNumbers', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     identificationtype = models.TextField(db_column='identificationType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     quantity = models.IntegerField(blank=True, null=True)
#     weightvalue = models.FloatField(db_column='weightValue', blank=True, null=True)  # Field name made lowercase.
#     emitteremissionsignatureauthor = models.CharField(db_column='emitterEmissionSignatureAuthor', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     emitteremissionsignaturedate = models.DateTimeField(db_column='emitterEmissionSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyname = models.CharField(db_column='transporterCompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     transportercompanysiret = models.CharField(db_column='transporterCompanySiret', max_length=17, blank=True, null=True)  # Field name made lowercase.
#     transportercompanyaddress = models.TextField(db_column='transporterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     transportercompanycontact = models.CharField(db_column='transporterCompanyContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     transportercompanyphone = models.CharField(db_column='transporterCompanyPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     transportercompanymail = models.CharField(db_column='transporterCompanyMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissenumber = models.CharField(db_column='transporterRecepisseNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissedepartment = models.CharField(db_column='transporterRecepisseDepartment', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     transporterrecepissevaliditylimit = models.DateTimeField(db_column='transporterRecepisseValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyvatnumber = models.CharField(db_column='transporterCompanyVatNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     transportertransportsignatureauthor = models.CharField(db_column='transporterTransportSignatureAuthor', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     transportertransportsignaturedate = models.DateTimeField(db_column='transporterTransportSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionacceptationstatus = models.TextField(db_column='destinationReceptionAcceptationStatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destinationreceptionrefusalreason = models.TextField(db_column='destinationReceptionRefusalReason', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionidentificationnumbers = models.TextField(db_column='destinationReceptionIdentificationNumbers', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destinationreceptionidentificationtype = models.TextField(db_column='destinationReceptionIdentificationType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destinationoperationcode = models.CharField(db_column='destinationOperationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyname = models.CharField(db_column='destinationOperationNextDestinationCompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanysiret = models.CharField(db_column='destinationOperationNextDestinationCompanySiret', max_length=17, blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyaddress = models.TextField(db_column='destinationOperationNextDestinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanycontact = models.CharField(db_column='destinationOperationNextDestinationCompanyContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyphone = models.CharField(db_column='destinationOperationNextDestinationCompanyPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanymail = models.CharField(db_column='destinationOperationNextDestinationCompanyMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     destinationoperationsignatureauthor = models.CharField(db_column='destinationOperationSignatureAuthor', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     destinationoperationsignaturedate = models.DateTimeField(db_column='destinationOperationSignatureDate', blank=True, null=True)  # Field name made lowercase.
#     transportertransporttakenoverat = models.DateTimeField(db_column='transporterTransportTakenOverAt', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationdate = models.DateTimeField(db_column='destinationOperationDate', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionquantity = models.IntegerField(db_column='destinationReceptionQuantity', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptionweight = models.FloatField(db_column='destinationReceptionWeight', blank=True, null=True)  # Field name made lowercase.
#     destinationreceptiondate = models.DateTimeField(db_column='destinationReceptionDate', blank=True, null=True)  # Field name made lowercase.
#     weightisestimate = models.BooleanField(db_column='weightIsEstimate', blank=True, null=True)  # Field name made lowercase.
#     destinationoperationnextdestinationcompanyvatnumber = models.TextField(db_column='destinationOperationNextDestinationCompanyVatNumber', blank=True, null=True)  # Field name made lowercase.
#     emittercustominfo = models.TextField(db_column='emitterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     destinationcustominfo = models.TextField(db_column='destinationCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     transportercustominfo = models.TextField(db_column='transporterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     transportertransportplates = models.TextField(db_column='transporterTransportPlates', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'Bsvhu'
#
#
class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    siret = models.TextField(unique=True)
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    securitycode = models.IntegerField(
        db_column="securityCode"
    )  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    gerepid = models.TextField(
        db_column="gerepId", blank=True, null=True
    )  # Field name made lowercase.
    codenaf = models.TextField(
        db_column="codeNaf", blank=True, null=True
    )  # Field name made lowercase.
    contactemail = models.TextField(
        db_column="contactEmail", blank=True, null=True
    )  # Field name made lowercase.
    contactphone = models.TextField(
        db_column="contactPhone", blank=True, null=True
    )  # Field name made lowercase.
    website = models.TextField(blank=True, null=True)
    givenname = models.TextField(
        db_column="givenName", blank=True, null=True
    )  # Field name made lowercase.
    transporterreceiptid = models.ForeignKey(
        "Transporterreceipt",
        models.DO_NOTHING,
        db_column="transporterReceiptId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    traderreceiptid = models.ForeignKey(
        "Traderreceipt",
        models.DO_NOTHING,
        db_column="traderReceiptId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    ecoorganismeagreements = models.TextField(
        db_column="ecoOrganismeAgreements", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    companytypes = models.TextField(
        db_column="companyTypes", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    brokerreceiptid = models.ForeignKey(
        Brokerreceipt,
        models.DO_NOTHING,
        db_column="brokerReceiptId",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    verificationcode = models.TextField(
        db_column="verificationCode"
    )  # Field name made lowercase.
    verificationstatus = models.TextField(
        db_column="verificationStatus"
    )  # Field name made lowercase. This field type is a guess.
    verificationmode = models.TextField(
        db_column="verificationMode", blank=True, null=True
    )  # Field name made lowercase. This field type is a guess.
    verificationcomment = models.TextField(
        db_column="verificationComment", blank=True, null=True
    )  # Field name made lowercase.
    verifiedat = models.DateTimeField(
        db_column="verifiedAt", blank=True, null=True
    )  # Field name made lowercase.
    # vhuagrementdemolisseurid = models.ForeignKey('Vhuagrement', models.DO_NOTHING, db_column='vhuAgrementDemolisseurId', blank=True, null=True)  # Field name made lowercase.
    # vhuagrementbroyeurid = models.ForeignKey('Vhuagrement', models.DO_NOTHING, db_column='vhuAgrementBroyeurId', blank=True, null=True)  # Field name made lowercase.
    allowbsdasritakeoverwithoutsignature = models.BooleanField(
        db_column="allowBsdasriTakeOverWithoutSignature", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Company"


class Companyassociation(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    role = models.TextField()  # This field type is a guess.
    companyid = models.ForeignKey(
        Company, models.DO_NOTHING, db_column="companyId"
    )  # Field name made lowercase.
    userid = models.ForeignKey(
        "User", models.DO_NOTHING, db_column="userId"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "CompanyAssociation"


# class Declaration(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     codes3ic = models.TextField(db_column='codeS3ic', blank=True, null=True)  # Field name made lowercase.
#     nomets = models.TextField(db_column='nomEts', blank=True, null=True)  # Field name made lowercase.
#     annee = models.TextField(blank=True, null=True)
#     codedechet = models.TextField(db_column='codeDechet', blank=True, null=True)  # Field name made lowercase.
#     libdechet = models.TextField(db_column='libDechet', blank=True, null=True)  # Field name made lowercase.
#     gereptype = models.TextField(db_column='gerepType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'Declaration'
#
#
# class Ecoorganisme(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     siret = models.TextField(unique=True)
#     name = models.TextField()
#     address = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'EcoOrganisme'
#
#
# class Form(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     emittertype = models.TextField(db_column='emitterType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     emitterpickupsite = models.TextField(db_column='emitterPickupSite', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyname = models.TextField(db_column='emitterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     emittercompanysiret = models.TextField(db_column='emitterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyaddress = models.TextField(db_column='emitterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     emittercompanycontact = models.TextField(db_column='emitterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     emittercompanyphone = models.TextField(db_column='emitterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     emittercompanymail = models.TextField(db_column='emitterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     recipientcap = models.TextField(db_column='recipientCap', blank=True, null=True)  # Field name made lowercase.
#     recipientprocessingoperation = models.TextField(db_column='recipientProcessingOperation', blank=True, null=True)  # Field name made lowercase.
#     recipientcompanyname = models.TextField(db_column='recipientCompanyName', blank=True, null=True)  # Field name made lowercase.
#     recipientcompanysiret = models.TextField(db_column='recipientCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     recipientcompanyaddress = models.TextField(db_column='recipientCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     recipientcompanycontact = models.TextField(db_column='recipientCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     recipientcompanyphone = models.TextField(db_column='recipientCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     recipientcompanymail = models.TextField(db_column='recipientCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyname = models.TextField(db_column='transporterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     transportercompanysiret = models.TextField(db_column='transporterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyaddress = models.TextField(db_column='transporterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     transportercompanycontact = models.TextField(db_column='transporterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyphone = models.TextField(db_column='transporterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     transportercompanymail = models.TextField(db_column='transporterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     transporterreceipt = models.TextField(db_column='transporterReceipt', blank=True, null=True)  # Field name made lowercase.
#     transporterdepartment = models.TextField(db_column='transporterDepartment', blank=True, null=True)  # Field name made lowercase.
#     transportervaliditylimit = models.DateTimeField(db_column='transporterValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     transporternumberplate = models.TextField(db_column='transporterNumberPlate', blank=True, null=True)  # Field name made lowercase.
#     wastedetailscode = models.TextField(db_column='wasteDetailsCode', blank=True, null=True)  # Field name made lowercase.
#     wastedetailsonucode = models.TextField(db_column='wasteDetailsOnuCode', blank=True, null=True)  # Field name made lowercase.
#     wastedetailsquantity = models.DecimalField(db_column='wasteDetailsQuantity', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     wastedetailsquantitytype = models.TextField(db_column='wasteDetailsQuantityType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     readableid = models.TextField(db_column='readableId', unique=True)  # Field name made lowercase.
#     status = models.TextField()  # This field type is a guess.
#     sentat = models.DateTimeField(db_column='sentAt', blank=True, null=True)  # Field name made lowercase.
#     sentby = models.TextField(db_column='sentBy', blank=True, null=True)  # Field name made lowercase.
#     isaccepted = models.BooleanField(db_column='isAccepted', blank=True, null=True)  # Field name made lowercase.
#     receivedat = models.DateTimeField(db_column='receivedAt', blank=True, null=True)  # Field name made lowercase.
#     quantityreceived = models.DecimalField(db_column='quantityReceived', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     processingoperationdone = models.TextField(db_column='processingOperationDone', blank=True, null=True)  # Field name made lowercase.
#     wastedetailsname = models.TextField(db_column='wasteDetailsName', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.BooleanField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
#     receivedby = models.TextField(db_column='receivedBy', blank=True, null=True)  # Field name made lowercase.
#     wastedetailsconsistence = models.TextField(db_column='wasteDetailsConsistence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     processedby = models.TextField(db_column='processedBy', blank=True, null=True)  # Field name made lowercase.
#     processedat = models.DateTimeField(db_column='processedAt', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationprocessingoperation = models.TextField(db_column='nextDestinationProcessingOperation', blank=True, null=True)  # Field name made lowercase.
#     tradercompanyname = models.TextField(db_column='traderCompanyName', blank=True, null=True)  # Field name made lowercase.
#     tradercompanysiret = models.TextField(db_column='traderCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     tradercompanyaddress = models.TextField(db_column='traderCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     tradercompanycontact = models.TextField(db_column='traderCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     tradercompanyphone = models.TextField(db_column='traderCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     tradercompanymail = models.TextField(db_column='traderCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     traderreceipt = models.TextField(db_column='traderReceipt', blank=True, null=True)  # Field name made lowercase.
#     traderdepartment = models.TextField(db_column='traderDepartment', blank=True, null=True)  # Field name made lowercase.
#     tradervaliditylimit = models.DateTimeField(db_column='traderValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     processingoperationdescription = models.TextField(db_column='processingOperationDescription', blank=True, null=True)  # Field name made lowercase.
#     notraceability = models.BooleanField(db_column='noTraceability', blank=True, null=True)  # Field name made lowercase.
#     signedbytransporter = models.BooleanField(db_column='signedByTransporter', blank=True, null=True)  # Field name made lowercase.
#     transporterisexemptedofreceipt = models.BooleanField(db_column='transporterIsExemptedOfReceipt', blank=True, null=True)  # Field name made lowercase.
#     customid = models.TextField(db_column='customId', blank=True, null=True)  # Field name made lowercase.
#     wasteacceptationstatus = models.TextField(db_column='wasteAcceptationStatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     wasterefusalreason = models.TextField(db_column='wasteRefusalReason', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationcompanyname = models.TextField(db_column='nextDestinationCompanyName', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationcompanysiret = models.TextField(db_column='nextDestinationCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationcompanyaddress = models.TextField(db_column='nextDestinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationcompanycontact = models.TextField(db_column='nextDestinationCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationcompanyphone = models.TextField(db_column='nextDestinationCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationcompanymail = models.TextField(db_column='nextDestinationCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     emitterworksitename = models.TextField(db_column='emitterWorkSiteName', blank=True, null=True)  # Field name made lowercase.
#     emitterworksiteaddress = models.TextField(db_column='emitterWorkSiteAddress', blank=True, null=True)  # Field name made lowercase.
#     emitterworksitecity = models.TextField(db_column='emitterWorkSiteCity', blank=True, null=True)  # Field name made lowercase.
#     emitterworksitepostalcode = models.TextField(db_column='emitterWorkSitePostalCode', blank=True, null=True)  # Field name made lowercase.
#     emitterworksiteinfos = models.TextField(db_column='emitterWorkSiteInfos', blank=True, null=True)  # Field name made lowercase.
#     transportercustominfo = models.TextField(db_column='transporterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#     recipientistempstorage = models.BooleanField(db_column='recipientIsTempStorage', blank=True, null=True)  # Field name made lowercase.
#     temporarystoragedetailid = models.OneToOneField('Temporarystoragedetail', models.DO_NOTHING, db_column='temporaryStorageDetailId', blank=True, null=True)  # Field name made lowercase.
#     signedat = models.DateTimeField(db_column='signedAt', blank=True, null=True)  # Field name made lowercase.
#     currenttransportersiret = models.TextField(db_column='currentTransporterSiret', blank=True, null=True)  # Field name made lowercase.
#     nexttransportersiret = models.TextField(db_column='nextTransporterSiret', blank=True, null=True)  # Field name made lowercase.
#     nextdestinationcompanycountry = models.TextField(db_column='nextDestinationCompanyCountry', blank=True, null=True)  # Field name made lowercase.
#     isimportedfrompaper = models.BooleanField(db_column='isImportedFromPaper')  # Field name made lowercase.
#     ecoorganismename = models.TextField(db_column='ecoOrganismeName', blank=True, null=True)  # Field name made lowercase.
#     ecoorganismesiret = models.TextField(db_column='ecoOrganismeSiret', blank=True, null=True)  # Field name made lowercase.
#     wastedetailspackaginginfos = models.JSONField(db_column='wasteDetailsPackagingInfos')  # Field name made lowercase.
#     signedby = models.TextField(db_column='signedBy', blank=True, null=True)  # Field name made lowercase.
#     wastedetailspop = models.BooleanField(db_column='wasteDetailsPop')  # Field name made lowercase.
#     ownerid = models.CharField(db_column='ownerId', max_length=30)  # Field name made lowercase.
#     appendix2rootformid = models.CharField(db_column='appendix2RootFormId', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     brokercompanyname = models.TextField(db_column='brokerCompanyName', blank=True, null=True)  # Field name made lowercase.
#     brokercompanysiret = models.TextField(db_column='brokerCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     brokercompanyaddress = models.TextField(db_column='brokerCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     brokercompanycontact = models.TextField(db_column='brokerCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     brokercompanyphone = models.TextField(db_column='brokerCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     brokercompanymail = models.TextField(db_column='brokerCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     brokerreceipt = models.TextField(db_column='brokerReceipt', blank=True, null=True)  # Field name made lowercase.
#     brokerdepartment = models.TextField(db_column='brokerDepartment', blank=True, null=True)  # Field name made lowercase.
#     brokervaliditylimit = models.DateTimeField(db_column='brokerValidityLimit', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Form'
#
#
# class Grant(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     code = models.TextField(unique=True)
#     expires = models.IntegerField()
#     redirecturi = models.TextField(db_column='redirectUri')  # Field name made lowercase.
#     userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
#     applicationid = models.ForeignKey(Application, models.DO_NOTHING, db_column='applicationId')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Grant'
#
#
# class Installation(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     codes3ic = models.TextField(db_column='codeS3ic', blank=True, null=True)  # Field name made lowercase.
#     nomets = models.TextField(db_column='nomEts', blank=True, null=True)  # Field name made lowercase.
#     regime = models.TextField(blank=True, null=True)
#     libregime = models.TextField(db_column='libRegime', blank=True, null=True)  # Field name made lowercase.
#     seveso = models.TextField(blank=True, null=True)  # This field type is a guess.
#     libseveso = models.TextField(db_column='libSeveso', blank=True, null=True)  # Field name made lowercase.
#     familleic = models.TextField(db_column='familleIc', blank=True, null=True)  # Field name made lowercase.
#     urlfiche = models.TextField(db_column='urlFiche', blank=True, null=True)  # Field name made lowercase.
#     s3icnumerosiret = models.TextField(db_column='s3icNumeroSiret', blank=True, null=True)  # Field name made lowercase.
#     irepnumerosiret = models.TextField(db_column='irepNumeroSiret', blank=True, null=True)  # Field name made lowercase.
#     gerepnumerosiret = models.TextField(db_column='gerepNumeroSiret', blank=True, null=True)  # Field name made lowercase.
#     sirenenumerosiret = models.TextField(db_column='sireneNumeroSiret', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Installation'
#
#
# class Membershiprequest(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     status = models.TextField()  # This field type is a guess.
#     statusupdatedby = models.TextField(db_column='statusUpdatedBy', blank=True, null=True)  # Field name made lowercase.
#     companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyId')  # Field name made lowercase.
#     userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
#     sentto = models.TextField(db_column='sentTo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'MembershipRequest'
#
#
# class Rubrique(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     codes3ic = models.TextField(db_column='codeS3ic', blank=True, null=True)  # Field name made lowercase.
#     rubrique = models.TextField(blank=True, null=True)
#     alinea = models.TextField(blank=True, null=True)
#     dateautorisation = models.TextField(db_column='dateAutorisation', blank=True, null=True)  # Field name made lowercase.
#     etatactivite = models.TextField(db_column='etatActivite', blank=True, null=True)  # Field name made lowercase.
#     regimeautorise = models.TextField(db_column='regimeAutorise', blank=True, null=True)  # Field name made lowercase.
#     activite = models.TextField(blank=True, null=True)
#     volume = models.TextField(blank=True, null=True)
#     unite = models.TextField(blank=True, null=True)
#     category = models.TextField(blank=True, null=True)
#     wastetype = models.TextField(db_column='wasteType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'Rubrique'
#
#
# class Statuslog(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     status = models.TextField()  # This field type is a guess.
#     userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
#     formid = models.ForeignKey(Form, models.DO_NOTHING, db_column='formId')  # Field name made lowercase.
#     loggedat = models.DateTimeField(db_column='loggedAt', blank=True, null=True)  # Field name made lowercase.
#     updatedfields = models.JSONField(db_column='updatedFields')  # Field name made lowercase.
#     authtype = models.TextField(db_column='authType')  # Field name made lowercase. This field type is a guess.
#
#     class Meta:
#         managed = False
#         db_table = 'StatusLog'
#
#
# class Temporarystoragedetail(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     tempstorerquantitytype = models.TextField(db_column='tempStorerQuantityType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     tempstorerquantityreceived = models.DecimalField(db_column='tempStorerQuantityReceived', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     tempstorerwasteacceptationstatus = models.TextField(db_column='tempStorerWasteAcceptationStatus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     tempstorerwasterefusalreason = models.TextField(db_column='tempStorerWasteRefusalReason', blank=True, null=True)  # Field name made lowercase.
#     tempstorerreceivedat = models.DateTimeField(db_column='tempStorerReceivedAt', blank=True, null=True)  # Field name made lowercase.
#     tempstorerreceivedby = models.TextField(db_column='tempStorerReceivedBy', blank=True, null=True)  # Field name made lowercase.
#     tempstorersignedat = models.DateTimeField(db_column='tempStorerSignedAt', blank=True, null=True)  # Field name made lowercase.
#     destinationisfilledbyemitter = models.BooleanField(db_column='destinationIsFilledByEmitter', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyname = models.TextField(db_column='destinationCompanyName', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanysiret = models.TextField(db_column='destinationCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyaddress = models.TextField(db_column='destinationCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanycontact = models.TextField(db_column='destinationCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanyphone = models.TextField(db_column='destinationCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     destinationcompanymail = models.TextField(db_column='destinationCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     destinationcap = models.TextField(db_column='destinationCap', blank=True, null=True)  # Field name made lowercase.
#     destinationprocessingoperation = models.TextField(db_column='destinationProcessingOperation', blank=True, null=True)  # Field name made lowercase.
#     wastedetailsonucode = models.TextField(db_column='wasteDetailsOnuCode', blank=True, null=True)  # Field name made lowercase.
#     wastedetailsquantity = models.DecimalField(db_column='wasteDetailsQuantity', max_digits=65, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
#     wastedetailsquantitytype = models.TextField(db_column='wasteDetailsQuantityType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     transportercompanyname = models.TextField(db_column='transporterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     transportercompanysiret = models.TextField(db_column='transporterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyaddress = models.TextField(db_column='transporterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     transportercompanycontact = models.TextField(db_column='transporterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyphone = models.TextField(db_column='transporterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     transportercompanymail = models.TextField(db_column='transporterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     transporterisexemptedofreceipt = models.BooleanField(db_column='transporterIsExemptedOfReceipt', blank=True, null=True)  # Field name made lowercase.
#     transporterreceipt = models.TextField(db_column='transporterReceipt', blank=True, null=True)  # Field name made lowercase.
#     transporterdepartment = models.TextField(db_column='transporterDepartment', blank=True, null=True)  # Field name made lowercase.
#     transportervaliditylimit = models.DateTimeField(db_column='transporterValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     transporternumberplate = models.TextField(db_column='transporterNumberPlate', blank=True, null=True)  # Field name made lowercase.
#     signedbytransporter = models.BooleanField(db_column='signedByTransporter', blank=True, null=True)  # Field name made lowercase.
#     signedby = models.TextField(db_column='signedBy', blank=True, null=True)  # Field name made lowercase.
#     signedat = models.DateTimeField(db_column='signedAt', blank=True, null=True)  # Field name made lowercase.
#     wastedetailspackaginginfos = models.JSONField(db_column='wasteDetailsPackagingInfos')  # Field name made lowercase.
#     tempstorersignedby = models.TextField(db_column='tempStorerSignedBy', blank=True, null=True)  # Field name made lowercase.
#     transportercustominfo = models.TextField(db_column='transporterCustomInfo', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'TemporaryStorageDetail'
#
#
class Traderreceipt(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    receiptnumber = models.TextField(
        db_column="receiptNumber"
    )  # Field name made lowercase.
    validitylimit = models.DateTimeField(
        db_column="validityLimit"
    )  # Field name made lowercase.
    department = models.TextField()

    class Meta:
        managed = False
        db_table = "TraderReceipt"


#
# class Transportsegment(models.Model):
#     id = models.CharField(primary_key=True, max_length=30)
#     segmentnumber = models.IntegerField(db_column='segmentNumber', blank=True, null=True)  # Field name made lowercase.
#     transportercompanysiret = models.TextField(db_column='transporterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyname = models.TextField(db_column='transporterCompanyName', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyaddress = models.TextField(db_column='transporterCompanyAddress', blank=True, null=True)  # Field name made lowercase.
#     transportercompanycontact = models.TextField(db_column='transporterCompanyContact', blank=True, null=True)  # Field name made lowercase.
#     transportercompanyphone = models.TextField(db_column='transporterCompanyPhone', blank=True, null=True)  # Field name made lowercase.
#     transportercompanymail = models.TextField(db_column='transporterCompanyMail', blank=True, null=True)  # Field name made lowercase.
#     transporterisexemptedofreceipt = models.BooleanField(db_column='transporterIsExemptedOfReceipt', blank=True, null=True)  # Field name made lowercase.
#     transporterreceipt = models.TextField(db_column='transporterReceipt', blank=True, null=True)  # Field name made lowercase.
#     transporterdepartment = models.TextField(db_column='transporterDepartment', blank=True, null=True)  # Field name made lowercase.
#     transportervaliditylimit = models.DateTimeField(db_column='transporterValidityLimit', blank=True, null=True)  # Field name made lowercase.
#     transporternumberplate = models.TextField(db_column='transporterNumberPlate', blank=True, null=True)  # Field name made lowercase.
#     mode = models.TextField(blank=True, null=True)  # This field type is a guess.
#     readytotakeover = models.BooleanField(db_column='readyToTakeOver', blank=True, null=True)  # Field name made lowercase.
#     previoustransportercompanysiret = models.TextField(db_column='previousTransporterCompanySiret', blank=True, null=True)  # Field name made lowercase.
#     takenoverat = models.DateTimeField(db_column='takenOverAt', blank=True, null=True)  # Field name made lowercase.
#     takenoverby = models.TextField(db_column='takenOverBy', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
#     formid = models.ForeignKey(Form, models.DO_NOTHING, db_column='formId')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'TransportSegment'
#
#
class Transporterreceipt(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    receiptnumber = models.TextField(
        db_column="receiptNumber"
    )  # Field name made lowercase.
    validitylimit = models.DateTimeField(
        db_column="validityLimit"
    )  # Field name made lowercase.
    department = models.TextField()

    class Meta:
        managed = False
        db_table = "TransporterReceipt"


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    email = models.TextField(unique=True)
    password = models.TextField()
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.
    isactive = models.BooleanField(
        db_column="isActive", blank=True, null=True
    )  # Field name made lowercase.
    applicationid = models.CharField(
        db_column="applicationId", max_length=30, blank=True, null=True
    )  # Field name made lowercase.
    activatedat = models.DateTimeField(
        db_column="activatedAt", blank=True, null=True
    )  # Field name made lowercase.
    firstassociationdate = models.DateTimeField(
        db_column="firstAssociationDate", blank=True, null=True
    )  # Field name made lowercase.
    isadmin = models.BooleanField(db_column="isAdmin")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "User"


class Useraccounthash(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    email = models.TextField()
    companysiret = models.CharField(
        db_column="companySiret", max_length=25
    )  # Field name made lowercase.
    hash = models.TextField(unique=True)
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    role = models.TextField()  # This field type is a guess.
    acceptedat = models.DateTimeField(
        db_column="acceptedAt", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "UserAccountHash"


class Useractivationhash(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    hash = models.TextField(unique=True)
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    userid = models.CharField(
        db_column="userId", max_length=30
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "UserActivationHash"


class Vhuagrement(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    agrementnumber = models.CharField(
        db_column="agrementNumber", max_length=50
    )  # Field name made lowercase.
    department = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "VhuAgrement"


# class Bsfftobsffficheintervention(models.Model):
#     a = models.ForeignKey(Bsff, models.DO_NOTHING, db_column='A')  # Field name made lowercase.
#     b = models.ForeignKey(Bsffficheintervention, models.DO_NOTHING, db_column='B')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = '_BsffToBsffFicheIntervention'
#         unique_together = (('a', 'b'),)


# In models.py
class CompanyProxy(Company):
    class Meta:
        proxy = True
