import unittest
from app.models import User, Comment
from flask_login import current_user
from app import db

class TestComments(unittest.TestCase):
    def setUp(self):        
        self.new_comment = Comment(pitch_id=12, title='Awesome', comment="Nice presentation...", postedAt="2019-05-27 14:15:43.587649", user_id=1)
        
        def tearDown(self):
         Comment.query.delete()
         User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id, 12)
        self.assertEquals(self.new_comment.title, 'Awesome')
        self.assertEquals(self.new_comment.comment, 'Nice presentation...')
        self.assertEquals(self.new_comment.postedAt, '2022-05-09 14:15:43.587649')
        
        def test_save_review(self):
             self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
        
        def test_get_comment_by_id(self):
             self.new_comment.save_comment()
        got_comment = Comment.get_comment(12345)
        self.assertTrue(len(got_comment) == 1)