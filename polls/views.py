# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpRequest, HttpResponse

from celery import shared_task
from .models import Question


@shared_task
def create_question():
    Question.objects.create(question_text="this is created from celery")


def hello(request: HttpRequest) -> HttpResponse:
    create_question.delay()
    return HttpResponse("creted question model via celery v3")
