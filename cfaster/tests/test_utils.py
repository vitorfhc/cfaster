#!/usr/bin/env python3
from unittest import TestCase

from cfaster.scrapers.utils import (
        urls,
        )

class TestURLs(TestCase):
    def test_base_case_true(self):
        self.assertTrue(urls.validate_url('https://google.com', 'google'))
        self.assertTrue(urls.validate_url('google.com', 'google'))
        self.assertTrue(urls.validate_url('http://google.com', 'google'))

        self.assertTrue(urls.validate_url('https://www.google.com', 'google'))
        self.assertTrue(urls.validate_url('www.google.com', 'google'))
        self.assertTrue(urls.validate_url('http://www.google.com', 'google'))

        self.assertTrue(urls.validate_url('https://www.google.co', 'google'))
        self.assertTrue(urls.validate_url('www.google.co.uk', 'google'))
        self.assertTrue(urls.validate_url('http://www.google.biz', 'google'))

        self.assertTrue(urls.validate_url('https://www.google.co/asdf', 'google'))
        self.assertTrue(urls.validate_url('www.google.co.uk/bar/baz/buzz', 'google'))

    def test_base_case_false(self):
        self.assertFalse(urls.validate_url('https://www.facebook.co', 'google'))
        self.assertFalse(urls.validate_url('www.notgoogle.co.uk', 'google'))
        self.assertFalse(urls.validate_url('http://www.something.does.not.exist.biz', 'google'))

    def test_subdomain_true(self):
        self.assertTrue(urls.validate_url('https://www.facebook.google.co', 'google'))
        self.assertTrue(urls.validate_url('www.another.sub.domain.google.co.uk', 'google'))
        self.assertTrue(urls.validate_url('http://www.google.google.biz', 'google'))

    def test_subdomain_false(self):
        self.assertFalse(urls.validate_url('https://www.google.facebook.co', 'google'))
        self.assertFalse(urls.validate_url('https://www.google.facebook.com', 'google'))
        self.assertFalse(urls.validate_url('www.another.sub.domain.google.fake.co.uk', 'google'))
        self.assertFalse(urls.validate_url('http://www.google.giggle.ly', 'google'))

