#!/bin/python

"""
UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

    #>>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    300

The rules of bowling are as follows:

(1) A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll one, two, or three.  Your total
score is the sum of your scores for the ten frames.
(2) If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, bowling([8, 1, 7, ...]) means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
(3) If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, bowling([8, 2, 7, ...]) means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
(4) If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, bowling([10, 7, 3, ...]) means that you get a strike, you score
10 + 7 + 3 = 20 in the first frame; the second frame starts with the 7.

"""


def bowling_one(balls):
    """Compute the total score for a player's game of bowling.
    """

    frame_scores = []
    i = 0
    while len(frame_scores) < 10:
        current_roll = balls[i]
        if current_roll == 10:
            next_roll = balls[i + 1]
            next_next_roll = balls[i + 2]
            frame_scores.append(current_roll + next_roll + next_next_roll)
            i += 1  # next frame
        elif current_roll < 10:
            next_roll = balls[i + 1]
            current_score = current_roll + next_roll
            if current_score == 10:
                next_next_roll = balls[i + 2]
                frame_scores.append(current_score + next_next_roll)
            else:
                frame_scores.append(current_score)
            i += 2
    total_score = sum(frame_scores)
    return total_score



# Norvig-ian Solution
def bowling_two(balls, frame=1):
    """Compute the total score for a player's game of bowling_two.
    """

    if len(balls) <= 2 or frame == 10:
        return sum(balls)
    elif balls[0] == 10:
        return balls[0] + balls[1] + balls[2] + bowling_two(balls[1:], frame+1)  # strike
    elif balls[0] + balls[1] == 10:
        return balls[0] + balls[1] + balls[2] + bowling_two(balls[2:], frame+1)  # spare
    else:
        return balls[0] + balls[1] + bowling_two(balls[2:], frame+1)  # open


# Concise iteration
def bowling_three(balls):
    """Compute the total score for a player's game of bowling_two.
    """

    score = 0
    i = 0
    for frame in range(10):
        score += balls[i] + balls[i + 1]
        if balls[i] + balls[i + 1] >= 10:
            score += balls[i + 2]
        i += 2 if balls[i] < 10 else 1
    return score


def test_bowling(bowling_function):
    assert   0 == bowling_function([0] * 20)
    assert  20 == bowling_function([1] * 20)
    assert  80 == bowling_function([4] * 20)
    assert 190 == bowling_function([9,1] * 10 + [9])
    assert 300 == bowling_function([10] * 12)
    assert 200 == bowling_function([10, 5,5] * 5 + [10])
    assert  11 == bowling_function([0,0] * 9 + [10,1,0])
    assert  12 == bowling_function([0,0] * 8 + [10, 1,0])

test_bowling(bowling_one)
test_bowling(bowling_two)
test_bowling(bowling_three)
