import unittest

import pydantic_core

import openfoodfacts


class TestAPIConfig(unittest.TestCase):
    def test_valid_user_agent(self):
        config = openfoodfacts.APIConfig(user_agent="Valid User Agent")
        assert config.user_agent == "Valid User Agent"

    def test_invalid_user_agent_type(self):
        with self.assertRaises(pydantic_core.ValidationError) as ctx:
            openfoodfacts.APIConfig(user_agent=None)
            self.assertTrue("valid string" in ctx.exception)

    def test_blank_user_agent(self):
        with self.assertRaises(pydantic_core.ValidationError) as ctx:
            openfoodfacts.APIConfig(user_agent="")
            self.assertTrue("cannot be empty" in ctx.exception)
