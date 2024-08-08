from django.contrib.staticfiles.finders import AppDirectoriesFinder


class CustomAppDirectoriesStaticFinder(AppDirectoriesFinder):
    source_dir = "common"

    def check(self, **kwargs):
        if hasattr(super(), "check"):
            return super().check(**kwargs)
        return []
