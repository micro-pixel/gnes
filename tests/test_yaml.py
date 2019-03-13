import os
import unittest

from src.nes import PipelineEncoder


class TestYaml(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dump_path = os.path.join(dirname, 'dump.yml')

    def tearDown(self):
        if os.path.exists(self.dump_path):
            os.remove(self.dump_path)

    def test_dump(self):
        pe0 = PipelineEncoder(10, a=23, b='32', c=['123', '456'])
        pe0.dump_yaml(self.dump_path)
        self.assertTrue(os.path.exists(self.dump_path))
        pe = PipelineEncoder.load_yaml(self.dump_path)
        self.assertEqual(type(pe), PipelineEncoder)
        self.assertEqual(pe0._init_kwargs_dict, pe._init_kwargs_dict)

    # def test_load(self):
    #     with open(self.dump_path, 'w') as fp:
    #         fp.write("!PipelineEncoder\n\
    #                               a: 23\n\
    #                               b: '32'\n\
    #                               c: ['123', '456']")
    #     pe = PipelineEncoder.load_yaml(self.dump_path)
    #     self.assertEqual(type(pe), PipelineEncoder)
    #     self.assertEqual(pe._init_kwargs_dict, {'kwargs': {'a': 23, 'b': '32', 'c': ['123', '456']}, 'args': ()})