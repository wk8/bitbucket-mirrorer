from django.contrib import admin

import models

admin.site.register(models.RepoUser)
admin.site.register(models.Repo)
admin.site.register(models.BackupConfig)
