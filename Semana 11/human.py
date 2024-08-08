class Head:
    def __init__(self, hair, nose, lips, eyes, ears, chin):
        self.hair = hair
        self.nose = nose
        self.lips = lips
        self.eyes = eyes
        self.ears = ears
        self.chin = chin

class Torso:
    def __init__(self, chest, abdomen):
        self.chest = chest
        self.abdomen = abdomen

class Arm:
    def __init__(self, hand):
        self.hand = hand
    
class Hand:
    def __init__(self, fingers):
        self.fingers = fingers

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Feet:
    def __init__(self, toes):
        self.toes = toes

class Human:
    def __init__(self, head, torso, right_arm, left_arm, right_hand, left_hand, right_leg, left_leg, feet):
        self.head = head
        self.torso = torso
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_hand = right_hand
        self.left_hand = left_hand
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.feet = feet

head = Head(hair='black', nose=1, lips=1, eyes=2, ears=2, chin=1)
torso = Torso(chest='muscular', abdomen='strong')
left_arm = Arm(hand='left hand')
right_arm = Arm(hand='right hand')
left_hand = Hand(fingers=5)
right_hand = Hand(fingers=5)
left_leg = Leg(feet='left feet')
right_leg = Leg(feet='right feet')
feet = Feet(toes=10)

human = Human(
    head=head,
    torso=torso,
    left_arm=left_arm,
    right_arm=right_arm,
    left_hand=left_hand,
    right_hand=right_hand,
    left_leg=left_leg,
    right_leg=right_leg,
    feet=feet
)

print(f"Human has {human.head.eyes} eyes and a {human.torso.abdomen} abdomen.")