import db_actions
import re

# gets hashtags from post with real expressions
def get_hashtags(post):
    finder = re.compile(r"#(\w+)")
    return set(finder.findall(post))
