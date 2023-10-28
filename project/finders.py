from django.contrib.staticfiles.finders import AppDirectoriesFinder


class CustomAppDirectoriesStaticFinder(AppDirectoriesFinder):
    source_dir = "common"
