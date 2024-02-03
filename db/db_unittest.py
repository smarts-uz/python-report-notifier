import  unittest
from .db_functions import *
class TestDbFunctions(unittest.TestCase):

    def test_topic_title(self):
        self.assertEqual(get_title_from_user_and_message("https://t.me/c/2098866683/33/103"),'Samandar Komilov  |  this is Uzbekistan!')
        self.assertNotEqual(get_title_from_user_and_message("https://t.me/c/2098866683/33/101"),"somebody | Yahoo olga dostlar!")







if __name__ == '__main__':
    unittest.main()