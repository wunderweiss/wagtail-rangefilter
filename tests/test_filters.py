import datetime

from django.test import TestCase
from django.utils.timezone import make_aware
from wagtail.test.utils import WagtailTestUtils

from tests.testapp.models import TestModel


class TestIndexView(TestCase, WagtailTestUtils):
    def setUp(self):
        self.login()

        self.test_model_1 = TestModel.objects.create(
            date_time_1=make_aware(datetime.datetime(2022, 9, 20, 10, 1, 0)),
            date_time_2=make_aware(datetime.datetime(2022, 9, 20, 10, 1, 0)),
        )
        self.test_model_2 = TestModel.objects.create(
            date_time_1=make_aware(datetime.datetime(2022, 9, 21, 10, 1, 0)),
            date_time_2=make_aware(datetime.datetime(2022, 9, 21, 10, 1, 0)),
        )
        self.test_model_3 = TestModel.objects.create(
            date_time_1=make_aware(datetime.datetime(2022, 9, 22, 10, 1, 0)),
            date_time_2=make_aware(datetime.datetime(2022, 9, 22, 10, 1, 0)),
        )

    def get(self, params=None):
        return self.client.get("/admin/wagtail_rangefilter_testapp/testmodel/", params)

    def assert_object_list(self, response, expected):
        actual = set(response.context["object_list"])
        self.assertSetEqual(actual, set(expected))

    def test_unfiltered(self):
        response = self.get()
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_1,
                self.test_model_2,
                self.test_model_3,
            ],
        )

    def test_date_filter(self):
        response = self.get(params={"date_time_1__range__gte": "2022-09-20"})
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_1,
                self.test_model_2,
                self.test_model_3,
            ],
        )

        response = self.get(
            params={
                "date_time_1__range__gte": "2022-09-21",
                "date_time_1__range__lte": "",
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_2,
                self.test_model_3,
            ],
        )

        response = self.get(
            params={
                "date_time_1__range__gte": "2022-09-21",
                "date_time_1__range__lte": "2022-09-21",
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_2,
            ],
        )

        response = self.get(params={"date_time_1__range__lte": "2022-09-21"})
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_1,
                self.test_model_2,
            ],
        )

    def test_date_time_filter(self):
        response = self.get(params={"date_time_2__range__gte": "2022-09-20 10:01"})
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_1,
                self.test_model_2,
                self.test_model_3,
            ],
        )

        # exclude the first item by adding 1s
        response = self.get(
            params={
                "date_time_2__range__gte": "2022-09-20 10:01:01",
                "date_time_2__range__lte": "",
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_2,
                self.test_model_3,
            ],
        )

        response = self.get(
            params={
                "date_time_2__range__gte": "2022-09-20 10:02",
                "date_time_2__range__lte": "2022-09-22 10:00",
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_2,
            ],
        )

        response = self.get(params={"date_time_2__range__lte": "2022-09-21 10:01"})
        self.assertEqual(response.status_code, 200)
        self.assert_object_list(
            response,
            [
                self.test_model_1,
                self.test_model_2,
            ],
        )
