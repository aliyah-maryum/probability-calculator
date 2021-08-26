import copy
import random
# Consider using the modules imported above.
class Hat:
  def __init__(self, **balls):
    self.contents = []
    for key, value in balls.items():
      for n in range(value):
       self.contents.append(str(key))
  def draw(self, num_balls):
    random_balls = []
    if num_balls > len(self.contents):
      return self.contents
    else:
      for n in range(num_balls):
        random_ball = self.contents.pop(random.randint(0, len(self.contents)-1))
        random_balls.append(random_ball)
    return random_balls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  balls_drawn_dict = {}
  for n in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    expected_balls_copy = copy.deepcopy(expected_balls)
    count = 0
    balls_drawn = hat_copy.draw(num_balls_drawn)
    for ball_drawn in balls_drawn:
      if ball_drawn not in balls_drawn_dict.keys():
        balls_drawn_dict[ball_drawn] = 1
      else:
        balls_drawn_dict[ball_drawn] += 1
    for key, value in expected_balls_copy.items():
      if key in balls_drawn_dict.keys() and value <= balls_drawn_dict[key]:
        count += 1
    successes = successes + 1 if count == len(expected_balls) else successes
    balls_drawn_dict.clear()
  probability = successes / num_experiments
  return probability

  
