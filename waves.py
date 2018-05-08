from sys import argv

script, height, length = argv

wave = height
board = length
prompt = ' > '

def rippin(wave, board):
    print 'The waves are {} feet high'.format(wave)
    print 'Your board is {} inches long'.format(board)
    print 'Are you ready to rock it?'
    answer = raw_input(prompt)
    print '{}, alright then get it going either way'.format(answer)
rippin(wave, board)
