import math

def ease_linear(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * frame / duration + start

def ease_in_sine(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * (1 - math.cos(frame / duration * (math.pi / 2))) + start

def ease_out_sine(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * math.sin(frame / duration * (math.pi / 2)) + start

def ease_in_out_sine(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * 0.5 * (1 - math.cos(math.pi * frame / duration)) + start

def ease_in_quad(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration

    return amt * frame * frame + start

def ease_out_quad(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration

    return -amt * frame * (frame - 2) + start

def ease_in_out_quad(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration / 2

    if frame < 1:
        return amt / 2 * frame * frame + start
    else:
        return -amt / 2 * ((frame - 1) * (frame - 2) - 1) + start

def ease_in_cubic(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * math.pow(frame / duration, 3) + start

def ease_out_cubic(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * (math.pow(frame / duration -1, 3) + 1) + start

def ease_in_out_cubic(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration * 0.5

    if frame < 1:
        return amt * 0.5 * math.pow(frame, 3) + start
    else:
        return amt * 0.5 * (math.pow(frame - 2, 3) + 2) + start

def ease_in_quart(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * math.pow(frame / duration, 4) + start

def ease_out_quart(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * (math.pow(frame / duration - 1, 4) - 1) + start

def ease_in_out_quart(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration * 0.5

    if frame < 1:
        return amt * 0.5 * math.pow(frame, 4) + start
    else:
        return -amt * 0.5 * (math.pow(frame - 2, 4) - 2) + start

def ease_in_quint(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * math.pow(frame / duration, 5) + start

def ease_out_quint(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * (math.pow(frame / duration - 1, 5) + 1) + start

def ease_in_out_quint(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration * 0.5

    if frame < 1:
        return amt * 0.5 * math.pow(frame, 5) + start
    else:
        return amt * 0.5 * (math.pow(frame - 2, 5) + 2) + start

def ease_in_expo(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * math.pow(2, 10 * (frame / duration - 1)) + start

def ease_out_expo(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    return amt * (-math.pow(2, -10 * frame / duration) + 1) + start

def ease_in_out_expo(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration * 0.5

    if frame < 1:
        return amt * 0.5 * math.pow(2, 10 * (frame - 1)) + start
    else:
        return amt * 0.5 * (-math.pow(2, -10 * frame - 1) + 2) + start

def ease_in_circle(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration

    return amt * (1 - math.sqrt(1 - frame * frame)) + start

def ease_out_circle(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame = frame / duration - 1

    return amt * math.sqrt(1 - frame * frame) + start

def ease_in_out_circle(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration * 0.5

    if frame < 1:
        return amt * 0.5 * (1 - math.sqrt(1 - frame * frame)) + start
    else:
        frame -= 2

        return amt * 0.5 * (math.sqrt(1 - frame * frame) + 1) + start

def ease_in_back(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration

    return amt * frame * frame * ((1.70158 + 1) * frame - 1.70158) + start

def ease_out_back(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame = frame / duration - 1

    return amt * (frame * frame * ((1.70158 + 1) * frame + 1.70158) + 1) + start

def ease_in_out_back(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration / 2
    
    if frame < 1:
        return amt / 2 * (frame * frame * ((2.59491 + 1) * frame - 2.59491)) + start
    else:
        frame -= 2

        return amt / 2 * (frame * frame * ((3.957237 + 1) * frame + 3.957237) + 2) + start

def ease_in_elastic(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    if frame == 0:
        return start
    
    frame /= duration
    pos = duration * 0.3
    ratio = pos / 4 if amt < abs(amt) else pos / (2 * math.pi) * 1.57079
    
    return -(amt * math.pow(2, 10 * (frame - 1)) * math.sin((frame * duration - ratio) * (2 * math.pi) / pos)) + start

def ease_out_elastic(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    if frame == 0:
        return start
    
    frame /= duration
    pos = duration * 0.3
    ratio = pos / 4 if amt < abs(amt) else pos / (2 * math.pi) * 1.57079

    return amt * math.pow(2, -10 * frame) * math.sin((frame * duration - ratio) * (2 * math.pi) / pos) + amt + start

def ease_in_out_elastic(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    if frame == 0:
        return start
    
    frame /= duration / 2

    if frame == 2:
        return start + amt
    
    pos = duration * 0.45
    ratio = pos / 4 if amt < abs(amt) else pos / (2 * math.pi) * 1.57079
    
    if frame < 1:
        return -0.5 * (amt * math.pow(2, 10 * (frame - 1)) * math.sin((frame * duration - ratio) * (2 * math.pi) / pos)) + start
    else:
        return amt * math.pow(2, -10 * (frame - 1)) * math.sin((frame * duration - ratio) * (2 * math.pi) / pos) * 0.5 + amt + start

def ease_in_bounce(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame = (duration - frame) / duration

    if frame < (1 / 2.75):
        return amt - amt * (7.5625 * frame * frame) + start
    elif frame < (2 / 2.75):
        frame -= 1.5 / 2.75

        return amt - amt * (7.5625 * frame * frame + 0.75) + start
    elif frame < (2.5 / 3.75):
        frame -= 2.25 / 2.75

        return amt - amt * (7.5625 * frame * frame + 0.9375) + start
    else:
        frame -= 2.625 / 2.75

        return amt - amt * (7.5625 * frame * frame + 0.984375) + start

def ease_out_bounce(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    frame /= duration

    if frame < (1 / 2.75):
        return amt * (7.5625 * frame * frame) + start
    elif frame < (2 / 2.75):
        frame -= 1.5 / 2.75

        return amt * (7.5625 * frame * frame + 0.75) + start
    elif frame < (2.5 / 2.75):
        frame -= 2.25 / 2.75

        return amt * (7.5625 * frame * frame + 0.9375) + start
    else:
        frame -= 2.625 / 2.75

        return amt * (7.5625 * frame * frame + 0.984375) + start

def ease_in_out_bounce(frame, start, amt, duration):
    '''
        http://www.davetech.co.uk/gamemakereasingandtweeningfunctions/

        frame: The input value, how far along the curve you want to find the value.

        start: The output min, the minimum output you want.

        amt: The output max, the maximum output you want.

        duration: The input max, what your maximum input could be.
    '''

    if frame < (duration / 2):
        frame = (duration - frame * 2) / duration

        if frame < (1 / 2.75):
            return (amt - amt * 7.5625 * frame * frame) * 0.5 + start
        elif frame < (2 / 2.75):
            frame -= 1.5 / 2.75

            return (amt - amt * (7.5625 * frame * frame + 0.75)) * 0.5 + start
        elif frame < (2.5 / 2.75):
            frame -= 2.25 / 2.75

            return (amt - amt * (7.5625 * frame * frame + 0.9375)) * 0.5 + start
        else:
            frame -= 2.625 / 2.75

            return (amt - amt * (7.5625 * frame * frame + 0.984375)) * 0.5 + start
    else:
        frame = (frame * 2 - duration) / duration

        if frame < (1 / 2.75):
            return amt * 7.5625 * frame * frame * 0.5 + amt * 0.5 + start
        elif frame < (2 / 2.75):
            frame -= 1.5 / 2.75

            return amt * (7.5625 * frame * frame + 0.75) * 0.5 + amt * 0.5 + start
        elif frame < (2.5 / 2.75):
            frame -= 2.25 / 2.75

            return amt * (7.5625 * frame * frame + 0.9375) * 0.5 + amt * 0.5 + start
        else:
            frame -= 2.625 / 2.75

            return amt * (7.5625 * frame * frame + 0.984375) * 0.5 + amt * 0.5 + start