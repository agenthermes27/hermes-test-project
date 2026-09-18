"""Tests for main module."""

import pytest
from hermes_test_project.main import greet, add, multiply


class TestGreet:
    def test_default_greeting(self):
        assert greet() == "Hello, World!"

    def test_custom_greeting(self):
        assert greet("Hermes") == "Hello, Hermes!"

    def test_empty_string(self):
        assert greet("") == "Hello, !"


class TestAdd:
    def test_positive_integers(self):
        assert add(2, 3) == 5

    def test_negative_integers(self):
        assert add(-1, -2) == -3

    def test_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5


class TestMultiply:
    def test_positive_integers(self):
        assert multiply(4, 5) == 20

    def test_by_zero(self):
        assert multiply(7, 0) == 0
        assert multiply(0, 7) == 0

    def test_negative(self):
        assert multiply(-3, 4) == -12
        assert multiply(-3, -4) == 12
