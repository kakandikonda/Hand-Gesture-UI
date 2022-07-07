from random import random
import cv2

class Target:
    def __init__(self, image):
        # Give this target a randomized x, y, and radius
        self.radius = random() * 50 + 50
        self.x = random() * image.shape[1]
        self.y = random() * image.shape[0]

    def draw(self, image):
        # Draw this target on the screen #(int(self.x), int(self.y)) int(self.radius)
        cv2.circle(image, (100, 100), 20, (255, 0, 0), -1)

    def point_is_within_me(self, x, y):
        # Use the distance formula to determine if the point is within the circle
        return (x - self.x) ** 2 + (y - self.y) ** 2 < self.radius ** 2

    def hit_by_points(self, points):
        for point in points:
            if self.point_is_within_me(point[0], point[1]):
                return True
        return False