#!/usr/bin/env python3

import json
import unittest
import multicon

class TestMultiConfig(unittest.TestCase):
	def test_simple_for_three_configs(self):
		c1 = {
			'a': 123,
			'b': 256,
			'c': [1, 2, 3],
			'd': {
				'da': 1,
				'db': 2,
				'dc': 3,
				'dd': {
					'dda': 997
				}
			}
		}

		c2 = {
			'b': 112,
			'e': 9427
		}

		c3 = {
			'd': {
				'db': 18,
				'dd': [1, 2, 3, 4, 5, 6, 7],
			}
		}

		multiconfig = multicon.MultiConfig([c1, c2, c3], {})
		config = dict(multiconfig)

		self.assertTrue(config == {
			'a': 123,
			'b': 112,
			'c': [1, 2, 3],
			'e': 9427,
			'd': {
				'da': 1,
				'db': 18,
				'dc': 3,
				'dd': [1, 2, 3, 4, 5, 6, 7]
			}
		})


if __name__ == '__main__':
	unittest.main()
