from django.test import SimpleTestCase


class QuxImportSmokeTest(SimpleTestCase):
    """Verify qux APIs used by qjango survive the submodule→pip migration."""

    def test_seo_mixin_importable(self):
        from qux.seo.mixin import SEOMixin
        self.assertTrue(callable(SEOMixin))

    def test_token_auth_importable(self):
        from qux.token.models import CustomTokenAuthentication
        self.assertTrue(callable(CustomTokenAuthentication))

    def test_auth_urls_importable(self):
        from qux.auth.urls import appurls
        self.assertTrue(hasattr(appurls, "urlpatterns"))

    def test_application_home_view_resolves(self):
        from apps.gizmo.views.appviews import ApplicationHomeView
        view = ApplicationHomeView.as_view()
        # Should not raise ImportError — that's the contract
        self.assertTrue(callable(view))
