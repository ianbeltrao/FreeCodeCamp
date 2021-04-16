import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)
        print(self.contents)
    
    def draw(self, number):
        rand = random.randrange(len(self.contents)+1)
        all_removed = []
        if number >= len(self.contents):
            return self.contents
        for i in range(number):
            rand = random.randrange(len(self.contents))
            removed = self.contents.pop(rand)
            all_removed.append(removed)
        return all_removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.copy(hat)
        sample = hat_copy.draw(num_balls_drawn)
        ok = True
        for key in expected_balls.keys():
            if sample.count(key) < expected_balls[key]:
                ok = False
                break
        if ok:
            count += 1
    return count / num_experiments
        