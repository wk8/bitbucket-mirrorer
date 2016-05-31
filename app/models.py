import datetime

from django.db import models

# FIXME: set proper indices!


class RepoUser(models.Model):
    # FIXME: restrict that? choices=...?
    backend = models.CharField(default='Github', max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Repo(models.Model):
    # FIXME: restrict that? choices=...?
    backend = models.CharField(default='Github', max_length=255)
    user = models.ForeignKey(
        RepoUser, null=True, blank=True, related_name='+',
        help_text='Can stay blank if your configuration(s) do(es) not require making authenticated calls for this repo')
    slug = models.CharField(max_length=255, help_text='e.g. wk8/bitbucketmirrorer')


class BackupConfig(models.Model):
    source_repo = models.ForeignKey(Repo, related_name='+', on_delete=models.CASCADE)
    target_repo = models.ForeignKey(Repo, related_name='+', on_delete=models.CASCADE)

    successful_update_interval = models.DurationField(
        default=datetime.timedelta(hours=6),
        help_text='How long to wait before updating again after a successful update')
    failed_update_interval = models.DurationField(
        default=datetime.timedelta(hours=1),
        help_text='How long to wait before updating again after a failed update')


class BackupConfigRuns(models.Model):
    config = models.ForeignKey(BackupConfig, on_delete=models.CASCADE)

    last_run_at = models.DateTimeField(null=True, blank=True)
    last_run_status = models.NullBooleanField()
