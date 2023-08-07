from datetime import datetime, date
from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import Blogpost, Topic, Comment
from django.contrib.auth.models import User


class ModelPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user1',
            password='hlo',
        )
        self.topic = Topic.objects.create(
            slug="ttt",
            title="ttt",
            text="rrrrrr",
            authors=self.user,
        )
        self.obj = Blogpost.objects.create(
                                slug="title",
                                title="Title",
                                text="Text",
                                author=self.user,
                                )
        self.obj.topics.set([self.topic])
    def test_create_blog(self):
        self.assertTrue(Blogpost.objects.exists())

    def test_created_at_blog(self):
        self.assertEqual(date, type(self.obj.created_at))

    def test_updated_at_blog(self):
        self.assertEqual(datetime, type(self.obj.updated_at))


    def test_post_has_many_topics_blog(self):
        self.obj.topics.create(title="Topic1")
        self.assertEqual(2, self.obj.topics.count())

    def test_get_absolute_url_for_post_blog(self):
        expected_url = self.obj.slug
        self.assertEquals(self.obj.slug, expected_url)

    def test_post_detail_view_blog(self):
        url = reverse('get_blog', args=[self.obj.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.obj.title, str(resp.content))

    def test_post_delete_blog(self):
        self.url = reverse('post_delete', args=[self.obj.pk])
        response = self.client.delete(self.url)
        self.assertEqual(302, response.status_code)


class ClientPostTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username='test_user1',
            password='hlo',
        )

    def test_form_validity(self):
        response = self.c.get(reverse("create"))
        self.assertEqual(response.status_code, 302)

    def test_not_found_error(self):
        response = self.c.get("/fsgdgdgbr/hdfbdfbth")
        self.assertEqual(response.status_code, 404)

    def test_publish_post(self):
        self.c.force_login(self.user)
        new_post_response = self.c.get("/create/", follow=True)
        self.assertEqual(new_post_response.status_code, 200)


class ClientTopicTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username='test_user1',
            password='hlo',
        )

    def test_form_validity(self):
        response = self.c.get(reverse("topic_create"))
        self.assertEqual(response.status_code, 302)

    def test_publish_topic(self):
        self.c.force_login(self.user)
        new_post_response = self.c.get("/topic_create/", follow=True)
        self.assertEqual(new_post_response.status_code, 200)


class TopicPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user1',
            password='hlo',
        )
        self.obj = Topic.objects.create(
            slug="title",
            title="Title",
            text="Text",
            authors=self.user,
        )

    def test_create_topic(self):
        self.assertTrue(Topic.objects.exists())

    def test_created_at_topic(self):
        self.assertEqual(date, type(self.obj.created_at))

    def test_updated_at_topic(self):
        self.assertEqual(datetime, type(self.obj.updated_at))

    def test_get_absolute_url_for_topic(self):
        expected_url = self.obj.slug
        self.assertEquals(self.obj.slug, expected_url)

    def topic_detail_view(self):
        url = reverse('get_topic', args=[self.obj.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.obj.title, str(resp.content))

    def test_topic_delete(self):
        self.url = reverse('topic_delete', args=[self.obj.pk])
        response = self.client.delete(self.url)
        self.assertEqual(302, response.status_code)

    def test_topic_update(self):
        new_data = {
            "title": "Updated topic",
            "slug": "updated-new-topic",
            "text": "Updated content sentence.",
        }
        self.url = reverse('topic_edit',  args=[self.obj.pk])
        response = self.client.put(path=self.url, data = new_data, follow=True)
        self.assertEqual(200, response.status_code)
        updated_topic = Topic.objects.get(id=self.obj.id)
        self.assertTrue(updated_topic.title, new_data["title"])

class CommentPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user1',
            password='hlo',
        )
        self.topic = Topic.objects.create(
            slug="ttt",
            title="ttt",
            text="rrrrrr",
            authors=self.user,
        )
        self.post = Blogpost.objects.create(
            slug="title",
            title="Title",
            text="Text",
            author=self.user,
        )
        self.post.topics.set([self.topic])

        self.obj = Comment.objects.create(
            text="Text",
            author=self.user,
            blogpost=self.post
        )

    def test_create_comment(self):
        self.assertTrue(Topic.objects.exists())

    def test_created_at_comment(self):
        self.assertEqual(date, type(self.obj.created_at))

    def test_updated_at_comment(self):
        self.assertEqual(datetime, type(self.obj.updated_at))

